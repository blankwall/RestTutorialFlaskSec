from flask import Flask, render_template, request,Response
import json
import random
import ast
from model import TaskDB
# Create an instance of the Flask class
app = Flask(__name__)
app.db = TaskDB()

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
    return json.dumps(app.db.load_db()),200

@app.route('/tasks', methods = ["POST"])
def create_task():
    global tasks
    new_task = ast.literal_eval(request.data.decode('utf-8'))
    new_task["id"] = str(random.randint(1000,9999))

    if not app.db.validate(new_task):
        return "Error: malformed",412

    if not app.db.add_task(new_task):
        return "Error: malformed",412

    return json.dumps(app.db.load_db()),201


@app.route('/tasks/<task_id>', methods = ["PUT"])
def update_task(task_id):
    request_data = ast.literal_eval(request.data.decode('utf-8'))
    if not request_data.get("oldName"):
        return "Error: incorrect data",412

    tasks = app.db.load_db()
    my_task = [i for i in tasks if i["name"] == request_data["oldName"]][0]
    my_task["name"] = request_data["name"]
    app.db.save_db()
    return "OK",200

@app.route('/tasks/<task_id>', methods = ["DELETE"])
def delete_task(task_id):
    found = -1
    tasks = app.db.load_db()

    for index,i in enumerate(tasks):
        if i["id"] == task_id:
            found = index
            break

    if found == -1:
        return "Not Found",412

    del tasks[found]
    app.db.save_db()

    return "OK",201


# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)