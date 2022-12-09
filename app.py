from flask import Flask
import utils

app = Flask(__name__)


@app.route("/")
def load_info():
    """
    Загружает информацию обо всех кандидатах
    """
    candidates = []
    for candidate in utils.get_all():
        candidates.append("<pre>\n"
                          f"Имя кандидата - {candidate['name']}\n"
                          f"Позиция кандидата: {candidate['position']}\n"
                          f"Навыки через запятую: {candidate['skills']}\n"
                          "</pre>")
    return "".join(candidates)


@app.route("/candidates/<int:uid>")
def load_info_candidate(uid):
    """
    Загружает информацию кандидата по его pk
    :param uid: номер кандидата (pk)
    """
    candidate = utils.get_by_pk(uid)
    url = candidate["picture"]
    return f"<img src='({url})'>\n" \
           "<pre>\n" \
           f"Имя кандидата - {candidate['name']}\n" \
           f"Позиция кандидата: {candidate['position']}\n" \
           f"Навыки через запятую: {candidate['skills']}\n" \
           "</pre>"


@app.route("/skills/<skill_name>")
def load_skills_candidate(skill_name):
    """
    Загружает список подходящих кандидатов
    :param skill_name: необходимый скилл
    """
    return utils.get_by_skill(skill_name)


app.run()
