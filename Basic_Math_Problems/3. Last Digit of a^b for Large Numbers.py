class FindLastDigit :
    def LastDigit(self,a,b):
        a = int(a)
        b = int(b)

        if a == 0 and b == 0 :
            return 1
        if b == 0 :
            return 1
        if a == 0 :
            return 0
        
        L = a % 10

        if b % 4 == 0 :
            res = 4
        else :
            res = b % 4

        N = pow(L,res)

        return N % 10
    
obj = FindLastDigit()
a = 2738
b = 276

print("The Last Digit is",obj.LastDigit(a,b))

