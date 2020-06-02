var form_select = false;
var alert_select = false;
var bookmark_select = false;
$(document).ready(function() {
    $('.other').on('click', function() {
        $(' #other_subject').removeClass('other_subject');
        $(' .hied').removeClass('other_subject'); 
        $(' .hied_div').removeClass('other_subject'); 
        $(' .other').addClass('other_subject');  
        $(' .other_div').addClass('other_subject'); 
    })
    $('.hied').on('click', function() {
        $(' #other_subject').addClass('other_subject');   
        $(' .hied').addClass('other_subject'); 
        $(' .hied_div').addClass('other_subject'); 
        $(' .other').removeClass('other_subject'); 
        $(' .other_div').removeClass('other_subject'); 
    })
    $('.settings-button').on('click', function() {
        if(form_select == true){
            $(' .form').addClass('close_form_select');
            form_select = false;
        }    
        else if(form_select == false){
            $(' .form').removeClass('close_form_select');
            form_select = true;
        }        
    })
    $(".alert-button").on('click', function() {
        if(alert_select == true){
            $(" .notification-menu").removeClass("on");
            alert_select = false;
        }
        else if(alert_select == false && bookmark_select == false ){
            $(" .notification-menu").addClass("on");
            alert_select = true;
        }
    });
    $(".bookmark-button").on('click', function() {
        if(bookmark_select == true){
            $(" .bookmark-menu").removeClass("on");
            bookmark_select = false;
        }
        else if(bookmark_select == false && alert_select == false){
            $(" .bookmark-menu").addClass("on");
            bookmark_select = true;
        }
    });
})
