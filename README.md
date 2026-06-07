# 📄 AI Resume Analyzer

## Overview

AI Resume Analyzer is a Python-based web application that analyzes resumes against job descriptions and calculates a compatibility score using NLP techniques.

The application helps users understand how well their resume matches a job role and identifies important missing skills.

## Features

* Upload Resume (PDF)
* Resume Text Extraction
* Job Description Analysis
* Resume Match Score Calculation
* Missing Skills Detection
* Interactive Streamlit Interface

## Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* PyPDF2

## Project Structure

AI_Resume_Analyzer/

├── app.py

├── resume_parser.py

├── matcher.py

├── skills.py

├── requirements.txt

└── README.md

## Installation

Clone the repository:

git clone https://github.com/Theertha-ed/AI-Resume-Analyzer.git

Navigate to the project folder:

cd AI-Resume-Analyzer

Install dependencies:

pip install -r requirements.txt

## Running the Application

Run:

python -m streamlit run app.py

The application will open in your browser.

## How It Works

1. Upload a resume in PDF format.
2. Paste a job description.
3. The system extracts resume text.
4. NLP-based similarity analysis is performed.
5. A match score is generated.
6. Missing skills are displayed.

## Future Improvements

* Resume Improvement Suggestions
* ATS Compatibility Score
* Analysis History
* Interview Question Generator
* Gemini AI Integration
* Resume Ranking System

## Author

Theertha

GitHub: https://github.com/Theertha-ed

## License

This project is intended for educational and portfolio purposes.
