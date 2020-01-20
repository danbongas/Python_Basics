print("Check If String is Palindrome : \n") 

def reverse(str1):
    return str1[::-1]

def isPalindrome(str1):
    rev = reverse(str1)

    if(str1 == rev):
       return True
    return False

str1 = input("Input String:")
ans = isPalindrome(str1)

if ans == 1:
    print("Yes")
else:
   print("No")       
    
           