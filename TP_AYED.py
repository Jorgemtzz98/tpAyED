import os
import getpass
ADMIN_USER = "admin@shopping.com"
ADMIN_PASS = "12345"
valido=False
intentos= 3
us = ""
cl = ""
contP=0
contC=0
contI=0
minR=""
mini=0
maxR=""
maxi=0
Indum="Indumentaria"
perf="Perfumeria"
com="Comida"

def opcionesm1():
    print(" -------------------------------------------")
    print (" | Menu de locales, ingrese una opcion:    |")
    print(" |a: Crear locales                         |")
    print(" |b: Modificar local                       |")
    print(" |c: Eliminar local                        |")
    print(" |d: Volver a menu anterior                |")
    print(" -------------------------------------------")

def menu1(): #menu de locales
    opcionesm1()
    opc1 =input()
    while opc1 != "d":
        if opc1 == "a" :
            carga() 
        elif opc1 == "b" :
            cartel() 
        elif opc1 == "c" :
            cartel() 
        else:
            print("Ingrese una opcion correcta")
        opcionesm1()
        opc1 =input()

def  modmax(x,nx):
    global maxR
    global maxi
    if x > maxi: 
        maxi=x
        maxR=nx

def modmin():
    global maxR
    global maxi
    global mini
    global minR
    if contI<contP:
        if contI<contC:
            mini=contI
            minR=Indum
        elif contI>contC:
            mini=contC
            minR=com
    elif contI>contP:
        if contP<contC:
            mini=contP
            minR=perf
        elif contP>contC:
            mini=contC
            minR=com
    if maxi>0:
        print("El rubro con menos locales es " ,minR, "con ", mini, "local/es")
        print("El rubro con mas locales es " ,maxR, "con ", maxi, "local/es")
    elif maxi==0:
        print("Aun no se han cargado datos.")

def carga():
    global maxR
    global maxi
    global contI
    global contP
    global contC
    global Indum
    global perf
    global com
    
    print("Ingrese el nombre del local - * para finalizar:")
    n = input()
    while n!= "*":
        print("Ingrese la ubicacion del local:")
        ubi = input()
        print("---------------------------------")
        print("|Ingrese el rubro del local:    |")
        print("|I para Indumentaria            |")
        print("|P para Permumeria              |")
        print("|C para Comida                  |")
        print("---------------------------------")
        r= input().upper()
        while r!="I" and r!="P" and r!="C":
            print("---------------------------------")
            print("|Ingrese una opcion valida      |")
            print("|Ingrese el rubro del local:    |")
            print("|I para Indumentaria            |")
            print("|P para Permumeria              |")
            print("|C para Comida                  |")
            print("---------------------------------")
            r= input().upper()
        if r=="I":
            contI +=1
            modmax(contI,Indum)
        elif r=="P":
            contP +=1
            modmax(contP,perf)
        elif r=="C":
            contC +=1
            modmax(contC,com)
        print("Local cargado con exito")
        print("Ingrese el nombre del local - * para finalizar:")
        n = input()
    modmin()


def  cartel():
    print("Esta funcionalidad esta en construccion")


def opcionesm4():
    print(" ----------------------------------------------")
    print ("|Menu de novedades, ingrese una opcion:      |")
    print(" |a: Crear novedades                          |")
    print(" |b: Modificar novedades                      |")
    print(" |c: Eliminar novedad                         |")
    print(" |d: Ver reporte de novedades                 |")
    print(" |e: Volver a menu anterior                   |")
    print(" ----------------------------------------------")

def menu4(): #menu gestion de novedades
    opcionesm4()
    opc4 =input()
    while opc4 != "e":
        os.system("cls")
        if opc4 == "a" :
            cartel() #crear novedades
        elif opc4 == "b" :
            cartel() #mod noved
        elif opc4 == "c" :
            cartel() #elim nove
        elif opc4 == "d" :
            cartel() #reporte novedades
        else:
            print("Ingrese una opcion correcta")
        opcionesm4()
        opc4 =input()

def opciones():
    print("Menu de Administrador:")
    print("-------------------------------------------------")
    print("""|   Ingrese una opcion:                         | """)
    print("""|   1. Gestión de locales                       |""")
    print("""|   2. Crear cuentas de dueños de locales       |""")
    print("""|   3. Aprobar / Denegar solicitud de descuento |""")
    print("""|   4. Gestión de Novedades                     |""")
    print("""|   5. Reporte de utilización de descuentos     |""")
    print("""|   0. Salir                                    |""")
    print("-------------------------------------------------")

def menu():
    opciones()
    opc =int(input())
    while opc != 0:
        os.system("cls")
        if opc == 1 :
            menu1()
        elif opc == 2 :
            cartel()
        elif opc == 3 :
            cartel()
        elif opc == 4 :
            menu4()
        elif opc == 5 :
            cartel()
        else:
            print("Ingrese una opcion correcta")
        opciones()
        opc =int(input())

def login():
    global valido, intentos
    while intentos >= 1 and not valido:
        intentos= intentos - 1
        print("Ingrese usuario:")
        us = input()
        print("Ingrese clave:") #OCULTAR CONTRASEÑA
        cl = getpass.getpass()
        os.system("cls")
        if us == ADMIN_USER and cl == ADMIN_PASS:
            valido = True
        else:
            if intentos>0:
                    print("Contraseña incorrecta le quedan ", intentos,"intentos")
            else:
                    print("Ya no le quedan intentos.")
# Programa principal 
login()
os.system("cls")
if valido:
        menu()