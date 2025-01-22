from flask import Flask, render_template, request,Response
import json
import random
import ast
# Create an instance of the Flask class
app = Flask(__name__)

tasks = [
    {"id":"1234","name":"helloworld1"},
    {"id":"9876","name":"helloworld2"},
    {"id":"5678","name":"helloworld3"},
]

# Define a route for the home page
@app.route('/<filename>')
def home(filename):
    if "css" in filename:
        mtype = 'text/css'
    elif "html" in filename:
        mtype = 'text/html'
    else:
        mtype = 'text/plain'

    return Response(open(filename).read(), mimetype=mtype)

# Define a route for a page that accepts a name as a query parameter
@app.route('/tasks', methods = ["GET"])
def read_tasks():
    return json.dumps(tasks),200

@app.route('/tasks', methods = ["POST"])
def create_task():
    global tasks
    new_task = ast.literal_eval(request.data.decode('utf-8'))
    if new_task.get("name") == None:
        return "Error: no name provided",412

    if any([i for i in tasks if i["name"] == new_task["name"]]):
        return "Error task already exists",412

    new_task["id"] = str(random.randint(1000,9999))
    tasks += [new_task]
    return json.dumps(tasks),201


@app.route('/tasks/<task_id>', methods = ["PUT"])
def update_task(task_id):
    global tasks
    request_data = ast.literal_eval(request.data.decode('utf-8'))
    if not request_data.get("oldName"):
        return "Error: incorrect data",412

    my_task = [i for i in tasks if i["name"] == request_data["oldName"]][0]
    my_task["name"] = request_data["name"]
    return "OK",200

@app.route('/tasks/<task_id>', methods = ["DELETE"])
def delete_task(task_id):
    global tasks
    found = -1
    for index,i in enumerate(tasks):
        if i["id"] == task_id:
            found = index
            break

    if found == -1:
        return "Not Found",412

    del tasks[found]
    return "OK",201


# Run the app
if __name__ == '__main__':
    app.run(debug=True)