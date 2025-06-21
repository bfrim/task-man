from flask import Flask, render_template

app = Flask(__name__)

tasks = []
task_id = 0

@app.route("/")
def index():
    return render_template("index.html")

app.run(debug=True)