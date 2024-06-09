
// Login/Register Section

document.addEventListener('DOMContentLoaded', function() {
    const login_btn = document.getElementById('login-btn');
    const register_btn = document.getElementById('register-btn');

    login_btn.addEventListener('click', function() {
        window.location.href = "/login";
    });

    register_btn.addEventListener('click', function() {
        window.location.href = "/register";
    });
});