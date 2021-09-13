def lcs(s1,s2):
    m = len(s1)
    n = len(s2)
    L = [[0 for i in range(n + 1)] for j in range(m + 1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])  
                
    for i in L:
        print(i)

    index = L[m][n]
    lcs_arr = [""] * (index+1)
    lcs_arr[index] = ""
    i = m
    j = n

    while i > 0 and j > 0: 
        if s1[i-1] == s2[j-1]:
            lcs_arr[index-1] = s1[i-1]
            i -= 1 
            j -= 1 
            index -=1 
        elif L[i-1][j] > L[i][j-1]:
            i -= 1 
        else: 
            j -= 1 

    # Printing the sub sequences
    print("S1 : " + s1 + "\nS2 : " + s2)
    print("LCS: " + "".join(lcs_arr))

if __name__ == '__main__':
    s1 = "ACADB"
    s2 = "CBDA"
    lcs(s1,s2)