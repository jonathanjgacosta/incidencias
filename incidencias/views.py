from django.shortcuts import render_to_response
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template import RequestContext
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from incidencias.models import Incidencia, Incidencia_Escalada, Comentarios_Incidencia
from incidencias.forms import IncidenciaForm, IncidenciaEscaladaForm, ComentarioForm

def ir_panel(request, template_name='inicio.html'):
	id_usuario=request.session['id']
	incidencias = Incidencia.objects.filter(usuario_id=id_usuario)
	return render_to_response(template_name, {"incidencias":incidencias},  context_instance=RequestContext(request))

class IncidenciaCreateView(CreateView):
	model = Incidencia
	form_class = IncidenciaForm
	success_url = "/panel_principal"
	def form_valid(self, form):
		incidencia = form.save(commit=False)
		incidencia.usuario_id = self.request.session['id']
		incidencia.save()
		return HttpResponseRedirect(self.success_url)

class IncidenciaListView(ListView):
	model = Incidencia
	paginate_by = 5

class IncidenciaView(DetailView):
	model = Incidencia

class IncidenciaUpdateView(UpdateView):
	model = Incidencia
	form_class = IncidenciaForm
	success_url = "/incidencia/listado/"

class EscalarCreateView(CreateView):
	model = Incidencia_Escalada
	form_class = IncidenciaEscaladaForm
	success_url = "/panel_principal"

	def form_valid(self, form):
		incidencia = form.save(commit=False)
		incidencia.usuario_id = self.request.session['id']
		incidencia.incidencia_id = self.kwargs['id']
		incidencia.save()
		#actualizo el registro en la tabla incidencia con el ID del usuario seleccionado
		incidencia_object = Incidencia.objects.get(pk=self.kwargs['id'])
		incidencia_object.usuario_id = self.request.POST['usuario']
		incidencia_object.save(force_update=True)
		return HttpResponseRedirect(self.success_url)

class EscalarListView(ListView):
	model = Incidencia_Escalada

	def get_queryset(self):
		self.usuario_id = self.request.session['id']
		return Incidencia_Escalada.objects.filter(usuario_id=self.usuario_id)
		
	paginate_by = 5

class ComentarioCreateView(CreateView):
	model = Comentarios_Incidencia
	form_class = ComentarioForm
	success_url = "/panel_principal"
	def form_valid(self, form):
		incidencia = form.save(commit=False)
		incidencia.usuario_id = self.request.session['id']
		incidencia.incidencia_id = self.kwargs['id']
		incidencia.save()
		return HttpResponseRedirect(self.success_url)

class ComentarioListView(ListView):
	model = Comentarios_Incidencia

	def get_queryset(self):
		self.idincidencia = self.kwargs['id']
		return Comentarios_Incidencia.objects.filter(incidencia_id=self.idincidencia)

	paginate_by = 5

class ComentarioUpdateView(UpdateView):
	model = Comentarios_Incidencia
	form_class = ComentarioForm
	success_url = "/comentario/listado/"
	