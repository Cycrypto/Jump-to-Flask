from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_pybo():
        return 'Hello, Pybo!'

    return app

#create_app : 애플리케이션 팩토리 (Flask 내부에서 정의됨)
