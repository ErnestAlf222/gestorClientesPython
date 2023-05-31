import re
import os
import platform

def limpiarPantalla():
    if platform.system() == 'Windows':
       os.system('cls')
    else:
        os.system('clear') 

def leerTexto(longitudMin=0,longitudMax=100,mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto= input('> ')
        if len(texto) >= longitudMin and len(texto)<=longitudMax:
            return texto

def dniValidate(dni, lista):
    if not re.match('[0-9]{2}[A-Z]$',dni):
        print('DNI Incorrecto debe cumplir el formato')
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print('DNI utilizado por otro cliente')
            return False
    return True