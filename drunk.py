x = int(input())

def suds(x):
   
    #x = abs(x)
    while x > 0:
        print('%d bottles of beer' % x)
        x = x - 1
    if x == 0:
            pass
    return
suds(x)
    