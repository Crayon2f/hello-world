# coding=utf-8
import random
import MySQLdb
import datetime
import time


#  从8号到15号，每天人数 + 10 ，作品数+80；15号到25号，每天 + 20， 作品数+160；25到31号每天+ 50，作品数+400.
from mysql.sql_error import SQLError


class IncreaseVirtualArtistTask:

    def __init__(self, run_date=datetime.datetime.now(), activity_id=10000005):
        self.__init_db()
        self.__run_date = run_date.date()
        self.__activity_id = activity_id
        self.__increase_artist_count = 10
        self.__already_increase = False
        if 15 < self.__run_date.day < 25:
            self.__increase_artist_count = 20
        if 25 < self.__run_date.day < 31:
            self.__increase_artist_count = 50

    def __init_db(self):
        self.__connection = MySQLdb.connect(
            host='59.110.25.244',
            port=3306,
            user='root',
            passwd='mt_58art@',
            db='58art_test',
            charset='utf8'
        )
        self.__cursor = self.__connection.cursor(MySQLdb.cursors.DictCursor)

    def get_random_time(self):
        random_time_list = []
        start_millis = 9 * 3600
        end_millis = 17 * 3600
        for var in range(0, self.__increase_artist_count):
            second = random.uniform(start_millis, end_millis)
            minute, second = divmod(second, 60)
            hour, minute = divmod(minute, 60)
            random_time_list.append("%s %02d:%02d:%02d" % (self.__run_date, hour, minute, second))
        return random_time_list

    def generate(self):
        segment_sql = ''
        insert_sql = 'INSERT INTO activity_registration(`activity_id`,`real_name`, `artwork_count`, `create_time`, `update_time`) VALUES'
        random_time_list = self.get_random_time()
        for index, segment in enumerate(random_time_list):
            segment_sql += "(10000005, 'python shell', %d, '%s', '%s')" % (int(random.uniform(6, 11)), segment, segment)
            if index == len(random_time_list) - 1:
                segment_sql += ';'
            else:
                segment_sql += ','
        insert_sql += segment_sql
        print insert_sql
        self.__cursor.execute(insert_sql)
        self.__connection.commit()
        self.__already_increase = True
        self.__connection.close()
        print '%s has increased '


if __name__ == '__main__':

    task = IncreaseVirtualArtistTask()
    print 'complete !!'

    # while True:
    #     today = datetime.datetime.now()
    #     if today.month > 3:
    #         break
    #     if today.hour == 0:
    #         try:
    #             task = IncreaseVirtualArtistTask()
    #             task.generate()
    #             print '----------- wait an hour ------------'
    #             time.sleep(3600)
    #         except SQLError, error:
    #             print error.message
    #             print error
    #     else:
    #         print "now is %d'clock, isn't zero not yet" % today.hour
