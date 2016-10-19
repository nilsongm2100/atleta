# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

class atleta (osv.osv): 
	_name= 'atleta'
	
	_columns={
		'cedula': fields.integer('Cédula de Identidad',size=10, required=True, help='Introduzca su número de de cédula de identidad'),
		'nombre': fields.char('Nombre',size=50, required=True, help='Introduzca su nombre completo'),
		'disciplina': fields.char('Disciplina',size=30, required=True, help='Indique el nombre de la disciplina'),
		'categoria': fields.char('Categoria',size=30, required=True, help='Introduzca la categoría a la que pertenece'),
		'rendimiento':fields.char('Rendimiento',size=30, required=True, help='Introduzca su apellido'),	
	}
	
	_defaults={
	
	}
