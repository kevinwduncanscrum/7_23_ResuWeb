from flask import Flask, render_template

app = Flask(__name__)


@app.route("/7_23_ResuWeb/<name>")
def profile(name):
    return render_template("word.html", name=name)

if __name__ == "__main__":
    app.run()



