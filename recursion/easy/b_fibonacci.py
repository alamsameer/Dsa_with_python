class Fibonacci:
    def genFib(self,n:int)->int:
        if n==0 or n==1:
            return n
        return self.genFib(n-1)+self.genFib(n-2)
x=Fibonacci()
x.genFib(5)
print('x.genFib(5): ', x.genFib(5))
print('x.genFib(4): ', x.genFib(4))