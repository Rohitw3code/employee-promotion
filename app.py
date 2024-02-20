from flask import Flask, render_template
import os
import tempfile

app = Flask(__name__)

@app.route('/')
def index():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Render the temporary HTML file
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
