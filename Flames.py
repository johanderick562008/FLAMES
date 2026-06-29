def flames(x,y):
    for i in x[:]:
        for j in y:
            if i==j:
                x.remove(i)
                y.remove(j)
                break
    z = len(x+y)

    a = ['Friend', 'Love', 'Affection', 'Marriage', 'Enemy', 'Sister']
    i = 6
    while i>1:
        j = z
        while j-i>0:
            j-=i
        a = a[j:]+a[:j]
        a.pop()
        i-=1
    
    return ('The relationship is {}'.format(a[0]))

x = list(input("Enter name 1: ").lower().replace(' ',''))
y = list(input("Enter name 2: ").lower().replace(' ',''))
print(flames(x,y))
        


 

