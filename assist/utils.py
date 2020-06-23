from datetime import datetime
import time


def generat_sequence(list):
    """
      generate sequence number from against max number of the list
    """
    try:
        return max(list) + 1
    except:
        return 1


def to_int(num):
    """
      Convert string to int, if string is not a int , return -1
    """
    try:
        return int(num)
    except:
        return -1


def parse_arguments(args):
    return [i for i in args.split(' ') if len(i) > 0]


def date_stamp():
    ts = time.time()
    return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %A')

def time_stamp():
    ts = time.time()
    return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


def to_datetime(timestamp):
    return datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')


def duration(timestamp1, timestamp2):
    return to_datetime(timestamp2) - to_datetime(timestamp1)


if __name__ == '__main__':
    t1='2018-12-06 18:58:51'
    t2='2018-12-06 21:52:42'
    print("(" + str(duration(t1, t2)) + ")")
