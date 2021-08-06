def count_1(k):
    count = 0
    bin_k = list(bin(k)[2:])
    for e in bin_k:
        if e == '1':
            count += 1
    return count

if __name__ == '__main__':
    k = int(input("Input integer k : "))
    print(count_1(k))
