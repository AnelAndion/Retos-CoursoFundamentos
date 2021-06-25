#Reto4
def DescontarMedicamento(m,s,ts,d):
    if s == 1 and ts == 1:
        m[0][0] = int(m[0][0]) - d
        return m
    else:
        s -= 1
        ts -= 1
        m[s][ts] = int(m[s][ts]) - d
        return m

def proceso(m,s,ts,d):
    if s == 1 and ts == 1:
        m[0][0].append(d) 
        return m
    else:
        s -= 1
        ts -= 1
        m[s][ts].append(d)
        return m

def conteo(m,s,pacientesAtender):
    if s == 1 and pacientesAtender == 1:
        m[0][0] = 1
        return m
    else:
        s = s - 1
        pacientesAtender = pacientesAtender - 1
        m[s][pacientesAtender] = 1
        return m

while True:
    Entrada1 = input().split(" ")# -cantidad de sucursale n | k tipos de medicamentos | m cantidad pacientes atender
    # verificar los datos en el arreglo
    if int(Entrada1[0]) < 1 or int(Entrada1[1]) < 1:
        continue # repite ciclo
    break #todo bien, terminda

Entrada2 = [] # matriz sucursal por tipo de medicamento
for i in range(int(Entrada1[0])):
    medicamentos = input().split(" ") # leer medicamento segun la sucursal
    Entrada2.append(medicamentos)
print(Entrada2) # para prueba

# crear matriz de tres dimensiones
V3 = []
for i in range(int(Entrada1[0])):
    V1 = []
    for j in range(int(Entrada1[1])):
        V1.append([0])
    V3.append(V1)

# crear matriz para el conteo
matrizConteo = []
for i in range(int(Entrada1[0])):
    listaConteo = []
    for j in range(int(Entrada1[2])):
        listaConteo.append(0)
    matrizConteo.append(listaConteo) 

for m in range(int(Entrada1[2])):
    #informacion de los pacientes
    informacionPacientes = input().split(" ") # leer #sucursal | tipo medicamento | #existencias | info | nivel glucosa

    if int(informacionPacientes[0]) > int(Entrada1[0]) or int(informacionPacientes[1]) > int(Entrada1[1]):
        continue

    if int(informacionPacientes[2]) < 0 : continue # las existencia no pueden ser cero

    if informacionPacientes[3].lower() == "ayunas":
        if float(informacionPacientes[4]) < 4.4:
            Entrada2 = DescontarMedicamento(Entrada2,int(informacionPacientes[0]),int(informacionPacientes[1]),int(informacionPacientes[2]))
            V3 = proceso(V3,int(informacionPacientes[0]),int(informacionPacientes[1]),int(informacionPacientes[2]))
        elif 7 > float(informacionPacientes[4]) >= 6.1:
            Entrada2 = DescontarMedicamento(Entrada2,int(informacionPacientes[0]),int(informacionPacientes[1]),int(informacionPacientes[2]))
            V3 = proceso(V3,int(informacionPacientes[0]),int(informacionPacientes[1]),int(informacionPacientes[2]))
        elif float(informacionPacientes[4]) >= 7:
            Entrada2 = DescontarMedicamento(Entrada2,int(informacionPacientes[0]),int(informacionPacientes[1]),int(informacionPacientes[2]))
            V3 = proceso(V3,int(informacionPacientes[0]),int(informacionPacientes[1]),int(informacionPacientes[2]))
    elif informacionPacientes[3].lower() == "posprandial":
        if 11 > float(informacionPacientes[4]) >= 7.8:
            Entrada2 = DescontarMedicamento(Entrada2,int(informacionPacientes[0]),int(informacionPacientes[1]),int(informacionPacientes[2]))
            V3 = proceso(V3,int(informacionPacientes[0]),int(informacionPacientes[1]),int(informacionPacientes[2]))
        elif float(informacionPacientes[4]) >= 11:
            Entrada2 = DescontarMedicamento(Entrada2,int(informacionPacientes[0]),int(informacionPacientes[1]),int(informacionPacientes[2]))
            V3 = proceso(V3,int(informacionPacientes[0]),int(informacionPacientes[1]),int(informacionPacientes[2]))

    matrizConteo = conteo(matrizConteo,int(informacionPacientes[0]),m)
    

for i in range(int(Entrada1[0])):
    print(f"{i + 1}") # numero de la sucursal
    
    menor = 1000
    mayor = 0
    pos = 0
    suma = 0

    for j in range(len(Entrada2[i])):
        if int(Entrada2[i][j]) < menor:
            menor = int(Entrada2[i][j])
            if j == 0: pos = 1
            else: pos = j + 1
    print(f"{pos} {menor}")
    pos = 0
    for j in range(len(Entrada2[i])):
        if int(Entrada2[i][j]) > mayor:
            mayor = int(Entrada2[i][j])
            if j == 0: pos = 1
            else: pos = j + 1
    print(f"{pos} {mayor}")
    # juego ------------------------
    menor = 1000
    for j in range(int(Entrada1[1])):
        arreglo3 = V3[i][j]
        for z in range(len(arreglo3)):
            suma = suma + arreglo3[z]
            if arreglo3[z] < menor:
                menor = arreglo3[z]
    promedio = suma / int(Entrada1[1])
   
    mayor = 0
    for j in range(int(Entrada1[1])):
        arreglo3 = V3[i][j]
        for z in range(len(arreglo3)):
            if arreglo3[z] > mayor:
                mayor = arreglo3[z]
    print("{:.2f} {:.2f} {:.2f}".format(menor,promedio,mayor))

    # contar 
    iterador = 0
    for j in range(len(matrizConteo[i])):
        if matrizConteo[i][j] == 1:
            iterador = iterador + 1

    if iterador == 0:
        print("0.00")
    else:
        promedio2 = suma / iterador
        print("{:.2f}".format(promedio2))

menor = 1000
pos1 = 0
for i in range(int(Entrada1[0])):
    lista3 = V3[i][0]
    if len(lista3) > 1:
        lista3.remove(0)
    
    if min(lista3) < menor:
        menor = min(lista3)
        pos1 = i + 1
    
mayor = 0
pos2 = 0
for i in range(int(Entrada1[0])):
    lista4 = V3[i][0]
    if max(lista4) > mayor:
        mayor = max(lista4)
        pos2 = i + 1

print(f"{pos1} {menor}")
print(f"{pos2} {mayor}")
 



"""
print(Entrada2)
print(V3)
print(matrizConteo)
"""
        


