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

    $.each(featuredPosts, function(key, value){
        
        
        let titleDiv = $("<div class = 'row namerow'><div class = 'col-md-12'><a href = '/view/"+value["id"]+"'> <span class = 'name'>"+value["project"]+"</span></a></div>")
        let newDiv = $("<div class = 'row'>")
        let imageDiv = $("<div class = 'col-md-7'> <a href = '/view/" + value["id"]+ "'>" + "<img class = 'small' src = '" + value["image"]+ "'> </a> </div>")
        newDiv.append(imageDiv)

        let textDiv = $("<div class = 'col-md-5 featuretext'>")
        
        textDiv.append("<span class = 'blue'>" + value["neighborhood"]+ "</span><br><br>")
        textDiv.append("<div><span class = 'blue'>Category</span><br><span class = 'blue'>" + value["category"]+ "</span></div><br>")
        textDiv.append("<div><span class = 'blue'>Development Cost</span><br><span class = 'blue'>" + cleanCost(value["cost"])+ "</span><br>")
        
        newDiv.append(textDiv)
        
        let divName = "feature" + String(key + 1)
        console.log(divName)
        $("#" + divName).append(titleDiv)
        $("#" + divName).append(newDiv)
    })


    
    
})