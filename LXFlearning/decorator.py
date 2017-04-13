import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        runfunc=func(*args,**kw)
        return runfunc
    return wrapper

@log
def now():
    print('2016-12-28')


