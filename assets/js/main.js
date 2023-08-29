// Fix Tabs Js
$(window).scroll(function () {
    if ($(window).scrollTop() >= 150) {
      $(".tab-navigation").addClass("fix-style");
    } else {
      $(".tab-navigation").removeClass("fix-style");
    }
  });

    // Reset scroll position when a button with class "nav-link" is clicked
  $(document).ready(function() {
    $(".nav-link").on("click", function() {
      $("html, body").scrollTop(0);
    });
  });
