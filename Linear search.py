pos = -1

list = [2,4,8,9,41]
n = 41

def search(list,n):
    for i in list:
        globals()['pos'] = i
        if i == n:
            return True


if search(list,n):
    print('found at',pos)
else:
    print('not found')


