from django import forms
from apps.profesores.models import *
from apps.alumnos.models import *
class RegistrarAlumno(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = [
            "Matricula",
            "ApellidoPaterno",
            "ApellidoMaterno",
            "Nombres",
            "Grupo",
            "Uno",
            "Dos",
            "Tres",
            "Cuatro",
        ]
        labels = {
            "Matricula": "Matrícula",
            "ApellidoPaterno": "Apellido Paterno",
            "ApellidoMaterno": "Apellido Materno",
            "Nombres": "Nombres",
            "Grupo": "Grupos",
            "num_list": "Extra",
            "Uno": "Uno",
            "Dos": "Dos",
            "Tres": "Tres",
            "Cuatro": "Cuatro",
        }
        widgets = {
            "Matricula": forms.TextInput(attrs={"class":"form-control", 'type':'number'}),
            "ApellidoPaterno": forms.TextInput(attrs={"class":"form-control"}),
            "ApellidoMaterno": forms.TextInput(attrs={"class":"form-control"}),
            "Nombres": forms.TextInput(attrs={"class":"form-control"}),
            "Grupo": forms.CheckboxSelectMultiple(),
            "num_list": forms.CheckboxSelectMultiple(),
        }
class RegistrarProfesor(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = [
            "Matricula",
            "ApellidoPaterno",
            "ApellidoMaterno",
            "Nombres",
            "Grupo",
        ]
        labels = {
            "Matricula": "Matrícula",
            "ApellidoPaterno": "Apellido Paterno",
            "ApellidoMaterno": "Apellido Materno",
            "Nombres": "Nombres",
            "Grupo": "Grupos",
        }
        widgets = {
            "Matricula": forms.TextInput(attrs={"class": "form-control", 'type':'number'}),
            "ApellidoPaterno": forms.TextInput(attrs={"class": "form-control"}),
            "ApellidoMaterno": forms.TextInput(attrs={"class": "form-control"}),
            "Nombres": forms.TextInput(attrs={"class": "form-control"}),
            "Grupo": forms.CheckboxSelectMultiple(),
        }
class RegistrarJuego(forms.ModelForm):
    class Meta:
        model = Problemas
        fields = [
            "Descripcion",
            "VectorEntrada",
            "VectorSalida",
            "VectorPiso",
        ]
        labels = {
            "Descripcion": "Descripción del problema",
            "VectorEntrada": "Vector de entrada del problema(solo números separados por coma)",
            "VectorSalida": "Vector de salida del problema(solo números separados por coma)",
            "VectorPiso": "Vector de piso del problema(solo números separados por coma)",
        }
        widgets = {
            "Descripcion": forms.TextInput(attrs={"class": "form-control"}),
            "VectorEntrada": forms.TextInput(attrs={"class": "form-control"}),
            "VectorSalida": forms.TextInput(attrs={"class": "form-control"}),
            "VectorPiso": forms.TextInput(attrs={"class": "form-control"}),
        }
class RegistrarGrupo(forms.ModelForm):
    class Meta:
        model = Grupos
        fields = [
            "Descripcion",
        ]
        labels = {
            "Descripcion": "Descripción del grupo",
        }
        widgets = {
            "Descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }
class IniciarSesion(forms.Form):
    Matricula = forms.CharField(label="Usuario", max_length=8, widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Matrícula del alumno"}))
class IniciarSesionProf(forms.Form):
    Matricula = forms.CharField(label="Usuario", max_length=8, widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Matrícula del profesor"}))
