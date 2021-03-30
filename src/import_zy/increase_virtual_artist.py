# coding=utf-8
import datetime
import random

import pymysql
import uuid


#  从8号到15号，每天人数 + 10 ，作品数+80；15号到25号，每天 + 20， 作品数+160；25到31号每天+ 50，作品数+400.


class IncreaseVirtualArtistTask:
    def __init__(self, run_date=datetime.datetime.now(), activity_id=10000005):
        self.__init_db()
        self.__run_date = run_date.date()
        self.__activity_id = activity_id
        self.__increase_artist_count = 50
        self.__increase_artwork_count = 7
        self.__already_increase = False
        self.__start_random_number = 1
        # if 15 < self.__run_date.day <= 25:
        #     self.__increase_artist_count = 20
        # if 25 < self.__run_date.day <= 31:
        #     self.__increase_artist_count = 50
        #     self.__increase_artist_count = 50

    def __init_db(self):

        self.__connection = pymysql.connect(
            # host='59.110.25.244',
            # port=3306,
            # user='root',
            # passwd='mt_58art@',
            # db='58art_test',
            # charset='utf8'
            host='mt-58art-database-open.mysql.rds.aliyuncs.com',
            port=3306,
            user='mt_art58',
            passwd='Admin_58art',
            db='art58',
            charset='utf8'
        )
        self.__cursor = self.__connection.cursor(pymysql.cursors.DictCursor)

    def __get_random_time(self):
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
        insert_sql = 'INSERT INTO activity_registration(`activity_id`,`user_id`,`real_name`, `artwork_count`,is_virtual, `create_time`, `update_time`) VALUES'
        random_time_list = self.__get_random_time()
        for index, segment in enumerate(random_time_list):
            user_id = uuid.uuid4()
            segment_sql += "(%s, '%s', 'python shell', %d, 1,'%s', '%s')" % (
                self.__activity_id, user_id, self.__increase_artwork_count, segment, segment)
            if index == len(random_time_list) - 1:
                segment_sql += ';'
            else:
                segment_sql += ','
            self.__start_random_number = self.__start_random_number + 1
        insert_sql += segment_sql
        print(insert_sql)


if __name__ == '__main__':

    for days in range(27, 32):
        today = datetime.datetime.today()
        less_day = datetime.timedelta(days=days)
        # print(today + less_day)
        task = IncreaseVirtualArtistTask(today + less_day, 10000012)
        task.generate()

    print('complete !!')
    # while True:
    #     today = datetime.datetime.now()
    #     if today.month > 3:
    #         break
    #     if today.hour == 0:
    #         try:
    #             task = IncreaseVirtualArtistTask()
    #             task.generate()
    #             print('----------- wait an hour ------------')
    #             time.sleep(3600)
    #         except BaseException, error:
    #             print(error.message)
    #             print(error)
    #     else:
    #         print("now is %d'clock, isn't zero not yet" % today.hour)
    #         print('----------- wait an hour ------------')
    #         time.sleep(3600)
