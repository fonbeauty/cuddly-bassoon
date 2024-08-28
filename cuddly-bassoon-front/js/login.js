const togglePassword = document.getElementById("togglePassword");
const loginForm = document.getElementById('login-form');
const errorMessageDiv = document.getElementById('error-message');
const username = document.getElementById('username');
const password = document.getElementById('password');
// const showHelp = document.getElementById("showHelp");

togglePassword.addEventListener("click", function () {
    // toggle the type attribute
    const type = password.getAttribute("type") === "password" ? "text" : "password";
    password.setAttribute("type", type);
    // toggle the icon
    this.classList.toggle("bi-eye");
});

// showHelp.addEventListener("click", function () {
//     showHelpWindow()
// });

// prevent form submit
const form = document.querySelector("form");
form.addEventListener('submit', function (e) {
    e.preventDefault();
});


loginForm.addEventListener('submit', (e) => {
    e.preventDefault();

//    try {
//        const userData = login(username.value, password.value);
//        console.log(userData);
//    } catch (error) {
//        console.error('Error logging in:', error);
//    }


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


// function showHelpWindow() {
//     alert("test data:\nAdministrator: admin / admin\nUser: user / user");
// }

function login(username, password) {
    const body = {
        login: username,
        password: password
    }

    // sendRequest('GET', 'https://jsonplaceholder.typicode.com/users')
    //     .then(data => console.log(data))
    //     .catch(err => console.log(err))
    sendRequest('POST', 'http://127.0.0.1:8003/api/login', body)
        .then(data => console.log(data))
        .catch(err => console.log(err))
    // response = sendRequest('POST', 'http://127.0.0.1/api/login')
    // const response = fetch('https://jsonplaceholder.typicode.com/users', {
    //     method: 'GET',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     // body: JSON.stringify({ username, password })
    // });

    // if (!response.ok) {
    //     throw new Error('Server responded with error');
    // }

    // return response.json();
}


function sendRequest(method, url, body = null) {
    const headers = {
        'Content-Type': 'application/json'
    }
    return fetch(url, {
        mode: "no-cors",
        method: method,
        body: JSON.stringify(body),
        headers: headers
    }).then(response => {
        if (response.ok) {
            return response.json()
        }

        return response.json().then(error => {
            const e = new Error('Что-то пошло не так')
            e.data = error
            throw e
        })
    })
}


// // Пример использования функции
// try {
//     const userData = login('user123', 'password123');
//     console.log(userData);
// } catch (error) {
//     console.error('Error logging in:', error);
// }
