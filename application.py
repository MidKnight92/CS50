from flask import Flask, render_template, jsonify, redirect, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure to use SQLite database
# db = SQL("sqlite:///books.db")

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()