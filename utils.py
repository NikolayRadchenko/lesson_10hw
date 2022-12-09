import json


def load_candidates():
    with open("data/candidates.json", encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_all():
    return load_candidates()


def get_by_pk(pk):
    candidates = load_candidates()
    for candidate in candidates:
        if candidate["pk"] == pk:
            return candidate


def get_by_skill(skill_name):
    candidates = load_candidates()
    candidate_with_skill = []
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"]:
            candidate_with_skill.append(candidate["name"])
    return ", ".join(candidate_with_skill)
