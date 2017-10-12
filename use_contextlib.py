from contextlib import contextmanager

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")


from urllib.request import urlopen

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
