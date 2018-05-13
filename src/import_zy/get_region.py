# coding=utf-8
import MySQLdb
import pandas as pd
import math
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

connection = MySQLdb.connect(host='mt-58art-database-open.mysql.rds.aliyuncs.com',
                             port=3306,
                             user='mt_art58',
                             passwd='Admin_58art',
                             db='art58',
                             charset='utf8')
cursor = connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)


def get_name():
    sql = "SELECT concat_ws('-',parent.REGION_NAME, child.REGION_NAME)AS name ,child.id  FROM " \
          "region child LEFT JOIN region parent ON child.PARENT_ID = parent.ID"

    region_dict = {}
    cursor.execute(sql)
    result = cursor.fetchall()
    for region in result:
        if not region['id'] in region_dict:
            region_dict[region['id']] = region['name']
    return region_dict


def replace_region():
    data = pd.read_csv("/Users/goufeifan/Downloads/temp_cvs.csv", encoding="UTF-8")
    region_dict = get_name()
    region_id_list = []
    for index, row in data.iterrows():
        region_id_list.append(row[4])
    name_list = []
    for region_id in region_id_list:
        region_name = u'未知' if type(region_id) is float and math.isnan(region_id) else region_dict[region_id]
        name_list.append(region_name)

    return name_list


if __name__ == '__main__':
    region_name_list = replace_region()
    temp_list = []
    data_frame = pd.DataFrame({'region_name': region_name_list})
    data_frame.to_csv("/Users/goufeifan/Downloads/temp_cvs1.csv", index=False, sep=',')
