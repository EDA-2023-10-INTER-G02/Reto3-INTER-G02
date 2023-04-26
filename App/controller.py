"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TO DO: Llamar la función del modelo que crea las estructuras de datos
    control = model.new_data_structs()
    return control


# Funciones para la carga de datos

def load_data(control, filename):
    """
    Carga los datos del reto
    """
    filename = cf.data_dir + filename
    input_file = csv.DictReader(open(filename, encoding="utf-8"),delimiter=",")
    time_i = get_time()
    for accidente in input_file:
        model.add_data(control, accidente)
    time_f = get_time()
    total_time = delta_time(time_i,time_f)
    return control
    # TO DO: Realizar la carga de datos


# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass

def get_size(control):
    return model.data_size(control)


def req_1(control, fecha_inicio, fecha_fin):
    """
    Retorna el resultado del requerimiento 1
    """
    # TO DO: Modificar el requerimiento 1
    time_i = get_time()
    #tracemalloc.start()
    #mem_i = get_memory()
    rta = model.req_1(control,fecha_inicio,fecha_fin)
    #mem_f = get_memory()
    #tracemalloc.stop()
    time_f = get_time()
    total_time = delta_time(time_i,time_f)
    #total_mem = delta_memory(mem_f,mem_i)
    return rta,total_time


def req_2(control,clase,via):
    """
    Retorna el resultado del requerimiento 2
    """
    # TO DO: Modificar el requerimiento 2
    time_i = get_time()
    #tracemalloc.start()
    #memory_i = get_memory()
    rta = model.req_2(control,clase,via)
    #memory_f = get_memory()
    #tracemalloc.stop()
    time_f = get_time()
    total_time = delta_time(time_i,time_f)
    #final_mem = delta_memory(memory_f,memory_i)
    return rta,total_time


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control, gravedad, fecha_in, fecha_fi):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    return model.req_4(control, gravedad, fecha_in, fecha_fi)


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control,mes,año,latitud,longitud,radio,cantidad):
    """
    Retorna el resultado del requerimiento 6
    """
    # TO DO: Modificar el requerimiento 6
    time_i = get_time()
    #tracemalloc.start()
    #memory_i = get_memory()
    rta = model.req_6(control,mes,año,latitud,longitud,radio,cantidad)
    #memory_f = get_memory()
    #tracemalloc.stop()
    time_f = get_time()
    time = delta_time(time_i,time_f)
    #final_mem = delta_memory(memory_f,memory_i)
    return rta,time
    


def req_7(control,mes,ano):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    return model.req_7(control,mes,ano)


def req_8(control,clase,fecha_in,fecha_fi):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    return model.req_8(control,clase,fecha_in,fecha_fi)


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
