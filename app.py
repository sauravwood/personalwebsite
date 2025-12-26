from flask import Flask, render_template, request
import smtplib
import os
import gunicorn

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        
        send_email(name, email, message)
    
    return render_template("contact.html")

def send_email(name, email, message):
    sender_email = os.getenv("EMAIL_ADDRESS")
    sender_password = os.getenv("EMAIL_PASSWORD")
    receiver_email = "saurabhrajaure648@gmail.com"

    if not sender_email or not sender_password:
        raise Exception("Email credentials not found")

    email_message = f"""
   subject: New Contact Message

    Name: {name}
    Email: {email}

    Message:
    {message}
    """

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, email_message)


if __name__ == "__main__":
    app.run() 
    
