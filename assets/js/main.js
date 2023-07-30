// Fix Tabs Js
$(window).scroll(function () {
    if ($(window).scrollTop() >= 150) {
      $(".tab-navigation").addClass("fix-style");
    } else {
      $(".tab-navigation").removeClass("fix-style");
    }
  });
