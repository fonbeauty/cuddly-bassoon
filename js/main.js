// Создаем массив задач
let tasks = [];

// Добавляем слушатель события click к кнопке добавления задачи
document.getElementById('add-task-btn').addEventListener('click', () => {
    // Получаем текстовое поле для ввода задачи
    let taskInput = document.createElement('input');
    taskInput.type = 'text';
    taskInput.placeholder = 'Enter a new task...';

    // Создаем кнопку сохранения задачи
    let saveTaskBtn = document.createElement('button');
    saveTaskBtn.textContent = 'Save';
    saveTaskBtn.addEventListener('click', () => {
        // Получаем текст из поля ввода
        let taskText = taskInput.value.trim();

        // Добавляем задачу в массив
        tasks.push({ text: taskText, completed: false });

        // Обновляем DOM-страницу
        updateTaskList();

        // Сбрасываем поле ввода
        taskInput.value = '';
    });

    // Вставляем поля ввода и кнопку сохранения в страницу
    tbodyRef = document.getElementById('task-list')
    newRow = tbodyRef.insertRow()
    var newText = document.createTextNode('*');
    newRow.insertCell().appendChild(newText)
    newRow.insertCell().appendChild(taskInput)
    newRow.insertCell().appendChild(saveTaskBtn)
    // document.getElementById('new-row').appendChild(taskInput);
    // document.getElementById('new-row').appendChild(saveTaskBtn);
});

// Обновляем DOM-страницу с задачами
function updateTaskList() {
    let taskListHTML = '';
    let i = 0
    // Цикл по задачам
    tasks.forEach((task) => {
        i += 1
        let taskHTML = `
        <tr>
            <td>${i}</td>
            <td id="input-col" class="task ${task.completed ? 'completed' : ''}" >
                ${task.text}
            </td>
            <td>
                <button onclick="completeTask(${tasks.indexOf(task)})">Complete</button>
                <button onclick="deleteTask(${tasks.indexOf(task)})">Delete</button>
            </td>
        </tr>`;

        taskListHTML += taskHTML;
    });

    document.getElementById('task-list').innerHTML = taskListHTML;
}

// Упрощаем задачу
function completeTask(index) {
    tasks[index].completed = true;
    updateTaskList();
}

// Удаляем задачу
function deleteTask(index) {
    tasks.splice(index, 1);
    updateTaskList();
}
