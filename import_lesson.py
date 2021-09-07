class Bad_name(Exception):
    pass


def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise Bad_name (name + 'bad  name')
