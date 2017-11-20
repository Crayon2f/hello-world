from kit import str_kit
from mysql.sql_error import SQLError


class Validator:
    def __init__(self):
        pass

    @staticmethod
    def check_table(table):
        if str_kit.str_is_none(table):
            raise SQLError('table cant\'t be None and should be str()')

    @staticmethod
    def check_query_params(params):
        if params not in [list, set, str, tuple]:
            raise SQLError('params type error, please choose str, set, list, tuple')
