# coding=utf-8
from docx import Document
from docx.shared import Pt

document = Document()

document.add_heading(u'个人简历', 0)
document.add_paragraph()

paragraph = document.add_paragraph()
name = paragraph.add_run(u'姓名：')
name.font.size = Pt(12)
name.font.name = u'微软雅黑'
name.bold = True
paragraph.add_run(u'张三')

paragraph = document.add_paragraph()
name = paragraph.add_run(u'出生日期：')
name.font.size = Pt(12)
name.font.name = u'微软雅黑'
name.bold = True
paragraph.add_run('1989-10-09')

paragraph = document.add_paragraph()
name = paragraph.add_run(u'现居住地：')
name.font.size = Pt(12)
name.font.name = u'微软雅黑'
name.bold = True
paragraph.add_run(u'北京-朝阳区')

paragraph = document.add_paragraph()
name = paragraph.add_run(u'毕业院校：')
name.font.size = Pt(12)
name.font.name = u'微软雅黑'
name.bold = True
paragraph.add_run(u'首都师范大学')

paragraph = document.add_paragraph()
name = paragraph.add_run(u'毕业院校：')
name.font.size = Pt(12)
name.font.name = u'微软雅黑'
name.bold = True
paragraph.add_run(u'\r11111')

document.save("C:\\Users\\Lenovo\\Desktop\\test2.docx")
