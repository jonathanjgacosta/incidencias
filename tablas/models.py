#encoding:utf-8
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Gerencia(models.Model):

	opciones_habilitado = (
		(1, 'Activo'),
		(0, 'Inactivo'),
	)

	descripcion = models.CharField(max_length=100, unique=True)
	habilitado = models.IntegerField(choices=opciones_habilitado,
									default=1)
	def __unicode__(self):
		return self.descripcion


class Tipo_Usuario(models.Model):

	opciones_habilitado = (
		(1, 'Activo'),
		(0, 'Inactivo'),
	)

	descripcion = models.CharField(max_length=100, unique=True)
	habilitado = models.IntegerField(choices=opciones_habilitado,
									default=1)
	def __unicode__(self):
		return self.descripcion


class Estatus_Incidencia(models.Model):

	opciones_habilitado = (
		(1, 'Activo'),
		(0, 'Inactivo'),
	)

	descripcion = models.CharField(max_length=100, unique=True)
	habilitado = models.IntegerField(choices=opciones_habilitado,
									default=1)
	def __unicode__(self):
		return self.descripcion


class Origen(models.Model):

	opciones_habilitado = (
		(1, 'Activo'),
		(0, 'Inactivo'),
	)

	descripcion = models.CharField(max_length=100, unique=True)
	habilitado = models.IntegerField(choices=opciones_habilitado,
									default=1)
	def __unicode__(self):
		return self.descripcion


class Requerimiento(models.Model):

	opciones_habilitado = (
		(1, 'Activo'),
		(0, 'Inactivo'),
	)

	descripcion = models.CharField(max_length=100, unique=True)
	habilitado = models.IntegerField(choices=opciones_habilitado,
									default=1)
	def __unicode__(self):
		return self.descripcion


class Tipo_Incidencia(models.Model):

	opciones_habilitado = (
		(1, 'Activo'),
		(0, 'Inactivo'),
	)

	descripcion = models.CharField(max_length=100, unique=True)
	fecha_estimada_solucion = models.CharField(max_length=50)
	habilitado = models.IntegerField(choices=opciones_habilitado,
									default=1)
	def __unicode__(self):
		return self.descripcion