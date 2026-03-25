document.addEventListener("DOMContentLoaded", () => {
    initializeLoader();
    initializeNavigation();
    initializeThemeToggle();
    initializeMobileMenu();
    initializeBackToTop();
    initializeRevealAnimations();
    initializeContactForm();
});

function initializeLoader() {
    const loader = document.getElementById("loading-screen");
    if (!loader) {
        return;
    }

    const hideLoader = () => {
        if (!loader.parentNode) {
            return;
        }
        loader.classList.add("hidden");
        window.setTimeout(() => {
            if (loader.parentNode) {
                loader.remove();
            }
        }, 350);
    };

    if (document.readyState === "complete") {
        hideLoader();
    } else {
        window.addEventListener("load", hideLoader, { once: true });
        window.setTimeout(hideLoader, 1200);
    }
}

function initializeNavigation() {
    const navbar = document.getElementById("navbar");
    const currentPath = normalizePath(window.location.pathname);

    document.querySelectorAll(".nav-link").forEach((link) => {
        const linkPath = normalizePath(new URL(link.href, window.location.origin).pathname);
        if (linkPath === currentPath) {
            link.classList.add("active");
        }
    });

    const syncNavbar = () => {
        if (!navbar) {
            return;
        }
        navbar.classList.toggle("scrolled", window.scrollY > 12);
    };

    syncNavbar();
    window.addEventListener("scroll", syncNavbar, { passive: true });
}

function initializeThemeToggle() {
    const toggle = document.getElementById("theme-toggle");
    if (!toggle) {
        return;
    }

    const icon = toggle.querySelector("i");
    const label = toggle.querySelector(".theme-toggle-label");
    const preferredTheme = window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    const savedTheme = localStorage.getItem("portfolio-theme") || preferredTheme;

    applyTheme(savedTheme, icon, label);

    toggle.addEventListener("click", () => {
        const currentTheme = document.documentElement.getAttribute("data-theme") || "light";
        const nextTheme = currentTheme === "dark" ? "light" : "dark";
        localStorage.setItem("portfolio-theme", nextTheme);
        applyTheme(nextTheme, icon, label);
    });
}

function initializeMobileMenu() {
    const toggle = document.getElementById("mobile-menu-toggle");
    const panel = document.getElementById("nav-panel");

    if (!toggle || !panel) {
        return;
    }

    const closePanel = () => {
        panel.classList.remove("active");
        toggle.setAttribute("aria-expanded", "false");
    };

    toggle.addEventListener("click", () => {
        const isOpen = panel.classList.toggle("active");
        toggle.setAttribute("aria-expanded", String(isOpen));
    });

    document.querySelectorAll(".nav-link").forEach((link) => {
        link.addEventListener("click", closePanel);
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            closePanel();
        }
    });
}

function initializeBackToTop() {
    const button = document.getElementById("back-to-top");
    if (!button) {
        return;
    }

    const sync = () => {
        button.classList.toggle("visible", window.scrollY > 360);
    };

    sync();
    window.addEventListener("scroll", sync, { passive: true });
    button.addEventListener("click", () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });
}

function initializeRevealAnimations() {
    const items = document.querySelectorAll("[data-reveal]");
    if (items.length === 0) {
        return;
    }

    if (!("IntersectionObserver" in window)) {
        items.forEach((item) => item.classList.add("is-visible"));
        return;
    }

    const observer = new IntersectionObserver((entries, currentObserver) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-visible");
                currentObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.18 });

    items.forEach((item) => observer.observe(item));
}

function initializeContactForm() {
    const form = document.getElementById("contact-form");
    const statusBox = document.getElementById("contact-form-status");
    if (!form || !statusBox) {
        return;
    }

    const submitButton = form.querySelector('button[type="submit"]');
    const originalText = submitButton ? submitButton.innerHTML : "";

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const formData = new FormData(form);
        const payload = {
            name: String(formData.get("name") || "").trim(),
            email: String(formData.get("email") || "").trim(),
            subject: String(formData.get("subject") || "").trim(),
            message: String(formData.get("message") || "").trim(),
        };

        if (!payload.name || !payload.email || !payload.message) {
            showFormStatus(statusBox, "Please fill in your name, email, and message.", "error");
            return;
        }

        if (submitButton) {
            submitButton.disabled = true;
            submitButton.innerHTML = "Sending...";
        }

        try {
            const response = await fetch("/api/contact", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload),
            });

            const result = await response.json();
            if (!response.ok) {
                throw new Error(result.message || "Unable to send message.");
            }

            form.reset();
            showFormStatus(statusBox, result.message, "success");
            showNotification("Message sent successfully.", "success");
        } catch (error) {
            const message = error instanceof Error ? error.message : "Unable to send message.";
            showFormStatus(statusBox, message, "error");
            showNotification(message, "error");
        } finally {
            if (submitButton) {
                submitButton.disabled = false;
                submitButton.innerHTML = originalText;
            }
        }
    });
}

function applyTheme(theme, icon, label) {
    document.documentElement.setAttribute("data-theme", theme);

    if (icon) {
        icon.className = theme === "dark" ? "fas fa-sun" : "fas fa-moon";
    }

    if (label) {
        label.textContent = theme === "dark" ? "Light" : "Dark";
    }
}

function normalizePath(pathname) {
    if (!pathname || pathname === "/") {
        return "/";
    }
    return pathname.replace(/\/+$/, "");
}

function showFormStatus(element, message, type) {
    element.textContent = message;
    element.className = `form-status is-visible ${type}`;
}

function showNotification(message, type) {
    const notification = document.createElement("div");
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    document.body.appendChild(notification);

    window.setTimeout(() => {
        notification.remove();
    }, 2800);
}
