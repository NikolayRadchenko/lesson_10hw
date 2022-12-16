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
    Возвращает список всех кандидатов
    """
    candidates = load_candidates()
    candidate_with_name = []
    for candidate in candidates:
        candidate_with_name.append(candidate["name"])
    return ", ".join(candidate_with_name)


def get_by_name(candidate_name):
    """
    Возвращает кандидата по его name
    :param candidate_name: имя кандидата
    """
    candidates = load_candidates()
    candidate_with_name = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            candidate_with_name.append(candidate)
    return candidate_with_name


def get_by_id(candidate_id):
    """
    Возвращает кандидата по его id
    :param candidate_id: id кандидата
    """
    candidates = load_candidates()
    for candidate in candidates:
        if candidate["id"] == candidate_id:
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
        if skill_name.lower() in candidate["skills"].lower():
            candidate_with_skill.append(candidate)
    return candidate_with_skill
