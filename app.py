from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Route for the main page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "registration" in request.form:
            # Redirect to the registration page
            return redirect(url_for("registration"))
        elif "login" in request.form:
            # Redirect to the login page
            return redirect(url_for("login"))
    return render_template("index.html")


# Route for the registration page
@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        # You can handle registration form submission here
        username = request.form.get("username")
        password = request.form.get("password")
        # Here, you would typically add the user to the database
        return redirect(url_for("login"))  # Redirect to the login page after registration
    return render_template("registration.html")


# Route for the login page
# Route for the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Handle login form submission
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Here, you would typically check the username and password from a database
        # If login is successful, pass the username to the select page
        return redirect(url_for("select", username=username))  # Passing the username to the select page
    
    return render_template("login.html")


# Route for the select page after login
@app.route("/select", methods=["GET", "POST"])
def select():
    # Access the username passed from the login page
    username = request.args.get("username")
    
    if request.method == "POST":
        # Handle form submission (if needed)
        pass
    
    return render_template("select.html", username=username)  # Pass username to the template


if __name__ == "__main__":
    app.run(debug=True)

