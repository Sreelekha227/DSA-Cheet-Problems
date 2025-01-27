class CountDigits :
    def DigitCount(self,n) :

        if n == 0:
            return 1
        
        count = 0
        while n!= 0:
            n = n//10
            count +=1

        return count
        
obj = CountDigits()
n = 333
print("The number of digits are",obj.DigitCount(n))

    