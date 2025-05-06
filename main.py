#!/usr/bin/env python3

import subprocess
import keyboard

def elimnar_2_primeros_items():
    cont = 0
    while cont < 2:
        listar.pop(0)
        cont+=1


def detectar_input():
    contador =0
    entrada = ""
    print("Escribe algo sin presionar Enter:")
    while True:
        tecla = keyboard.read_event().name  # Captura la tecla presionada
        if tecla == "esc":  # Para terminar con la tecla ESC
            break
        if tecla == "space":
            tecla = " "
        entrada += tecla
        contador += 1
        mostrar_comandos(entrada,contador)

       
        


def mostrar_comandos(entrada,contador):
    indice = 0
    if  len(entrada) == 1:
        indice = next(i for i, dic in enumerate(lista2) if dic["id"] == entrada)

    for i in lista2[indice]["arreglo"]:
        if i[0:contador] == entrada:
            print(f"*.{i}")
        


    

    
def ordenar_por_letra_arreglo():
    for a in listar:
        inicial = a[0]
        if len(lista2) == 0:
            cont=[]
            cont.append(a)
            lista2.append({"id":inicial,"arreglo":cont})
            
        else:
            comprobante = False
            for i in range(0,len(lista2)):
                if  inicial == lista2[i]["id"]:
                    comprobante = True

            if comprobante == False:
                cont=[]
                lista2.append({"id":inicial,"arreglo":cont})
                cont.append(a)
            else:
                indice = next(i for i, dic in enumerate(lista2) if dic["id"] == inicial)
                lista2[indice]["arreglo"].append(a)
                    

#variables necesarias
resultado = subprocess.run(["ls" , "/bin/"], capture_output=True, text=True)
listar = list(resultado.stdout.split())
lista2 = []



elimnar_2_primeros_items()
ordenar_por_letra_arreglo()
detectar_input()








        
            

"""
for i in lista2:
    print("-"*20)
    print(f"COMANDOS CON {i["id"].upper()}")
    for e in i["arreglo"]:
        print(f"*.{e}")"""
        




            
    

                
            

        

