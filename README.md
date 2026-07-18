# AI Resume Analyzer & Cover Letter Generator

A Flask web app that generates customized cover letters using OpenAI's GPT API based on a candidate's resume and a target job description.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Run

```bash
python app.py
```

Open http://localhost:5000 in your browser.

## Usage

1. Paste your resume as JSON into the first field
2. Paste the job description as JSON into the second field
3. Click "Generate Cover Letter"

### Resume format

```json
{
  "name": "Ayesha Khan",
  "experience": "3 years in data science, working with NLP and time-series forecasting.",
  "skills": ["Python", "TensorFlow", "Pandas", "Prompt Engineering"],
  "projects": ["AI-powered chatbot for finance", "Anomaly detection for manufacturing sensors"]
}
```

### Job description format

```json
{
  "title": "NLP Research Associate",
  "requirements": ["NLP", "ML deployment", "LLM fine-tuning", "Python"]
}
```

## Sample Outputs

Visit `/samples` to see pre-generated cover letter comparisons across different resume/job combinations.

## Project Structure

```
├── app.py                  # Flask application
├── generator.py            # OpenAI API integration & prompt engineering
├── templates/
│   ├── index.html          # Main form + output page
│   └── samples.html        # Sample output comparisons
├── static/
│   └── style.css           # Styling
├── samples/
│   └── sample_outputs.json # Pre-generated sample comparisons
├── requirements.txt
└── .env.example
```
