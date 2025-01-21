// DOM elements
const taskForm = document.getElementById('task-form');
const taskInput = document.getElementById('task-input');
const taskList = document.getElementById('task-list');

// API endpoint
const API_URL = 'http://127.0.0.1:5000/tasks';

// Fetch and display tasks
async function loadTasks() {
  const response = await fetch(API_URL);
  const tasks = await response.json();

  taskList.innerHTML = '';
  tasks.forEach(task => {
    const li = document.createElement('li');
    li.innerHTML = `
      <span>${task.name}</span>
      <div>
        <button onclick="deleteTask(${task.id})">Delete</button>
        <button onclick="editTask(${task.id}, '${task.name}')">Edit</button>
      </div>
    `;
    taskList.appendChild(li);
  });
}

// Add task
taskForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  
  const taskName = taskInput.value.trim();
  if (!taskName) return;

  const newTask = {
    name: taskName
  };

  await fetch(API_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(newTask)
  });

  taskInput.value = '';
  loadTasks(); // Refresh the task list
});

// Delete task
async function deleteTask(id) {
  await fetch(`${API_URL}/${id}`, {
    method: 'DELETE'
  });

  loadTasks(); // Refresh the task list
}

// Edit task
function editTask(id, currentName) {
  const newName = prompt('Edit Task Name:', currentName);
  if (newName && newName !== currentName) {
    const updatedTask = {
      name: newName,
      oldName: currentName
    };

    fetch(`${API_URL}/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(updatedTask)
    })
    .then(() => loadTasks()); // Refresh the task list
  }
}

// Initialize by loading tasks
loadTasks();
