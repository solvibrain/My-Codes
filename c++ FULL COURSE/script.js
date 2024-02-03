// script.js

// Custom JavaScript code goes here

// Example: Smooth scrolling on navigation link click
$(document).ready(function() {
    $('.nav-link').on('click', function(e) {
      e.preventDefault();
  
      var target = $(this).attr('href');
      var offset = $(target).offset().top;
  
      $('html, body').animate({
        scrollTop: offset
      }, 500);
    });
  });
  