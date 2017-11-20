class SQLError(BaseException):
    def __init__(self, error_msg):
        self.message = error_msg
