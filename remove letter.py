def delchar(s,c):
    
    if (len(c)==1):
        for i in range(len(s)):
            if (c is not s[i]):
                print(s[i])
            else:
                continue
s=input("Enter the string:")
c=input("Enter a charater to be deleted:")
delchar(s,c)
