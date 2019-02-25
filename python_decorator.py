import datetime
import logging
from functools import wraps


def logger(subfunc):
    FORMAT = '%(levelname)s %(asctime)-15s %(message)s'
    logging.basicConfig(format=FORMAT, filename='{}.log'.format(
        subfunc.__name__), level=logging.INFO)

    @wraps(subfunc)
    def wrapper_function(*args, **kwargs):
        logging.info('[{}] starts'.format(subfunc.__name__))
        result = subfunc(*args, **kwargs)
        logging.info('[{}] ends'.format(subfunc.__name__))
        return result
    return wrapper_function


def timer(subfunc):
    @wraps(subfunc)
    def wrapper_function(*args, **kwargs):
        tnow = datetime.datetime.now()
        result = subfunc(*args, **kwargs)
        logging.info('[{}] elapsed {:,.0f} milliseconds'.format(subfunc.__name__,
                                                                (datetime.datetime.now() - tnow).total_seconds() * 1000))
        return result
    return wrapper_function


@timer
@logger
def printDaysToBday():
    tday = datetime.date.today()
    bday = datetime.date(tday.year, 10, 19)
    print('days till bday: {} days'.format(daysBetweenDays(tday, bday)))


@timer
@logger
def daysBetweenDays(d1, d2):
    return (d2 - d1).days


printDaysToBday()
