from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route("/")
def load_info():
    """
    Загружает информацию обо всех кандидатах
    """
    return render_template("list.html", data=utils.load_candidates())


@app.route("/candidate/<int:id>")
def load_info_candidate(id):
    """
    Загружает информацию кандидата по его id
    :param id: id кандидата
    """
    if id != 8:
        candidate = utils.get_by_id(id)
        return render_template("single.html", candidate_name=candidate["name"], position=candidate["position"],
                               url=candidate["picture"], skills=candidate["skills"])
    else:
        candidate = utils.get_by_id(id)
        return render_template("my_page.html", candidate_name=candidate["name"], position=candidate["position"],
                               url=candidate["picture"], skills=candidate["skills"])


@app.route("/search/<candidate_name>")
def load_found_candidates(candidate_name):
    """
    Загружает информацию кандидата по его имени
    :param candidate_name: имя кандидата
    :return: Возвращает странички найденных кандидатов
    """
    candidate = utils.get_by_name(candidate_name)
    return render_template("search.html", data=candidate, count=len(candidate))


@app.route("/skills/<skill_name>")
def load_skills_candidate(skill_name):
    """
    Загружает список подходящих кандидатов
    :param skill_name: необходимый скилл
    """
    candidate_with_skill = utils.get_by_skill(skill_name)
    return render_template("skill.html", skill_name=skill_name,
                           data=candidate_with_skill, count=len(candidate_with_skill))


app.run()
