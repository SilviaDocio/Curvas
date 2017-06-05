# Palindrome of string
str=raw_input("Enter the string\n")
ln=len(str)
for i in range(ln/2) :
    if(str[ln-i-1]!=str[i]):
        break
if(i==(ln/2)-1):
    print "Palindrome"
else:
    print "Not Palindrome"
