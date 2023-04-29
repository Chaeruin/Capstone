# -*- coding:utf-8 -*-
import mysql.connector
import Adafruit_DHT as sensor
from datetime import datetime
import time

while True:
    try:
        # MySQL 데이터베이스 연결
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1234",
            database="mysql"
        )
        cursor = connection.cursor()

        # 센서에서 온습도 값 읽기
        humidity, temperature = sensor.read_retry(sensor.DHT22, 4)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 데이터베이스에 값 삽입
        query = "INSERT INTO tblSensorDHT22 VALUES (%s, %s, %s)"
        values = (timestamp, humidity, temperature)
        cursor.execute(query, values)
        connection.commit()
        
        print(timestamp,"Humidity: ""%0.2f"%humidity,"Temperature: ""%0.2f"% temperature)

        if temperature > 22.0 and humidity >51.7:
            print("온도와 습도가 너무 높습니다")
            break
        elif temperature >22.0:
            print("온도가 너무 높습니다")
            break
        elif humidity > 51.7:
            print("습도가 너무 높습니다")
            break
        
        

        # 연결 및 커서 닫기
        cursor.close()
        connection.close()

        # 5초간 대기
        time.sleep(60)

    except mysql.connector.Error as error:
        print("MySQL 데이터베이스 연결 오류: {}".format(error))

    finally:
        # 연결 및 커서 닫기
        cursor.close()
        connection.close()
