import datetime


def defaulthandler(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
