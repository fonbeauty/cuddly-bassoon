const loginForm = document.getElementById('login-form');
const errorMessageDiv = document.getElementById('error-message');
const username = document.getElementById('username')
const password = document.getElementById('password')

loginForm.addEventListener('submit', (e) => {
	e.preventDefault();



	if (username.value === 'admin' && password.value === 'password') {
		alert('Login successful!');
		location.href = 'index.html'; // redirect to another page
	} else {
		errorMessageDiv.style.color = "red"
		errorMessageDiv.textContent = 'Invalid username or password';
	}
});