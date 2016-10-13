# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

class atleta (osv.osv): 
	_name="atleta"
	
	_columns={
		'cedula': fields.integer('Cédula de Identidad',size=10, required=True, help='Introduzca su número de de cédula de identidad'),
		'nombre': fields.char('Nombre',size=30, required=True, help='Introduzca su nombre'),
		'apellido':fields.char('Apellido',size=30, required=True, help='Introduzca su apellido'),
		'fecha_nacimiento':fields.date('Fecha de nacimiento'),
	}
	
	_defaults={
	
	}
