from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db:SQLAlchemy = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    #ORM
    db.init_app(app)
    migrate.init_app(app, db)

    #BLUE PRINT
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app

# create_app : 애플리케이션 팩토리 (Flask 내부에서 정의됨)
# flask db migrate : 모델 새로 생성 또는 변경할 떄 사용
# flask db upgrade : 모델의 변경된 내용을 실제 db에 적용시 사용


