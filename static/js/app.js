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
    //e.preventDefault();
    document.getElementById("save").style.display = "block";
    setTimeout(function(){
        $('#save').fadeOut('slow');
    }, 750);
});


/* SETTING MANIPULATION */

function del(obj)
{
    var week = [
        obj.parentNode.parentNode.previousElementSibling.children[0].children[0].children[0].children[0].children[1].attributes.style.value,
        obj.parentNode.parentNode.previousElementSibling.children[0].children[0].children[0].children[1].children[1].attributes.style.value,
        obj.parentNode.parentNode.previousElementSibling.children[0].children[0].children[0].children[2].children[1].attributes.style.value,
        obj.parentNode.parentNode.previousElementSibling.children[0].children[0].children[0].children[3].children[1].attributes.style.value,
        obj.parentNode.parentNode.previousElementSibling.children[0].children[0].children[0].children[4].children[1].attributes.style.value,
        obj.parentNode.parentNode.previousElementSibling.children[0].children[0].children[0].children[5].children[1].attributes.style.value,
        obj.parentNode.parentNode.previousElementSibling.children[0].children[0].children[0].children[6].children[1].attributes.style.value
    ];

    var days = [];
    for (i = 0; i < week.length; ++i)
    {
        if (week[i] == "border-color: #f26816; color: #f26816;")
        { days.push(String(i)); }
    }
    
    var clock = obj.parentNode.parentNode.previousElementSibling.children[2].innerText;
    var time = clock.split(":");

    var seek = {'purpose': 'del', 'data': {'days': days, 'hrs': time[0], 'mins': time[1]}};
    var req = new XMLHttpRequest();

    req.open('POST', '/', true);

    req.onreadystatechange = function()
    {
        if(req.readyState == 4 && req.status == 200)
        { location.reload(); }
    }

    req.send(JSON.stringify(seek));
}