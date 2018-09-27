# coding=utf-8
import traceback

import MySQLdb
import sys
import os
import math
from kit import config_kit
from docx import Document
from docx.shared import Pt
from oss import oss_kit
from import_zy import get_region

reload(sys)
sys.setdefaultencoding('utf-8')

connection = MySQLdb.connect(host='mt-58art-database-open.mysql.rds.aliyuncs.com',
                             port=3306,
                             user='mt_art58',
                             passwd='Admin_58art',
                             db='art58',
                             charset='utf8')
cursor = connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)

# artwork_dir = '/Volumes/Crayon2f/artworks/'
artwork_dir = u'f:\\artworks\\'
change_sign = '-'
activity_id = config_kit.CONFIG.get('activity', 'id')


def create_dir():
    sql = "SELECT user_id FROM activity_registration WHERE activity_id = %s AND user_id <> ''" % activity_id
    cursor.execute(sql)
    user_list = cursor.fetchall()
    for user in user_list:
        os.mkdir(artwork_dir + user['user_id'])


def get_artwork():
    sql = "SELECT  `NAME` AS name, ID id, AUTHOR author, `client` FROM voting_artwork WHERE ACTIVITY_ID = %s" \
          % activity_id
    cursor.execute(sql)
    return cursor.fetchall()


def download_artwork_form_oss():
    artwork_list = get_artwork()
    index_out = 0
    _oss_kit = oss_kit.OssKit()
    for artwork in artwork_list:
        index_out += 1
        print index_out
        dir_name = artwork_dir + artwork['author']
        artwork_name = translate_sign(artwork['name'].strip())
        artwork_path = '%s/%s.jpg' % (dir_name, artwork_name)
        if os.path.exists(artwork_path):
            artwork_path = recursion(artwork_path, 0)
        bucket_name = 'mt-official'
        if not artwork['client'] == '58':
            bucket_name = 'mt-zy-official'
            if _oss_kit.get_bucket_name() == 'mt-official':
                _oss_kit = oss_kit.OssKit(bucket_name)
        elif artwork['client'] == '58':
            if _oss_kit.get_bucket_name() == 'mt-zy-official':
                _oss_kit = oss_kit.OssKit()

        key_list = get_oss_key(artwork['id'], bucket_name)
        try:
            if len(key_list) > 0:
                key = key_list[0]
                if not os.path.exists(artwork_path):
                    _oss_kit.download(str(key['key']), artwork_path)
                if len(key_list) > 1:
                    for index, append_key in enumerate(key_list[1:]):
                        append_dir = '%s/detail/' % dir_name
                        if not os.path.exists(append_dir):
                            os.mkdir(append_dir)
                        append_path = '%s/%s[%d].jpg' % (append_dir, artwork_name, index + 1)
                        if not os.path.exists(append_path):
                            _oss_kit.download(str(append_key['key']), append_path)
            else:
                print artwork['id'] + ' has not oss_key'
        except BaseException, exception:
            print(exception.message)
            print('===== %s =====' % artwork['id'])
            traceback.print_exc()


def get_oss_key(artwork_id, bucket_name):
    sql = "select key_value as `key` from art_images where source_id = '%s' and " \
          "bucket_name = '%s' and RULE_CODE = 'artwork_open' order by category desc " % (artwork_id, bucket_name)
    cursor.execute(sql)
    return cursor.fetchall()


def translate_sign(origin):
    if origin is '':
        return origin
    return origin.replace('<', change_sign).replace('>', change_sign).replace(':', change_sign) \
        .replace('"', change_sign).replace('/', change_sign).replace('\\', change_sign) \
        .replace('|', change_sign).replace('?', change_sign).replace('*', change_sign)


def export_resume():
    region_dict = get_region.get_name()
    sql = "SELECT ar.user_id, ar.real_name, ar.birthday, ar.live_place AS live_place, su.GRADUATEPLACE AS school," \
          " ar.terminal FROM activity_registration ar LEFT JOIN sys_user su ON ar.user_id = su.ID " \
          "WHERE ar.activity_id = %s " % activity_id
    cursor.execute(sql)
    user_list = cursor.fetchall()
    index = 0
    for user in user_list:
        index += 1
        print index
        personal_exhibition = []
        joint_exhibition = []
        try:
            if user['terminal'] != 'zai_yi':
                show_sql = "select NAME as name, SPACENAME as space_name, CITY as city, `YEAR` as  `year`, " \
                           "TYPE as type from art_show_extern where CRT_TELLER_ID = '%s' ORDER BY YEAR desc" % \
                           user['user_id']
                cursor.execute(show_sql)
                show_list = cursor.fetchall()
                if len(show_list) > 0:
                    for show in show_list:
                        if int(show['type']) == 0:
                            personal_exhibition.append(show)
                        else:
                            joint_exhibition.append(show)
            region_id = user['live_place'] if user['live_place'] and user['live_place'] != '' else None
            region_name = u'未知' if (None is region_id) or (type(region_id) is float and math.isnan(region_id)) else \
                region_dict[region_id]
            real_name = str(user['real_name']).strip()
            out_path = u"%s%s\\个人简历.docx" % (artwork_dir, user['user_id'])
            if not os.path.exists(artwork_dir + user['user_id']):
                out_path = u"%s%s.docx" % (artwork_dir, translate_sign(real_name))
            write_word(joint_exhibition, personal_exhibition, out_path, real_name, user['birthday'], region_name,
                       user['school'])
            print user['real_name'] + ' resume export successful '
        except BaseException, exception:
            print exception.message
            traceback.print_exc()
            print "export word error user_id ==> %s" % user['user_id']


