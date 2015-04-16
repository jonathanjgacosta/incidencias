from django.db import models
from django.conf import settings
from tablas.models import Estatus_Incidencia, Origen, Requerimiento, Tipo_Incidencia
from usuarios.models import MyUser
from django.contrib.auth.models import User

class Incidencia(models.Model):

		opciones_afiliado = (
		(1, 'Afiliado'),
		(0, 'No Afiliado'),
	)

		titulo = models.CharField(max_length=100, unique=True)
		descripcion = models.TextField()
		fecha_inicio = models.DateField(verbose_name='Fecha de inicio')
		fecha_fin = models.DateField(verbose_name='Fecha de finalizacion')
		tipo_incidencia = models.ForeignKey(Tipo_Incidencia,null=True)
		estatus = models.ForeignKey(Estatus_Incidencia,null=True)
		origen = models.ForeignKey(Origen,null=True)
		requerimiento = models.ForeignKey(Requerimiento,null=True)
		usuario = models.ForeignKey(MyUser,null=True)
		nombre = models.CharField(max_length=50)
		email = models.EmailField(
        	verbose_name='Direccion email',
        	max_length=255,
        	unique=True,
		)
		telefono = models.CharField(max_length=15)
		prefijo = models.CharField(max_length=10)
		empresa = models.CharField(max_length=255)
		afiliado = models.IntegerField(choices=opciones_afiliado,
									default=1)

		def __unicode__(self):
			return self.titulo


class Incidencia_Escalada(models.Model):

	fecha_escalada = models.DateField(verbose_name='Fecha de Escalado')
	comentario = models.TextField(null=True)
	incidencia = models.ForeignKey(Incidencia,null=True)
	usuario = models.ForeignKey(MyUser,null=True)

	def __unicode__(self):
		return self.incidencia


class Comentarios_Incidencia(models.Model):

	incidencia = models.ForeignKey(Incidencia,null=True)
	usuario = models.ForeignKey(MyUser,null=True)
	comentario = models.TextField(null=True)
	fecha = models.DateField(verbose_name='Fecha Comentario')
	adjunto_doc = models.FileField(upload_to='documentos',verbose_name='Adjuntar Documento')
	adjunto_img = models.ImageField(upload_to='imagen', verbose_name='Adjuntar Imagen')

	def __unicode__(self):
		return self.comentario