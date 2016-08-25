$(document).ready(function(){
    var date_rel = $('#date_rel').val();
    if(!date_rel){
        $(".input-group.date").datepicker("setDate", new Date());
        $(".input-group.date").datepicker({ autoclose: true, todayHighlight: true, todayBtn: true, "setDate": new Date() });
    }
    $(".input-group.date").datepicker().on('changeDate', function(ev){
        $(".input-group.date").datepicker('hide');
    });
});
