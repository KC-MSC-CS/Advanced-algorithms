# KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0]*M
    j = 0
    LPSArray(pat, M, lps)
    i = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1  
        if j == M:
            print ("Found pattern at index " + str(i-j))
            j = lps[j-1]
            p=1
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
            p=0
    if p==0 :
        print("Pattern not found")
        
#FUNCTION FOR MARKING LPS.                
def LPSArray(pat, M, lps):
    len = 0 
    lps[0]
    i = 1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1

txt =  input("Enter TEXT:\n")
pat = input("Enter PATTERN:\n")
KMPSearch(pat, txt)