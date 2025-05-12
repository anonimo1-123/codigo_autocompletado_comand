#!/usr/bin/env python3
import subprocess
import keyboard
import sys

#esta funcion


def detectar_input():
    contador = 0
    entrada = ""
    texto = "Ingrese el comando: "

    sys.stdout.write(texto) 
    sys.stdout.flush()
    while True:
        
        
        evento = keyboard.read_event()  

        if str(evento.name) == "esc":  
            break

        if evento.event_type == keyboard.KEY_UP:  
            entrada += str(evento.name)  
            contador += 1
            sys.stdout.write("\r" + texto + entrada)  
            sys.stdout.flush()
            mostrar_comandos(entrada, contador)
        
  
def mostrar_comandos(entrada,contador):
    indice = 0
    if  len(entrada) == 1:
        indice = next(i for i, dic in enumerate(lista2) if dic["id"] == entrada)
    cont = 1
    print("\n")
    for i in lista2[indice]["arreglo"]:
        if i[0:contador] == entrada:
        
            print(f"{cont}.{i}")
            cont += 1
         
    
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
del listar[:2]
lista2 = []


def main(): 
    ordenar_por_letra_arreglo()
    detectar_input()

if __name__ == "__main__":
    main()