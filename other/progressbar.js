var NUM_SECONDS = 5;
var pbId = '#pb_identifier';
var stepUpdate = NUM_SECONDS*10;

var progress = 0;
var timer = setInterval(updateProgressBar, stepUpdate);

function updateProgressBar(){
    $(pbId).progressbar({
        value: ++progress
    });
    if(progress == 100)
        clearInterval(timer);
}

$(function () {
    $(pbId).progressbar({
        value: progress
    });
});