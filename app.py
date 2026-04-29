"""
AI Resume Analyzer Web App
Author: Anshuman Sikdar
"""

from flask import Flask, render_template, request

app = Flask(__name__)


def analyze_resume(text):
    text = text.lower()
    result = []

    # Skill detection
    skills = {
        "python": "✔ Python detected",
        "machine learning": "✔ Machine Learning detected",
        "data analysis": "✔ Data Analysis detected",
        "java": "✔ Java detected",
    }

    for skill, message in skills.items():
        if skill in text:
            result.append(message)

    # Missing important skills
    if "python" not in text:
        result.append("⚠ Python missing")
    if "machine learning" not in text:
        result.append("⚠ Machine Learning missing")

    # Suggested roles
    result.append("")
    result.append("Suggested Roles:")
    result.extend([
        "- Data Analyst",
        "- AI/ML Intern",
        "- Software Developer"
    ])

    # Suggestions
    result.append("")
    result.append("Suggestions:")
    result.extend([
        "- Add more technical projects",
        "- Include GitHub profile",
        "- Highlight key skills clearly"
    ])

    return result


@app.route("/", methods=["GET", "POST"])
def home():
    output = []

    if request.method == "POST":
        resume = request.form.get("resume", "").strip()

        if not resume:
            output = ["⚠ Please enter resume text"]
        else:
            output = analyze_resume(resume)

    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(debug=True)
