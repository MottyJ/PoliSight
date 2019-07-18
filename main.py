import os
from pymysql import connect, cursors
import bottle



connection = connect(host='localhost',
                     user='root',
                     password='hulk',
                     db='test',
                     charset='utf8',
                     cursorclass=cursors.DictCursor)
print(connection)

def connect(sql):
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except:
        connection.close()

my_query = connect("select longitude,LATITUDE from db_head")
print(my_query)

@bottle.route('/')
def index():

    return bottle.template("index.html")


@bottle.route('/css/<filename:re:.*\.css>')
def d(filename):
    return bottle.static_file(filename,  root='static/css')


@bottle.route('./static/js/<filename:re:.*\.js>')
def a(filename):
    return bottle.static_file(filename,  root='static/js')




def main():

    bottle.run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
    connect()
