$(document).ready(function() {
    $('#pw_eye').click(function(){
        pwd = $(".password");
        if(pwd.attr('type') == 'password'){
            pwd.attr('type', 'text')
        } else (
            pwd.attr('type', 'password')
        )
    });

});