from fuzzywuzzy import fuzz

def match_skills(resume_skills, jd_skills):
    matched = []
    missing = []

    for skill in jd_skills:
        found = False
        for res_skill in resume_skills:
            if fuzz.partial_ratio(skill.lower(), res_skill.lower()) > 80:
                matched.append(skill)
                found = True
                break
        if not found:
            missing.append(skill)

    return list(set(matched)), list(set(missing))

def compute_match_score(matched, total_required):
    if total_required == 0:
        return 0
    return round((len(matched) / total_required) * 100, 2)

def match_resume_to_jd(resume_data, jd_data):
    resume_skills = resume_data.get('skills', []) + resume_data.get('tools', [])
    jd_skills = jd_data.get('required_skills', []) + jd_data.get('tools', [])

    print("Resume Extracted Skills + Tools:", resume_skills)
    print("JD Required Skills + Tools:", jd_skills)

    matched, missing = match_skills(resume_skills, jd_skills)
    match_score = compute_match_score(matched, len(jd_skills))

    return {
        'match_score': match_score,
        'matched_skills': matched,
        'missing_skills': missing
    }
