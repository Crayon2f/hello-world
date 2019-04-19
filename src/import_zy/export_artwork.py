# coding=utf-8
import traceback

import MySQLdb
import sys
import os
import math
import time
from kit import config_kit
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn
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
    if len(user_list) > 0:
        if not os.path.exists(artwork_dir):
            os.mkdir(artwork_dir)
    for user in user_list:
        os.mkdir(artwork_dir + user['user_id'])


def get_artwork():
    sql = "SELECT  `NAME` AS name, ID id, AUTHOR author, `client` FROM voting_artwork WHERE ACTIVITY_ID = %s " % activity_id
    cursor.execute(sql)
    return cursor.fetchall()


def download_artwork_form_oss():
    artwork_list = get_artwork()
    index_out = 0
    bucket_name = 'mt-original'
    _oss_kit = oss_kit.OssKit(bucket_name)
    for artwork in artwork_list:
        index_out += 1
        print index_out
        dir_name = artwork_dir + artwork['author']
        artwork_name = translate_sign(artwork['name'].strip())
        artwork_path = '%s/%s.jpg' % (dir_name, artwork_name)
        if os.path.exists(artwork_path):
            artwork_path = recursion(artwork_path, 0)
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
          "bucket_name = '%s' and RULE_CODE = 'original' order by category desc " % (artwork_id, bucket_name)
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
    sql = "SELECT ar.user_id, ar.real_name, ar.birthday, ar.live_place AS live_place," \
          " ar.terminal, su.BIRTHPLACE as birth_place FROM " \
          "activity_registration ar LEFT JOIN sys_user su ON ar.user_id = su.ID " \
          "WHERE ar.activity_id = %s and ar.user_id <> '' and ar.user_id is not null" % activity_id
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
            education_list = get_education_list(user['user_id'])
            write_word(joint_exhibition, personal_exhibition, out_path, real_name, user['birthday'], region_name,
                       user['birth_place'], education_list)
            print user['real_name'] + ' resume export successful '
        except BaseException, exception:
            print exception.message
            traceback.print_exc()
            print "export word error user_id ==> %s" % user['user_id']


def get_education_list(user_id):
    sql = "select * from artist_education where user_id = '%s' order by education asc" % user_id
    cursor.execute(sql)
    return cursor.fetchall()


def write_word(joint_exhibition, personal_exhibition, out_path, real_name='', birthday='', live_place='',
               birth_place='', education_list=None):
    if education_list is None:
        education_list = []
    document = Document()
    document.styles['Normal'].font.name = u'宋体'
    document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')

    paragraph = document.add_paragraph()
    if real_name is None:
        real_name = ''
    name = paragraph.add_run(u'%s' % real_name)
    name.font.size = Pt(12)
    name.bold = True

    paragraph = document.add_paragraph()
    paragraph.add_run(u'%s生于%s' % (birthday, birth_place))
    paragraph = document.add_paragraph()
    if education_list and len(education_list) > 0:
        for education in education_list:
            education_str = ''
            if education['education'] == 2000:
                education_str = u'学士'
            elif education['education'] == 3000:
                education_str = u'硕士'
            elif education['education'] == 4000:
                education_str = u'博士'
            if education_str != '':
                if education['years'] > time.localtime().tm_year:
                    paragraph.add_run(u'%d将毕业于%s%s系 获%s学位' % (
                        education['years'], education['university'], education['series'], education_str))
                else:
                    paragraph.add_run(u'%d毕业于%s%s系 获%s学位' % (
                        education['years'], education['university'], education['series'], education_str))
                paragraph = document.add_paragraph()
    paragraph.add_run(u'现工作生活于%s' % live_place)

    paragraph = document.add_paragraph('\n')
    name = paragraph.add_run(u'个展')
    name.font.size = Pt(12)
    name.bold = True

    generate_show(paragraph, document, personal_exhibition)

    paragraph = document.add_paragraph('\n')
    name = paragraph.add_run(u'联展')
    name.font.size = Pt(12)
    name.bold = True

    generate_show(paragraph, document, joint_exhibition)
    document.save(out_path)


def generate_show(paragraph, document, exhibition_list):

    exhibition_map = {}
    exhibition_list = filter(lambda e: e['name'] != '无', exhibition_list)
    if len(exhibition_list) > 0:
        year_list = []
        for exhibition in exhibition_list:
            year = exhibition['year']
            if year not in exhibition_map:
                exhibition_map[year] = [exhibition]
            else:
                exhibition_map[year].append(exhibition)
            if year not in year_list:
                year_list.append(year)
        for year in year_list:
            paragraph = document.add_paragraph()
            paragraph.add_run(u'%s' % year)
            for exhibition in exhibition_map[year]:
                paragraph = document.add_paragraph()
                paragraph.add_run(u'%s，%s，%s' % (exhibition['name'], exhibition['space_name'], exhibition['city']))
    else:
        paragraph = document.add_paragraph()
        paragraph.add_run(u'无')


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
        oss_kit_.download(key, os.path.join(author_dir, u'方案' + key[key.index('.'):]))


def fix_name_duplicate_artwork():
    dir_list = os.listdir(artwork_dir)
    for user_dir in dir_list:
        artwork_list = os.listdir(os.path.join(artwork_dir, user_dir))
        artwork_map = {}
        for artwork in artwork_list:
            artwork_path = os.path.join(artwork_dir, user_dir, artwork)
            artwork = artwork[0:artwork.find('(1)')]
            if artwork not in artwork_map:
                artwork_map[artwork] = [artwork_path]
            else:
                artwork_map[artwork].append(artwork_path)
            # if os.path.isfile(artwork_path):
            #     if artwork_path.find('(1)') > 0:
            #         print artwork_path
            # suffix = os.path.splitext(artwork_path)[1]
            # if suffix != '.jpg':
            #     index = artwork_path.find('.jpg')
            #     new_path = artwork_path[0:index] + artwork_path[index + 4:] + '.jpg'
            #     print artwork_path + " ==> " + new_path
            #     os.rename(artwork_path, new_path)
        for key in artwork_map:
            duplicate_artwork = artwork_map[key]
            if len(duplicate_artwork) > 1:
                i = 1
                for name in duplicate_artwork:
                    new_path = os.path.join(name[0:name.find('(1)')] + '[' + str(i) + ']') + '.jpg'
                    print name + " ==> " + new_path
                    os.rename(name, new_path)
                    i += 1


if __name__ == '__main__':
    # create_dir()
    # download_artwork_form_oss()
    # fix_name_duplicate_artwork()
    export_resume()
    # export_attachment()
    # translate()
