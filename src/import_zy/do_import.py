# coding=utf-8
import pandas as pd
import uuid
import MySQLdb
import datetime
import math
import traceback
from oss import oss_kit


def get_uuid():
    return str(uuid.uuid4()).replace('-', '').upper()


# connection = MySQLdb.connect(host='59.110.25.244',
#                              port=3306,
#                              user='root',
#                              passwd='mt_58art@',
#                              db='58art_test',
connection = MySQLdb.connect(host='mt-58art-database-open.mysql.rds.aliyuncs.com',
                             port=3306,
                             user='mt_art58',
                             passwd='Admin_58art',
                             db='art58',
                             charset='utf8')
cursor = connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)

password = 'E10ADC3949BA59ABBE56E057F20F883E'

activity_id = '10000005'


def execute(sql):
    cursor.execute(sql)


def get_oss_key(param_code):
    return 'artwork_main/%s/%s/%s/%s/%s.jpg' % (
        datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, param_code,
        get_uuid())


if __name__ == '__main__':
    # data = pd.read_excel("/Users/goufeifan/Downloads/artwork_info_one.xlsx")
    data = pd.read_excel("/Users/goufeifan/Downloads/artwork_info.xlsx")
    user_art_dict = {}
    try:
        for index, row in data.iterrows():  # 获取每行的index、row
            user_id = int(row[2])
            age = row[5] if not math.isnan(row[5]) else 2016
            material = u'未知' if type(row[9]) == float and math.isnan(row[9]) else row[9]
            artwork = (row[1], row[3], row[6], material, age)
            if user_id in user_art_dict:
                user_art_dict[user_id].append(artwork)
            else:
                user_art_dict[user_id] = [artwork]

        # user_data = pd.read_excel("/Users/goufeifan/Downloads/user_info_one.xlsx")
        user_data = pd.read_excel("/Users/goufeifan/Downloads/user_info.xlsx")
        for index, row in user_data.iterrows():
            artwork_info = user_art_dict[row[0]]
            print(row[0])
            user_id = get_uuid()
            insert_user_sql = "INSERT INTO sys_user  (ID, PASSWORD, NICKNAME, NAME, EMAIL, MOBILEPHONE, BIRTHDAY, GRADUATEPLACE, AWARD, ROLE, REGISTTIME, STATE, IS_EDIT, IS_IMPORT, client) " \
                              "VALUE ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', 0, '2018-04-19 20:00:00', 0, 1, 'NO', 'zai_yi')" % (
                                  user_id, password, row[1], row[4], row[3], row[2], row[9][0:11], row[7], row[11]
                              )
            execute(insert_user_sql)

            insert_record_dql = "INSERT into activity_registration(activity_id, user_id, artwork_count, real_name, birthday, live_nation, live_place, mobile, email, terminal) " \
                                "value (10000005, '%s', %s, '%s','%s','%s','%s','%s','%s','%s')" % (
                                    user_id, len(artwork_info), row[4], row[9][0:11], u'中国', '', row[2], row[3], 'pc'
                                )
            execute(insert_record_dql)
            insert_voting_sql = "INSERT INTO voting(id, show_id, user_id, round, over, voting_user_id) VALUE ('%s', '%s', '%s', '%s', '%s', '%s') " % (
                get_uuid(), activity_id, user_id, 1, 0, 0
            )
            execute(insert_voting_sql)
            for info in artwork_info:
                art_id = info[0]
                print(' --- %s' % art_id)
                artwork_id = get_uuid()
                insert_art_sql = "INSERT INTO voting_artwork(ID, NAME, AUTHOR, SIZE, MATERIAL, AGE,client, ACTIVITY_ID) VALUE " \
                                 "('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                                     artwork_id, info[1], user_id, info[2], info[3], info[4], 'zai_yi', activity_id
                                 )
                execute(insert_art_sql)
                image_path = '/Users/goufeifan/Downloads/image/%s.jpg' % art_id
                code = get_uuid()
                oss_key = get_oss_key(code)
                oss_kit.OssKit().upload(oss_key, image_path)
                insert_image_sql = "INSERT INTO art_images (CODE, SOURCE_ID, BUCKET_NAME, KEY_VALUE, CATEGORY, RULE_CODE) VALUES  " \
                                   "('%s','%s','mt-zy-official','%s','artwork_main','artwork_open'),('%s','%s','mt-zy-official','%s','artwork_main','original')" % (
                                       code, artwork_id, oss_key, code, artwork_id, oss_key
                                   )
                execute(insert_image_sql)
            connection.commit()
    except BaseException, e:
        print e.message
        traceback.print_exc()
        connection.rollback()
    finally:
        connection.close()
