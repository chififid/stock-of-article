$(document).ready(function() {
    $('.other').on('click', function(){
        $(' #other_subject').removeClass('other_subject');
        $(' .hied').removeClass('other_subject'); 
        $(' .hied_div').removeClass('other_subject'); 
        $(' .other').addClass('other_subject');  
        $(' .other_div').addClass('other_subject'); 
    })
    $('.hied').on('click', function(){
        $(' #other_subject').addClass('other_subject');   
        $(' .hied').addClass('other_subject'); 
        $(' .hied_div').addClass('other_subject'); 
        $(' .other').removeClass('other_subject'); 
        $(' .other_div').removeClass('other_subject'); 
    })
})
