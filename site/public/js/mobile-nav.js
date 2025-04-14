// Mobile navigation toggle functionality
document.addEventListener('DOMContentLoaded', function() {
  // Get the toggle button and navbar elements
  const navToggle = document.querySelector('.navbar-toggle');
  const navbarCollapse = document.querySelector('#huxblog_navbar .navbar-collapse');
  
  // Toggle the menu when the hamburger button is clicked
  if (navToggle) {
    navToggle.addEventListener('click', function(e) {
      e.preventDefault();
      navToggle.classList.toggle('active');
      navbarCollapse.classList.toggle('in');
    });
  }
  
  // Close mobile menu when clicking outside of it
  document.addEventListener('click', function(event) {
    const isClickInside = navToggle.contains(event.target) || 
                          navbarCollapse.contains(event.target);
    
    if (!isClickInside && navbarCollapse.classList.contains('in')) {
      navToggle.classList.remove('active');
      navbarCollapse.classList.remove('in');
    }
  });
  
  // Close menu on window resize if screen becomes larger than mobile breakpoint
  window.addEventListener('resize', function() {
    if (window.innerWidth > 767 && navbarCollapse.classList.contains('in')) {
      navToggle.classList.remove('active');
      navbarCollapse.classList.remove('in');
    }
  });
});