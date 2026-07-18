import json
from flask import Flask, render_template, request
from dotenv import load_dotenv
from generator import generate_cover_letter

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    cover_letter = None
    resume_data = None
    job_data = None
    error = None

    if request.method == "POST":
        try:
            resume_text = request.form.get("resume", "").strip()
            job_text = request.form.get("job_description", "").strip()

            if not resume_text or not job_text:
                error = "Both resume and job description are required."
            else:
                resume_data = json.loads(resume_text)
                job_data = json.loads(job_text)
                cover_letter = generate_cover_letter(resume_data, job_data)
        except json.JSONDecodeError:
            error = "Invalid JSON format. Please check your input."
        except Exception as e:
            error = f"Generation failed: {e}"

    return render_template(
        "index.html",
        cover_letter=cover_letter,
        resume_data=resume_data,
        job_data=job_data,
        error=error,
    )


@app.route("/samples")
def samples():
    with open("samples/sample_outputs.json") as f:
        samples = json.load(f)
    return render_template("samples.html", samples=samples)


if __name__ == "__main__":
    app.run(debug=True)
