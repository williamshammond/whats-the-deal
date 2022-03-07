$(document).ready(function(){


    function boldCategory(info,keyword){
        let lowInfo = info.toLowerCase()
        let lowWord = keyword.toLowerCase()

        let index = lowInfo.indexOf(lowWord)
        let prev = info.slice(0,index)
        let mid = info.slice(index,index+keyword.length)
        let after = info.slice(index+keyword.length)
        return prev + "<span class = 'orange highlight'>" + mid + "</span>" + after 
    }

    function boldFromList(infoList,keyword){
        let lowWord = keyword.toLowerCase()
        let info = ""
        let index = 0
        let word = ""

        for(key in infoList){

            info = infoList[key]
            let lowInfo = info.toLowerCase()
            
            index = lowInfo.indexOf(lowWord)
            if(index != -1){
                word = info
                break
            }  
        }

        let prev = info.slice(0,index)
        let mid = info.slice(index,index+keyword.length)
        let after = info.slice(index+keyword.length)
        return prev + "<span class = 'orange highlight'>" + mid + "</span>" + after 
        
    }

    function loadResults(){

        $.each(results, function(key,value) {


            let category = Object.keys(value)[0]
            let item = value[category]

            console.log(item)
            
            let name = item.project
            
            //Create container row for result
            let resultDiv = $("<div class = 'row resultrow'>")

            //Add image to result with link to corresponding page
            let imageDiv = $("<div class = 'col-md-3'> <a href = '/view/" + item["id"]+ "'>" + "<img class = 'thumbnail' src = '" + item["image"]+ "'> </a> </div>")
            resultDiv.append(imageDiv)

            //Check for categories that match
            if(category == "project"){
                console.log("It is project")
                let nameDiv = $("<div class = 'col-md-3'><div class = 'featuretext'><a href = '/view/"+item["id"]+"'> <span class = 'name'>"+boldCategory(item["project"],search)+"</span>")
                resultDiv.append(nameDiv)
            }
            else{
                let nameDiv = $("<div class = 'col-md-3'><div class = 'featuretext'><a href = '/view/"+item["id"]+"'> <span class = 'name'>"+item["project"]+"</span>")
                resultDiv.append(nameDiv)
            }

            if(category == "neighborhood"){
                console.log("It is neighborhood")
                let neighborhoodDiv = $("<div class = 'col-md-3'><div class = 'featuretext'><span class = 'searchinfo'>" + boldCategory(item["neighborhood"],search) + "</span>")
                resultDiv.append(neighborhoodDiv)
            }
            else{
                let neighborhoodDiv = $("<div class = 'col-md-3'><div class = 'featuretext'><span class = 'searchinfo'>" + item["neighborhood"]+ "</span>")
                resultDiv.append(neighborhoodDiv)
            }

            if(category == "developers"){
                console.log("It is developer")
                let developersDiv = $("<div class = 'col-md-3'><div class = 'featuretext'><span class = 'searchinfo'> Developer:<br>" + boldFromList(item["developers"],search) + "</span>")
                resultDiv.append(developersDiv)
            }

            if(category == "financiers"){
                console.log("It is developer")
                let financiersDiv = $("<div class = 'col-md-3'><div class = 'featuretext'><span class = 'searchinfo'>Financier:<br>" + boldFromList(item["financiers"],search) + "</span>")
                resultDiv.append(financiersDiv)
            }

            if(category == "contractors"){
                console.log("It is developer")
                let contractorsDiv = $("<div class = 'col-md-3'><div class = 'featuretext'><span class = 'searchinfo'>Contractor:<br>" + boldFromList(item["contractors"],search) + "</span>")
                resultDiv.append(contractorsDiv)
            }
            
            



            $(resultsplace).append(resultDiv)
            $(resultsplace).append("<hr>")
         })
    }


    loadResults()

})
