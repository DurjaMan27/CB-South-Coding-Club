
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
list = [3, 6, 7, 6, 7, 10, 12, 13, 11, 12]
str_list = ["Kevin", "Coding", "Club", "CB South", "Python"]
list2 = [1, 2, 3, 4]

def second_largest(list):
    list.remove(max(list))
    return max(list)

print(second_largest(list))

#max()
#min()

str_list.sort()
print(str_list)
str_list.remove("Club")
print(str_list)

#append() #adds element to end of list
#clear() #removes all elements from list
#copy() #returns a copy of list
#count() #returns number of elements with value
#extend() #for combining elements in two lists
#index() #returns index of first element with value
#insert() #inserts element at index position
#pop() #removes the element index position
#remove() #removes first item with value
#sort() sorts list
#reverse()

#in, not in

"""def my_max(list):
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

print(my_min(list))"""

x = input("What's your name?")
print(x)



