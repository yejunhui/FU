#本文件需要用到pymysql
import pymysql

class pmysql:
    def __init__(self):
        conn = pymysql.connect(host='localhost',user='user',password='123456',db='d')
        conn.autocommit(True)
        self.cur = conn.cursor()


    def msql(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def cls(self):
        self.cur.close()

