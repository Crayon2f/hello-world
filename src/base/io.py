# coding=utf-8
# IO流

# ioStr = raw_input("输入：")
# print ioStr


# inputStr = input("enter your input:")
# print inputStr

# for i in range(2, 10, 2):
#     print i * 5
import os

file_write_start = open('C:\\Users\\feifan.gou\\Desktop\\python.txt', 'w+')

# fo.close()

# write
file_write_start.write("write to file =++++++++++++++++++++")

file_write_start.close()
# read
fi = open(file_write_start.name, 'r+')
readStr = fi.read(10)
print readStr, fi.tell()

'''
    offset 移动的位置, from 0:开头,1:当前位置,2:结尾 
'''

fi.seek(2, 1)
readStr = fi.read(9)
print readStr

fi.close()
# append
file_write_end = open(file_write_start.name, 'a+')
file_write_end.write(' ============= append to file ')
file_write_end.close()

fi = open(file_write_start.name, 'r+')
readStr = fi.read()
print readStr
# fo.close()
fi.close()
print file_write_start.name, file_write_start.mode, file_write_start.closed


# rename
# os.rename('C:\\Users\\feifan.gou\\Desktop\\python_rename.txt', 'C:\\Users\\feifan.gou\\Desktop\\python_rename2.txt')

# remove
# os.remove("C:\\Users\\feifan.gou\\Desktop\\remove.txt")

# mk_dir
# os.mkdir('C:\\Users\\feifan.gou\\Desktop\\test_mk_dir')

print os.getcwd()  # 当前工程的根目录

# os.chdir('C:\\Users\\feifan.gou\\Desktop')  # 切换目录,更改当前目录
# os.mkdir('test_chdir')

# os.rmdir('test_mk_dir2')  # 删除文件夹,前提是文件中没有文件

# 读取行
readLineFile = open("C:\\Users\\feifan.gou\\Desktop\\python_lines.txt", 'r+')
print readLineFile.readline()
print readLineFile.readline()
print readLineFile.readline(4)
print len(readLineFile.readlines())
print readLineFile.readlines(1)






