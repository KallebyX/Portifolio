(function() {
  // Modern theme controller with Apple-like transitions
  const ThemeController = {
    init() {
      this.createToggleButton();
      this.initializeTheme();
      this.updateButtonIcon();
    },

    createToggleButton() {
      if (document.getElementById('theme-toggle')) return;
      
      const toggleButton = document.createElement('button');
      toggleButton.id = 'theme-toggle';
      toggleButton.className = 'toggle-theme';
      toggleButton.setAttribute('aria-label', 'Toggle dark mode');
      toggleButton.setAttribute('type', 'button');

      toggleButton.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        const isDark = document.body.classList.contains('dark-mode');
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
        this.updateButtonIcon();
        this.updateGoogleButton();
        
        // Trigger a custom event for other components
        window.dispatchEvent(new CustomEvent('themeChanged', { detail: { isDark } }));
      });

      document.body.appendChild(toggleButton);
    },

    updateButtonIcon() {
      const toggleButton = document.getElementById('theme-toggle');
      if (!toggleButton) return;
      
      const isDark = document.body.classList.contains('dark-mode');
      toggleButton.innerHTML = isDark ? '☀️' : '🌙';
      toggleButton.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
    },

    updateGoogleButton() {
      const googleBtn = document.getElementById('google-login-btn');
      if (googleBtn) {
        const isDark = document.body.classList.contains('dark-mode');
        googleBtn.src = isDark ? '/static/img/google_dark.png' : '/static/img/google_light.png';
      }
    },

    initializeTheme() {
      const savedTheme = localStorage.getItem('theme');
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      
      if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
        document.body.classList.add('dark-mode');
      }
      
      this.updateButtonIcon();
      this.updateGoogleButton();
    }
  };

  // Modern scroll and navigation effects
  const NavigationController = {
    init() {
      this.setupSmoothScrolling();
      this.setupNavbarEffects();
      this.setupActiveLinks();
    },

    setupSmoothScrolling() {
      document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
          e.preventDefault();
          const target = document.querySelector(this.getAttribute('href'));
          if (target) {
            target.scrollIntoView({
              behavior: 'smooth',
              block: 'start'
            });
          }
        });
      });
    },

    setupNavbarEffects() {
      const navbar = document.querySelector('.navbar');
      if (!navbar) return;

      let lastScrollY = window.scrollY;
      const handleScroll = () => {
        const currentScrollY = window.scrollY;
        
        // Add/remove shrink class
        if (currentScrollY > 50) {
          navbar.classList.add('navbar-shrink');
        } else {
          navbar.classList.remove('navbar-shrink');
        }

        lastScrollY = currentScrollY;
      };

      window.addEventListener('scroll', handleScroll, { passive: true });
      handleScroll(); // Initial call
    },

    setupActiveLinks() {
      const currentPath = window.location.pathname;
      const navLinks = document.querySelectorAll('.nav-link');

      navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
          link.classList.add('active');
        } else {
          link.classList.remove('active');
        }
      });
    }
  };

  // Enhanced form controller
  const FormController = {
    currentStep: 1,
    
    init() {
      this.setupFormValidation();
      this.setupStepNavigation();
    },

    setupFormValidation() {
      const forms = document.querySelectorAll('form');
      forms.forEach(form => {
        form.addEventListener('submit', this.handleFormSubmit.bind(this));
        
        // Real-time validation
        const inputs = form.querySelectorAll('input, textarea, select');
        inputs.forEach(input => {
          input.addEventListener('blur', this.validateField.bind(this));
          input.addEventListener('input', this.clearFieldError.bind(this));
        });
      });
    },

    validateField(e) {
      const field = e.target;
      const value = field.value.trim();
      
      // Remove existing error styling
      field.classList.remove('is-invalid');
      
      // Basic validation
      if (field.hasAttribute('required') && !value) {
        this.showFieldError(field, 'Este campo é obrigatório');
        return false;
      }
      
      if (field.type === 'email' && value && !this.isValidEmail(value)) {
        this.showFieldError(field, 'Por favor, insira um email válido');
        return false;
      }
      
      return true;
    },

    clearFieldError(e) {
      const field = e.target;
      field.classList.remove('is-invalid');
      const errorMsg = field.parentNode.querySelector('.invalid-feedback');
      if (errorMsg) {
        errorMsg.remove();
      }
    },

    showFieldError(field, message) {
      field.classList.add('is-invalid');
      
      // Remove existing error message
      const existingError = field.parentNode.querySelector('.invalid-feedback');
      if (existingError) {
        existingError.remove();
      }
      
      // Add new error message
      const errorDiv = document.createElement('div');
      errorDiv.className = 'invalid-feedback';
      errorDiv.textContent = message;
      field.parentNode.appendChild(errorDiv);
    },

    isValidEmail(email) {
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    },

    handleFormSubmit(e) {
      const form = e.target;
      const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
      let isValid = true;

      inputs.forEach(input => {
        if (!this.validateField({ target: input })) {
          isValid = false;
        }
      });

      if (!isValid) {
        e.preventDefault();
        const firstError = form.querySelector('.is-invalid');
        if (firstError) {
          firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
          firstError.focus();
        }
      } else {
        // Show loading state
        const submitBtn = form.querySelector('button[type="submit"]');
        if (submitBtn) {
          const originalText = submitBtn.innerHTML;
          submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Enviando...';
          submitBtn.disabled = true;
          
          // Reset after a delay if form doesn't redirect
          setTimeout(() => {
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
          }, 5000);
        }
      }
    },

    // Multi-step form navigation
    nextStep() {
      const current = document.getElementById(`step-${this.currentStep}`);
      if (!current) return;
      
      // Validate current step
      const inputs = current.querySelectorAll('input[required], textarea[required], select[required]');
      let isValid = true;
      
      inputs.forEach(input => {
        if (!this.validateField({ target: input })) {
          isValid = false;
        }
      });
      
      if (!isValid) return;
      
      current.classList.add('d-none');
      this.currentStep++;
      const next = document.getElementById(`step-${this.currentStep}`);
      if (next) {
        next.classList.remove('d-none');
        next.scrollIntoView({ behavior: 'smooth' });
      }
    },

    prevStep() {
      const current = document.getElementById(`step-${this.currentStep}`);
      if (!current) return;
      
      current.classList.add('d-none');
      this.currentStep--;
      const prev = document.getElementById(`step-${this.currentStep}`);
      if (prev) {
        prev.classList.remove('d-none');
        prev.scrollIntoView({ behavior: 'smooth' });
      }
    }
  };

  // Project filter with smooth animations
  const ProjectFilter = {
    init() {
      this.setupFilters();
    },

    setupFilters() {
      const filterButtons = document.querySelectorAll('.filter-btn');
      filterButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
          const category = e.target.textContent.toLowerCase();
          this.filterProjects(category === 'todos' ? 'todos' : category);
          this.updateActiveFilter(e.target);
        });
      });
    },

    filterProjects(category) {
      const projects = document.querySelectorAll('.project');
      
      projects.forEach(project => {
        const shouldShow = category === 'todos' || project.classList.contains(category);
        
        if (shouldShow) {
          project.style.display = 'block';
          project.style.opacity = '0';
          project.style.transform = 'scale(0.9)';
          
          // Animate in
          setTimeout(() => {
            project.style.transition = 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
            project.style.opacity = '1';
            project.style.transform = 'scale(1)';
          }, 10);
        } else {
          project.style.transition = 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
          project.style.opacity = '0';
          project.style.transform = 'scale(0.9)';
          
          setTimeout(() => {
            project.style.display = 'none';
          }, 300);
        }
      });
    },

    updateActiveFilter(activeButton) {
      document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.remove('active');
      });
      activeButton.classList.add('active');
    }
  };

  // Performance optimizations
  const PerformanceOptimizer = {
    init() {
      this.setupLazyLoading();
      this.setupPageTransitions();
    },

    setupLazyLoading() {
      const images = document.querySelectorAll('img');
      
      if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              const img = entry.target;
              if (img.dataset.src) {
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
              }
              imageObserver.unobserve(img);
            }
          });
        });

        images.forEach(img => {
          if (img.dataset.src) {
            imageObserver.observe(img);
          }
        });
      } else {
        // Fallback for older browsers
        images.forEach(img => {
          if (img.dataset.src) {
            img.src = img.dataset.src;
          }
        });
      }
    },

    setupPageTransitions() {
      // Add smooth page transitions
      document.querySelectorAll('a').forEach(link => {
        if (link.hostname === window.location.hostname && 
            !link.hasAttribute('download') && 
            !link.getAttribute('href').startsWith('#')) {
          
          link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href && href !== '#') {
              e.preventDefault();
              document.body.style.opacity = '0';
              document.body.style.transition = 'opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
              
              setTimeout(() => {
                window.location.href = href;
              }, 300);
            }
          });
        }
      });
    }
  };

  // Initialize everything when DOM is ready
  function initializeApp() {
    // Initialize AOS if available
    if (typeof AOS !== 'undefined') {
      AOS.init({
        duration: 800,
        easing: 'ease-out-cubic',
        once: true,
        offset: 100
      });
    }

    // Initialize all controllers
    ThemeController.init();
    NavigationController.init();
    FormController.init();
    ProjectFilter.init();
    PerformanceOptimizer.init();

    // Handle success modal
    const modalSucesso = document.getElementById('modalSucesso');
    if (modalSucesso && modalSucesso.dataset.show === 'true') {
      new bootstrap.Modal(modalSucesso).show();
    }

    // Listen for theme system changes
    if (window.matchMedia) {
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
        if (!localStorage.getItem('theme')) {
          document.body.classList.toggle('dark-mode', e.matches);
          ThemeController.updateButtonIcon();
        }
      });
    }
  }

  // Expose some methods globally for template compatibility
  window.filterProjects = (category) => ProjectFilter.filterProjects(category);
  window.nextStep = () => FormController.nextStep();
  window.prevStep = () => FormController.prevStep();

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeApp);
  } else {
    initializeApp();
  }

})();