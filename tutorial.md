#### TaskService

## Getting Started

In this tutorial, we will walk through the process of building a microservice web application using Flask, a lightweight web framework in Python, and RESTful principles to manage tasks. The goal is to create a small, independent service within a larger system that handles task-related operations such as creating, reading, updating, and deleting tasks. This service will communicate with other components of the system via well-defined APIs, following the principles of REST (Representational State Transfer).

Flask is an extremely popular web framework in Python due to its simplicity, flexibility, and ease of use. Flask does not come with the overhead of more monolithic frameworks, making it an excellent choice for building small, independent microservices. It is designed to be lightweight and modular, allowing developers to easily integrate third-party extensions when needed. Flask applications are often structured around the concept of "routes" or "endpoints," which map specific HTTP requests (such as GET, POST, PUT, DELETE) to functions that execute the logic behind those requests. These routes form the core of a RESTful API, where clients interact with resources (like tasks) using standard HTTP methods.

RESTful design refers to building web services in a way that they adhere to the principles of Representational State Transfer. This means your service exposes resources via unique URIs, and each resource can be manipulated through standard HTTP methods: GET for reading data, POST for creating new resources, PUT/PATCH for updating resources, and DELETE for removing them. RESTful APIs are stateless, meaning each request from a client must contain all the information needed to process it, without relying on stored information from previous requests. This statelessness makes RESTful services easy to scale and maintain.

To get started, we'll use ChatGPT to generate boilerplate code that will include not only the backend logic in Flask but also the frontend components (HTML and CSS) for interacting with the task service. ChatGPT will help speed up the process by providing ready-made templates and code snippets, allowing us to focus on the core logic of our task service.

The core operations on the backend will follow CRUD (Create, Read, Update, Delete) principles, which represent the four basic actions that can be performed on any resource. These operations are the foundation of our task service:

    Create (POST): This operation allows users to create a new task by submitting the necessary data (e.g., task name, description) via an HTTP POST request. This data is then saved to the database.
    Read (GET): The GET method retrieves information about a task or a list of tasks. This could include fetching all tasks or a specific task by its unique identifier.
    Update (PUT/PATCH): The PUT method is used to update a task's information, such as modifying its name or description. PATCH can be used for partial updates if only certain fields need to be changed.
    Delete (DELETE): The DELETE method allows users to remove a task from the system, either by its ID or through other identifying data.

Each of these CRUD operations will be mapped to specific endpoints in our Flask app, providing a straightforward, consistent API that other parts of the system can interact with. By structuring our app as a microservice and using RESTful principles, we ensure that our task service can be easily integrated, scaled, and maintained within a larger system.


## ChatGPT Code

- original_task_service/app.js

In summary, this JavaScript code provides a simple front-end interface for interacting with a task management microservice built with Flask. It leverages the Fetch API to communicate with the backend, allowing users to perform CRUD operations (Create, Read, Update, Delete) on tasks. The loadTasks function loads the tasks, the addTask function creates a new task, deleteTask removes a task, and editTask updates an existing task. By following this pattern, you can easily extend the functionality and integrate more advanced features into your application.

- original_task_service/app.py

This Python code uses Flask, a lightweight web framework, to create a simple web application. Here's a summary of the key components:

    Flask Initialization: The Flask class is imported and an instance of it is created with app = Flask(__name__). This instance is the core of the web application.

    Route Definition: The @app.route('/') decorator defines a route for the home page (the root URL, /). When a user visits the root URL, the home() function is called, which returns the string "Hello, World!".

    App Execution: The if __name__ == '__main__': block ensures that the app runs only if this script is executed directly (not when imported as a module). The app.run(debug=True) starts the Flask development server with debugging enabled, allowing for easier error tracking and automatic reloading during development.

This is a minimal Flask app that responds with a basic "Hello, World!" message when accessed via the browser.

- original_task_service/index.html style.css

Styling and HTML

### Flask Server Setup Tutorial for Task Management API

In this tutorial, we will set up a basic Flask server to serve an API for a task management system. This guide will cover the steps for reverse engineering the JavaScript code, creating appropriate Flask routes, and setting up the necessary CRUD functionality.

### Steps Overview

1. **Setting Up Flask Routes**
2. **Accessing Stylesheets**
3. **Configuring the API Endpoint**
4. **Returning Tasks Data in JSON Format**

### 1. **Setting Up Flask Routes**

To begin, we need a route to serve files from the backend, such as stylesheets. This is done by setting up a route that reads files from the system.

```python
@app.route('/<filename>')
def home(filename):
    return open(filename).read()
```

