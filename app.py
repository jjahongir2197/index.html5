from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET","POST"])
def todo():

    if request.method == "POST":

        task = request.form["task"]
        tasks.append(task)

        return f"Tasks: {tasks}"

    return render_template("index.html")

app.run(debug=True)
