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

    detected = []

    for skill, message in skills.items():
        if skill in text:
            result.append(message)
            detected.append(skill)

    # Missing important skills
    if "python" not in detected:
        result.append("⚠ Python missing")
    if "machine learning" not in detected:
        result.append("⚠ Machine Learning missing")

    # Suggested roles
    result.append("")
    result.append("Suggested Roles:")
    roles = ["Data Analyst", "AI/ML Intern", "Software Developer"]
    for role in roles:
        result.append(f"- {role}")

    # Suggestions
    result.append("")
    result.append("Suggestions:")

    if "python" not in detected:
        result.append("- Learn Python basics")
    if "machine learning" not in detected:
        result.append("- Add ML projects")

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
