from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
task_id = 0

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=['POST'])
def add_task():
    global task_id
    task_name = request.form.get("task_name")
    if task_name:
        tasks.append({'id': task_id, 'name': task_name, 'completed': False})
        task_id += 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)