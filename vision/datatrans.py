import pymysql, logging, sys
import dataprocess

host = "mysql.hostname.com"
port = "3306"
database = "result"       # 우리가 쓰는 데이터베이스 이름
username = "sunny"      # 우리가 쓰는 유저네임
password = "sunny123"   # 우리가 쓰는 패스워드


def main():

    try:
    #DB Connection 생성
        conn = pymysql.connect(host, user=username, passwd=password, db=database, use_unicode=True, charset='utf8')
        cursor = conn.cursor()

    except:
        logging.error("")
        sys.exit(1)

	
    # cursor.execute("show tables")
    #print(cursor.fetchall())

    # 무ㅓ넣을까
    # 일단 DB 새로 생성해놓고 (result db)
    # result, datetime, temp, humidity? 넘겨야 하나
    # 아니면 result fk fk ? 이건 너무 복잡할듯..
    query = """INSERT INTO result(result, date_time, temp, humidity)
                VALUES (%s, %s, %.1f, %.1f)"""
    result = dataprocess.result
    date_time = dataprocess.date_time
    temp = dataprocess.temp
    humidity = dataprocess.humidity

    cursor.execute(query, (result, date_time, temp, humidity))
    conn.commit()
    
    conn.close()
    
    
if __name__ == '__main__':
	main()