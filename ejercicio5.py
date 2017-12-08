#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

sistemas = ['angie','juan','jonatan']
op_interna = ['quintero','fernando','yeudiel']
incidentes = ['demian','anduin','diana','victor','vacante']
auditorias = ['juan','fernando','oscar','daniel','gonzalo','cristian','jorge','virgilio']

var1 = filter((lambda fil: 'i' in fil), (lambda sist, op, inci, audi: sist + op + inci + audi)(sistemas, op_interna, incidentes, auditorias))

ls = ','.join(map((lambda up: up.upper()), var1))
print ls
#expresion funcional:
# 1) funcion lambda que sume las cuatro listas
# 2) filtre la lista resultante para obtener todos los nombres que tienen una "i"
# 3) convierta a mayusculas el resultado anterior
#UNA SOLA EXPRESION
