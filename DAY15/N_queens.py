from typing import List

def solveNQueens(n, rook=None):
    a=[]
    row=[]
    col=[]
    pd=[]
    nd=[]
    b=[['.']*n for i in range(n)]
    
    if rook:
        rook_row, rook_col = rook
        b[rook_row][rook_col] = 'R'
        row.append(rook_row)
        col.append(rook_col)
    
    def bt(r):
        if r == n:
            l = ["".join(i) for i in b]
            a.append(l)
            return 
        for c in range(n):
            if r in row or c in col or (r+c) in pd or (r-c) in nd:
                continue
            b[r][c] = 'Q'
            row.append(r)
            col.append(c)
            pd.append(r + c)
            nd.append(r - c)
            bt(r + 1)
            b[r][c] = '.'
            row.remove(r)
            col.remove(c)
            pd.remove(r + c)
            nd.remove(r - c)
    
    bt(0)
    return a

# Example usage
n = 4
rook_position = (1, 1)  # Placing a rook at position (1, 1)
solutions = solveNQueens(n, rook=rook_position)
print(f"Solutions with a rook at {rook_position}:")
for i in solutions:
    for j in i:
        print(j)
    print()
