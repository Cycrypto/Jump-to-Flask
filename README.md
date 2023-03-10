# Jump-to-Flask

## RUN
- 가상환경에서 실행할 것 > `Scripts/activate`
- `flask run` 명령어 사용시 `(myproject) ..\path\Jump-to-Flask\projects>` 에서 실행시킬것
- `set FLASK_APP=pybo` 설정후 사용, 필요시 DEBUG모드도 켤 것

## Task


### 2022
**(12.23)**
- 가상환경 만들기 
- 플라스크 환경 만들기
    - `DEBUG` = TRUE :: 디버그모드 활성화, 디버깅 결과 메시지를 웹에 출력함
    - `set FLASK_APP=pybo` :: 기본 앱 설정

- pybo.py 파일을 __init__.py로 수정하고, app을 애플리케이션 팩토리로 바꿈

- 블루프린트 생성 및 등록

**(12.24)**
- ORM
- SQLAlchemy를 이용하여 모델 생성 (Question, Answer)
- 각 모델에 대한 URL 매핑 및 탬플릿 생성
- 답글 폼 생성 및 POST 방식으로 댓글 쓰고 읽기 가능


### 2023
**(01.12)**
- `static` 폴더 생성 및 `style.css`적용
## DIRECTORY 

### 구상
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

### 현재 디렉터리 구조
```bash
│  config.py
│  pybo.db
│
├─migrations
│  │  alembic.ini
│  │  env.py
│  │  README
│  │  script.py.mako
│  │
│  ├─versions
│  │  │  c5e26495a16f_.py
│  │  │
│  │  └─__pycache__
│  │          c5e26495a16f_.cpython-310.pyc
│  │
│  └─__pycache__
│          env.cpython-310.pyc
│
├─pybo
│  │  models.py
│  │  __init__.py
│  │
│  ├─templates
│  │  └─question
│  │          question_detail.html
│  │          question_list.html
│  │
│  ├─views
│  │  │  answer_views.py
│  │  │  main_views.py
│  │  │  question_views.py
│  │  │
│  │  └─__pycache__
│  │          answer_views.cpython-310.pyc
│  │          main_views.cpython-310.pyc
│  │          question_views.cpython-310.pyc
│  │
│  └─__pycache__
│          models.cpython-310.pyc
│          __init__.cpython-310.pyc
│
└─__pycache__
        config.cpython-310.pyc
        pybo.cpython-310.pyc
```

### To DO

**(01.12)**
- 부트스트랩을 이용한 화면 꾸미기
- `https://wikidocs.net/81050`