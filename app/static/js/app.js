/**
 * Created by maoxie on 2017/9/14.
 */
$('.navbar-item').bind({
    'mouseenter': showMenu,
    'mouseleave': hideMenu
});
function showMenu(e){
    let menu = $(this).find('.navbar-menu');
    if (!menu) { return; }
    menu.css({
        "visibility": 'visible'
    });
}
function hideMenu(e){
    let menu = $(this).find('.navbar-menu');
    if (!menu) { return; }
    menu.css({
        "visibility": 'hidden'
    });
}