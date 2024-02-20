#nonlocal keyword
def sample():
    name = "Anshumaan,"

    def sample2():
        nonlocal name
        print(name)
        name = "tested"
        print(name)

    sample2()
    print(name)

sample()

#raise keyword
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return x / y

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print("Exception occurred:", e)