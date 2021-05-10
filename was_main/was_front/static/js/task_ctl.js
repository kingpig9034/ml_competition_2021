$( document ).ready(function() {
    $('#deleteAllTask').click(function(){
        var delete_url = "http://localhost:9030/api/v1/videoTasks/"+cam_id + "/delete/"
        $.ajax({
            url : delete_url,
            type: "POST",
            
            success: function(response){
                console.log(response)
                location.reload();
            }
        });
    });
});
