// Fix Tabs Js
$(window).scroll(function () {
  if ($(window).scrollTop() >= 150) {
    $(".tab-navigation").addClass("fix-style");
  } else {
    $(".tab-navigation").removeClass("fix-style");
  }
});

// Reset scroll position when a button with class "nav-link" is clicked
$(document).ready(function () {
  $(".nav-link").on("click", function () {
    $("html, body").scrollTop(0);
  });
});

// Feedback button to show form
$(document).ready(function () {
  // Add a click event listener to the button
  $("#showFormButton").on("click", function () {
    // hide the button
    $("#showFormButton").addClass("hide");
    // Add the "show" class to the feedback form
    $("#feedback-form").addClass("show");
  });
});

// Feedback button to hide form
$(document).ready(function () {
  // Add a click event listener to the button
  $("#hideFormButton").on("click", function () {
    // show the button
    $("#showFormButton").removeClass("hide");
    // remove the "show" class to the feedback form
    $("#feedback-form").removeClass("show");
  });
});

