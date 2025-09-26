from flask import Flask, render_template, session, request
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/masters")
def masters():
    return render_template("masters.html")

@app.route("/services")
def service():
    return render_template("services.html")


@app.route("/cart")
def cart():
    cart_items=session.get("cart",[])
    return render_template("cart.html",cart_items=cart_items)


if __name__ == "__main__":
    app.run(debug=True)
