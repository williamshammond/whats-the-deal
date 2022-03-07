/*
let map;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: -34.397, lng: 150.644 },
        zoom: 8,
    });
}
*/

$(document).ready(function(){

    

    function cleanCost(cost){
        if(cost.length == 12){
            return "$" + cost.slice(0,2) + "." + cost.slice(2,3) + " Billion"
        }
        else if(cost.length == 11){
            return "$" + cost.slice(0,2) + "." + cost.slice(2,3) + " Billion"
        }
        else if(cost.length == 10){
            return "$" + cost.slice(0,1) + "." + cost.slice(1,3) + " Billion"
        }
        else if(cost.length == 9){
            return "$" + cost.slice(0,2) + "." + cost.slice(2,3) + " Million"
        }
        else if(cost.length == 8){
            return "$" + cost.slice(0,2) + "." + cost.slice(2,3) + " Million"
        }
        else if(cost.length == 7){
            return "$" + cost.slice(0,1) + "." + cost.slice(1,3) + " Million"
        }

        return cost  
    }

    function cleanSQFT(sqft){
        if(sqft.length == 12){
            return "$" + sqft.slice(0,2) + "." + sqft.slice(2,3) + " Billion"
        }
        else if(sqft.length == 11){
            return "$" + sqft.slice(0,2) + "." + sqft.slice(2,3) + " Billion"
        }
        else if(sqft.length == 10){
            return "$" + sqft.slice(0,1) + "." + sqft.slice(1,3) + " Billion"
        }
        else if(sqft.length == 9){
            return "$" + sqft.slice(0,2) + "." + sqft.slice(2,3) + " Million"
        }
        else if(sqft.length == 8){
            return "$" + sqft.slice(0,2) + "." + sqft.slice(2,3) + " Million"
        }
        else if(sqft.length == 7){
            return "$" + sqft.slice(0,1) + "." + sqft.slice(1,3) + " Million"
        }

        return sqft  


    }
    
})