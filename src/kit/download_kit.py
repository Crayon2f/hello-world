# coding=utf-8
import urllib
import os


class DownloadKit:
    def __init__(self, remote_url, download_path):
        self.__remote_url = remote_url
        self.__download_path = download_path

    def download_by_retrieve(self):
        urllib.urlretrieve(self.__remote_url, self.__download_path, self.callback)

    @staticmethod
    def callback(downloaded, data_module, file_size):
        """
        :param downloaded:已经下载的数据块
        :param data_module:数据块的大小
        :param file_size:远程文件的大小
        :return:
        """
        percent = 100.0 * downloaded * data_module / file_size
        if percent > 100:
            percent = 100
        print '%.2f%%' % percent


if __name__ == '__main__':
    url = 'https://aweme.snssdk.com/aweme/v1/playwm/?video_id=480c083064944b4abf79ee2efbb18e65&line=0'
    path = os.path.join('d:\\downloads\\video', 'polaris.mp4')
    DownloadKit(url, path).download_by_retrieve()
