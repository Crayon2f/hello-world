# coding:utf-8
import pymysql

from kit import config_kit, str_kit
from mysql.sql_error import SQLError
from mysql.sql_cnd import *
from mysql.sql_validator import Validator


class MySQL:
    def __init__(self):
        self.__connection = pymysql.connect(host=config_kit.CONFIG.get('db-mysql', 'host'),
                                            port=config_kit.CONFIG.getint('db-mysql', 'port'),
                                            user=config_kit.CONFIG.get('db-mysql', 'username'),
                                            passwd=config_kit.CONFIG.get('db-mysql', 'password'),
                                            db=config_kit.CONFIG.get('db-mysql', 'database'),
                                            charset=config_kit.CONFIG.get('db-mysql', 'charset'))
        self.__cursor = self.__connection.cursor(pymysql.cursors.DictCursor)

    def query(self, table, params='*', cnd=None):
        Validator.check_table(table)
        if params is None or len(params) == 0:
            params = '*'
        Validator.check_query_params(params)
        query_sql = 'select '
        if type(params) in [set, list, tuple]:
            query_sql += ','.join(params)
        else:
            query_sql += params
        query_sql += ' from %s ' % table
        if cnd is not None:
            query_sql += cnd.generate()
        print(query_sql)
        self.__cursor.execute(query_sql)
        return self.__cursor.fetchall()

    def query_one(self, table, param='*', cnd=None):
        query_list = self.query(table, param, cnd)
        if len(query_list) > 0:
            return query_list[0]
        else:
            return {}

    def delete_by_cnd(self, table, cnd=None):
        Validator.check_table(table)
        if cnd is None:
            raise SQLError('cnd cant\'t be None')
        delete_sql = 'delete from %s ' % table + cnd.generate()
        print(delete_sql)
        count = self.__cursor.execute(delete_sql)
        self.__connection.commit()
        return count

    def delete_by_id(self, table, delete_id):
        Validator.check_table(table)
        if None is delete_id:
            raise SQLError('delete id can\'t be None')
        return self.delete_by_cnd(table, Cnd().where(SqlExpression().exp_and('id', equal, delete_id)))

    def insert(self, table, bean):
        Validator.check_table(table)
        if None is bean or len(bean) == 0:
            raise SQLError('bean can\'t be None')
        insert_sql = 'insert into %s(%s) value (%s)' % (table, ','.join(bean.keys()), ','.join(bean.values()))
        print(insert_sql)
        return self.__cursor.execute(insert_sql)

    def insert_many(self, table, beans):
        Validator.check_table(table)
        if None is beans or len(beans) == 0:
            raise SQLError('beans can\'t be None')
        values_sql = EMPTY
        for bean in beans:
            values_sql += ',(%s)' % ','.join(bean.values())
        insert_sql = 'insert into %s (%s) values %s' % (table, ','.join(beans[0].keys()), values_sql[1:])
        print(insert_sql)
        return self.__cursor.execute(insert_sql)

    def close(self):
        self.__connection.close()


if __name__ == '__main__':
    try:
        # test_bean = {
        #     'province_id': '2222',
        #     'city_name': 'test',
        #     'description': 'test'
        # }
        # result = MySQL().insert('city', test_bean)
        # print(result)
        # print(MySQL().delete_by_id('city', 3414))
        sql_exp = SqlExpression().exp_and('id', equal, 4415)
        result = MySQL().query_one('activity_registration', '*', Cnd().where(sql_exp))
        print(result)

    except SQLError as error:
        print(error.message)
        print(type(error))
        print(error)
        # print('str(Exception):\t', str(Exception))
        # print('str(e):\t\t', str(e1))
        # print('repr(e):\t', repr(e1))
        # print('e.message:\t', e1.message)
        # # print('traceback.print_exc():' % traceback.print_exc())
        # # print('traceback.format_exc():\n%s' % traceback.format_exc())
        # print(type(repr(45)))
