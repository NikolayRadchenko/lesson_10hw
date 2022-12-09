import json


def load_candidates():
    """
    Загружает данные из JSON файла
    :return: возвращает данные в формате Python
    """
    with open("data/candidates.json", encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_all():
    """
    Возвращает данные на всех кандидатов
    """
    return load_candidates()


def get_by_pk(pk):
    """
    Возвращает кандидата по его pk
    :param pk: номер кандидата
    """
    candidates = load_candidates()
    for candidate in candidates:
        if candidate["pk"] == pk:
            return candidate


def get_by_skill(skill_name):
    """
    Выполняет поиск по кандидатам по скиллу
    :param skill_name: скилл для поиска по кандидатам
    :return Возвращает подходящих кандидатов
    """
    candidates = load_candidates()
    candidate_with_skill = []
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"]:
            candidate_with_skill.append(candidate["name"])
    return ", ".join(candidate_with_skill)
