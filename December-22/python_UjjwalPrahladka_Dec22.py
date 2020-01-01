def alt_balls(N, arr):
    for i in range(N):
        count = 1
        if arr[i] == 'B':
            is_previous_blue = True
        else:
            is_previous_blue = False
        for j in range(i+1,N):
            if (arr[j] == 'R' and is_previous_blue) or (arr[j] == 'B' and not is_previous_blue):
                count += 1
                is_previous_blue = not is_previous_blue
            else:
                break
        print(count, end = ' ')
order = input('Enter space separated colors(B for blue and R for red: ').split()
alt_balls(len(order), order)