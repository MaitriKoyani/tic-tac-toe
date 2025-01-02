print('Game Start!')
l1=[[1,2,3],[4,5,6],[7,8,9]]
dict={}
n=1
fact=False

def printmatrix():
    for i in range(3):
        for j in range(3):
            if j==2:
                print('',l1[i][j],end='')
            else:
                print('',l1[i][j],'|',end='')
        if i==2:
            print('\n')
        else:
            print('\n--- --- ---')
def checkwin(k):
    global fact
    if (l1[0][0]==l1[1][0]==l1[2][0] and l1[0][0]!='') or (l1[0][0]==l1[0][1]==l1[0][2] and l1[0][0]!='') or (l1[0][0]==l1[1][1]==l1[2][2] and l1[0][0]!='') or (l1[0][2]==l1[1][1]==l1[2][0] and l1[2][0]!='') or (l1[0][1]==l1[1][1]==l1[2][1] and l1[0][1]!='') or (l1[0][2]==l1[1][2]==l1[2][2] and l1[0][2]!='') or (l1[1][0]==l1[1][1]==l1[1][2] and l1[1][0]!='') or (l1[2][0]==l1[2][1]==l1[2][2] and l1[2][0]!=''):
        fact=True
        print(k,"win")
        
l2=[]
ch=int(input("Enter first X or O \nfor X enter 1\nfor O enter 2\n :"))
if ch==1:
    h='X'
    l='O'
else:
    h='O'
    l='X'
printmatrix()
for i in range(9):
    n=1
    if i%2==0:
        k=h
    else:
        k=l
    print(k,"It's your turn\t",end='')
    m=int(input('which position:'))
    while m in l2:
        m=int(input('Please! enter right position:'))
    l2.append(m)
    
    for i in range(3):
        for j in range(3):
            
            if n==m:
                print('enter')
                l1[i][j]=k
            n+=1
            
    printmatrix()
    checkwin(k)
    if fact:
        break
print('Game End!')