x = 'global x'


def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)
    inner()
    print(x)


outer()
print(x)
