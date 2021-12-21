def navigation(filename, position=0, depth=0, aimed=False, aim=0):
    with open(filename) as f:
        arr = f.readlines()
    for el in arr:
        el = el.strip().split()
        el[1] = int(el[1])
        if el[0] == 'forward': 
            position += el[1]
            if aimed: 
                depth += aim * el[1]
        
        if el[0] == 'up':
            if aimed: aim-=el[1] 
            else: depth -= el[1]
        if el[0] == 'down':
            if aimed: aim+=el[1] 
            else: depth += el[1]
            


    print(f"position:{position}, depth:{depth}")
    print(position*depth)
        
        
        

navigation('day2.txt');
navigation('day2.txt', aimed=True);
