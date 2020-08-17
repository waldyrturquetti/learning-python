import math

teta = float(input('digite o valor de Teta:'))


rad = math.radians(teta)  
print(teta)

#teta = math.radians(teta)  
#print(teta)

print('O valor de sen:{:.2f}, cos:{:.2f} e tan:{:.2f}'. format( math.sin(rad), math.cos(rad), math.tan(rad) ))