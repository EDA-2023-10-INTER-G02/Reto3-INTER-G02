﻿"""
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
import datetime
assert cf
import math

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data_structs = {"accidentes": None,
                    "dateIndex": None,
                    }
    
    data_structs["accidentes"] = lt.newList("ARRAY_LIST")
    data_structs["dateIndex"] = om.newMap(omaptype="RBT",
                                      comparefunction=compareDates)
    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    updateDateIndex(data_structs["dateIndex"], data)
    lt.addLast(data_structs["accidentes"],data)
    return data_structs

    #TODO: Crear la función para agregar elementos a una lista

def updateDateIndex(map, accidente):
    occuraccident = accidente["FECHA_OCURRENCIA_ACC"]
    accidentdate = datetime.datetime.strptime(occuraccident, "%Y/%m/%d")
    entry = om.get(map, accidentdate.date())
    if entry is None:
        datentry = newDataEntry(accidente)
        om.put(map, accidentdate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, accidente)
    return map

# Funciones para creacion de datos
def newDataEntry(accidente):
    entry = {"lstaccidentes":None,"clase":None, "gravedad":None}
    entry["lstaccidentes"] = lt.newList("ARRAY_LIST", compareDates)
    entry["clase"] = mp.newMap(maptype='PROBING')
    #entry["gravedad"] = mp.newMap()
    return entry
    
def addDateIndex(dataentry, accidente):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    lst = dataentry["lstaccidentes"]
    lt.addLast(lst, accidente)
    merg.sort(lst,compareHour)
    claseIndex = dataentry["clase"]
    claseEntry = mp.get(claseIndex, accidente["CLASE_ACC"])
    if claseEntry is None:
        lista_acc_clase = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lista_acc_clase,accidente)
        mp.put(claseIndex,accidente["CLASE_ACC"],lista_acc_clase)
    else:
        entry = me.getValue(claseEntry)
        lt.addLast(entry,accidente)
        
# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(data_structs["accidentes"])


def req_1(data_structs,fecha_inicio,fecha_fin):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    fecha_i = datetime.datetime.strptime(fecha_inicio, "%Y/%m/%d")
    fecha_in = fecha_i.date()
    fecha_f = datetime.datetime.strptime(fecha_fin, "%Y/%m/%d")
    fecha_fi = fecha_f.date()
    entry = om.values(data_structs["dateIndex"], fecha_in, fecha_fi)
    total_accidentes = 0
    lst_accidentes = lt.newList('ARRAY_LIST')
    for date in lt.iterator(entry):
        total_accidentes += lt.size(date["lstaccidentes"])
        lt.addLast(lst_accidentes,date["lstaccidentes"])
        
    return total_accidentes,lst_accidentes


def req_2(data_structs, clase, via):
    """
    Función que soluciona el requerimiento 2
    """
    # TO DO: Realizar el requerimiento 2
    arbol = data_structs["dateIndex"]
    dias = om.keySet(arbol)
    lst_acc_via = lt.newList('ARRAY_LIST')
    for dia in lt.iterator(dias):
        key_value_dia = om.get(arbol,dia)
        mapa_clase = me.getValue(key_value_dia)["clase"]
        contains = mp.contains(mapa_clase,clase)
        if contains:
            acc_clase = mp.get(mapa_clase,clase)
            lst_acc_clase = me.getValue(acc_clase)
            for accidente in lt.iterator(lst_acc_clase):
                if via in accidente["DIRECCION"]:
                    lt.addLast(lst_acc_via,accidente)
                    
    numero_acc = lt.size(lst_acc_via)
    lst_3_acc_recientes = lt.subList(lst_acc_via,numero_acc-2,3)
    merg.sort(lst_3_acc_recientes,sort_criteria_date)
    return lst_3_acc_recientes,numero_acc

def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs,mes,año,latitud,longitud,radio,cantidad):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    arbol = data_structs["dateIndex"]
    meses = {"ENERO":1,"FEBRERO":2,"MARZO":3,"ABRIL":4,"MAYO":5,"JUNIO":6,"JULIO":7,"AGOSTO":8,"SEPTIEMBRE":9,"OCTUBRE":10,
             "NOVIEMBRE":11,"DICIEMBRE":12}
    mess = meses[mes]
    if mes == "ENERO" or mes == "MARZO" or mes == "MAYO" or mes =="JULIO" or mes == "AGOSTO" or mes == "OCTUBRE" or mes == "DICIEMBRE":
        dia_fin = 31
    elif mes == "FEBRERO":
        dia_fin = 28
    else:
        dia_fin = 30
    fecha_i = datetime.datetime(año,mess,1)
    fecha_f = datetime.datetime(año,mess,dia_fin)
    dias = om.values(arbol,fecha_i.date(),fecha_f.date())
    acc_zona = om.newMap(omaptype='RBT',comparefunction=compareDates)
    for entry in lt.iterator(dias):
        lst_accidents = entry["lstaccidentes"]
        for accidente in lt.iterator(lst_accidents):
            lat1 = (latitud*3.14)/180
            lon1 = (longitud*3.14)/180
            lat2 = (float(accidente["LATITUD"])*3.14)/180
            lon2 = (float(accidente["LONGITUD"])*3.14)/180
            sin2 = (math.sin((lat2-lat1)/2))**2
            part2 = math.cos(lat1)*math.cos(lat2)*(math.sin((lon2-lon1)/2))**2
            distancia = 2 * math.asin(math.sqrt(sin2 + part2)) * 6371
            if distancia <= radio:
                om.put(acc_zona,distancia,accidente)
    llaves = om.keySet(acc_zona)
    lst_acc_zona = lt.newList(datastructure='ARRAY_LIST')
    for valor in lt.iterator(llaves):
        key_value = om.get(acc_zona,valor)
        accidente = me.getValue(key_value)
        lt.addLast(lst_acc_zona,accidente)
    if cantidad <= lt.size(lst_acc_zona):
        sub_lst = lt.subList(lst_acc_zona,1,cantidad)
    else:
        sub_lst = 0
    return sub_lst
        
def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compareHour(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TO DO: Crear función comparadora de la lista
    data_1 = data_1["HORA_OCURRENCIA_ACC"]
    data_2 = data_2["HORA_OCURRENCIA_ACC"]
    
    if data_1 < data_2:
        return True
    else:
        return False

def compareDates(date1, date2):
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
# Funciones de ordenamiento


def sort_criteria_date(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    data_1 = data_1["FECHA_OCURRENCIA_ACC"]
    data_2 = data_2["FECHA_OCURRENCIA_ACC"]
    
    if data_1 > data_2:
        return True
    else:
        return False
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

"""mapa = om.newMap(omaptype="RBT")
om.put(mapa,"bad bunny","agosto")
llave_valor = om.get(mapa,"bad bunny")
valor = me.getValue(llave_valor)
print(valor)"""