const togglePassword = document.getElementById("togglePassword");
const loginForm = document.getElementById('login-form');
const errorMessageDiv = document.getElementById('error-message');
const username = document.getElementById('username');
const password = document.getElementById('password');
const showHelp = document.getElementById("showHelp");

togglePassword.addEventListener("click", function () {
    // toggle the type attribute
    const type = password.getAttribute("type") === "password" ? "text" : "password";
    password.setAttribute("type", type);
    // toggle the icon
    this.classList.toggle("bi-eye");
});

showHelp.addEventListener("click", function () {
    showHelpWindow()
});

// prevent form submit
const form = document.querySelector("form");
form.addEventListener('submit', function (e) {
    e.preventDefault();
});


loginForm.addEventListener('submit', (e) => {
    e.preventDefault();

    if (username.value === 'admin' && password.value === 'admin') {
        openWindow("admin.html"); // redirect to another page
    }
    else if (username.value === 'user' && password.value === 'user') {
        // alert('Login successful!');
        openWindow("main.html"); // redirect to another page
    } else {
        errorMessageDiv.style.color = "red"
        errorMessageDiv.textContent = 'Invalid username or password';
    }
});



function openWindow(page) {
    openedWindow = window.open(page);
    return openWindow
}

function closeOpenedWindow(window_to_close) {
    window_to_close.close();
}


function showHelpWindow() {
    alert("test data:\nAdministrator: admin / admin\nUser: user / user");
}