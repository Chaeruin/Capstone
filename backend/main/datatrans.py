import pymysql, logging, sys
import dataprocess

host = "192.168.119.119"
port = "3306"
database = "mysql"       # 우리가 쓰는 데이터베이스 이름
username = "chm"      # 우리가 쓰는 유저네임
password = "1234"   # 우리가 쓰는 패스워드


def main():

    try:
    #DB Connection 생성
        conn = pymysql.connect(
            host=host, user=username, 
            passwd=password, db=database, 
            use_unicode=True, 
            charset='utf8'
        )
        cursor = conn.cursor()

    except:
        logging.error("")
        sys.exit(1)

    query = '''INSERT INTO main_result(result, date_time, temp, humidity)
                VALUES (%s, %s, %s, %s)'''
    result = dataprocess.result
    date_time = dataprocess.date_time
    temp = dataprocess.temperature
    humidity = dataprocess.humidity

    cursor.execute(query, (result, date_time, temp, humidity))
    conn.commit()
    
    conn.close()
    
if __name__ == '__main__':
	main()