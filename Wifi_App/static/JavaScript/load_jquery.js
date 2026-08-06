$(document).ready(function(){

  $('.userinfo').click(function(){
    
    var userid = $(this).data('id');
 
    // AJAX request
    $.ajax({
     url: 'ajaxfile.php',
     type: 'post',
     data: {userid: userid},
     success: function(response){ 
       // Add response in Modal body
       $('.modal-body').html(response);
 
       // Display Modal
       $('#myModal').modal('show'); 
     }
   });
  });
 });