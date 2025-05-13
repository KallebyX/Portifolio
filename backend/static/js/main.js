(function() {
  // AOS Animation Init
  AOS.init();

  // Scroll suave para âncoras internas
  (function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
          behavior: 'smooth'
        });
      });
    });
  })();

  // Filtro de projetos
  const projectFilter = {
    filter: function(category) {
      const projects = document.querySelectorAll('.project');
      projects.forEach(project => {
        project.style.display = (category === 'todos' || project.classList.contains(category)) ? 'block' : 'none';
      });
    }
  };

  // Controle de etapas do formulário
  let currentStep = 1;
  const formSteps = {
    next: function() {
      const current = document.getElementById(`step-${currentStep}`);
      if (!current) return;
      current.classList.remove('active');
      currentStep++;
      const next = document.getElementById(`step-${currentStep}`);
      if (!next) return;
      next.classList.add('active');
    },
    prev: function() {
      const current = document.getElementById(`step-${currentStep}`);
      if (!current) return;
      current.classList.remove('active');
      currentStep--;
      const prev = document.getElementById(`step-${currentStep}`);
      if (!prev) return;
      prev.classList.add('active');
    }
  };

  // Dark Mode Controller
  const darkModeController = {
    updateButtonIcon: function() {
      const toggleButton = document.getElementById('theme-toggle');
      if (!toggleButton) return;
      toggleButton.innerHTML = document.body.classList.contains('dark-mode') ? '🌙' : '☀️';
    },
    updateGoogleButton: function() {
      const googleBtn = document.getElementById('google-login-btn');
      if (googleBtn) {
        googleBtn.src = document.body.classList.contains('dark-mode') ? '/static/img/google_dark.png' : '/static/img/google_light.png';
      }
    },
    createToggleButton: function() {
      const toggleButton = document.createElement('button');
      toggleButton.id = 'theme-toggle';
      Object.assign(toggleButton.style, {
        position: 'fixed',
        bottom: '20px',
        right: '20px',
        backgroundColor: '#f0f0f0',
        border: 'none',
        borderRadius: '50%',
        width: '40px',
        height: '40px',
        cursor: 'pointer',
        boxShadow: '0 2px 6px rgba(0,0,0,0.2)',
        fontSize: '20px',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        transition: 'background-color 0.3s ease'
      });

      toggleButton.addEventListener('mouseenter', () => toggleButton.style.backgroundColor = '#ddd');
      toggleButton.addEventListener('mouseleave', () => toggleButton.style.backgroundColor = '#f0f0f0');
      toggleButton.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        localStorage.setItem('theme', document.body.classList.contains('dark-mode') ? 'dark' : 'light');
        darkModeController.updateButtonIcon();
        darkModeController.updateGoogleButton();
      });

      document.body.appendChild(toggleButton);
    },
    initializeTheme: function() {
      if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-mode');
      }
      this.updateButtonIcon();
      this.updateGoogleButton();
    }
  };

  // Executar ao carregar a página
  window.addEventListener('DOMContentLoaded', () => {
    darkModeController.createToggleButton();
    darkModeController.initializeTheme();

    const modalSucesso = document.getElementById('modalSucesso');
    if (modalSucesso && modalSucesso.dataset.show === 'true') {
      new bootstrap.Modal(modalSucesso).show();
    }
  });

  // Expor alguns métodos globais para uso nos templates (opcional)
  window.filterProjects = projectFilter.filter;
  window.nextStep = formSteps.next;
  window.prevStep = formSteps.prev;

})();