def count_me(filename, window_size = 1):

    with open(filename) as f:
        arr = map(int, f.readlines())

    windows = []
    counter = 0
    for i in range(len(arr)):        
        windows.append(sum(arr[i:i+window_size]))
    for j in range(len(windows)-1):
        if windows[j] < windows[j+1]:
            counter += 1
        
    

    print(counter)

count_me('day1.txt')
count_me('day1b.txt', 3)
    

