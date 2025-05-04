#!/usr/bin/env python3

import subprocess


def elimnar_2_primeros_items():
    for i in range(0,2):
        listar.pop(0)


#variables necesarias
resultado = subprocess.run(["ls" , "/bin/"], capture_output=True, text=True)
listar = list(resultado.stdout.split())
lista2 = []



elimnar_2_primeros_items()

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
                





        
            

"""
for i in lista2:
    print("-"*20)
    print(f"COMANDOS CON {i["id"].upper()}")
    for e in i["arreglo"]:
        print(f"*.{e}")"""
        




            
    

                
            

        

