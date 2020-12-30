var map
var mapin
var initCoor ={ lat: 28.639776041703794, lng: -106.07337679520055 };
var markers = [];


$('.likebutton').click(function(){
    var catid;
    var total;
    var value;
    catid = $(this).data("catid");
    $.ajax(
    {
        type:"GET",
        url: "/likepost",
        data:{
                post_id: catid
        },
        success: function( data ) 
        {
            total = $('#'+ catid).attr("data-total")
            if ($('#'+catid).attr("data-value") == 'Like'){
                $( '#liked'+catid ).text((parseInt(total) + 1));
                $( '#heart'+catid ).css('color', 'red')
                $('#'+catid).attr("data-total", parseInt(total) + 1)
                $('#'+catid).attr("data-value", 'Unlike')
            }
            else{
                $( '#liked'+catid ).text((parseInt(total) - 1));
                $( '#heart'+catid ).css('color', 'black')
                $('#'+catid).attr("data-total", parseInt(total) - 1)
                $('#'+catid).attr("data-value", 'Like')
            }
        }
    })
})

$('.cuscard').click(function(){// Mostrar localizacion de un lugar
    let catid;
    catid = $(this).data("catid");
    $.ajax(
    {
        type:"GET",
        url: "/getCoor",
        data:{
                post_id: catid
        },
        success: function( data ) 
        {
            console.log(data)
            setMapOnAll(null);
            addMarker(data);
            map.setZoom(18);
            map.panTo(data);
        }
    })
})

function addMarker(location) {
    const marker = new google.maps.Marker({
      position: location,
      map: map,
      animation: google.maps.Animation.DROP,
    });
    markers.push(marker);
  }

  function addMarkerMapin(location) {
    setMapOnAll(null);
    const marker = new google.maps.Marker({
      position: location,
      map: mapin,
      animation: google.maps.Animation.DROP,
    });
    markers.push(marker);
  }

  function setMapOnAll(map) {
    for (let i = 0; i < markers.length; i++) {
      markers[i].setMap(map);
    }
  }

  function showMarkers() {
    setMapOnAll(map);
  }

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
      center: initCoor,
      zoom: 13,
    });
  }

  function initMapin() {
    mapin = new google.maps.Map(document.getElementById("mapin"), {
      center: initCoor,
      zoom: 13,
    });
    google.maps.event.addListener(mapin, 'click', function( event ){
        let dire = event.latLng.lat()+", "+event.latLng.lng();
        document.getElementById("location").value = dire;
        document.getElementById("latlo").value = event.latLng.lat();
        document.getElementById("lnglo").value = event.latLng.lng();
        let dir = {
            'lat':event.latLng.lat(),
            'lng':event.latLng.lng()
        }
        console.log(dir);
        addMarkerMapin(dir);
      });
  }

  $(function() {
    $( 'a[href$="#"]' ).each(function() {
        $( this ).attr( 'href','javascript:void(0);' )
    });
});

function mostrarTodo(){
    $.ajax(
        {
            type:"GET",
            url: "/fullMapView",
            success: function( data ) 
            {
                console.log(data)
                setMapOnAll(null);
                map.setZoom(13);
                map.panTo(initCoor);
                for (let index = 0; index < data['res'].length; index++) {
                    addMarker(data['res'][index]);
                }
            }
        })
}

function getAddress(latlng){
    $.ajax(
        {
            type:"GET",
            data:{
                latlng: latlng
                },
            url: "/getAddress",
            success: function( data ) 
            {
                alert(data['loc']);
            }
        })
}

function validateForm(){
  coors = document.getElementById("location").value;
  desc = document.getElementById("desc").value;
  if (coors == "" || desc == "") {
    swal({
      icon: "error",
      title: "Oops",
      text: "The fields were no filled correctly"
    });
    return false;
  }else{
    swal({
      icon: "success",
      title: "The report was posted successfully",
      text: "The report is going to appear at the end of the list.",
      confirm: {
        text: "OK",
        value: true,
        visible: true,
        className: "",
        closeModal: true
      }
    });
    return true;
  }
}


