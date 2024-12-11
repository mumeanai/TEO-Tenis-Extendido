import csv
from datetime import datetime, date
import datetime
from typing import NamedTuple

Parcial = NamedTuple('Parcial', 
                [('juegos_j1',int),
                 ('juegos_j2',int)])
PartidoTenis = NamedTuple('PartidoTenis', 
                [('fecha',datetime.date), 
                 ('jugador1',str), 
                 ('jugador2',str), 
                 ('superficie',str), 
                 ('resultado', list[Parcial]), 
                 ('errores_nf1',int), 
                 ('errores_nf2',int)])


def lee_partidos_tenis(ruta:str) -> list[PartidoTenis]:
    '''
    lee un fichero de entrada en formato CSV codificado en UTF-8 y 
    devuelve una lista de tuplas de tipo PartidoTenis conteniendo
    todos los datos almacenados en el fichero. Le puede ser de 
    ayuda la función datetime.strptime(cadena, '%d/%m/%Y') para 
    el parseo de fechas. Para implementar esta función defina la 
    siguiente función auxiliar:
    '''
    with open(ruta, encoding='utf-8') as f:
        lector = csv.reader(ruta, delimiter=";")
        res = []
        for fecha, j1, j2, superficie, parcial1, parcial2, parcial3, e1, e2 in lector:
        fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
        resultado = parsea_parciales(parcial1, parcial2, parcial3)
        e1 = int(e1)
        e2 = int(e2)
        res.append(
            PartidoTenis(fecha, j1, j2, superficie, resultado, e1,e2)
            )
        return res


def parsea_parciales(p1:str, p2:str, p3:str) ->list[Parcial]: 
    '''
    Toma una cadena con el resultado de un set o parcial y 
    devuelve una tupla de tipo Parcial que representa ese set. 
    La cadena de entrada se espera que tenga los juegos del set 
    del primer jugador, seguido de un guión y los juegos del set 
    del segundo jugador, es decir, int-int.
    '''
    if p3 == "0-0":
        return [
            parsea_parcial(p1),
            parsea_parcial(p2),        
        ]
    else:
        return [
            parsea_parcial(p1),
            parsea_parcial(p2),
            parsea_parcial(p3)        
        ]
    
def parsea_parcial(parcial):
    juegos1, juegos2 = parcial.split("-")
    return Parcial(int(juegos1), int(juegos2))


def partidos_menos_errores():
    '''
    recibe una lista de tipo PartidoTenis y devuelve el partido 
    con menor número de errores no forzados entre los dos jugadores.
    '''
    pass

def jugador_mas_partidos(): 
    '''
    recibe una lista de tipo PartidoTenis y devuelve una tupla 
    con el nombre del jugador que más partidos ha jugado y el 
    número de partidos.
    '''
    #counter o defauldict(int)
    #hacemos .items y luego max()
    pass

def tenista_mas_victorias():
    '''
    recibe una lista de tuplas de tipo PartidoTenis, y dos fechas,
    ambas de tipo date, y con valor por defecto None. Devuelve 
    el nombre del tenista que ha tenido más victorias en los 
    partidos jugados entre las fechas (ambas inclusive). Si la 
    primera fecha es None, la función devuelve el tenista con 
    más victorias hasta la segunda fecha (inclusive). Si la 
    segunda fecha es None, la función devuelve el tenista con 
    más victorias desde la primera fecha (inclusive). Finalmente,
    si las dos fechas son None, la función devuelve el tenista 
    con más victorias de toda la lista, independientemente de la
    fecha. Para implementar esta función defina la siguiente 
    función auxiliar:

    ganador: que recibe una tupla de tipo PartidoTenis y devuelve 
    el nombre del jugador que ganó ese partido.
    '''
    #if (fecha1 == None or  fecha1<=p.fecha) and (fecha2 == None or p.fecha <= fecha2)
    pass

def media_errores_por_jugador(): 
    '''
    recibe una lista de tuplas de tipo PartidoTenis y devuelve 
    una lista de tuplas ordenadas con el nombre de cada jugador 
    y su media de errores no forzados. La lista estará ordenada 
    por la media de errores de menor a mayor.
    '''
    #diccionario con suma y otra con conteos, y luego recorres los items
    #listas con los elementos y diccionario, luego recorreer elementos 
    pass