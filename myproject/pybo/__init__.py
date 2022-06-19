from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db=SQLAlchemy()
migrate=Migrate()
#db,migrate 객체 생성. 전역변수.

def create_app():
    app=Flask(__name__)
    app.config.from_object(config)
    #config.py에 작성한 항목을 읽는 것.

    #ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    #db, migrate를 app에 등록

    #db객체 등을create_app 안에서 생성하면 블루프린트 등 다른 모듈에서 사용할 수 없음.
    #그래서 객체들을 create_app '밖'에서 생성하고, 이걸 앱에 등록할 때 create_app 함수에서 init_app 함수로 진행.

    #블루프린트
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    return app
