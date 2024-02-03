// // This function will animate the header when the user scrolls down the page.
// function animateHeader() {
//     var header = document.getElementById("header");
//     var offset = window.scrollY;
//     if (offset > 0) {
//       header.style.transform = "translateY(" + offset + "px)";
//     } else {
//       header.style.transform = "translateY(0px)";
//     }
//   }
  
//   // This function will add a smooth scroll to the links in the navigation bar.
//   function smoothScroll(e) {
//     e.preventDefault();
//     var target = e.target.getAttribute("href");
//     var offset = target.offsetTop;
//     window.scrollTo(0, offset);
//   }
  
//   // This function will add a fade effect to the testimonials when the user scrolls over them.
//   function fadeTestimonials() {
//     var testimonials = document.querySelectorAll(".testimonial");
//     for (var i = 0; i < testimonials.length; i++) {
//       testimonials[i].addEventListener("mouseover", function() {
//         this.style.opacity = "0.8";
//       });
//       testimonials[i].addEventListener("mouseleave", function() {
//         this.style.opacity = "1";
//       });
//     }
//   }
  
//   // This function will initialize the JavaScript code.
//   window.onload = function() {
//     animateHeader();
//     smoothScroll();
//     fadeTestimonials();
//   };
  // Add a fade in animation to the header when the page loads.
window.onload = function() {
    document.getElementById("header").classList.add("fade-in");
  };
  
  // Add a slide down animation to the testimonials when the user scrolls to the bottom of the page.
  window.onscroll = function() {
    if (window.scrollY > 500) {
      document.getElementById("testimonials").classList.add("slide-down");
    } else {
      document.getElementById("testimonials").classList.remove("slide-down");
    }
  };
  
  // Add a dark theme to the website when the user clicks on the "Dark Mode" button.
  document.getElementById("dark-mode").addEventListener("click", function() {
    document.body.classList.toggle("dark-mode");
  });
  