# coding=utf-8

import sys

import os
import shutil
import traceback

reload(sys)
sys.setdefaultencoding('gbk')


def scan_less_file():
    path = r'g:/artworks/'
    file_list = os.listdir(path)
    index = 0

    for f in file_list:
        f_list = os.listdir(path + f)
        inner_index = 0
        flag = False
        for child in f_list:
            if child.endswith('.jpg'):
                flag = True
                # inner_index += 1
        # if 6 > inner_index > 0:
        #     for child in f_list:
        #         if child.endswith('.jpg'):
        #             file_path = u'%s%s/%s' % (path, f, child)
        #             print file_path
        #             os.remove(u'%s%s/%s' % (path, f, child))
        if not flag:
            print f
    print(index)


def rename():
    path = r'g:\artworks'
    file_list = os.listdir(path)
    for child_dir in file_list:
        author_dir = path + '\\' + child_dir
        old = author_dir + '\\detail'
        if not os.path.exists(old):
            continue
        new = author_dir + u'\\细节图'
        os.rename(old, new)
        print child_dir + ' complete !'

        # resume_path = os.path.join(author_dir, u'个人简历.docx')
        # new_resume_path = os.path.join(author_dir, u'个人简历', u'个人简历.docx')
        # new_resume_dir = os.path.join(author_dir, u'个人简历')
        # if not os.path.exists(new_resume_dir):
        #     os.mkdir(new_resume_dir)
        # try:
        #     shutil.move(resume_path, new_resume_path)
        #     print child_dir + ' complete !'
        # except BaseException, e:
        #     print e.message
        #     traceback.print_exc()
        #     print child_dir + ' is fail '


def dir_rename(target_dir, new_name):
    file_list = os.listdir(target_dir)

    if len(file_list) <= 0:
        os.rename(target_dir, new_name)


if __name__ == '__main__':
    # rename()
    # scan_less_file()
    # shutil.move(r"g:\t.txt", r'g:\other\t.txt')
    # old = r'G:\artworks\0000a32b-8313-4d93-8bbf-97156b6c574d\detail'
    # new = r'G:\artworks\0000a32b-8313-4d93-8bbf-97156b6c574d' + u'\\细节图'
    # os.rename(old, new)
    var = 'kkk.jpg'
    print(var[var.index('.'):])
