def outer():
    def inner():
        def innerinner():
            print("Hello World")
        return innerinner
    return inner

func01 = outer()
func02 = func01
func02()
outer()()()

def organize(*funcs):
    for func in funcs:
        func()

def add():
    print(20 +10)

def minus():
    print(20 -10)

def multiply():
    print(20 *10)

organize(add, minus, multiply)



