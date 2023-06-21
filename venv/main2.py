a = int(input("enter a:"))
b = int(input("enter b:"))

try:
    if b == 0:
        raise ZeroDivisionError
    else:
        print(a / b)
except ZeroDivisionError as e:
    print("ZDE error")

print('The end')
