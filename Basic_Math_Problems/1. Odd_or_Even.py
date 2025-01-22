class odd_or_even:
    def isEven(self,n):
        return(n%2==0)
    
if __name__ == "__main__" :
    obj = odd_or_even()
    n = 28
    if obj.isEven(n):
        print("true")
    else:
        print("false")