
"""x = 0
str = "string"

for num in str:
    print(num)

for i in range(1, 101):
    x = x + i

x = 1
y = 5


while x != y:
    print(x)
    x += 1

print("exited")
"""
list = [3, 6, 7, 6, 7, 10, 12]

def my_max(list):
    temp_max = list[0]
    for num in list:
        if num > temp_max:
            temp_max = num

    return temp_max

def my_min(list):
    temp_max = list[0]
    for num in list:
        if num < temp_max:
            temp_max = num

    return temp_max

print(my_min(list))






