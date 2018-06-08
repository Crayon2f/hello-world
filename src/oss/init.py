import oss2

from kit import config_kit


class Init:
    def __init__(self, bucket_name=None):
        self.__auth = oss2.Auth(config_kit.CONFIG.get('oss', 'access_key_id'),
                                config_kit.CONFIG.get('oss', 'access_key_secret'))
        self.__service = oss2.Service(self.__auth, config_kit.CONFIG.get('oss', 'endpoint'))
        self._bucket = oss2.Bucket(self.__auth, self.__service.endpoint, config_kit.CONFIG.get('oss', 'bucket_name'))
        if bucket_name is not None:
            self._bucket = oss2.Bucket(self.__auth, self.__service.endpoint, bucket_name)

    def _get_bucket_name(self):
        return self._bucket.bucket_name
