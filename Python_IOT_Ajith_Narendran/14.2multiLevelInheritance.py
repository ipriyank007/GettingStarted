class A:
    def myfunction(self):
        print('Im in class A')

class B(A):
    def myfunction(self):
        print('Im in class B')

class C(B):
    def myfunction(self):
        print('Im in class C')

obj = B()
obj.myfunction()