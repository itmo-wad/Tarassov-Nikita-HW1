from flask import Flask, render_template,  redirect


app = Flask(__name__)


@app.route('/')
def default_route():
    return redirect("/profile")


@app.route('/profile')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=8880, debug=True)
