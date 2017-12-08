#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice

calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = ['Alonso',
            'Eduardo',
            'Gerardo',
            'Rafael',
            'Antonio',
            'Fernanda',
            'Angel',
            'Itzel',
            'Karina',
            'Esteban',
            'Alan',
            'Samuel',
            'Jose',
            'Guadalupe',
            'Angel',
            'Ulises']

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])

def dos_tup():
	aprobados = []
	reprobados = []
	ls1 = []
	ls2 = []
	for alumno in calificacion_alumno:
		if calificacion_alumno[alumno] >= 8:
			aprobados.append(alumno)

		else:
			reprobados.append(alumno)

	return tuple(aprobados), tuple(reprobados)
		
def promedio():
	calif = 0
	for alumno in calificacion_alumno:
		calif = calificacion_alumno[alumno] + calif 
	promedio = calif / len(calificacion_alumno) 
	print 'El promedio es: %s' % promedio


def conj_calif():
	c1 = set()
	for alumno in calificacion_alumno:
		c1.add(calificacion_alumno[alumno])
	print 'El conjunto es: %s' % c1

asigna_calificaciones()
imprime_calificaciones()
var1 = dos_tup()
promedio()
conj_calif()

print var1
