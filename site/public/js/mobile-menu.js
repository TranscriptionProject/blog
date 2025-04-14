// Mobile Menu JavaScript
document.addEventListener('DOMContentLoaded', function() {
  // Get the toggle button and mobile nav elements
  const mobileToggle = document.querySelector('.mobile-toggle');
  const mobileNav = document.querySelector('#mobile-nav');
  const body = document.body;
  
  if (mobileToggle && mobileNav) {
    // Toggle menu when hamburger is clicked
    mobileToggle.addEventListener('click', function(e) {
      e.preventDefault();
      mobileToggle.classList.toggle('active');
      mobileNav.classList.toggle('open');
      
      // Toggle class on body to adjust padding when menu is open
      body.classList.toggle('nav-open');
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
      const isClickInside = mobileToggle.contains(event.target) || 
                           mobileNav.contains(event.target);
      
      if (!isClickInside && mobileNav.classList.contains('open')) {
        mobileToggle.classList.remove('active');
        mobileNav.classList.remove('open');
        body.classList.remove('nav-open');
      }
    });
    
    // Close menu on window resize if screen becomes larger than mobile breakpoint
    window.addEventListener('resize', function() {
      if (window.innerWidth > 767 && mobileNav.classList.contains('open')) {
        mobileToggle.classList.remove('active');
        mobileNav.classList.remove('open');
        body.classList.remove('nav-open');
      }
    });
    
    // Close menu when clicking a link in the mobile menu
    const mobileNavLinks = mobileNav.querySelectorAll('a');
    mobileNavLinks.forEach(function(link) {
      link.addEventListener('click', function() {
        mobileToggle.classList.remove('active');
        mobileNav.classList.remove('open');
        body.classList.remove('nav-open');
      });
    });
  }
});