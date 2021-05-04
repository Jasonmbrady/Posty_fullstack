$(document).ready(function() {
    $('.hidden').hide();
    $('#pw_eye').click(function(){
        pwd = $(".password");
        if(pwd.attr('type') == 'password'){
            pwd.attr('type', 'text')
        } else (
            pwd.attr('type', 'password')
        )
    });

    $('#new_task').submit(function(event){
        event.preventDefault();
        $.ajax({
            url: "/create_task",
            method: "POST",
            data: $(this).serialize(),
            success: function(res){
                console.log(res);
                console.log("Success!")
            }
        });
    });
    
    // $('#category').change(function(){
    //     // display a list of matching categories
    //         // AJAX call to DB getting all tasks
    //         // if category not in categories, add to categories
    //         // loop through categories, appending to list
    //         // if value == cat.slice(0,value.length)
    //     let str = $('#catList').val();
    //     console.log(str);
    //     console.log("hello");
    
    
    // });
    
}) 
function catHandler(value){
    $(".remove").remove();
    var cats = $('.hidden').text().split(" ").filter(function(item){
        return item != "" && item != "\n"
    });
    let unique = {};
    // var catStr = "";
    for (const cat in cats){
        if (!unique.hasOwnProperty(cats[cat])){
            unique[cats[cat]] = true;
        }
    }
    for (const [key, val] of Object.entries(unique)){
        if(key.slice(0, value.length).toLowerCase() == value.toLowerCase() && value != ""){
            const catStr = "<li class='remove'>" + key + "</li>"
            $('.catList').append(catStr);
        }
    }

}