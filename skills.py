skills_database = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "pandas",
    "numpy",
    "git",
    "aws"
]

def find_missing_skills(resume_text, job_description):

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    missing = []

    for skill in skills_database:

        if skill in job_description and skill not in resume_text:
            missing.append(skill)

    return missing