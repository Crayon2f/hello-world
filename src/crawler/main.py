# # coding=utf-8
# import urllib2
# import json
# import requests
# import os
#
#
# def simple_crawl():
#     # response = urllib2.urlopen('https://www.douyin.com/aweme/v1/music/aweme/?music_id=6495982215716375309'
#     #                            '&count=1000&cursor=0&aid=1128&screen_limit=3&download_click_limit=3')
#     response = urllib2.urlopen('https://www.douyin.com/aweme/v1/hot_aweme/?app_id=1128&cursor=0&'
#                                'count=36&parent_rid=20180224161540010006024153722C5B&aweme_id=6523080391090244867')
#     result_json = json.load(response)
#     for index, info in enumerate(result_json['aweme_list']):
#         try:
#             file_path = 'D:/downloads/video/polaris/' + str(index) + '.mp4'
#             if not os.path.exists(file_path):
#                 url = info['video']['play_addr']['url_list'][0]
#                 video_resp = requests.get(url)
#                 with open(file_path, 'wb') as code:
#                     code.write(video_resp.content)
#         except Exception:
#             continue
#
#
# if __name__ == '__main__':
#    simple_crawl()
