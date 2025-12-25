// Hamburger menu
const hamburger = document.querySelector(".hamburger");
const navbar = document.querySelector(".navbar");

hamburger.addEventListener("click", () => {
    navbar.classList.toggle("active");
});

// Scroll animace
const animatedElements = document.querySelectorAll(".animate");
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add("show");
        }
    });
});
animatedElements.forEach(el => observer.observe(el));

// Vanta.js animace
document.addEventListener("DOMContentLoaded", () => {
  VANTA.WAVES({
      el: "#hero",
      mouseControls: true,
      touchControls: true,
      gyroControls: false,
      color: 0x0070bb,
      shininess: 50,
      waveHeight: 20,
      waveSpeed: 0.8,
      zoom: 0.85
  });
});
