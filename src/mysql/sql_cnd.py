# coding=utf-8
from datetime import datetime

from kit.str_kit import *

"""定义sql 操作符"""
percent = "%"
not_equal = " <> "
equal = " = "
lesser = " < "
lesser_equal = " <= "
greater = " > "
greater_equal = " >= "
_in = " in "
not_in = " not in "
where = ' where '
_and = ' and '
_or = ' or '
like = ' like '


class Cnd:
    def __init__(self):
        self.__order = EMPTY
        self.__limit = EMPTY
        self.__condition = EMPTY

    def where(self, sql_exp):
        if not sql_exp:
            raise BaseException('sql_exp can not be None')
        if self.__condition is EMPTY:
            self.__condition += '%s%s' % (where, sql_exp.generate_exp())
        return self

    def join_and(self, sql_exp):
        if not sql_exp:
            raise BaseException('sql_exp can not be None')
        if self.__condition is EMPTY:
            self.__condition += '%s%s' % (where, sql_exp.generate_exp())
        else:
            self.__condition += '%s%s' % (_and, sql_exp.generate_exp())
        return self

    def join_or(self, sql_exp):
        if not sql_exp:
            raise BaseException('sql_exp can not be None')
        if self.__condition is EMPTY:
            self.__condition += '%s%s' % (where, sql_exp.generate_exp())
        else:
            self.__condition += '%s%s' % (_or, sql_exp.generate_exp())
        return self

    def asc(self, field):
        if self.__order is EMPTY:
            self.__order = field + 'asc'
        else:
            self.__order += (', ' + field + 'asc')
        return self

    def desc(self, field):
        if self.__order is EMPTY:
            self.__order = field + 'desc'
        else:
            self.__order += (', ' + field + 'desc')
        return self

    def limit(self, offset=0, limit=20):
        self.__limit = 'limit %d,%d' % (offset, limit)
        return self

    def generate(self):
        whole_cnd = EMPTY
        if self.__condition is not EMPTY:
            whole_cnd += self.__condition
        if self.__order is not EMPTY:
            whole_cnd += 'order by %s' % self.__order
        if self.__limit is not EMPTY:
            whole_cnd += self.__limit
        return whole_cnd


class SqlExpression:
    def __init__(self):
        self.__group = []
        self.__join = _and

    def exp(self, whole):
        self.__group.append(whole)
        return self

    def __exp(self, field, op, value):
        value_type = type(value)
        if value_type is str:
            expression = '%s%s\'%s\'' % (field, op, value)
        elif value_type in [int, long]:
            expression = '%s%s%d' % (field, op, value)
        elif value_type in [list, set, tuple] and op == _in:
            expression = '%s in (%s)' % (field, ','.join(str(v) for v in value))
        elif value_type is datetime:
            expression = '%s%s\'%s\'' % (field, op, datetime.strftime(value, '%Y-%m-%d %H:%M:%S'))
        else:
            raise BaseException('value type error, please choose: number, string, datetime, collection, tuple')
        self.__group.append(expression)

    def is_null(self, field):
        if str_is_not_none(field):
            self.__group.append('%s is null' % field)
        return self

    def is_not_null(self, field):
        if str_is_not_none(field):
            self.__group.append('%s is not null' % field)
        return self

    def like(self, field, value):
        self.__group.append('%s%s%s' % (field, like, percent + value + percent))
        return self

    def like_start(self, field, value):
        self.__group.append('%s%s%s' % (field, like, value + percent))
        return self

    def like_end(self, field, value):
        self.__group.append('%s%s%s' % (field, like, value + percent))
        return self

    def exp_and(self, field, op, value):
        self.__exp(field, op, value)
        return self

    def exp_or(self, field, op, value):
        self.__exp(field, op, value)
        self.__join = _or
        return self

    def generate_exp(self):
        return '(%s) ' % self.__join.join(self.__group)


if __name__ == '__main__':
    expression1 = SqlExpression().exp_and('name', equal, '张三').exp_and('age', greater_equal, 34)
    expression2 = SqlExpression().like('name', 'z').exp_and('birthday', equal, datetime.now())
    expression3 = SqlExpression().exp_and('name', _in, ['z', 'd', 'd', 'f']).exp_and('birthday', equal, datetime.now())
    print Cnd().where(expression1).join_or(expression2).join_or(expression3).generate()
