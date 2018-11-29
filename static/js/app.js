$(document).foundation()


/* HOUR INCREMENTATION AND DECREMENTATION */

$('#inch').click(function()
{
    var $input = $(this).parents('.clock').find('.hrs');
    var val = parseInt($input.val(), 10);
    if (val == 23)
    { $input.val(0); }
    else
    { $input.val(val + 1); }
});
  
$('#dech').click(function()
{
    var $input = $(this).parents('.clock').find('.hrs');
    var val = parseInt($input.val(), 10);
    if (val == 0)
    { $input.val(23); }
    else
    { $input.val(val - 1); }
});


/* MINUTE INCREMENTATION AND DECREMENTATION */

$('#incm').click(function()
{
    var $input = $(this).parents('.clock').find('.mins');
    var val = parseInt($input.val(), 10);
    if (val == 55)
    { $input.val(0); }
    else
    { $input.val(val + 5); }
});
  
$('#decm').click(function()
{
    var $input = $(this).parents('.clock').find('.mins');
    var val = parseInt($input.val(), 10);
    if (val == 0)
    { $input.val(55); }
    else
    { $input.val(val - 5); }
});


/* SAVE CONFIRMATION NOTIFICATION */

$('#submit').click(function(e)
{
    e.preventDefault();
    document.getElementById("save").style.display = "block";
    setTimeout(function(){
        $('#save').fadeOut('slow');
    }, 750);
});