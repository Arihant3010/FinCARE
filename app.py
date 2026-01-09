from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("main.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/signup")
def signup_page():
    return render_template("signup.html")

@app.route("/do_login", methods=["POST"])
def do_login():
    email = request.form.get("email")
    password = request.form.get("password")

    if email and password:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login_page"))

@app.route("/do_signup", methods=["POST"])
def do_signup():
    return redirect(url_for("login_page"))

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)