This route listens for any requests to /filename, where filename can be any file in the backend.
The file is read and returned as the response.

### 2.  Configuring the API Endpoint

The JavaScript code initially points to a remote API URL:

`const API_URL = 'https://your-backend-api.com/tasks';`

We need to update this to point to our local Flask server during development:

`const API_URL = 'http://localhost:5000/tasks';  // Flask server URL`

### 3. Handling Data Fetching

The JavaScript code fetches task data using the following code:

`const response = await fetch(API_URL);`

This sends a GET request to the server to retrieve the tasks. The server is expected to return data in JSON format, with each task containing at least id and name fields. The JavaScript code processes this data as follows:

```
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

```

### 4. Backend Task Data Route

To implement the GET /tasks API endpoint in Flask, we define a route that returns a list of tasks in JSON format:

```
@app.route('/tasks', methods=["GET"])
def read_tasks():
    tasks = [
        {"id": 1, "name": "Task 1"},
        {"id": 2, "name": "Task 2"}
    ]
    return json.dumps(tasks)
```

- The route /tasks listens for GET requests.
- It returns a list of task objects in JSON format, each containing an id and name.

### Final Notes

This simple Flask server and JavaScript setup allows us to interact with a basic task management API. You can expand upon this by adding routes for creating, updating, and deleting tasks following the standard CRUD conventions.


# How to Create a Task in the Task Management API

In this section, we will break down the process of creating a new task from both the **front-end** and the **back-end**.

### Front-End: Sending a Request to Create a Task

On the front-end, we have a form where users can input the name of a task and submit it. Here's how it works:

```javascript
taskForm.addEventListener('submit', async (event) => {
  event.preventDefault();  // Prevents the default form submission behavior
  
  const taskName = taskInput.value.trim();  // Get the trimmed task name
  if (!taskName) return;  // If no task name is provided, exit

  const newTask = {
    name: taskName  // Create a new task object
  };

  // Send the task to the server using a POST request
  await fetch(API_URL, {
    method: 'POST',  // Specify the HTTP method as POST
    headers: {
      'Content-Type': 'application/json'  // Indicate that the request body is JSON
    },
    body: JSON.stringify(newTask)  // Convert the new task object to a JSON string
  });

  taskInput.value = '';  // Clear the task input field
  loadTasks();  // Refresh the task list to include the new task
});
```

- Step 1: The submit event listener captures the form submission.
- Step 2: We extract the task name entered by the user, ensuring it's trimmed of any whitespace.
- Step 3: If the task name is valid, we create an object (newTask) with the name property.
- Step 4: A POST request is sent to the server's /tasks endpoint with the newTask object in the request body (converted into JSON).
- Step 5: After the task is successfully submitted, the task input field is cleared, and the task list is refreshed using loadTasks().


### Back-End: Handling Task Creation in Flask

Now, let's look at how we handle the incoming request and create a new task on the server using Flask.

```
@app.route('/tasks', methods=["POST"])
def create_task():
    global tasks  # Referencing the global task list
    new_task = ast.literal_eval(request.data.decode('utf-8'))  # Parse the incoming JSON data

    # Check if the task name is provided
    if new_task.get("name") == None:
        return "Error: no name provided", 400

    # Check if the task already exists
    if any([i for i in tasks if i["name"] == new_task["name"]]):
        return "Error: task already exists", 400

    # Generate a unique ID for the new task
    new_task["id"] = str(random.randint(1000, 9999))

    # Add the new task to the tasks list
    tasks += [new_task]

    # Return the updated list of tasks in JSON format
    return json.dumps(tasks), 201
```

- Step 1: The route /tasks listens for POST requests and is responsible for creating a new task.
- Step 2: The incoming request data is parsed using ast.literal_eval to safely convert the JSON body into a Python dictionary.
- Step 3: We check if the name field is provided. If not, an error message is returned with a 400 HTTP status code.
- Step 4: Next, we ensure the task doesn't already exist in the tasks list by checking if any task has the same name. If a duplicate - is found, we return an error message.
- Step 5: We generate a random ID for the new task using random.randint(1000, 9999) and add it to the tasks list.
- Step 6: The server responds with the updated list of tasks in JSON format and a 201 HTTP status code to indicate that the resource was successfully created.

### Final Notes

This Create Task functionality follows the CRUD (Create, Read, Update, Delete) convention, where:

    The front-end captures the user input and sends it to the back-end via a POST request.
    The back-end processes the data, validates it, creates a new task, and returns the updated list of tasks.

This implementation ensures that tasks are created only if they have a name, and prevents duplicates from being added to the list.