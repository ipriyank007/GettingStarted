class A:
    def dois(self, a):
        self.a = a
        print(a)
class B(A):
    def dothat(self,b):
        self.b = b
        print(b*2)
class C(B):
    def dothis(self, c):
        self.c = c
        print(c*3)
obj = C()
obj.dothis(4)
obj.dothat(4)
obj.dois(4)