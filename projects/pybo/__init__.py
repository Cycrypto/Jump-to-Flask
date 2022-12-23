from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app

#create_app : 애플리케이션 팩토리 (Flask 내부에서 정의됨)
