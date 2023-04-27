"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate as tab
import matplotlib.pyplot as plt
from IPython.display import display
import folium
import traceback
default_limit = 1000 
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 2")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control,filename):
    """
    Carga los datos
    """
    #TO DO: Realizar la carga de datos
    controller.load_data(control,"siniestros/datos_siniestralidad-" +filename)


def print_caragaDatos(sublista):
    """
        Función que imprime un dato dado su ID
    """
    list_of_lists = []
    headerss = ["CODIGO_ACCIDENTE","FECHA_HORA_ACC","LOCALIDAD","DIRECCION","GRAVEDAD","CLASE_ACC","LATITUD","LONGITUD"]
    
    for accidente in lt.iterator(sublista):
        lista_acc = []
        lista_acc.append(accidente["CODIGO_ACCIDENTE"])
        lista_acc.append(accidente["FECHA_HORA_ACC"])
        lista_acc.append(accidente["LOCALIDAD"])
        lista_acc.append(accidente["DIRECCION"])
        lista_acc.append(accidente["GRAVEDAD"])
        lista_acc.append(accidente["CLASE_ACC"])
        lista_acc.append(accidente["LATITUD"])
        lista_acc.append(accidente["LONGITUD"])
        list_of_lists.append(lista_acc)
    print(tab(list_of_lists,tablefmt='grid',headers=headerss))
    
    #TO DO: Realizar la función para imprimir un elemento
    
def opciones_tamaño():
    tamano = int(input("Elija el tamaño del archivo:\n1.Small (1%)\n2.5%\n3.10%\n4.20%\n5.30%\n6.50%\n7.80%\n8.Large (100%)\n"))
    tamanos=["small.csv","5pct.csv","10pct.csv","20pct.csv","30pct.csv","50pct.csv","80pct.csv","large.csv"]
    return tamanos[tamano-1]

def fechas(fecha_in,fecha_fi):
    if fecha_in == "" or fecha_fi == "":
        fecha_in = input("Escribir la fecha inicial: ")
        fecha_fi = input("Escribir la fecha final: ")
    while (fecha_in[4] != "/" or fecha_in[7] != "/") or (fecha_fi[4] != "/" or fecha_fi[7] != "/"):
        print("Alguna fecha quedó mal escrita, vuelva a hacerlo")
        fecha_in = input("Escribir la fecha inicial: ")
        fecha_fi = input("Escribir la fecha final: ")
    return fecha_in,fecha_fi

def print_tabla_req_1(lista):
    lst_of_lsts = []
    headerss = ["CODIGO_ACCIDENTE","FECHA_HORA_ACC","DIA_OCURRENCIA_ACC","LOCALIDAD","DIRECCION","GRAVEDAD","CLASE_ACC","LATITUD","LONGITUD"]
    for accidente_lst in lt.iterator(lista):
        for accidente in lt.iterator(accidente_lst):
            lista_acc = []
            lista_acc.append(accidente["CODIGO_ACCIDENTE"])
            lista_acc.append(accidente["FECHA_HORA_ACC"])
            lista_acc.append(accidente["DIA_OCURRENCIA_ACC"])
            lista_acc.append(accidente["LOCALIDAD"])
            lista_acc.append(accidente["DIRECCION"])
            lista_acc.append(accidente["GRAVEDAD"])
            lista_acc.append(accidente["CLASE_ACC"])
            lista_acc.append(accidente["LATITUD"])
            lista_acc.append(accidente["LONGITUD"])
            lst_of_lsts.append(lista_acc)
        
    print(tab(lst_of_lsts,tablefmt='grid',headers=headerss,maxcolwidths=13))
        
def print_tbala_req_2(lista):
    lst_of_lsts = []
    headerss = ["CODIGO_ACCIDENTE","FECHA_HORA_ACC","DIA_OCURRENCIA_ACC","LOCALIDAD","DIRECCION","GRAVEDAD","CLASE_ACC","LATITUD","LONGITUD"]
    for accidente in lt.iterator(lista):
        lista_acc = []
        lista_acc.append(accidente["CODIGO_ACCIDENTE"])
        lista_acc.append(accidente["FECHA_HORA_ACC"])
        lista_acc.append(accidente["DIA_OCURRENCIA_ACC"])
        lista_acc.append(accidente["LOCALIDAD"])
        lista_acc.append(accidente["DIRECCION"])
        lista_acc.append(accidente["GRAVEDAD"])
        lista_acc.append(accidente["CLASE_ACC"])
        lista_acc.append(accidente["LATITUD"])
        lista_acc.append(accidente["LONGITUD"])
        lst_of_lsts.append(lista_acc)
        
    print(tab(lst_of_lsts,tablefmt='grid',headers=headerss,maxcolwidths=13))
    
