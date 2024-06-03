def med(str1,str2):
    m, n  = len(str1), len(str2)
    matrix = [[0]*(n+1) for i in range(m+1)]
    ptr = [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        matrix[i][0] = i
        ptr[i][0] = 2
        
    for j in range(n+1):
        matrix[0][j] = j
        ptr[0][j] = 1
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1] == str2[j-1]:
                cost3 = matrix[i-1][j-1]
            else:
                cost3 = matrix[i-1][j-1]+2
            
            cost1 = matrix[i][j-1] + 1 
            cost2 = matrix[i-1][j] + 1
            matrix[i][j] = min(cost1,cost2,cost3)
            # 1 == left, 2 == down, 3 == diag
            if matrix[i][j] == cost3:
                ptr[i][j] = 3
            elif matrix[i][j] == cost1:
                ptr[i][j] = 1
            else:
                ptr[i][j] = 2
    ptr[0][0] = 0
    path = []
    i,j = m,n
    while i> 0 or j>0:
        if ptr[i][j] == 1:
            path.insert(0,f"insert {str2[j-1]}")
            j = j-1
        elif ptr[i][j] == 2:
            path.insert(0,f"del {str1[i-1]}")
            i = i-1
        
        elif ptr[i][j] == 3:
            path.insert(0,f"subs {str1[i-1]}-{str2[j-1]}")
            i = i-1
            j = j-1
            
    
    return matrix[m][n],path

#ex3
result , path= med("goal","pol")
print("ex3:")
print("distance: ",result)
print("operations: ",path)

#ex4
result , path= med("leda","deal")
print(" ")
print("ex4:")
print("distance: ",result)
print("operations: ",path)

#ex5: drive is closer to divers
result , path= med("drive","brief")
print(" ")
print("ex5:")
print("drive - brief")
print("distance: ",result)
print("operations: ",path)
print("drive - divers")
result , path= med("drive","divers")
print("distance: ",result)
print("operations: ",path)