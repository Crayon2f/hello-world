from datetime import datetime

print type('ddd') is str
print type(34.4) is float
print type(34) is int
print type(3434444444444L) is long
print type(datetime.now()) is datetime
print type([]) is list
print type(()) is tuple
print type({}) is dict

print ','.join(str(i) for i in (1, 3, 4, 5, 6))