def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TO DO: Imprimir el resultado del requerimiento 1
    fecha_inicio = input("Ingrese una fecha de inicio: ")
    fecha_fin = input("Ingrese una fecha de fin: ")
    rta, total_time = controller.req_1(control,fecha_inicio,fecha_fin)
    total_acc,lst_acc = rta
    print("\nHay " +str(total_acc)+" accidentes registrados entre " +fecha_inicio+ " y " + fecha_fin)
    print_tabla_req_1(lst_acc)
    print("Tiempo: "+str(total_time))
    
def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TO DO: Imprimir el resultado del requerimiento 2
    clase = input("Ingrese la clase del accidente: ")
    via = input("ingrese el nombre de la vía de la ciudad: ")
    rta,time = controller.req_2(control,clase,via)
    lst_3_acc,numero_acc = rta
    print("\nHay " +str(numero_acc)+" accidentes de la clase " +clase+" ocurridos a lo largo de la vía "+via+" y los tres más recientes son: ")
    print_tbala_req_2(lst_3_acc)
    print("Tiempo: "+str(time))

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control, gravedad, fecha_in, fecha_fi):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    top5, cantidad = controller.req_4(control, gravedad, fecha_in, fecha_fi)
    print("=============== Req No. 4 Inputs ===============")
    print("Reporte de los 5 accidentes con '" + gravedad + "' más recientes entre '" + fecha_in + "' y '" + fecha_fi + "'\n")
    print("=============== Req No. 4 Answer ===============")
    print("Hay ", str(cantidad), " accidentes entre las fechas '" + fecha_in + "' y '" + fecha_fi + "'\n")
    print(tab(top5["elements"], headers="keys", tablefmt='grid', maxcolwidths=13))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TO DO: Imprimir el resultado del requerimiento 6
    mes = input("Ingrese un mes: ")
    año = int(input("Ingrese un año: "))
    latitud = float(input("Ingrese la latitud: "))
    longitud = float(input("Ingrese la longitud: "))
    radio = float(input("Ingrese el radio: "))
    cantidad = int(input("Ingrese el número de accidentes: "))
    rta,time = controller.req_6(control,mes,año,latitud,longitud,radio,cantidad)
    if rta == 0:
        print("Intente con un número diferente de accidentes")
    else:
        print("\nLos " +str(cantidad)+" accidentes más cercanos al punto (" +str(latitud)+", "+str(longitud)+") dentro de un radio de "+str(radio)+" km para el mes de "+mes+" de "+str(año))
        print_tbala_req_2(rta)
    print("Tiempo: "+str(time))
    
def print_req_7(control,mes,ano):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    accidentes, horas, cantidad = controller.req_7(control,mes,ano)
    print("=============== Req No. 7 Answer ===============")
    print("Accidentes más tempranos y tardíos para el mes de", mes, "de", ano)
    for dia in accidentes:
        print("Accidentes del día " + dia)
        print(tab(accidentes[dia]["elements"], headers="keys", tablefmt='grid', maxcolwidths=13))
    plt.bar(list(horas.keys()),list(horas.values()))
    plt.xticks(rotation=90)
    plt.title("Frecuencia de " + str(cantidad) + " accidentes por hora del día\nPara el mes de " + mes + " de " + ano)
    plt.xlabel("Hora del día")
    plt.ylabel("Número de accidentes")
    plt.show()


def print_req_8(control,clase,fecha_in,fecha_fi):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    cantidad, accidentes = controller.req_8(control,clase,fecha_in,fecha_fi)
    print("=============== Req No. 8 Answer ===============")
    print("Hay " + str(cantidad) + " accidentes entre las fechas '" + fecha_in + "' y '" + fecha_fi +"'")
    mapa = folium.Map(location=[accidentes["elements"][0]["LATITUD"], accidentes["elements"][0]["LONGITUD"]])
    for accidente in lt.iterator(accidentes):
        folium.Marker(location=[accidente["LATITUD"], accidente["LONGITUD"]], popup="CODIGO_ACCIDENTE: " + accidente["CODIGO_ACCIDENTE"]).add_to(mapa)
    mapa.save("accidentes.html")


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                filename = opciones_tamaño()
                print("Cargando información de los archivos ....\n")
                load_data(control,filename)
                print("Archivos cargados: " + str(controller.get_size(control)))
                first_3 = lt.subList(control["accidentes"],1,3)
                last_3 = lt.subList(control["accidentes"],lt.size(control["accidentes"])-2,3)
                print("\nLos primeros tres registros de accidentes cargados fueron: ")
                print_caragaDatos(first_3)
                print("\nLos últimos tres registros de accidentes cargados fueron: ")
                print_caragaDatos(last_3)
                
            elif int(inputs) == 2:
                print_req_1(control)
                

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                gravedad = input("Escribir la gravedad a analizar: ")
                fecha_in,fecha_fi = fechas("", "")
                print_req_4(control, gravedad, fecha_in, fecha_fi)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                mes = input("Escribir el mes: ")
                ano = input("Escribir el año: ")
                print_req_7(control,mes,ano)

            elif int(inputs) == 9:
                clase = input("Escribir la clase a analizar: ")
                fecha_in,fecha_fi = fechas("", "")
                print_req_8(control,clase,fecha_in,fecha_fi)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
