# Jump-to-Flask

## Task

### (2022.12.23)
- 가상환경 만들기 
- 플라스크 환경 만들기
    - `DEBUG` = TRUE :: 디버그모드 활성화, 디버깅 결과 메시지를 웹에 출력함
    - `set FLASK_APP=pybo` :: 기본 앱 설정

- pybo.py 파일을 __init__.py로 수정하고, app을 애플리케이션 팩토리로 바꿈

- 블루프린트 생성 및 등록

### (2022.12.24)
- ORM
- SQLAlchemy를 이용하여 모델 생성 (Question, Answer)

## DIRECTORY 
```bash
├── pybo/
│      ├─ __init__.py
│      ├─ models.py
│      ├─ forms.py
│      ├─ views/
│      │   └─ main_views.py
│      ├─ static/
│      │   └─ style.css
│      └─ templates/
│            └─ index.html
└── config.py
```
