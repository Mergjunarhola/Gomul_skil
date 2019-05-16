from math import *
class Vigur:
    # ég oneline-aði allt bara mér til gamans
    # Smiður frumstillir x og y hnit vigurs eftir parametrum
    def __init__(self, x, y):
        self._X,self._Y=x,y

    # Þinn kóði hér

    # Fall sem skrifar hnit vigurs á skjá
    def prenta(self):
        print("["+" ".join(map(str,[self._X,self._Y]))+"]")
    # Þinn kóði hér

    # Fall sem skilar lengd
    def lengd(self):
        return float(format((self._X*self._X+self._Y*self._Y)**0.5,".2f"))
    # Þinn kóði hér

    # Fall sem skilar hallatölu
    def halli(self):
        return self._Y/self._X
    # Þinn kóði hér

    # Fall sem skilar þvervigri
    def þvervigur(self):
        return Vigur(-self._Y,self._X)
    # Þinn kóði hér

    # Fall sem skilar stefnuhorni
    def stefnuhorn(self):
        return format((((atan2(self._Y,self._X))/pi)*180)%360,".1f")
    # Þinn kóði hér

    # Fall sem tekur vigur sem parameter og skilar horni milli vigra
    def horn(self, v):
        return abs(float(self.stefnuhorn())-float(v.stefnuhorn()))
        #return (v.stefnuhorn()-self.stefnuhorn())%360
    # Þinn kóði hér

    # Fall sem tekur vigur sem parameter og skilar summu vigri
    def summa(self, v):
        return Vigur(self._X+v._X,self._Y+v._Y)

# Keyrsluforrit
v1 = Vigur(1, 3)
v1.prenta()
print("Lengd: ", v1.lengd())
print("Halli: ", v1.halli())
vþ = v1.þvervigur()
print("Þvervigur: ", end=" ")
vþ.prenta()
print("Stefnuhorn: ", v1.stefnuhorn())
v2 = Vigur(-3, 1)
print("Horn milli vigra: ", v2.horn(v1))
v3 = v1.summa(v2)
print("Summa: ", end=" ")
v3.prenta()
