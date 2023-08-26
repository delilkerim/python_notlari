""" 
SUAL-1
Dairenin alanı : πr2
Dairenin çevresi: 2πr

Yarıçapı verilen bir dairenin alanını ve çevresini hesaplayınız. (π=3.14 alınacaktır.)
"""
# CEVAP-1
pi = 3.14
radius = int(input("Lütfen yarıçap değeri giriniz:"))
circleArea = pi * radius * radius
print("Dairenin alanı: " + str(circleArea))

circleCircumference = 2 * pi * radius
print("Dairenin çevresi:" + str(circleCircumference))
# print("Dairenin çevresi:" + str(circleCircumference)) yerine
print("Dairenin çevresi:",circleCircumference)


