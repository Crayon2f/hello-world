# coding=utf-8
class SQLOperator:
    """定义sql 操作符"""
    percent = "%"
    not_equal = " <> "
    equal = " = "
    lesser = " < "
    lesser_equal = " <= "
    greater = " > "
    greater_equal = " >= "

    def __init__(self):
        self.equal = '='
