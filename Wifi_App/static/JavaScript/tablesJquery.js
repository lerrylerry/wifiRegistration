$(document).ready(function() {
  $('#studreq').DataTable({
    scrollCollapse: true,
    paging : false,
  })
  $('#studreq2').DataTable({
    scrollCollapse: true,
    paging : false,
  })
  $('#studreq3').DataTable({
    scrollCollapse: true,
    paging : false,
  })
  $('#studreq4').DataTable({
    scrollCollapse: true,
    paging : false,
  })
  $('#studreq5').DataTable({
    scrollCollapse: true,
    paging : false,
  })
  $('#facreq').DataTable({
    scrollCollapse: true,
    paging : false,
  })
  $('#facreq2').DataTable({
    scrollCollapse: true,
    paging : false,
  })
  $('#facreq3').DataTable({
    scrollCollapse: true,
    paging : false,
  })
  $('#facreq4').DataTable({
    scrollCollapse: true,
    paging : false,
  })
  $('#facreq5').DataTable({
    scrollCollapse: true,
    paging : false,
  })
})

$("input[type='file']").click(function () {
  $("input[id='signature']").click();
});
$("input[id='signature']").change(function (e) {
  var $this = $(this);
  $this.next().html($this.val().split('\\').pop());
});