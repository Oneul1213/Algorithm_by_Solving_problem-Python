def right_rotate_k(arr, s, t, k):
    copy_arr = arr[s:t+1]
    for i, e in enumerate(copy_arr):
        idx = s+i+k
        if idx <= t:
            arr[idx] = e
        else:
            arr[idx%len(copy_arr)] = e

arr = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
print(arr)
right_rotate_k(arr, 0, 7, 2)
print(arr)
