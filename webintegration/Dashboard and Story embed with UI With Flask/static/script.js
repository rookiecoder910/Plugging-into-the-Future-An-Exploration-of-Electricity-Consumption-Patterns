// ─── Navbar Scroll Effect ───────────────────────────────────
const navbar = document.getElementById('navbar');
if (navbar) {
    window.addEventListener('scroll', () => {
        navbar.classList.toggle('scrolled', window.pageYOffset > 10);
    });
}

// ─── Smooth Scroll ─────────────────────────────────────────
document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
        e.preventDefault();
        const t = document.querySelector(a.getAttribute('href'));
        if (t) t.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
});

// ─── Scroll Reveal Animation ──────────────────────────────
const revealEls = document.querySelectorAll(
    '.feature-card, .viz-card, .arch-step, .stat-card, .embed-info-box'
);
const revealObs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            revealObs.unobserve(entry.target);
        }
    });
}, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });

revealEls.forEach((el, i) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = `opacity 0.5s ease ${(i % 6) * 0.06}s, transform 0.5s ease ${(i % 6) * 0.06}s`;
    revealObs.observe(el);
});

// ─── Auto-dismiss flash messages ─────────────────────────
document.querySelectorAll('.flash').forEach(flash => {
    setTimeout(() => {
        flash.style.opacity = '0';
        flash.style.transform = 'translateX(50px)';
        setTimeout(() => flash.remove(), 400);
    }, 5000);
});

// ─── Viz Card Hover Effect ────────────────────────────────
document.querySelectorAll('.viz-card').forEach(card => {
    card.addEventListener('mouseleave', () => {
        card.style.transform = '';
    });
});
