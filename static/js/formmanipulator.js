$(document).ready(function(){
    setCheckBoxValue('#can_create','#can_create_hv');
    setCheckBoxValue('#can_update','#can_update_hv');
    setCheckBoxValue('#can_delete','#can_delete_hv');

    $('#can_create').click(function()
    {
        setHiddenCheckBox('#can_create','#can_create_hv');
    });

    $('#can_update').click(function()
    {
        setHiddenCheckBox('#can_update','#can_update_hv');
    });

    $('#can_delete').click(function()
    {
        setHiddenCheckBox('#can_delete','#can_delete_hv');
    });

    function setHiddenCheckBox(checkbox, hidden){
        if($(checkbox).is(':checked')){
            $(hidden).val(1);
        }else{
            $(hidden).val(0);
        }
    }

    function setCheckBoxValue(checkbox, hidden){
        if($(hidden).val() === '1'){
            $(checkbox).prop('checked', true);
        }
    }
 });