import MySQLdb

from kit import config_kit

print


class MySQL:
    def __init__(self):
        self.__connection = MySQLdb.connect(host=config_kit.init().get('mysql', 'host'),
                                            port=config_kit.init().getint('mysql', 'port'),
                                            user=config_kit.init().get('mysql', 'user'),
                                            passwd=config_kit.init().get('mysql', 'password'),
                                            db=config_kit.init().get('mysql', 'database'),
                                            charset=config_kit.init().get('mysql', 'charset'))
    def query(self, table, ):
