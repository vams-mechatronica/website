/**
* Template Name: Arsha
* Template URL: https://bootstrapmade.com/arsha-free-bootstrap-html-template-corporate/
* Updated: Feb 22 2025 with Bootstrap v5.3.3
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

(function () {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  if (mobileNavToggleBtn) {
    mobileNavToggleBtn.addEventListener('click', mobileNavToogle);
  }

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
    navmenu.addEventListener('click', function (e) {
      e.preventDefault();
      this.parentNode.classList.toggle('active');
      this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
      e.stopImmediatePropagation();
    });
  });

  /**
   * Preloader
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  scrollTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  /**
   * Initiate glightbox
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function (swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  window.addEventListener("load", initSwiper);

  /**
   * Frequently Asked Questions Toggle
   */
  document.querySelectorAll('.faq-item h3, .faq-item .faq-toggle').forEach((faqItem) => {
    faqItem.addEventListener('click', () => {
      faqItem.parentNode.classList.toggle('faq-active');
    });
  });

  /**
   * Animate the skills items on reveal
   */
  let skillsAnimation = document.querySelectorAll('.skills-animation');
  skillsAnimation.forEach((item) => {
    new Waypoint({
      element: item,
      offset: '80%',
      handler: function (direction) {
        let progress = item.querySelectorAll('.progress .progress-bar');
        progress.forEach(el => {
          el.style.width = el.getAttribute('aria-valuenow') + '%';
        });
      }
    });
  });

  /**
   * Init isotope layout and filters
   */
  document.querySelectorAll('.isotope-layout').forEach(function (isotopeItem) {
    let layout = isotopeItem.getAttribute('data-layout') ?? 'masonry';
    let filter = isotopeItem.getAttribute('data-default-filter') ?? '*';
    let sort = isotopeItem.getAttribute('data-sort') ?? 'original-order';

    let initIsotope;
    imagesLoaded(isotopeItem.querySelector('.isotope-container'), function () {
      initIsotope = new Isotope(isotopeItem.querySelector('.isotope-container'), {
        itemSelector: '.isotope-item',
        layoutMode: layout,
        filter: filter,
        sortBy: sort
      });
    });

    isotopeItem.querySelectorAll('.isotope-filters li').forEach(function (filters) {
      filters.addEventListener('click', function () {
        isotopeItem.querySelector('.isotope-filters .filter-active').classList.remove('filter-active');
        this.classList.add('filter-active');
        initIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        if (typeof aosInit === 'function') {
          aosInit();
        }
      }, false);
    });

  });

  /**
   * Correct scrolling position upon page load for URLs containing hash links.
   */
  window.addEventListener('load', function (e) {
    if (window.location.hash) {
      if (document.querySelector(window.location.hash)) {
        setTimeout(() => {
          let section = document.querySelector(window.location.hash);
          let scrollMarginTop = getComputedStyle(section).scrollMarginTop;
          window.scrollTo({
            top: section.offsetTop - parseInt(scrollMarginTop),
            behavior: 'smooth'
          });
        }, 100);
      }
    }
  });

  /**
   * Navmenu Scrollspy
   */
  let navmenulinks = document.querySelectorAll('.navmenu a');

  function navmenuScrollspy() {
    navmenulinks.forEach(navmenulink => {
      if (!navmenulink.hash) return;
      let section = document.querySelector(navmenulink.hash);
      if (!section) return;
      let position = window.scrollY + 200;
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        document.querySelectorAll('.navmenu a.active').forEach(link => link.classList.remove('active'));
        navmenulink.classList.add('active');
      } else {
        navmenulink.classList.remove('active');
      }
    })
  }
  window.addEventListener('load', navmenuScrollspy);
  document.addEventListener('scroll', navmenuScrollspy);


  function showMessage(element, message) {
    element.textContent = message;
    element.style.display = "block";
    
    setTimeout(() => {
        element.classList.add("fade-out");
        setTimeout(() => {
            element.style.display = "none";
            element.classList.remove("fade-out");
        }, 1000);
    }, 3000);
}

  // contact-us form 
  document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".php-email-form");
    const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]")?.value;
    const subscribeForm = document.querySelector(".subscribe-to-newsletter").closest("form");
    const subscribedEmailForm = document.querySelector("#subscribe-to-email-base");

    function displayDjangoMessage(type, message) {
      const messageContainer = document.createElement("div");
      messageContainer.className = `alert alert-${type}`;
      messageContainer.textContent = message;
      document.body.prepend(messageContainer);
      setTimeout(() => messageContainer.remove(), 5000);
  }


    if (form) {

      form.addEventListener("submit", async function (event) {
        event.preventDefault();
        event.stopPropagation(); // Prevent bubbling issues

        const formData = {
          name: document.getElementById("name-field").value,
          email: document.getElementById("email-field").value,
          subject: document.getElementById("subject-field").value,
          message: document.getElementById("message-field").value
        };

        try {
          const response = await fetch("api/contact-us/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": csrftoken
            },
            body: JSON.stringify(formData)
          });

          if (response.ok) {
            console.log("Form submitted successfully!");
            document.querySelector(".sent-message").style.display = "block";
            form.reset();
          } else {
            console.error("Server error:", response.status);
            document.querySelector(".error-message").innerText = "Failed to submit the form.";
            document.querySelector(".error-message").style.display = "block";
          }
        } catch (error) {
          console.error("Fetch error:", error);
          document.querySelector(".error-message").innerText = "An error occurred. Please try again.";
          document.querySelector(".error-message").style.display = "block";
        }
      });
    }

    if (subscribeForm) {
      subscribeForm.addEventListener("submit", async function (event) {
        event.preventDefault();

        const emailInput = subscribeForm.querySelector("input[name='email']");
        const email = emailInput.value;
        const submitButton = subscribeForm.querySelector("button[type='submit']");

        submitButton.disabled = true;

        try {
          const response = await fetch("api/subscribe-to-newsletter/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": csrftoken
            },
            body: JSON.stringify({ email })
          });
          const data = await response.json();

          submitButton.disabled = false;

          if (response.ok) {
            const successMessage = document.querySelector(".subscribed-message");
            showMessage(successMessage, "Thanks for Subscribing!");
            emailInput.value = "";
          } else {
            const errorMessage = document.querySelector(".error-subscribed-message");
            showMessage(errorMessage, "Subscription failed. Please try again.");
            
          }
        } catch (error) {
          submitButton.disabled = false;
          const errorMessage = document.querySelector(".error-subscribed-message");
          showMessage(errorMessage, "Subscription failed. Please try again.");
        }
      });
    }

    if (subscribedEmailForm) {
      subscribedEmailForm.addEventListener("submit", async function (event) {
          event.preventDefault(); // Prevent page reload
          
          // const formData = new FormData(subscribedEmailForm);
          const emailInput = subscribedEmailForm.querySelector("input[name='email']");
          const email = emailInput.value;
          const submitButton = subscribedEmailForm.querySelector("input[type='submit']");
          // const loadingMessage = subscribedEmailForm.querySelector(".loading");
          const errorMessage = subscribedEmailForm.querySelector(".error-message");
          const successMessage = subscribedEmailForm.querySelector(".sent-message");

          // Show loading state
          // loadingMessage.style.display = "block";
          errorMessage.style.display = "none";
          successMessage.style.display = "none";
          submitButton.disabled = true;

          try {
              const response = await fetch("api/subscribe-to-newsletter/", {
                  method: "POST",
                  headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken
                  },
                  body: JSON.stringify({ email })
              });

              const data = await response.json();
              // loadingMessage.style.display = "none";
              submitButton.disabled = false;

              if (response.ok) {
                  successMessage.style.display = "block";
                  emailInput.value = ""; // Clear input field
                  setTimeout(() => {
                      successMessage.style.display = "none";
                  }, 3000); // Auto-hide success message after 3 seconds
              } else {
                  errorMessage.style.display = "block";
                  errorMessage.textContent = data.error || "Subscription failed. Please try again.";
                  setTimeout(() => {
                      errorMessage.style.display = "none";
                  }, 3000); // Auto-hide error message after 3 seconds
              }
          } catch (error) {
              // loadingMessage.style.display = "none";
              submitButton.disabled = false;
              errorMessage.style.display = "block";
              errorMessage.textContent = "Failed to subscribe. Please try again.";
              setTimeout(() => {
                  errorMessage.style.display = "none";
              }, 3000);
          }
      });
  }
  });




})();