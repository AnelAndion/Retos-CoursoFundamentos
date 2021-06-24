# reto 1
x = input().lower()

if x == "ayunas":

    ng = float(input())

    if ng < 4.4:
        print("hipoglusemia")
    elif 6.1>ng>=4.4:
        print("sin diabetes")
    elif 7>ng>=6.1:
        print("pre diabetes")
    else:
        print("diabetes")

elif x == "posprandial":

    ng = float(input())
    
    if ng<7.8:
        print("sin diabetes")
    elif 11>ng>=7.8:
        print("pre diabetes")
    else:
        print("diabetes")

else:
    print("error en los datos")