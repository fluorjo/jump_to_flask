from flask import Blueprint, url_for
from werkzeug.utils import redirect

from pybo.models import Question

bp=Blueprint('main', __name__, url_prefix='/')
# "main"은 블루프린트의 "별칭". 나중에 자주 사용할 url_for 함수에서 사용
# url_prefix는 라우팅 함수의 애너테이션 URL 앞에 기본으로 붙일 접두어 URL을 의미

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
    # 템플릿 파일을 화면으로 렌더링 하는 함수. question_list.html이게 템플릿 파일.

