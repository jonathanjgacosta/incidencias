from django.forms import ModelForm
from django import forms
from incidencias.models import Incidencia, Incidencia_Escalada, Comentarios_Incidencia

class IncidenciaForm(ModelForm):
	class Meta:
		model = Incidencia
		widgets = {
			'descripcion': forms.Textarea(attrs={'class':'form-control', 'rows':'6'}),
			'titulo': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_inicio': forms.DateInput(attrs={'class':'form-control','id':'datetimepicker','data-date-format':'YYYY-MM-DD'}),
			'fecha_fin': forms.DateInput(attrs={'class':'form-control','id':'datetimepicker2','data-date-format':'YYYY-MM-DD'}),
			'tipo_incidencia': forms.Select(attrs={'class':'form-control'}),
			'estatus': forms.Select(attrs={'class':'form-control'}),
			'origen': forms.Select(attrs={'class':'form-control'}),
			'requerimiento': forms.Select(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'prefijo': forms.TextInput(attrs={'class':'form-control'}),
			'empresa': forms.TextInput(attrs={'class':'form-control'}),
			'afiliado': forms.Select(attrs={'class':'form-control'}),
			}
		exclude = ['usuario']

class IncidenciaEscaladaForm(ModelForm):
	class Meta:
		model = Incidencia_Escalada
		widgets = {
			'usuario': forms.Select(attrs={'class':'form-control'}),
			'fecha_escalada': forms.DateInput(attrs={'class':'form-control', 'id':'datetimepicker','data-date-format':'YYYY-MM-DD'}),
			'comentario': forms.Textarea(attrs={'class':'form-control', 'rows':'6'}),
			}
		exclude = ['incidencia']

class ComentarioForm(ModelForm):
	class Meta:
		model = Comentarios_Incidencia
		widgets = {
			'comentario': forms.Textarea(attrs={'class':'form-control', 'rows':'6'}),
			'fecha': forms.DateInput(attrs={'class':'form-control', 'id':'datetimepicker','data-date-format':'YYYY-MM-DD'}),
			'adjunto_doc': forms.FileInput(attrs={'class':'form-control'}),
			'adjunto_img': forms.FileInput(attrs={'class':'form-control'}),
			}
		exclude = ['incidencia','usuario']