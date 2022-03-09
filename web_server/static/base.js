

$(document).ready(function() {

    $(".base_button_handler").click( function(event){

        var the_id = event.target.id

        $.ajax(
            {
                url: "/button_handler_base",
                type: "get",
                data: {button_id: the_id},
                success: function(response) {
                    $("#response").html(response);
                },
                error: function(xhr) {
                    alert(xhr)
                }
            }
        );
    });


    // clear the response
    $("#clear").click(function(event){
        $("#response").html("");
    });


});





function openNav() {
    document.getElementById("mySidepanel").style.width = "250px";
}
    
    /* Set the width of the sidebar to 0 (hide it) */
function closeNav() {
    document.getElementById("mySidepanel").style.width = "0";
} 


