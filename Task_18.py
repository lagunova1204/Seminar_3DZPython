# Задача 18: Требуется найти в массиве A[0..N-1] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6

# -> 5
num = int(input("Введите количество элементов списка: "))
my_list = [0]*num
for i in range (len(my_list)):
    my_list[i] = int(input(f"Введите {i} элемент списка: "))
what_num = int(input("\nВведите число для поиска ближайшего к нему: "))
i = 0
while what_num == my_list[i]:
    i += 1
seach_num = my_list[i]
for list in my_list:
    if list != what_num:
        if abs(list - what_num) < abs(seach_num - what_num):
            seach_num = list
print(f"Ближайшее число к чилу {what_num} это: {seach_num}.")
