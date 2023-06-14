def binary_search(tg, lst: list) -> int:
    index = int(len(lst) / 2)
    first = 0
    last = len(lst)
    for i in range(len(lst)):
        if lst[index] == tg:
            return index
        elif tg < lst[index]:
            last = index
        else:
            first = index
        index = int((first+last) / 2)
    return 'Не найдено'


print(binary_search(6, [6, 7, 8, 15, 17]))
