// Get the form and its elements
const form = document.getElementById('registration-form');
const usernameInput = document.getElementById('username');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirm-password');
const togglePassword = document.getElementById("togglePassword");
const toggleConfirmPassword = document.getElementById("toggleConfirmPassword");
const password = document.getElementById('password')
const confirmPassword = document.getElementById('confirm-password')


togglePassword.addEventListener("click", function () {
    // toggle the type attribute
    const type = password.getAttribute("type") === "password" ? "text" : "password";
    password.setAttribute("type", type);
    // toggle the icon
    this.classList.toggle("bi-eye");
});


toggleConfirmPassword.addEventListener("click", function () {
    // toggle the type attribute
    const type = confirmPassword.getAttribute("type") === "password" ? "text" : "password";
    confirmPassword.setAttribute("type", type);
    // toggle the icon
    this.classList.toggle("bi-eye");
});
// prevent form submit
// const form = document.querySelector("form");
// form.addEventListener('submit', function (e) {
//     e.preventDefault();
// });


// Store entered data in local storage
form.addEventListener('submit', (e) => {
    e.preventDefault();
    const userData = {
        username: usernameInput.value,
        email: emailInput.value,
        password: passwordInput.value,
        confirmPassword: confirmPasswordInput.value,
    };
    localStorage.setItem('userData', JSON.stringify(userData));
});

// Validate form data
form.addEventListener('input', (e) => {
    if (!usernameInput.validity.valid || !emailInput.validity.valid || !passwordInput.validity.valid || !confirmPasswordInput.validity.valid) {
        // If any field is invalid, display error message
        const errorMessage = document.getElementById('error-message');
        errorMessage.textContent = 'Please fill out all fields correctly.';
        errorMessage.style.display = 'block';
    } else {
        // If form data is valid, hide error message
        const errorMessage = document.getElementById('error-message');
        errorMessage.style.display = 'none';
    }
});

// Check if password and confirm password match
passwordInput.addEventListener('input', (e) => {
    if (passwordInput.value !== confirmPasswordInput.value) {
        // If passwords don't match, display error message
        const passwordError = document.getElementById('password-error');
        passwordError.textContent = 'Passwords do not match.';
        passwordError.style.display = 'block';
    } else {
        // If passwords match, hide error message
        const passwordError = document.getElementById('password-error');
        passwordError.style.display = 'none';
    }
});