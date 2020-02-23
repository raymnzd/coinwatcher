$(document).ready(function() {
  $('#coin-table').DataTable({
    dom:"ftp",
    "bLengthChange": false,
    "order" : [[1,"desc"]]
  });
});
