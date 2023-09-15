from django.conf import settings
import pymysql

#이거를 temperature로 설정
def get_temperature():
    # MySQL 연결 설정
    connection = pymysql.connect(
        host='192.168.119.119',
        user='chm',
        password='1234',
        database='mysql'
    )

    # 커서 생성
    cursor = connection.cursor()

    # 쿼리 문
    query = "SELECT temperature FROM rspDHT22 ORDER BY timestamp DESC LIMIT 1"

    cursor.execute(query)

    # 결과값 가져오기
    result = cursor.fetchone()
    
    if result:
        no = result[0]
        print(no)
        return no
    else:
        return None
    
    # # MySQL 연결 종료
    cursor.close()
    connection.close()

#이거를 humidity로 설정
def get_humidity():
    # MySQL 연결 설정
    connection = pymysql.connect(
        host='192.168.119.119',
        user='chm',
        password='1234',
        database='mysql'
    )

    # 커서 생성
    cursor = connection.cursor()

    # 쿼리 문
    query = "SELECT humidity FROM rspDHT22 ORDER BY timestamp DESC LIMIT 1"

    cursor.execute(query)

    # 결과값 가져오기
    result = cursor.fetchone()
    
    if result:
        name = result[0]
        print(name)
        return name
    else:
        return None
    
    # MySQL 연결 종료
    cursor.close()
    connection.close()