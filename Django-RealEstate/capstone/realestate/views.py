from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.mail import EmailMessage
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import contactForm, DevelopmentForm
from .models import development

# Vista de la página de inicio
def home(request):
    # Obtener todos los proyectos de desarrollo
    developments = development.objects.all()

    # Manejar el envío del formulario
    if request.method == "POST":
        forms_contact = contactForm(data=request.POST)
        if forms_contact.is_valid():
            # Extraer datos limpios del formulario
            name = forms_contact.cleaned_data['name']
            lastname = forms_contact.cleaned_data['lastname']
            phonenumber = forms_contact.cleaned_data['phonenumber']
            email = forms_contact.cleaned_data['email']
            consultation = forms_contact.cleaned_data['consultation']

            # Crea el mensaje de correo electrónico con los datos proporcionados
            email_message = EmailMessage(
                "Mensaje de Real Estate",
                f"Nombre: {name} {lastname}\nTeléfono: {phonenumber}\nEmail: {email}\nConsulta: {consultation}",
                "#",  # Email del remitente (reemplazar con el email real)
                ["#"],  # Email del destinatario (reemplazar con el email real)
                reply_to=[email]
            )

            try:
                # Intentar enviar el correo electrónico
                email_message.send()
                return JsonResponse({'status': 'ok'}, status=200)
            except Exception as e:
                # Manejar errores al enviar el correo electrónico
                print(f"Error al enviar el correo electrónico: {e}")
                return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        else:
            # Retornar errores de validación si el formulario es inválido
            errors = forms_contact.errors.as_json()
            return JsonResponse({'status': 'invalid', 'errors': errors}, status=400)
    
    # Si es una solicitud GET, renderiza la página con un formulario de contacto vacío
    forms_contact = contactForm()
    return render(request, 'realestate/home.html', {
        'developments': developments, 
        'myform': forms_contact
    })

# Vista de la página de gestión, requiere inicio de sesión
@login_required(login_url='login')
def management(request):
    # Obtener todos los proyectos de desarrollo
    developments = development.objects.all()

    # Manejar la solicitud de eliminación
    if request.method == 'POST':
        if 'delete' in request.POST:
            ids_to_delete = request.POST.getlist('development_ids')

            # Eliminar proyectos de desarrollo seleccionados
            for dev_id in ids_to_delete:
                obj = get_object_or_404(development, id=dev_id)
                obj.delete()

            # Redirigir a la página de gestión después de la eliminación
            return redirect('management')

    # Renderizar la página de gestión con todos los desarrollos
    return render(request, 'realestate/management.html', {
        'developments': developments
    })

# Vista de la página de agregar desarrollo, requiere inicio de sesión
@login_required(login_url='login')
def add_development_view(request):
    # Manejar el envío del formulario
    if request.method == 'POST':
        form = DevelopmentForm(request.POST, request.FILES)
        if form.is_valid():
            # Guardar el nuevo proyecto de desarrollo
            form.save()
            return redirect('management')
    else:
        form = DevelopmentForm()
    
    # Representar la página del formulario de desarrollo de anuncios
    return render(request, 'realestate/add_development.html', {'form': form})

# Vista de la página de edición de desarrollo, requiere inicio de sesión
@login_required(login_url='login')
def edit_development(request, dev_id):
    # Obtener el proyecto de desarrollo a editar
    dev = get_object_or_404(development, id=dev_id)

    # Manejar el envío del formulario para la edición
    if request.method == 'POST':
        form = DevelopmentForm(request.POST, request.FILES, instance=dev)
        if form.is_valid():
            # Guardar el proyecto de desarrollo actualizado
            form.save()
            return redirect('management')
    else:
        form = DevelopmentForm(instance=dev)

    # Renderizar la página del formulario de edición de desarrollo
    return render(request, 'realestate/edit_development.html', {'form': form, 'development': dev})

# Vista de inicio de sesión
def login_view(request):
    if request.method == "POST":
        # Autenticar al usuario con el nombre de usuario y la contraseña proporcionados
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Si la autenticación es exitosa, iniciar sesión en el usuario y redirigirlo a la página de administración
            login(request, user)
            return HttpResponseRedirect(reverse("management"))
        else:
            # Si la autenticación falla, renderizar la página de inicio de sesión con un mensaje de error
            return render(request, "realestate/login.html", {
                "message": "Nombre de usuario y/o contraseña no válidos."
            })
    else:
        # Renderizar la página de inicio de sesión para la solicitud GET
        return render(request, "realestate/login.html")

# Vista de cierre de sesión
def logout_view(request):
    # Cerrar sesión del usuario y redirigir a la página de inicio
    logout(request)
    return HttpResponseRedirect(reverse("home"))

# Vistas para diferentes tipos de propiedades
def mobiledDwelling(request):
    # Página de renderizado para propiedades de viviendas móviles
    return render(request, 'realestate/mobiledDwelling.html')

def mobileBuildings(request):
    # Página de renderizado para propiedades de edificios móviles
    return render(request, 'realestate/mobileBuildings.html')

def mobileIndustries(request):
    # Página de renderizado para propiedades de industrias móviles
    return render(request, 'realestate/mobileIndustries.html')
