class CountDigits :
    def EvenlyDividesDigits(self,n) :

        string = str(n)
        count = 0

        for digit in string:
            d = int(digit)
            if d != 0 and n%d == 0:
                count += 1
        return count
    
obj = CountDigits()
n = 12
print("Number of digits that evenly divides the number is",obj.EvenlyDividesDigits(n))
