function getFeatured(){
    $.ajax({
        type: "POST",
        url: "get_featured",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify({"1":"1","2":"2","3":"3"}),
        success: function(result){
            let featured = result["featured"]
            $.each(featured, function(key, value){
                let newDiv = $("<div class = 'row'>")
                newDiv.html("<div class = 'col-md-7'> <a href = '/view/" + value["id"]+ "'> <img class = 'small' src = '" + value["image"]+ "'> </a> </div><div class = 'col-md-5'><div class = 'featuretext'><a href = '/view/"+value["id"]+"'> <span class = 'name'>"+value["project"]+"</span></a><br><span class = 'orange'>" + value["neighborhood"]+ "</span><br><br><span class = 'blue'>Category</span><br><span class = 'orange'>" + value["category"]+ "</span><br><br><span class = 'blue'>Development Cost</span><br><span class = 'orange'>" + cleanCost(value["cost"])+ "</span><br></div></div></div>")
                let divName = "feature" + String(key + 1)
                console.log(divName)
                $("#" + divName).append(newDiv)
                console.log("Success")
            })
        },
        error: function(request, status, error){
            console.log("Error")
            console.log(request)
            console.log(status)
            console.log(error)
        }
    })
}