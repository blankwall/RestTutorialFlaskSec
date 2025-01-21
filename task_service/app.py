from flask import Flask, render_template, request
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
    return open(filename).read()

# Define a route for a page that accepts a name as a query parameter
@app.route('/tasks', methods = ["GET"])
def read_tasks():
    return json.dumps(tasks)

@app.route('/tasks', methods = ["POST"])
def create_task():
    global tasks
    new_task = ast.literal_eval(request.data.decode('utf-8'))
    if new_task.get("name") == None:
        return "Error: no name provided"

    if any([i for i in tasks if i["name"] == new_task["name"]]):
        return "Error task already exists"

    new_task["id"] = str(random.randint(1000,9999))
    tasks += [new_task]
    return json.dumps(tasks)


@app.route('/tasks/<task_id>', methods = ["PUT"])
def update_task(task_id):
    global tasks
    request_data = ast.literal_eval(request.data.decode('utf-8'))
    if not request_data.get("oldName"):
        return "Error: incorrect data"

    my_task = [i for i in tasks if i["name"] == request_data["oldName"]][0]
    my_task["name"] = request_data["name"]
    return "OK"

# @app.route('/tasks/<task_id>', methods = ["DELETE"])
# def update_task(task_id):
#     global tasks
#     request_data = ast.literal_eval(request.data.decode('utf-8'))
#     if not request_data.get("oldName"):
#         return "Error: incorrect data"

#     for i in tasks:
#         if i["name"] == request_data["oldName"]:
#             del tasks[]

#     my_task["name"] = request_data["name"]
#     return "OK"


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