def write_word(joint_exhibition, personal_exhibition, out_path, real_name='', birthday='', live_place='', school=''):
    document = Document()

    document.add_heading(u'个人简历', 0)
    document.add_paragraph()

    paragraph = document.add_paragraph()
    name = paragraph.add_run(u'姓名：')
    name.font.size = Pt(12)
    name.font.name = u'微软雅黑'
    name.bold = True
    if real_name is None:
        real_name = ''
    paragraph.add_run(u'%s' % real_name)

    paragraph = document.add_paragraph()
    name = paragraph.add_run(u'出生日期：')
    name.font.size = Pt(12)
    name.font.name = u'微软雅黑'
    name.bold = True
    if birthday is None:
        birthday = ''
    paragraph.add_run(birthday)

    paragraph = document.add_paragraph()
    name = paragraph.add_run(u'现居住地：')
    name.font.size = Pt(12)
    name.font.name = u'微软雅黑'
    name.bold = True
    if live_place is None:
        live_place = ''
    paragraph.add_run(u'%s' % live_place)

    paragraph = document.add_paragraph()
    name = paragraph.add_run(u'毕业院校：')
    name.font.size = Pt(12)
    name.font.name = u'微软雅黑'
    name.bold = True
    if school is None:
        school = ''
    paragraph.add_run(u'%s' % school)

    paragraph = document.add_paragraph()
    name = paragraph.add_run(u'个展：')
    name.font.size = Pt(12)
    name.font.name = u'微软雅黑'
    name.bold = True
    if len(personal_exhibition) > 0:
        for exhibition in personal_exhibition:
            paragraph.add_run(u'\r %s %s %s %s' % (exhibition['year'], exhibition['name'], exhibition['space_name'],
                                                   exhibition['city']))

    paragraph = document.add_paragraph()
    name = paragraph.add_run(u'联展：')
    name.font.size = Pt(12)
    name.font.name = u'微软雅黑'
    name.bold = True
    if len(joint_exhibition) > 0:
        for exhibition in joint_exhibition:
            text = u'\r %s %s %s %s' % (exhibition['year'], exhibition['name'], exhibition['space_name'],
                                        exhibition['city'])
            # print text
            paragraph.add_run(text)
    document.save(out_path)


def recursion(path, index):
    if os.path.exists(path):
        index += 1
        path = '%s(%d)' % (path, index)
        return recursion(path, index)
    else:
        return path


def translate():
    sql = "SELECT user_id, real_name FROM activity_registration WHERE activity_id = %s and user_id <> '';" % activity_id
    cursor.execute(sql)
    user_list = cursor.fetchall()
    for user in user_list:
        author_dir = os.path.join(artwork_dir, user['user_id'])
        if os.path.exists(author_dir):
            new_author_dir = os.path.join(artwork_dir, translate_sign(user['real_name'].strip()))
            if os.path.exists(new_author_dir):
                new_author_dir = recursion(new_author_dir, 0)
            print(new_author_dir)
            try:
                os.rename(author_dir, new_author_dir)
                print user['real_name'] + ' success '
            except BaseException, e:
                print e.message
                traceback.print_exc()
                print user['user_id'] + ' fail'


def export_attachment():
    sql = 'select user_id, bucket_name, key_value from activity_attachment where activity_id = %s' % activity_id
    cursor.execute(sql)
    attachment_list = cursor.fetchall()
    for attachment in attachment_list:
        author_dir = os.path.join(artwork_dir, attachment['user_id'])
        oss_kit_ = oss_kit.OssKit(attachment['bucket_name'])
        key = str(attachment['key_value'])
        oss_kit_.download(key, os.path.join(author_dir, u'方案'+ key[key.index('.'):]))


if __name__ == '__main__':
    #
    #     select
    #     real_name,
    #     mobile,
    #     ar.email,
    #     ar.birthday,
    #     concat_ws('-', parent.REGION_NAME, region.REGION_NAME)
    #     live_place,
    #     su.GRADUATEPLACE
    # from activity_registration ar
    #
    # left
    # join
    # sys_user
    # su
    # on
    # ar.user_id = su.ID
    # left
    # join
    # region
    # region
    # on
    # region.ID = ar.live_place
    # left
    # join
    # region
    # parent
    # on
    # region.PARENT_ID = parent.ID
    # where
    # ar.activity_id = 10000007

    # create_dir()
    # download_artwork_form_oss()
    # export_resume()
    # export_attachment()
    translate()

