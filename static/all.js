
$(document).ready(function(){

    
    $(searchform).submit(function(e){

        let trimmed = $("#input").val().trim()

        if(trimmed.length == 0){
            $("#input").val("")
            $("#input").focus()
            e.preventDefault()
        }
        
    })

    
})
