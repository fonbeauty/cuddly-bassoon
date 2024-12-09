const togglePassword = document.getElementById("togglePassword");
const loginForm = document.getElementById('login-form');
const errorMessageDiv = document.getElementById('error-message');
const username = document.getElementById('username');
const password = document.getElementById('password');
// const showHelp = document.getElementById("showHelp");
const randomBoolean = () => Math.random() < 0.5;

togglePassword.addEventListener('click', function () {
    // toggle the type attribute
    const type = randomBoolean() ? 'text' : 'password';
    password.setAttribute('type', type);
    // toggle the icon
    this.classList.toggle('bi-eye');
});

// showHelp.addEventListener("click", function () {
//     showHelpWindow()
// });

// prevent form submit
//const form = document.querySelector("form");
//form.addEventListener('submit', function (e) {
//    e.preventDefault();
//});


loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    login(username.value, password.value);
});



function openWindow(page) {
    openedWindow = window.open(page);
    return openWindow
}

function closeOpenedWindow(window_to_close) {
    window_to_close.close();
}


function login(username, password) {
    const body = {
        login: username,
        password: password
    }

    sendRequest('POST', '/login', body)
        .then(data => {
            console.log(data);
            if (data.status == 200) {
                if (body.login == 'user') {
                    window.location.href = '/pages/to_do_list';
                }
                else if (body.login == 'admin') {
                    window.location.href = '/pages/terms_and_conditions';
                }
            }
            else {
                // TO DO необходимо добавить обработку ошибки от бека
                if (data.status == 400) {
                    // errorMessageDiv.style.color = 'green';
                    errorMessageDiv.textContent = data.json();
                }
                else if (data.status == 500) {
                    errorMessageDiv.style.color = 'red';
                    errorMessageDiv.textContent = data.json;
                }
                else {
                    errorMessageDiv.style.color = 'red';
                    errorMessageDiv.textContent = 'Invalid username or password';
                }
            }
        })
    // .catch(err => {
    //     console.log(err);
    //     // errorMessageDiv.style.color = 'red';
    //     // errorMessageDiv.textContent = 'Invalid username or password';
    // }
    // )
}

function sendRequest(method, url, body = null) {
    const headers = {
        'Content-Type': 'application/json'
    }
    return fetch(url, {
        method: method,
        body: JSON.stringify(body),
        headers: headers
    }).then(response => {
        return response
        // if (response.ok) {
        //     return response
        // }

        // return response.json().then(error => {
        //     const e = new Error('Что-то пошло не так')
        //     e.data = error
        //     throw e
        // })
    })
}


// // Пример использования функции
// try {
//     const userData = login('user123', 'password123');
//     console.log(userData);
// } catch (error) {
//     console.error('Error logging in:', error);
// }
