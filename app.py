from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)



if __name__ in "__main__":
    app.run(debug=True)
