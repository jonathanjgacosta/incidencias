from django import forms
from django.contrib import admin
from tablas.models import Gerencia, Tipo_Usuario
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from usuarios.models import MyUser


class UserCreationForm(forms.ModelForm):
    """Formulario para crear nuevos usuarios, incluyendo todos los campos requeridos
    y validaciones de repetir el password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Verificacion', widget=forms.PasswordInput)
    gerencia = forms.ModelChoiceField(queryset=Gerencia.objects.all())
    tipo_usuario = forms.ModelChoiceField(queryset=Tipo_Usuario.objects.all())

    class Meta:
        model = MyUser
        fields = ('email', 'date_of_birth','gerencia', 'tipo_usuario')

    def clean_password2(self):
        # Verificar que los passwords correspondan
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords no coinciden")
        return password2

    def save(self, commit=True):
        # Almacena el password en formato hash 
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """Formulario para actualizar los campos de los usuarios registrados.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin','gerencia', 'tipo_usuario', 'nombre', 'apellido', 'cargo')

    def clean_password(self):
        
        return self.initial["password"]


class MyUserAdmin(UserAdmin):
    # Formulario para agregar y modificar instancias de usuarios
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'date_of_birth', 'is_admin', 'gerencia', 'tipo_usuario', 'nombre', 'apellido', 'cargo')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informacion Personal', {'fields': ('date_of_birth','nombre', 'apellido')}),
        ('Datos Empresa', {'fields': ('cargo', 'gerencia', 'tipo_usuario')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2','gerencia', 'tipo_usuario', 'nombre', 'apellido', 'cargo')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(MyUser, MyUserAdmin)

admin.site.unregister(Group)
