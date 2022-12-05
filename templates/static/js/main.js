$(document).ready(function(){
    $('#poti').click(function(){
        $('.nav-collapse').css("left","0")
    })
    
    $('#closeBtn').click(function(){
        $('.nav-collapse').css("left","-100%")
    })
})