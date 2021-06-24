# Reto 2 ---------------------------------------

medicamento1 = int(input())
medicamento2 = int(input())

pasientesAtendidos = 0
pasientesMedicamento1 = 0
pasientesMedicamento2 = 0
resul1 = 0
resul2 = 0
stop = True
sstop = False

while stop == True:
    
    if medicamento1 == 0 or medicamento2 == 0:
        sstop = True
        break


    caracter = input().lower()

    if caracter == "ayunas":

        nivelGlucosa = float(input())
        
        
        if nivelGlucosa < 4.4:
            
            if medicamento2 > 0:
               medicamento2 = medicamento2 - 1
               pasientesMedicamento2 += 1 
            else:
                stop = False

        elif 7 > nivelGlucosa >= 6.1:
            
            if medicamento1 >= 4:
                medicamento1 = medicamento1 - 4
                pasientesMedicamento1 += 1
            else:
                stop = False

        elif nivelGlucosa >= 7:
            
            if medicamento1 >= 10:
                medicamento1 = medicamento1 - 10
                pasientesMedicamento1 += 1
            else:
                stop = False

    elif caracter == "posprandial":
        
        nivelGlucosa = float(input())

        if 11 > nivelGlucosa >= 7.8: 

            if medicamento1 >= 7:
                medicamento1 = medicamento1 - 7
                pasientesMedicamento1 += 1
            else:
                stop = False

        elif nivelGlucosa >= 11: 
            
            if medicamento1 >= 13:
                medicamento1 = medicamento1 - 13
                pasientesMedicamento1 += 1
            else: 
                stop = False

    pasientesAtendidos += 1

if sstop == True:
    print(pasientesAtendidos)
    print(pasientesMedicamento1,"0.00%")
    print(pasientesMedicamento2,"0.00%")
else:
    resul1 = (pasientesMedicamento1 * 100) / pasientesAtendidos
    resul2 = (pasientesMedicamento2 * 100) / pasientesAtendidos

    print(pasientesAtendidos)
    print("{} {:.2f}%".format(pasientesMedicamento1,resul1))
    print("{} {:.2f}%".format(pasientesMedicamento2,resul2))