from flask import Flask, render_template, request

app = Flask(__name__)

def analyze_resume(text):
    result = []

    if "python" in text.lower():
        result.append("✔ Python detected")
    else:
        result.append("⚠ Python missing")

    if "machine learning" in text.lower():
        result.append("✔ ML detected")
    else:
        result.append("⚠ ML missing")

    result.append("\nSuggested Roles:")
    result.append("- Data Analyst")
    result.append("- AI/ML Intern")

    return result


@app.route("/", methods=["GET", "POST"])
def home():
    output = []
    if request.method == "POST":
        resume = request.form["resume"]
        output = analyze_resume(resume)

    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(debug=True)