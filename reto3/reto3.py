n=int(input())
m=int(input())
med1=int(input())

for i in range (n):
    if n>1:		
	estado=input()
	nivelGlucosa=float(input())
	
    estado = input('ayunas')
    nivelGlucosa = float(input())

    if estado == "ayunas":
        
        
        if nivelGlucosa < 4.4:
            
            med2 = med2 - 1
            pacMed2 += 1 


        elif 7 > nivelGlucosa >= 6.1:
            
            med1 = med1 - 4
            pacMed1 += 1

        elif nivelGlucosa >= 7:
No me deja escribir más
Espere
med1 = med1 - 10
            pacMed1 += 1


    elif estado == "posprandial":
        

        if 11 > nivelGlucosa >= 7.8: 

            med1 = med1 - 7
            pacMed1 += 1


        elif nivelGlucosa >= 11: 
            
            med1 = med1 - 13
            pacMed1 += 1

    pacAten += 1

