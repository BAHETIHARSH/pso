# Nqueen
def iscolsafe(r,c):
    while r>=0:
        if mat[r][c] == 1:
            return False
        r -= 1
    return True

def isrdigonalsafe(r,c):
    while r>=0 and c<n:
        if mat[r][c] == 1:
            return False
        r -= 1
        c += 1
    return True
    

def isldigoanlsafe(r,c):
    while r>=0 and c>=0:
        if mat[r][c] == 1:
            return False
        r -= 1
        c -= 1
    return True

def issafe(r,c):
    return iscolsafe(r,c) and isrdigonalsafe(r,c) and isldigoanlsafe(r,c)
def placeQueens(r,c):
    if r>=n:
        return
    else:
        p = 0
        while c<n:
            p = issafe(r,c)
            
            if p :
                mat[r][c] = 1 
                b.update({r:c})
                break
            c += 1
        if p == 1:
            placeQueens(r+1,0)
        else:
            mat[r-1][b.get(r-1)] = 0
            placeQueens(r-1,b.get(r-1)+1)




n = int(input("Enter the number of queens : "))
mat = [[0 for i in range(n)] for j in range(n)]
b = {}
placeQueens(0,3)
for i in mat:
    print(i)
