# CS50 Final Project #
Welcome to my CS50 Final Project called Codigo Trapo Rojo, a webpage developed in Python and JavaScript using Django as a framework and different APIs such as Geocoding and Maps. It has a fully responsive layout using bootstrap that makes the page look great on a smartphone or tablet. This webpage uses sessions that keep you logged in, validations when accessing or creating an account, you can create different posts that contain additional information created automatically by Geocoding API in the background, you can react and see other posts locations in a map among, follow other users and see their activity and see who is following or being followed by among other functions.

#### Installation
  - Install project dependencies by running `pip install -r requirements.txt`. Dependencies include Django and Pillow module that allows Django to work with images.
  - Make and apply migrations by running `python manage.py makemigrations` and `python manage.py migrate`.
  - Create superuser with `python manage.py createsuperuser`. (This step is optional.)
  - Go to website address and start using it!.
  
#### Files and Directories
- `CodigoTrapoRojo` - Main application directory
   - `asgi.py` - It exposes the ASGI callable as a module-level variable
   - `settings.py` - Django settings for CodigoTrapoRojo project.
   - `urls.py` - CodigoTrapoRojo URL Configuration, list routes URLs to views.
   - `wsig.py` - It exposes the WSGI callable as a module-level variable named CodigoTrapoRojo.
   -`wsig.py` - It exposes the WSGI callable as a module-level variable named CodigoTrapoRojo.
- `network` - CodigoTrapoRojo's application directory (It contains all the logic.)
   - `\static\network` - It contains static files such as images, css and js files.
      - `\imgs` - Folder with the webpage images.
      - `logic.js` - it contains all JavaScript logic used in the webpage incluiding some of the used functions from different APIs
      - `style.css` - It contains the css used in most screens
   - `\templates\network` - Contains al application templates.
      - `config.html` - Profile configuration HTML.
      - `following.html` - Personal following profiles view HTML.
      - `index.html` - Main screen HTML.
      - `intro.html` - Intro with project description and context HTML.
      - `layout.html` - Shared html layout structure HTML.
      - `login.html` - Login screen HTML.
      - `newpost.html` - New post Screen HTML.
      - `profile.html` - Profile Screen HTML.
      - `register.html` - Register Screen HTML.
   - `admin.py` - Place where models are registered to be managed in the administrator module.
   - `apps.py` - Configured applications.
   - `models.py` - Contains all models used by the page.
   - `urls.py` - network URL Configuration, list routes URLs to views.
   - `views.py` - It contains all the Python logic and methods used in this Django Framework incluiding some APIs requests.
- `manage.py` - Django's command-line utility for administrative tasks.
- `requirements.txt` - libraries needed to run this application.
   

#### Justification
Código Trapo Rojo ( Red Cloth Code in Spanish ) is a concept of a tool that is planned to be used by organizations or individuals in Mexico that are willing to help others in vulnerable situations due to the COVID-19 crisis. The way this virus affects people varies drastically depending on the country. In the case of Mexico, a big number of elder people are in extreme poverty for the first time due to the economical crisis and the risk of being exposed to the virus. They need to receive help as soon as possible.

On this website, it is possible to help by reporting where help is needed the most. There are other functions such as tracking and observing if someone that you want to help is receiving help from others and follow other helpers to see their activities and reports. How does this is meant to connect with elders that are in extreme poverty and have no internet access?

Nowadays, people in vulnerable situations have been placing red clothes in front of their houses as a sign of help. The people that see those signs use to report to the local news these situations, or post photos on social media in order of making diffusion of it. Unfortunately, even though there are a lot of people willing to help, this framework has been not efficient at all because of the fact that news and social media posts are not made to last and are hard to track.

By using Código Trapo Rojo, the red cloth system that nowadays is used by many people at least in the north of Mexico could have a bigger scope and become more efficient. It is possible to connect with these vulnerable people that have no internet or ways to ask for help efficiently. The red cloth system is a pattern that is visible in the local news of different cities in the north of Mexico, there is much news about people giving help to vulnerable elders that ask for help using this non-technological system. 

