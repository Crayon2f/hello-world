# import sched
import time
import datetime


#
# count = 0
#
#
# def run(msg, start_time):
#     global count
#     count += 1
#     if count < 4:
#         run(msg, start_time)
#     print 'msg:%s, start_time:%s' % (msg, start_time)
#
#
# schedule = sched.scheduler(time.time, time.sleep)
# schedule.enter(1, 1, run, ('hello', time.time()))
# schedule.run()
#
# time.sleep(4)

def run():
    print 'do something'
    time.sleep(10)


if __name__ == '__main__':
    while True:
        while True:
            now = datetime.datetime.now()
            if now.minute == 6:
                run()
            else:
                time.sleep(5)
                print 'incompatible'
                break
