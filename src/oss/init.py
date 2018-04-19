import oss2

from kit import config_kit


class Init:
    def __init__(self):
        self.__auth = oss2.Auth(config_kit.CONFIG.get('oss', 'access_key_id'),
                                config_kit.CONFIG.get('oss', 'access_key_secret'))
        self.__service = oss2.Service(self.__auth, config_kit.CONFIG.get('oss', 'endpoint'))
        self._bucket = oss2.Bucket(self.__auth, self.__service.endpoint, config_kit.CONFIG.get('oss', 'bucket_name'))


