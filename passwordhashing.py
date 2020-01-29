pss=input("enter the password to hash:")
hsh=""
for i in pss:
    hsh=hsh+str(ord(i))
print(hsh)
