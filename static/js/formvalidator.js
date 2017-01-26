$(document).ready(function(){

  $('#amount').change(function(){
      var nummonths = get_nummonths();
      var percent = (parseFloat($("#interest").val()) * parseFloat(nummonths)) / 100;
      var amount = $('#amount').val();
      var t_pay = parseFloat(amount) + parseFloat(amount * percent);
      if(t_pay){
        $('#t_payable').val(t_pay);
        $('#t_payment').change();
      }
  });

  $('#interest').change(function(){
      var nummonths = get_nummonths();
      var percent = (parseFloat($("#interest").val()) * parseFloat(nummonths)) / 100;
      var amount = $('#amount').val();
      var t_pay = parseFloat(amount) + parseFloat(amount * percent);
      if(t_pay){
        $('#t_payable').val(t_pay);
        $('#t_payment').change();
      }
  });

  $('#payment').change(function(){
     var tpayment = parseFloat($('#totalpayment_hv').val());
     var payment = parseFloat($('#payment').val());
     if(tpayment){
         payment += parseFloat(tpayment);
     }
     if(payment){
        $('#t_payment').val(payment);
        $('#t_payment').change();
     }
  });

  $('#t_payment').change(function(){
      try{
          var tpayable = parseFloat($('#t_payable').val());
          var tpayment = parseFloat($('#t_payment').val());
          if(!tpayment){
            $('#outs_bal').val(tpayable);
          }else if(tpayable && tpayment){
              $('#outs_bal').val(tpayable - tpayment);
          }
      }catch(err){
          alert("error: " + err.message);
      }
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

    $('ul.nav > li > a[href="' + document.location.pathname + '"]').parent().addClass('active');

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

    $('.confirmDeleteUser').click(function(){
      if(confirm('Are you sure you want to remove this record?') == true){
          alert('id: ' + $(this).data('id'));
      }
    });

});

