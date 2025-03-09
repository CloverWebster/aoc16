with open('1.txt') as j:
    data = [i for i in j.read().strip().split(", ")]

direc = ['N','E','S','W','N']
pt2,chc = False,0
visited =[[0,0]]

def movement(num,dire):
    global totalx, totaly, curd
    if dire == 'R':
        for i in range(0,5):
            if direc[i] == curd:
                curd = direc[i+1]
                break
    else:
        for i in range(4,-1,-1):
            if direc[i] == curd:
                curd = direc[i-1]
                break
    if curd == 'N':
        totaly += num
    elif curd == 'E':
        totalx += num
    elif curd == 'S':
        totaly = totaly - num
    else:
        totalx = totalx - num


def check():
    global chc
    if chc%2 == 0:
        c1,c2 = 0,1
    else:
        c1,c2 = 1,0
    x = visited[len(visited)-1][c1]
    for i in range(c1,len(visited)-3,2):
        curr,curr1 = visited[i], visited[i+1]
        pen, fin = visited[len(visited)-2] , visited[len(visited)-1]
        y = curr[c2]
        if (x <= curr[c1] and x >= curr1[c1]) or (x >= curr[c1] and x <= curr1[c1]):
            if (y <= pen[c2] and y >= fin[c2]) or (y >= pen[c2] and y <= fin[c2]):
                return abs(x)+abs(y)
    chc += 1
    return False


totalx, totaly, curd = 0,0,'N'
for x in data:
    movement(int(x[1:]), x[0])
    if pt2 == False:
        cur = [totalx, totaly]
        visited.append(cur)
        if len(visited) >= 5:
            pt2 = check()
print('part 1:',abs(totalx)+abs(totaly))
print('part 2:',pt2)