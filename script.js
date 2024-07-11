const loginForm = document.getElementById('login-form');
const errorMessageDiv = document.getElementById('error-message');

loginForm.addEventListener('submit', (e) => {
	e.preventDefault();

	const username = document.getElementById('username').value;
	const password = document.getElementById('password').value;

	if (username === 'admin' && password === 'password') {
		alert('Login successful!');
		location.href = 'index.html'; // redirect to another page
	} else {
		errorMessageDiv.textContent = 'Invalid username or password';
	}
});