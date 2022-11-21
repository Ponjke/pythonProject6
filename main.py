'''
list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
list_f = [9, 3, 4, 1, 8, 6, 5, 2, 0, 7]
'''

1)
list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
list_c = list_a + list_b
print(list_c)

2)
list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
list_c = list_a + list_b
list_c[::2] = list_a
list_c[1::2] = list_b
print(list_c)

3)
list_a = [1, 2, 3, 4, 5]
a = list_a.pop(0), list_a.pop(1), list_a.pop(2)
print(list_a)

list_b = [6, 7, 8, 9, 10]
a = list_b.pop(0), list_b.pop(1), list_b.pop(2)
print(list_b)

4)
list_c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_c.sort(reverse=True)
list_d = list_c
list_d = list_c[:]
list_c.reverse()
print('List_c: ' , list_c)
print('List_d: ' , list_d)

5)
list_c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_d = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
res = [x + y for x, y in zip(list_c, list_d)]
print(res)

6)
list_f = [9, 3, 4, 1, 8, 6, 5, 2, 0, 7]
list_f.sort(reverse=True)
list_f = list_c = list_d
list_f = list_c[:]
list_f = list_d[:]
print(list_c)
list_d.reverse()
print(list_d)

7)
list_c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_d = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
list_of_tuple = [(x, y) for x, y in zip(list_c, list_d)]
print(list_of_tuple)



'''
tuple_a = (1, 2, 3, 4, 5)
tuple_b = (4, 5, 6, 7, 8)
tuple_c = (4, 5, 6, 7, 8, 9, 10, 11)
'''

1)
tuple_a = (1, 2, 3, 4, 5)
tuple_b = (4, 5, 6, 7, 8)
tuple_c = (4, 5, 6, 7, 8, 9, 10, 11)
tuple_d = tuple_a + tuple_b + tuple_c
print(tuple_d)

2) tuple_d = (1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 9, 10, 11)
res = []
for item in tuple_d:
    count = tuple_d.count(item)
    if count < 2:
        continue
    res.append((item, count))
print(tuple(res))

3)tuple_d = (1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 9, 10, 11)
res = []
elements = []
for element in tuple_d:
    count = tuple_d.count(element)
    if count > 1 and element not in elements:
        elements.append(element)
        indexes = []
        for index, item in enumerate(tuple_d):
            if item == element:
                indexes.append(index)
        res.append((element, tuple(indexes)))
print(tuple(res))