#Declarar

Cateto1 : int = 0
Cateto2 : int = 0
Hipotenusa : int = 0
import math

#Inicio

Cateto1 = int (input("Digite o valor do 1° cateto: "))
Cateto2 = int (input("Digite o valor do 2° cateto: "))
Hipotenusa = math.sqrt (Cateto1 * Cateto1 + Cateto2 * Cateto2)
print ("O valor da Hipotenusa é: ",Hipotenusa)

#Fim