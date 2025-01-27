class Reverse_a_number:
    def Reverse(self,n) :
       string = str(n)
       s = string[::-1]
       n = int(s)
       return n

obj = Reverse_a_number()
n = 123456789
print("Reversed number is",obj.Reverse(n)) 