# ====================== Computadora ==================================

import time

class Computer:
    def __init__(self):
        self.instrucciones_segundo = 1
        self.tiempo_acceso_disco = 5
        self.tamano_pagina = 4*1024
        self.capacidad_disco = float('inf')
        self.ram = bytearray(400*1024)  # Memoria RAM (es un array de bytes)
        self.disco_duro = {}  # El disco duo es un diccionario de bytes

    ############################ MEMORIA RAM ##############################

    # Leer un byte de memoria en la dirección especificada
    def leer_memoria(self, direccion):
        return self.ram[direccion]

    # Escribe un byte en memoria en la dirección especificada
    def escribir_memoria(self, direccion, valor):
        self.ram[direccion] = valor

    ############################ DISCO DURO ###############################

    # Lee un byte del disco en la dirección especificada
    def leer_disco_duro(self, direccion):
        time.sleep(self.tiempo_acceso_disco)
        return self.disco_duro.get(direccion, 0)

    # Escribe un byte en el disco en la dirección especificada
    def escribir_en_disco_duro(self, direccion, valor):
        time.sleep(self.tiempo_acceso_disco)
        self.disco_duro[direccion] = valor


    ############################ CORRER PROGRAMA ###########################

    # Ejecuta un programa en la computadora
    def run_programa(self, programa):
        recorredor_programa = 0  # Contador de programa
        while recorredor_programa < len(programa):
            codigo_programa = programa[recorredor_programa]
            if codigo_programa == 0:  # NOP
                recorredor_programa += 1
            elif codigo_programa == 1:  # LOAD
                direccion = programa[recorredor_programa+1]
                valor = self.leer_memoria(direccion)
                self.escribir_memoria(0, valor) 