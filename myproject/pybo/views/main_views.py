from flask import Blueprint, render_template

from pybo.models import Question

bp=Blueprint('main', __name__, url_prefix='/')
# "main"은 블루프린트의 "별칭". 나중에 자주 사용할 url_for 함수에서 사용
# url_prefix는 라우팅 함수의 애너테이션 URL 앞에 기본으로 붙일 접두어 URL을 의미

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    question_list=Question.query.order_by(Question.create_date.desc())
    #order_by=조회결과 정렬.desc=역순. 작성일시 순으로 조회하려면 desc 대신 asc().
    return render_template('question/question_list.html', question_list=question_list)
    # 템플릿 파일을 화면으로 렌더링 하는 함수. question_list.html이게 템플릿 파일.

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get(question_id)
    return render_template('question/question_detail.html', question=question)
