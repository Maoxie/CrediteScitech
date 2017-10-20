/**
 * Created by maoxie on 2017/9/14.
 */
$('.with-menu').bind({
    'mouseenter': showMenu,
    'mouseleave': hideMenu
});
function showMenu(e){
    let menu = $(this).find('.navbar-menu');
    if (!menu) { return; }
    menu.css({
        "height": "0px",
        "opacity": "0",
        "display": "block"
    });
    menu.animate({
        "height": "300px",
        "opacity": "1"
    },250);
}
function hideMenu(e){
    let menu = $(this).find('.navbar-menu');
    if (!menu) { return; }
    // menu.css({
    //     "visibility": 'hidden'
    // });
    menu.fadeOut();
}
$(document).ready(function(){
    let back_button = $("#back-to-top-button");
    back_button.hide();//隐藏go to top按钮
    $(function(){
        $(window).scroll(function(){
            if($(this).scrollTop()>20){//当window的scrolltop距离大于20时，back-to-top-button淡出，反之淡入
                back_button.fadeIn();
            } else {
                back_button.fadeOut();
            }
        });
    });
    // 给back-to-top-button一个点击事件
    back_button.click(function(){
        $("html,body").animate({scrollTop:0}, 200);//点击按钮时，以800的速度回到顶部，这里的800可以根据你的需求修改
        return false;
    });
    // 根据当前页面，改变navibar的高亮
    let current_page = eval($('#level-1-index').html()) || 0;
    $('#header-navibar').find('.navbar-button').each(function (i) {
        if (eval($(this).attr('data-index')) === current_page) {
            $(this).addClass('active');
        }
    });
});
