/**
 * Created by yzt on 2017/9/17.
 */
let AUTO_SWITCH_INTERVAL = 8000;
function CarouselSwitch(str){
    let num = parseInt(str);
    let var_current = $('#carousel-current');
    if (!num || num==parseInt(var_current.text())) { return; }
    let window_width = parseInt($(document.body).width());
    $('#carousel-pictures').css({
        "left": -(num-1) * window_width + 'px'
    });
    var_current.html(str);
    let total = parseInt($('#carousel-total').text());
    for (let i = 1; i<=total; i++) {
        let id_str = '#carousel-switch-'+i;
        if (i == num) {
            $(id_str).addClass('active');
        }else{
            $(id_str).removeClass('active');
        }
    }
    clearInterval(auto_switch);
    auto_switch = setInterval(SwitchImage, AUTO_SWITCH_INTERVAL);
}

function SwitchImage(){
    let total = parseInt($('#carousel-total').text());
    let current = parseInt($('#carousel-current').text());
    current += 1;
    if (current > total) { current = 1; }
    CarouselSwitch(current.toString())
}

let auto_switch = setInterval(SwitchImage, AUTO_SWITCH_INTERVAL);