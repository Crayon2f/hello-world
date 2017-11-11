import MySQLdb
import traceback
from kit import config_kit, str_kit

print


class MySQL:
    def __init__(self):
        self.__connection = MySQLdb.connect(host=config_kit.init().get('mysql', 'host'),
                                            port=config_kit.init().getint('mysql', 'port'),
                                            user=config_kit.init().get('mysql', 'username'),
                                            passwd=config_kit.init().get('mysql', 'password'),
                                            db=config_kit.init().get('mysql', 'database'),
                                            charset=config_kit.init().get('mysql', 'charset'))
        self.__cursor = self.__connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    def query(self, table, params='*', cnd=None):
        if str_kit.str_is_none(table):
            raise BaseException('table should be str')
        if params is None or len(params) == 0:
            params = '*'
        query_sql = 'select '
        if type(params) in [set, list, tuple]:
            query_sql += ','.join(params)
        elif type(params) is str:
            query_sql += params
        else:
            raise BaseException('params type error, please choose str, set, list, tuple')

        query_sql += ' from %s ' % table
        if cnd is not None:
            query_sql += cnd.generate()
        print query_sql
        self.__cursor.execute(query_sql)
        return self.__cursor.fetchall()


if __name__ == '__main__':
    try:
        print 9 / 0
        result = MySQL().query('city333')
        print result[0]['city_name']
    except (Exception('haa'), ZeroDivisionError, MySQLdb.ProgrammingError), e1:
        print type(e1)
        print e1
        print 'str(Exception):\t', str(Exception)
        print 'str(e):\t\t', str(e1)
        print 'repr(e):\t', repr(e1)
        print 'e.message:\t', e1.message
        # print 'traceback.print_exc():' % traceback.print_exc()
        # print 'traceback.format_exc():\n%s' % traceback.format_exc()
        print type(repr(45))

