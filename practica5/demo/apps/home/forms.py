from django import forms
from .models import Paciente, Profesionista, Horarios, Cursos, ProfesionistaPaciente, HorarioProfesionista

class Registrar_Paciente_Form(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = "__all__"

class Registrar_Profesionista_Form(forms.ModelForm):
    class Meta:
        model = Profesionista
        fields = "__all__"

class Registrar_Horarios_Form(forms.ModelForm):
    class Meta:
        model = Horarios
        fields = "__all__"

class Registrar_Cursos_Form(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = "__all__"
