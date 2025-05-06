let map;

function initMap() {

    var hayMarket = { lat: 52.6363, lng: -1.1317 }
    map = new google.maps.Map(document.getElementById("map"), {
        center: hayMarket,
        zoom: 17,
    });

    var marker = new google.maps.Marker({
        position: hayMarket,
        map: map
    });

}

$(".btn-warning").hover(
    function(){ $(this).addClass('progress-bar-animated') }
)

$(".btn-warning").mouseleave(
    function(){ $(this).removeClass('progress-bar-animated') }
)