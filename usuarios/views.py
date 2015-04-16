from usuarios.models import MyUser
from incidencias.models import Incidencia, Incidencia_Escalada
from django.contrib.auth import  authenticate, login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect


def inicio_sesion(request):
	email = request.POST['email']
	password = request.POST['password']
	user = authenticate(email=email, password=password)
	#consultando la data
	usuario = MyUser.objects.get(email=email)
	incidencias = Incidencia.objects.filter(usuario_id=usuario.id)
	#creando las sesiones
	request.session['nombre']=usuario.nombre+" "+usuario.apellido
	request.session['id']=usuario.id
	#validando
	if user is not None and user.is_active:
		login(request, user)
		return render_to_response('inicio.html', {"incidencias":incidencias},  context_instance=RequestContext(request))
	else:
		return render_to_response('login.html', {"error": 1}, context_instance=RequestContext(request))

def inicio(request, template_name='login.html'):
	return render_to_response(template_name, context_instance=RequestContext(request))


def cierre_sesion(request):
    logout(request)
    return HttpResponseRedirect("/")