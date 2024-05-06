import math


x = int(input("zadejte prvné číslo: "))
y = input("zadejte znak: ")
z = int(input("zadejte druhé číslo: "))

def kalkulacka():
    if "x" in y:
        print(x * z)
    else:
        if "/" in y:
            print(x / z)
            next
        else:
            if "+" in y:
                print(x + z)
                next
            else:
                if "-" in y:
                    print(x - z)
                    next
                else:
                    if "**" in y:
                        print(x ** z)
                        next
kalkulacka()
