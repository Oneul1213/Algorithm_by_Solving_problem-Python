def all_is(arr, len, k):
    return_val = 1
    for e in arr:
        if e != k:
            return_val = 0
            break
    return return_val

if __name__ == '__main__':
    print(all_is([3, 3, 3, 3], 4, 3))
    print(all_is([3, 3, 1, 3], 4, 3))
