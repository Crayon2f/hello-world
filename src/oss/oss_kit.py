# coding=utf-8
import os
from oss.init import Init
from kit import str_kit


class OssKit(Init):

    def upload(self, key, local_file):
        """
        上传
        :param key: OSS key
        :param local_file: 本地文件路径
        :return:
        """
        if str_kit.str_is_not_none(key):
            if os.path.exists(local_file):
                self._bucket.put_object_from_file(key, local_file)
                print('--- upload success ---')
            else:
                raise BaseException('local_file[%s] not exist' % local_file)
        else:
            print('key [%s] is empty' % key)

    def download(self, key, local_file):
        if str_kit.str_is_not_none(key):
            self._bucket.get_object_to_file(key, local_file)
            print('--- download success ---')
        else:
            print('key[%s] is empty' % key)

    def delete(self, key):
        if str_kit.str_is_not_none(key):
            self._bucket.delete_object(key)
            print('--- delete success ---')
        else:
            print('key[%s] is empty' % key)

    def get_bucket_name(self):
        return self._bucket.bucket_name
