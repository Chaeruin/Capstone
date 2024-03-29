import mysql.connector
import Adafruit_DHT as sensor
from datetime import datetime
import time

# MySQL 데이터베이스 연결
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="mysql"
)
cursor = connection.cursor()

while True:
    try:
        # 센서에서 온습도 값 읽기
        humidity, temperature = sensor.read_retry(sensor.DHT22, 4)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')

        # 데이터베이스에 값 삽입
        query = "INSERT INTO rspDHT22 VALUES (%s, %s, %s)"
        values = (timestamp, temperature, humidity)
        cursor.execute(query, values)
        connection.commit()

        print(timestamp,"Humidity: ""%0.2f"%humidity,"Temperature: ""%0.2f"% temperature)

        # 60초간 대기
        time.sleep(60)

    except mysql.connector.Error as error:
        print("MySQL 데이터베이스 연결 오류: {}".format(error))

# 연결 및 커서 닫기
cursor.close()
connection.close()