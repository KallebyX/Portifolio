// js/main.js

// AOS Animation Init
AOS.init();

// Scroll suave para âncoras internas (caso queira usar no futuro)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});

// Filtro de projetos (caso seja usado externamente também)
function filterProjects(category) {
  const projects = document.querySelectorAll('.project');
  projects.forEach(project => {
    if (category === 'todos' || project.classList.contains(category)) {
      project.style.display = 'block';
    } else {
      project.style.display = 'none';
    }
  });
}

// Controle de etapas do formulário (pode ser reutilizado)
let currentStep = 1;
function nextStep() {
  document.getElementById(`step-${currentStep}`).classList.remove('active');
  currentStep++;
  document.getElementById(`step-${currentStep}`).classList.add('active');
}
function prevStep() {
  document.getElementById(`step-${currentStep}`).classList.remove('active');
  currentStep--;
  document.getElementById(`step-${currentStep}`).classList.add('active');
}

// Toggle de Tema Claro/Escuro
const toggleButton = document.createElement('button');
toggleButton.innerHTML = "🌓";
toggleButton.id = "theme-toggle";
document.body.appendChild(toggleButton);

toggleButton.style.position = "fixed";
toggleButton.style.bottom = "20px";
toggleButton.style.right = "20px";
toggleButton.style.backgroundColor = "#f0f0f0";
toggleButton.style.border = "none";
toggleButton.style.borderRadius = "50%";
toggleButton.style.width = "40px";
toggleButton.style.height = "40px";
toggleButton.style.cursor = "pointer";
toggleButton.style.boxShadow = "0 2px 6px rgba(0,0,0,0.2)";
toggleButton.style.fontSize = "20px";
toggleButton.style.display = "flex";
toggleButton.style.alignItems = "center";
toggleButton.style.justifyContent = "center";
toggleButton.style.transition = "background-color 0.3s ease";

toggleButton.addEventListener("mouseenter", () => {
  toggleButton.style.backgroundColor = "#ddd";
});
toggleButton.addEventListener("mouseleave", () => {
  toggleButton.style.backgroundColor = "#f0f0f0";
});

toggleButton.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
  localStorage.setItem("theme", document.body.classList.contains("dark-mode") ? "dark" : "light");
});

// Persistência
window.addEventListener("DOMContentLoaded", () => {
  if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark-mode");
  }

  const modalSucesso = document.getElementById("modalSucesso");
  if (modalSucesso && modalSucesso.dataset.show === "true") {
    new bootstrap.Modal(modalSucesso).show();
  }
});