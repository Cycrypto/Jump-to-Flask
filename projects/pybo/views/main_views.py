from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')
# main : alias
# __name__ : "main_views"
# url_prefix : url 앞에 붙일 접두어 URL

@bp.route('/')
def index():
    return redirect(url_for('question.question_list'))