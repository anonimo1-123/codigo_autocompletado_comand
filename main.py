#!/usr/bin/env python3
import subprocess
import keyboard
import sys
#hola espero que sea de tu agrado mi codigo

def  ejecutar_comando_shell():
    resultado = subprocess.run(["ls" , "/bin/"], capture_output=True, text=True)
    lista_principal = list(resultado.stdout.split())
    del lista_principal[:2]
    lista2 = []
    return lista_principal,lista2


def detectar_input(lista):
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
            mostrar_comandos(entrada, contador,lista)
        
  
def mostrar_comandos(entrada,contador,lista_de_comandos):
    indice = 0
    if  len(entrada) == 1:
        indice = next(i for i, dic in enumerate(lista_de_comandos) if dic["id"] == entrada)
    cont = 1
    print("\n")
    for i in lista_de_comandos[indice]["arreglo"]:
        if i[0:contador] == entrada:
        
            print(f"{cont}.{i}")
            cont += 1
         
    
def ordenar_por_letra_arreglo(list1,list2):
    for a in list1:
        inicial = a[0]
        if len(list2) == 0:
            cont=[]
            cont.append(a)
            list2.append({"id":inicial,"arreglo":cont})
            
        else:
            comprobante = False
            for i in range(0,len(list2)):
                if  inicial == list2[i]["id"]:
                    comprobante = True

            if comprobante == False:
                cont=[]
                list2.append({"id":inicial,"arreglo":cont})
                cont.append(a)
            else:
                indice = next(i for i, dic in enumerate(list2) if dic["id"] == inicial)
                list2[indice]["arreglo"].append(a)
                    


def main(): 
    lista1,lista2 = ejecutar_comando_shell()
    ordenar_por_letra_arreglo(lista1,lista2)
    detectar_input(lista2)

if __name__ == "__main__":
    main() 