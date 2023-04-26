import pymysql, logging, sys
import dataprocess

host = "mysql.hostname.com"
port = "3306"
database = "test"       # 우리가 쓰는 데이터베이스 이름
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

    query = "INSERT INTO ... ..."
    cursor.execute(query)
    conn.commit()
    
    conn.close()
    
    
if __name__ == '__main__':
	main()