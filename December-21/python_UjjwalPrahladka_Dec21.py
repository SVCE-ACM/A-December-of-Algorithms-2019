def marching_partners(n = 0, H = [], d = 0):
    H.sort()
    count = 0
    while len(H) != 1:#checking if list is empty
        if H[1] - H[0] <= d:
            count += 1
            H = H[2:]
        else:
            H.pop(0)
    return count    