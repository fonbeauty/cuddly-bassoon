const togglePassword = document.getElementById("togglePassword");
const loginForm = document.getElementById('login-form');
const errorMessageDiv = document.getElementById('error-message');
const username = document.getElementById('username')
const password = document.getElementById('password')

togglePassword.addEventListener("click", function () {
    // toggle the type attribute
    const type = password.getAttribute("type") === "password" ? "text" : "password";
    password.setAttribute("type", type);
    // toggle the icon
    this.classList.toggle("bi-eye");
});

// prevent form submit
const form = document.querySelector("form");
form.addEventListener('submit', function (e) {
    e.preventDefault();
});


loginForm.addEventListener('submit', (e) => {
    e.preventDefault();

    if (username.value === 'admin' && password.value === 'admin') {
        window.open("admin.html"); // redirect to another page
    }
    else if (username.value === 'user' && password.value === 'user') {
        // alert('Login successful!');
        window.open("main.html"); // redirect to another page
    } else {
        errorMessageDiv.style.color = "red"
        errorMessageDiv.textContent = 'Invalid username or password';
    }
});


let openedWindow;

function openWindow() {
    openedWindow = window.open("admin.html");
}

function closeOpenedWindow() {
    openedWindow.close();
}