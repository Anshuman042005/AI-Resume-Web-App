"""
AI Resume Analyzer Web App
Author: Anshuman Sikdar
"""

from flask import Flask, render_template, request

app = Flask(__name__)


def analyze_resume(text):
    result = []

    text = text.lower()

    # Skill detection
    if "python" in text:
        result.append("✔ Python detected")
    else:
        result.append("⚠ Python missing")

    if "machine learning" in text:
        result.append("✔ Machine Learning detected")
    else:
        result.append("⚠ Machine Learning missing")

    if "data analysis" in text:
        result.append("✔ Data Analysis detected")

    # Suggestions
    result.append("")

    result.append("Suggested Roles:")
    result.append("- Data Analyst")
    result.append("- AI/ML Intern")
    result.append("- Software Developer")

    # Improvement tips
    result.append("")
    result.append("Suggestions:")
    result.append("- Add more technical projects")
    result.append("- Include GitHub profile")
    result.append("- Highlight key skills clearly")

    return result


@app.route("/", methods=["GET", "POST"])
def home():
    output = []

    if request.method == "POST":
        resume = request.form.get("resume", "")
        
        if resume.strip() == "":
            output = ["⚠ Please enter resume text"]
        else:
            output = analyze_resume(resume)

    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(debug=True)
