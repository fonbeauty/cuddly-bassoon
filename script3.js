// Initialize variables
let username = '';
let password = '';

// Add event listeners to buttons
document.getElementById('login-btn').addEventListener('click', login);
document.getElementById('register-btn').addEventListener('click', register);

// Function to handle login
function login() {
    // Get the username and password inputs
    let usernameInput = document.getElementById('username-input');
    let passwordInput = document.getElementById('password-input');

    // Check if the inputs are valid (e.g. not empty)
    if (!usernameInput.value || !passwordInput.value) {
        alert('Please fill out all fields');
        return;
    }

    // Check if the username and password match the expected values
    if (usernameInput.value === 'admin' && passwordInput.value === 'password') {
        // Login successful, show the notebook container
        document.getElementById('notebook-container').style.display = 'block';
    } else {
        alert('Invalid username or password');
    }
}

// Function to handle registration
function register() {
    // Get the username and password inputs
    let usernameInput = document.getElementById('username-input');
    let passwordInput = document.getElementById('password-input');

    // Check if the inputs are valid (e.g. not empty)
    if (!usernameInput.value || !passwordInput.value) {
        alert('Please fill out all fields');
        return;
    }

    // Store the username and password in local storage
    localStorage.setItem('username', usernameInput.value);
    localStorage.setItem('password', passwordInput.value);

    // Show a success message
    alert('Registration successful!');
}

// Function to handle form submission (not implemented yet)
function submitForm() {
    // Get the form data
    let formData = new FormData(document.getElementById('notebook-form'));

    // Send the form data to the server
    fetch('/notebook', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
}