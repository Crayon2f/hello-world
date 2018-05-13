# coding=utf-8
import pandas as pd

if __name__ == '__main__':
    # data = Series(
    #     [1, 2, 3, 4, 5],
    #     index=['first', 'second', 'third', 'fourth', 'fifth']
    # )
    # print data
    # print data.values
    # print data.index[0]
    # data = pd.read_excel("/Users/goufeifan/Downloads/test2.xls")
    # print data
    '''
          名字  工作
    ------------------------
          张三  老师
          Jack  演员
          李四  歌手
          王五  诗人
    '''
    # print data.columns
    # for key in data.keys():
    #     for content in data[key]:
    #         print content
    # print(data[key])
    # print data.values

    # '''
    #     loc:    data.loc[“横索引”][“纵索引”]
    #     iloc:    data.iloc[“横索引”][“纵索引”]
    # '''
    #
    # print data.loc[0][0]
    # print data.loc[1][u'工作']
    # print data.iloc[0][0]
    # print data.iloc[2][u'工作']
    #
    # print '-' * 20
    #
    # print data.loc[0:3][u'工作']  # 顾头顾腚
    # print data.iloc[0:3][u'工作']  # 顾头不顾腚
    #
    # # see ? the different !!
    #
    # '''
    #     对于loc来说，他的使用方法：
    #     data.loc[横索引（包前包后），列索引（用列名）（包前包后）]
    #
    #     对于iloc来说，他的使用方法：
    #     data.iloc[横索引（包前不包后），列索引（用序号）（包前不包后）]
    # '''
    #
    # print '-' * 30
    #
    # other_data = pd.read_excel('C:/Users/feifan.gou/Desktop/excel/test.xlsx', index_col=u'工作')  # 指定以哪列为索引
    # print other_data

    a = ['yi', '2', '3']
    b = ['yi', '5', '6']

    # 字典中的key值即为csv中列名
    dataFrame = pd.DataFrame({'a_name': a, 'b_name': b})

    # 将DataFrame存储为csv,index表示是否显示行名，default=True
    dataFrame.to_csv("/Users/goufeifan/Downloads/temp_cvs.csv", index=False, sep=',')
