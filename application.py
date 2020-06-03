import os, json , requests , request

from flask import Flask, session, redirect, render_template, request, jsonify, flash
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/" , methods=["POST","GET"]) 
def index():
    print(session)
    if request.method == "POST":
        searchItem = request.form.get("searchItem")
        if not searchItem:
            return render_template("index.html",userName = session['userName'])
        else:
            queryItem = "LOWER('%" + searchItem + "%')"
            query = "select * from books where LOWER(\"isbn\") LIKE "+queryItem+" or LOWER(\"title\") LIKE "+queryItem+" or LOWER(\"author\") LIKE "+queryItem+" LIMIT 1000;"
            rows = db.execute(query)
            print(rows.rowcount)
            if rows.rowcount==0:
                return render_template("indexSearch.html",searchItem = searchItem,noresults=True)
            else:
                result = rows.fetchall()
                return render_template("indexSearch.html",books=result,count=rows.rowcount,searchItem = searchItem,noresults=False)
    else:
        if 'idUser' not in session:
            return redirect('/login')
        else:
            return render_template("index.html",userName = session['userName'])

@app.route("/login",methods=["POST","GET"])
def login():
    session.clear()
    if request.method == "POST":
        if not request.form.get("user"):
            return render_template("login.html",nologed=True)#Failed login
        else:
            user = request.form.get("user")
            rows = db.execute("SELECT * FROM users where \"userName\" = :userName", {"userName": user})
            result = rows.fetchone()
            if not result:
                return render_template("login.html",nologed=True)#Failed login
            else:
                if result[2] == request.form.get("password"): #LOGED
                    session['idUser'] = result[0]
                    session['userName'] = result[1]
                    return redirect("/")
                else:
                    return render_template("login.html",nologed=True)#Failed login
    else:
        return render_template("login.html")

@app.route("/signup",methods=["POST","GET"])
def signup():
    session.clear()
    if request.method == "POST":
        newUser = request.form.get("newUser")
        confPass1 = request.form.get("confPass1")
        confPass2 = request.form.get("confPass2")
        if confPass1 != confPass2:
            return render_template("signup.html",failed=True , message = "Passwords do not match")#Failed signUp
        else:
            rows = db.execute("SELECT \"userName\" FROM users where \"userName\" = :userName", {"userName": newUser})
            result = rows.fetchone()
            if not result:
                db.execute("INSERT INTO users(\"userName\", \"password\") VALUES (:userName, :pass);", {"userName": newUser,"pass": confPass1})
                db.commit()
                return redirect("/login")
            else:
                return render_template("signup.html",failed=True , message = "There is already an account with that name")#Failed signUp
    else:
        session.clear()
        return render_template("signup.html")

@app.route("/logout",methods=["POST","GET"])
def logout():
    session.clear()
    return redirect("/")

@app.route("/book/<string:isbn>",methods=["POST","GET"])
def book(isbn):
    if 'idUser' not in session:
        return redirect("/")
    else:
        if  request.method == "POST":
            db.execute("INSERT INTO ratings(\"isbn\", \"user\" , \"rating\" , \"comment\") VALUES (:isbn, :user , :rating, :comment);", {"isbn": isbn,"user": session['userName'],"rating":request.form.get("points"),"comment":request.form.get("comment")})
            db.commit()

        rows = db.execute("select * from books where \"isbn\" = :isbn;", {"isbn": isbn})
        result = rows.fetchone()
        if not result:
            return render_template("error.html")
        else:
            bookInfo = rows.fetchall()
            key = os.getenv("GOODREADS_KEY")
            query = requests.get("https://www.goodreads.com/book/review_counts.json",params={"key": key, "isbns": isbn})
            response = query.json()
            response = response['books'][0]
            bookInfo.append(response)
            commentsQuery = db.execute("SELECT * FROM \"ratings\" where \"isbn\" = :isbn", {"isbn": isbn})
            if commentsQuery.rowcount==0:
               nocomments=True
               return render_template("book.html",isbn=isbn,title=result[1],author=result[2],year=result[3],bookInfo=bookInfo,nocomments=nocomments,allowsubmit=True)
            else:
                comments = commentsQuery.fetchall()
                nocomments = False
                allowsubmit = True
                for x in comments:
                    if session['userName'] == x[1]:
                        allowsubmit = False
                print(isbn)
                return render_template("book.html",isbn=isbn,title=result[1],author=result[2],year=result[3],bookInfo=bookInfo,nocomments=nocomments,comments=comments,allowsubmit=allowsubmit)

@app.route("/api/<isbn>", methods=['GET'])
def api(isbn):
    data=db.execute("SELECT * FROM books WHERE isbn = :isbn",{"isbn":isbn}).fetchone()
    if data==None:
        return render_template('404.html')

    key = os.getenv("GOODREADS_KEY")
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": key, "isbns": isbn})
    average_rating=res.json()['books'][0]['average_rating']
    work_ratings_count=res.json()['books'][0]['work_ratings_count']
    x = {
    "title": data.title,
    "author": data.author,
    "year": data.year,
    "isbn": isbn,
    "review_count": work_ratings_count,
    "average_score": average_rating
    }
    api=json.dumps(x)
    return render_template("api.json",api=api)