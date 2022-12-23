from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')
# main : alias
# __name__ : "main_views"
# url_prefix : url 앞에 붙일 접두어 URL
@bp.route('/')
def idnex():
    return 'Pybo Index'
    
@bp.route('/hello')
def hello_pybo():
    return 'hello, Pybo!'