import os
from pymysql import connect, cursors
import bottle



connection = connect(host='localhost',
                     user='root',
                     password='hulk',
                     db='imdb',
                     charset='utf8',
                     cursorclass=cursors.DictCursor)
print(connection)

def connect():
    try:
        with connection.cursor() as cursor:
            sql ="select full_name from actors"
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                print(i)

    except:
        connection.close()


@bottle.route('/')
def index():
    path = os.path.abspath(__file__)
    print("fasdafs")
    return bottle.template("index.html")


@bottle.route('/static/css/<filename:re:.*\.css>')
def d(filename):
    return bottle.static_file(filename,  root='static/css')


@bottle.route('/static/js/<filename:re:.*\.js>')
def a(filename):
    return bottle.static_file(filename,  root='static/js')




def main():
    connect()
    bottle.run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
