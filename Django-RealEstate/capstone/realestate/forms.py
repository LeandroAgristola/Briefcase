from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from .models import development # Asumiendo que 'development' es el modelo correcto
import re

# Validador personalizado para garantizar que el campo contenga solo letras
def validateOnlyLetters(value):
    if not value.isalpha():
        raise ValidationError('Este campo debe contener sólo letras.')

# Validador personalizado para garantizar que el campo contenga solo caracteres numéricos
def validateOnlynumbers(value):
    if not re.match(r'^\d+$', value):
        raise ValidationError('El número de teléfono debe contener solo números.')

# Validador personalizado para garantizar que el formato de la dirección de correo electrónico sea válido
def validateOnlyemail(value):
    try:
        validate = EmailValidator()
        validate(value)
    except ValidationError:
        raise ValidationError('Por favor, ingrese un correo electrónico válido.')
    return True

# Formulario para la página de contacto
class contactForm(forms.Form):
    # Campo para el nombre del usuario
    name = forms.CharField(
        max_length=100,
        validators=[validateOnlyLetters],
        label='Nombre', # <--- ¡Aquí está el cambio!
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Carlos'
        })
    )
    # Campo para el apellido del usuario
    lastname = forms.CharField(
        max_length=100,
        validators=[validateOnlyLetters],
        label='Apellido', # <--- ¡Aquí está el cambio!
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Perez'
        })
    )
    # Campo para el número de teléfono del usuario
    phonenumber = forms.CharField(
        max_length=20,
        validators=[validateOnlynumbers],
        label='Número de teléfono', # <--- ¡Aquí está el cambio!
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '0115345456'
        })
    )
    # Campo para la dirección de correo electrónico del usuario
    email = forms.EmailField(
        validators=[validateOnlyemail],
        label='Correo electrónico', # <--- ¡Aquí está el cambio!
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ejemplo@djangomail.com' # También ajusté el placeholder
        })
    )
    # Campo para la consulta o mensaje del usuario
    consultation = forms.CharField(
        label='Consulta', # <--- ¡Aquí está el cambio!
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Escribe tu consulta aquí'
        })
    )
    
# Formulario modelo para agregar o editar un proyecto de desarrollo
class DevelopmentForm(forms.ModelForm):
    class Meta:
        model = development  # Vincula el formulario al modelo 'development'
        fields = ['title', 'content', 'image', 'brochurePaper']  # Especifica los campos a incluir

        # Esto le dice a Django qué texto debe mostrar para cada etiqueta de campo.
        labels = {
            'title': 'Título',            # El campo 'title' se mostrará como 'Título' al usuario.
            'content': 'Contenido',       # El campo 'content' se mostrará como 'Contenido' al usuario.
            'image': 'Imagen',            # El campo 'image' se mostrará como 'Imagen' al usuario.
            'brochurePaper': 'Folleto (PDF)', # El campo 'brochurePaper' se mostrará como 'Folleto (PDF)' al usuario.
        }

        # Personaliza la apariencia de cada campo en el formulario (widgets)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa el título'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa el contenido',
                'rows': 6  # Número de filas en el área de texto
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'brochurePaper': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }
