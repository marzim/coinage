$(document).ready(function(){

  var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};

  $('#amount').change(function(){
      var nummonths = get_nummonths();
      var percent = (parseFloat($("#interest").val()) * parseFloat(nummonths)) / 100;

      var amount = $('#amount').val();
      var t_pay = parseFloat(amount) + parseFloat(amount * percent);
      if(t_pay){
        $('#total_payable').val(t_pay);
        $('#total_payment').change();
      }
  });

  $('#interest').val(Math.round($('#interest_hv').val()));

  $('#interest').change(function(){
      var nummonths = get_nummonths();
      var percent = (parseFloat($("#interest").val()) * parseFloat(nummonths)) / 100;

      var amount = $('#amount').val();
      var t_pay = parseFloat(amount) + parseFloat(amount * percent);
      if(t_pay){
        $('#total_payable').val(t_pay);
        $('#total_payment').change();
      }
  });

  $('#payment').change(function(){
     //var tpayment = parseFloat($('#totalpayment_hv').val());
     var payment = parseFloat($('#payment').val());
     //if(tpayment){
     //    payment += parseFloat(tpayment);
     //}
     if(payment){
        $('#total_payment').val(payment);
        $('#total_payment').change();
     }
     else
     {
        $('#total_payment').val(0);
        $('#total_payment').change();
     }
  });

  $('#total_payment').change(function(){
      try{
          var tpayable = parseFloat($('#total_payable').val());
          var tpayment = parseFloat($('#total_payment').val());
          if(!tpayment){
            $('#outstanding_balance').val(tpayable);
          }else if(tpayable && tpayment){
              $('#outstanding_balance').val(tpayable - tpayment);
          }
      }catch(err){
          alert("error: " + err.message);
      }
  });

  $('#customer_name').change(function(){
    alert("bitch please!");
  });

  $('#date_due').change(function()
  {
    $('#amount').change();
  });

  $('#ispenalty').click(function()
  {
    if($('#ispenalty').is(':checked')){
         var penalty = parseFloat($('#penalty_hv').val()) * parseFloat($('#numshares_hv').val());
         var total = parseFloat($('#newcontrib_amount').val().replace(',','')) + parseFloat(penalty);
        $('#newcontrib_penalty').val(penalty.toLocaleString());
        $('#newcontrib_total').val(total.toLocaleString());
        $('#ispenalty_hv').val(1)
     }else{
        $('#newcontrib_penalty').val(0);
        $('#newcontrib_total').val($('#newcontrib_amount').val());
        $('#ispenalty_hv').val(0)
     }
  });

  function get_nummonths(){
     var datedue = new Date($('#date_due').val());
     var daterel = new Date($('#date_rel').val());
     var numbermonth = parseFloat(datedue.getMonth() + 1) - parseFloat(daterel.getMonth() + 1);
     if(parseFloat(numbermonth) > 0)
     {
         if(parseFloat(datedue.getDate()) > parseFloat(daterel.getDate())){
            numbermonth += 1;
         }
     }
     return numbermonth <= 0 ? 1 : numbermonth;
  }

  $('#patronage').click(function()
  {
    if($('#patronage').is(':checked')){
        $('#patronage_hv').val(1)
     }else{
        $('#patronage_hv').val(0)
     }
  });

    $('#interest').val(Math.round($('#interest_hv').val()));
    $('#privilege').val($('#privilege_hv').val());

    if($('#ispenalty_hv').val() === '1'){
        $('#ispenalty').prop('checked', true);
    }

    if($('#patronage_hv').val() === '1'){
        $('#patronage').prop('checked', true);
    }

    $('#ismember').click(function()
    {
        if($('#ismember').is(':checked')){
            $('#member_hv').val(1);
        }else{
            $('#member_hv').val(0);
            $('#numbershares').val(0);
        }
    });

    if($('#member_hv').val() === '1'){
        $('#ismember').prop('checked', true);
        $('#collapseMemberPerks').collapse('show');
    }

    //$('ul.nav > li > a[href="' + document.location.pathname + '"]').parent().addClass('active');

    $('ul.nav > li > a[href$="/' + document.location.pathname.split("/")[1] + '"]').parent().addClass('active');

    function showDialogMessage(){
        $( "#dialog-message" ).dialog({
          modal: true,
          buttons: {
            Ok: function() {
              $( this ).dialog( "close" );
            }
          }
        });
    }

    $('.withdrawSavings').click(function(e)
    {
        e.preventDefault();
        var customerId = $(this).data('customerid');
        var customerName = $(this).data('customername');
        var customerAmount = $(this).data('description');
        $(".modal-body #customerId").val(customerId);
        $(".modal-body #customerName").val( customerName );
        $(".modal-body #amountValue").val(customerAmount);
    });

    $("#saveChanges").click(function(e)
    {
        e.preventDefault();
        $.ajax({
            url: '/savings/contributions/savingswithdraw',
            type: 'POST',
            data: $('#withdrawSavingsForm').serialize(),
        });
        location.reload();
    });

    $('.confirmDelete').click(function(e){
       e.preventDefault();
        var id = $(this).data('id');
        var name = $(this).data('name');
        var url = $(this).data('url');
        if(url === "/customers/delete/"){
            $(".modal-body #instructions").text("Please be aware that deleting this customer would also delete all loans/contributions connected to it.");
        }
        else if(url === "/loans/delete/"){
            name = name + " with outstanding balance of " + $(this).data('amount');
        }
        $(".modal-body #id").val(id);
        $(".modal-body #name").text(" '" + name + "' ");
        $(".modal-body #url").val(url);
    });

    $('#okdelete').click(function(e){
        var url = $(".modal-body #url").val();
        e.preventDefault();
        $.ajax({
            url: url,
            type: 'POST',
            data: $('#deleteForm').serialize(),
        });
        location.reload(true);
    });

    var sort_column = function sort_column(e, parameter, url) {
        e.preventDefault();
        var sort = getUrlParameter(parameter);
        var order_by = '';
        var span_class = '';
        if(sort === 'desc'){
            order_by = 'asc'
        }else{
            order_by = 'desc'
        }
        window.location.assign('/' + url + '/?' + parameter + '=' + order_by);
    }

    $('#loans_sortname').click(function(e){
        sort_column(e, 'name','loans');
    });

    $('#loans_sortamount').click(function(e){
        sort_column(e, 'amount','loans');
    });

    $('#loans_sortinterest').click(function(e){
        sort_column(e, 'interest','loans');
    });

    $('#loans_sorttpayable').click(function(e){
        sort_column(e, 'total_payable','loans');
    });

    $('#loans_sorttpayment').click(function(e){
        sort_column(e, 'total_payment','loans');
    });

    $('#loans_sortoutbal').click(function(e){
        sort_column(e, 'outstanding_balance','loans');
    });
});

