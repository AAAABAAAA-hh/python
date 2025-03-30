
def insert_sort(lst:list) -> list:
    for i in range(1, len(lst)):
        cur_val = lst[i]
        cur_pos = i
        while cur_pos > 0 and lst[cur_pos - 1] < cur_val:
            lst[cur_pos] = lst[cur_pos - 1]
            cur_pos -= 1

        lst[cur_pos] = cur_val

    return lst



























