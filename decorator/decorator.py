import functools

def log(func):
    @functools.wraps(func)#wrapper.__name__ = func.__name__
    def wrapper(*args, **kw):
        print('begin','call %s():' % func.__name__)
        result=func(*args, **kw)
        print('end','call %s():' % func.__name__)
        return result
    return wrapper

@log
def now():
    print('2015-3-25')

now()

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2015-3-25')

today()
print(today.__name__)

print('========================================')

def adcanceLog(*args):
    text = args[0] if isinstance(args[0],str) else 'log'
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s before %s():' % (text, func.__name__))
            result = func(*args, **kw)
            print('%s after %s():' % (text, func.__name__))
            return result
        return wrapper
    return decorator if isinstance(args[0],str) else decorator(args[0])

@adcanceLog
def now():
    print('2015-3-25')

now()

print('========================================')

@adcanceLog("execute")
def now():
    print('2015-3-25')

now()
