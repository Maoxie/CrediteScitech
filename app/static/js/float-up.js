/**
 * Created by yzt on 2017/10/20.
 */
$(document).ready(function() {
    $(".float-up").css({
        "opacity": "0"
    });
    $(window).trigger("scroll");
});
$(window).scroll(function() {
    $(".float-up").each(function(i) {
        let top_of_object, bottom_of_object, bottom_of_window, top_of_window;
        // bottom_of_object = $(this).position().top + $(this).outerHeight();
        top_of_object = $(this).offset().top;
        bottom_of_object = top_of_object + $(this).outerHeight();
        top_of_window = $(window).scrollTop();
        bottom_of_window = top_of_window + $(window).height();
        let this_top = $(this).position().top;
        if (bottom_of_window > top_of_object && top_of_window < bottom_of_object) {
            $(this).css({
               "top": this_top + 200
            });
            $(this).animate({
                "opacity": "1",
                "top": this_top
            }, 600);
            $(this).removeClass("float-up");
        }
    })
});
