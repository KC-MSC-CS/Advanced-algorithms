def naive(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        if text[ i : i + m ] == pattern:
            print("Pattern found at index:", i)

text=input("enter text")
pattern=input("enter pattern")
naive(text,pattern)