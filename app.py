from flask import Flask, request, render_template
import os
from scripts.extract_text import extract_text_from_pdf, extract_text_from_docx
from scripts.extract_info import extract_info
from scripts.extract_skills import extract_skills

app = Flask(__name__)

DATA_FOLDER = "data"
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

@app.route("/", methods=["GET", "POST"])
def upload_resume():
    if request.method == "POST":
        file = request.files["resume"]
        filename = file.filename
        file_path = os.path.join(DATA_FOLDER, filename)
        file.save(file_path)

        resume_text = extract_text_from_pdf(file_path) if filename.endswith(".pdf") else extract_text_from_docx(file_path)
        info = extract_info(resume_text)
        skills = extract_skills(resume_text)
        
        return render_template("results.html", info=info, skills=skills)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
