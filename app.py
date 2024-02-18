from flask import Flask, render_template, request
from api import ai, pdf, rank
import os

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the template folder path relative to the current directory
template_folder = os.path.join(current_directory, 'frontend')
static_folder = os.path.join(current_directory, )
UPLOAD_FOLDER = os.path.join(current_directory)

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

n = 0;

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/file", methods=["POST"])
def slide():
    if request.method == "POST":
        if "myfile" in request.files:
            uploaded_file = request.files["myfile"]
            if uploaded_file.filename != '':
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
                uploaded_file.save(file_path)
                pdf.img(file_path)  # Passing file_path to img() function
                path_to_image = '/p' + str(n) + '.png'
            return render_template("slide.html", path_to_image=path_to_image)
                
        return "No file selected"

@app.route('/submit', methods=['POST'])
def submit():
    answer = request.form['answer']
    # Process the data as needed    
    n = n + 1
    path_to_image = '/p' + n + '.png'
    return render_template("slide.html", path_to_image=path_to_image)

if __name__ == "__main__":
    app.run(debug=True)