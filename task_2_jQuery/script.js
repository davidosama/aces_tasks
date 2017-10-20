$(document).ready(function(){
    $("#btnText").click(function(){
        $(".navbar-brand").text("David")
    });
    
    $("#btnColors").click(function(){
        $(".navbar-custom, .p-border2, footer").css("background-color","red");
    });
    
    $("#btnBtns").click(function(){
        $("#btnText, #btnColors").toggle();
    });

});