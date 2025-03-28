skills_db = {"Python", "Machine Learning", "NLP", "Flask", "SQL", "AWS", "TensorFlow", "Data Science"}

def extract_skills(resume_text):
    words = set(resume_text.split())
    return list(skills_db.intersection(words))
