def descontarMedicamento(i,Ev,n):

    if i == 1:
        Ev[0] = Ev[0] - n
    else:
        i = i - 1
        Ev[i] = Ev[i] - n
    
    return Ev

while True:
    """
      Para ello, el sistema debe recibir como entrada la cantidad de sucursales (n) para la
      entrega de medicamentos seguido de la cantidad total de pacientes a atender (m)
    """
    entrada1 = input().split(" ") # los datos estan en string y lo necesitamos en enteros

    """
    si la cantidad de sucursales es menor a 1 se debe leer nuevamente ambos valores hasta
    que se ingrese un n válido.
    """

    if int(entrada1[0]) < 1: # el int es para transformar los datos en entero
        continue # en este paso vuelve a pedir entrada1

    break # rompe siclo

"""
Luego, para las n sucursales (numeradas de 1 a n) se debe
leer la cantidad de existencias actuales del medicamento 
"""
iterador = 0
ExistenciasActualesDelMedicamento = [] #vercto guardar las existencias del medicamento en cada sucursal " las n sucursales (numeradas de 1 a n)"
ExistenciasActualesDelMedicamentoCopia = [] # lo necesitamos 
while True:
    if iterador < int(entrada1[0]): # verifica que estemos en la sucursal correcta 
        cantidadMedicamento = int(input()) # medicamento por sucursal

        """
        leer la cantidad de existencias actuales del medicamento y esta debe ser mayor o igual
        a 1, y en caso de que no se cumpla se debe leer valores hasta que se ingrese uno
        válido.
        """
        if cantidadMedicamento >= 1: # verifica que la cantidad del medicamento sea mayor igual 1 
            ExistenciasActualesDelMedicamento.append(cantidadMedicamento) # agrega el medicamento al stop correspondiente
            ExistenciasActualesDelMedicamentoCopia.append(cantidadMedicamento)
            iterador+=1 # cambiar posicion el vector -- ayuda a mover hacia el siguiente hasta se ingrese todos los medicamentos de las sucursales
        else:
            continue #envia a pedir medicamentos sin canviar de posicion 
    else:
        break

"""
Finalmente, para los m pacientes se debe leer el número de la sucursal donde
será atendido, seguido de una cadena de caracteres (“ayunas” o “posprandial”) que
determina si el paciente se encuentra o no en ayunas y de un número real que
representa el nivel de glucosa en sangre en mmol/l.
"""
#entrada 3
for i in range(int(entrada1[1])):

    mDato = input().lower().split(" ")

    if mDato[1] == "ayunas":

        if float(mDato[2]) < 4.4:
            ExistenciasActualesDelMedicamento = descontarMedicamento(int(mDato[0]),ExistenciasActualesDelMedicamento,1)
        elif 7 > float(mDato[2]) >= 6.1:
            ExistenciasActualesDelMedicamento = descontarMedicamento(int(mDato[0]),ExistenciasActualesDelMedicamento,4)
        elif float(mDato[2]) >= 7:
            ExistenciasActualesDelMedicamento = descontarMedicamento(int(mDato[0]),ExistenciasActualesDelMedicamento,10)

    elif mDato[1] == "posprandial":
        
        if 11 > float(mDato[2]) >= 7.8:
            ExistenciasActualesDelMedicamento = descontarMedicamento(int(mDato[0]),ExistenciasActualesDelMedicamento,7)
        elif float(mDato[2]) >= 11:
            ExistenciasActualesDelMedicamento = descontarMedicamento(int(mDato[0]),ExistenciasActualesDelMedicamento,13)

"""
El programa debe mostrar por pantalla el número de la sucursal con la menor cantidad
de existencias, luego de realizar la entrega de las mismas, seguido de la cantidad antes
mencionada.
"""
menor = 1000
posicionMenor = 0
for i in range(len(ExistenciasActualesDelMedicamento)):
    if ExistenciasActualesDelMedicamento[i] < menor:
        menor = ExistenciasActualesDelMedicamento[i]
        if i == 0:
            posicionMenor = 1
        else:
            posicionMenor = i + 1
print(f"{posicionMenor}  {menor}")

"""
Luego, en una nueva línea se debe mostrar el número de la sucursal con
la mayor cantidad de existencias, luego de realizar la entrega de las mismas, seguido
de la cantidad antes mencionada.
"""
mayor = 0
posicionMayor = 0
for i in range(len(ExistenciasActualesDelMedicamento)):
    if ExistenciasActualesDelMedicamento[i] > mayor:
        mayor = ExistenciasActualesDelMedicamento[i]
        if i == 0:
            posicionMayor = 1
        else:
            posicionMayor = i + 1
print(f"{posicionMayor}  {mayor}")

"""
para cada una de las sucursales (en
orden ascendente por número y en líneas distintas) se debe mostrar su número seguido
de la proporción porcentual de las existencias del medicamento programadas para
entrega respecto a la cantidad de existencias actuales del medicamento en la sucursal
correspondiente, formateado a 2 cifras decimales y separado por espacio.
"""
resultado = []
for i in range(len(ExistenciasActualesDelMedicamento)):
    MedicamentosEntregados = ExistenciasActualesDelMedicamentoCopia[i] - ExistenciasActualesDelMedicamento[i]
    res = (MedicamentosEntregados * 100)/ ExistenciasActualesDelMedicamentoCopia[i]
    resultado.append(res)

for i in range(len(resultado)):
    print(i+1," {:.2f}%".format(resultado[i]))
