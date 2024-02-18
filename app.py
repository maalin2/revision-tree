from flask import Flask, render_template, request
from api import ai, pdf, rank
import os

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the template folder path relative to the current directory
template_folder = os.path.join(current_directory, 'frontend')
static_folder = os.path.join(current_directory, 'frontend')

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/file", methods=["POST"])
def slide():
    if request.method == "POST":
        if "myfile" in request.files:
            uploaded_file = request.files["myfile"]
            uploaded_file.save(uploaded_file.filename)
            pdf.img(uploaded_file.filename)
            return "hello"
        else:
            return "No file uploaded"


@app.route("/slide")  
def slide_page():
    path_to_image = "p0.png"
    return render_template("slide.html", path_to_image=path_to_image)


if __name__ == "__main__":
    app.run(debug=True)