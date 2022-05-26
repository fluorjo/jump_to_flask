import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))
#데이터베이스 접속 주소
#이 설정으로 sqlite 데이터베이스가 사용되고, 데이터베이스 파일은 pybo.db.로 저장됨.
SQLALCHEMY_TRACK_MODIFICATIONS = False
#SQLAlchemy의 이벤트를 처리하는 옵션

