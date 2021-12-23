import pymysql

con = pymysql.connect(host='localhost',user='root',password='123456',db='test',port=3306)
cur=con.cursor()
# cur.execute("INSERT INTO a1(name,id,age,gender) VALUES('王五',2,123,'男')")

cur.executemany("INSERT INTO a1(name,id,age,gender) VALUES('王五%s',%s,%s,'男')",list_1)



con.commit()

cur.close()
con.close()
