import pymysql
#打开数据库连接
db = pymysql.connect("localhost","root","123456","test1",charset='utf8')

#使用cursor（）方法创建一个游标对象 cursor
cursor = db.cursor()




def shujuku(u,d):
    global cursor,db
    user =u
    danmu =d
    # 使用 execute（）方法执行 SQL查询
    cursor.execute("SELECT VERSION()")

    # 使用fetchone（）方法获取单条数据
    data = cursor.fetchone()
    print("databse version:%s" % data)

    # SQL 插入语句
    sql = """INSERT INTO dan_mu(user,danmu)
         VALUES ('%s','%s')"""%(user,danmu)#注意写法
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 提交到数据库执行插入
       db.commit()
    except BaseException as e:
        print(e)
        db.rollback()
       # 如果发生错误则回滚
if __name__ == "__main__":
    shujuku("小红","恋人未满")
    db.close()
