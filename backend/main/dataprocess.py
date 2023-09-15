import imageread
from datetime import datetime
import pymysql

# Extract information what we want
ident = imageread.texts[0].description

# Decide the result of ident
if ident == '11' or ident == 'II' or ident == '||' or ident == 'll':
    result = '양성'
elif ident == '1' or ident == 'I' or ident == '|' or ident == 'l':
    result = '음성'
else:
    result = '검출 오류'

# Take real date time
date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

image = imageread.content

# take temperature and humidity to connect mysql

connection = pymysql.connect(
    host='192.168.119.119',  # 호스트 주소
    user='chm',  # 사용자 이름
    password='1234',  # 비밀번호
    database='mysql'  # 데이터베이스 이름
)

# 커서 생성
cursor = connection.cursor()

# 쿼리 실행
query = "SELECT temperature, humidity FROM rspDHT22 ORDER BY timestamp DESC LIMIT 1"
cursor.execute(query)

# 결과 가져오기
results = cursor.fetchone()

# 결과 처리
if results:
    temperature, humidity = results
else:
    print("테이블에 데이터가 없습니다.")

# 연결 및 커서 닫기
cursor.close()
connection.close()
