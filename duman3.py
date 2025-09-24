lst = [1, 2, 3, 4, 5]
print(lst[::-1])   # способ через срез
# или:
lst.reverse()
print(lst)
def list_sort(lst):
    return sorted(lst, key=abs, reverse=True)

print(list_sort([3, -10, 5, -2, 8]))
# Результат: [-10, 8, 5, 3, -2]
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

print(change([1, 2, 3, 4]))  
# Результат: [4, 2, 3, 1]
