from abc import ABC,abstractmethod
class araba (ABC):
    def yakitTuru(self):
        pass

class renault(araba):
    def yakitTuru(self):
        print("dizel")

class tesla(araba):
    def yakitTuru(self):
        print("elektrik")


class mercedes(araba):
    def yakitTuru(self):
        print("benzin")


r=renault()
r.yakitTuru()
t=tesla()
t.yakitTuru()
m=mercedes()
m.yakitTuru()
