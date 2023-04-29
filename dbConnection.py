# -*- coding:utf-8 -*-
import mysql.connector;

Maria_Config = {
 "user" : "root",
 "passwd" : "1234",
 "host" : "127.0.0.1",
 "database" : "mysql",
 "port" : "3306"
}

Maria = mysql.connector.connect(**Maria_Config)
print(Maria)
