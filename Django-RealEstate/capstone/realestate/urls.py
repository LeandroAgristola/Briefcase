from django.urls import path
from realestate import views
from django.conf import settings 
from django.conf.urls.static import static

# Patrones de URL para el proyecto
urlpatterns = [
    # Ruta de la página de inicio, vinculada a la vista de inicio
    path('', views.home, name="home"),

    # Ruta de la página de inicio de sesión, vinculada a la vista de inicio de sesión
    path("login", views.login_view, name="login"),

    # Ruta de la página de cierre de sesión, vinculada a la vista de cierre de sesión
    path("logout", views.logout_view, name="logout"),

    # Ruta de la página de gestión, vinculada a la vista de gestión (sección de administración)
    path('management/', views.management, name='management'),

    # Ruta para agregar un nuevo proyecto de desarrollo, vinculada a la vista add_development
    path('management/add/', views.add_development_view, name='add_development'),

    # Ruta para editar un proyecto de desarrollo existente, vinculada a la vista edit_development
    # La parte <int:dev_id> de la ruta permite el manejo dinámico de los ID de desarrollo
    path('management/edit/<int:dev_id>/', views.edit_development, name='edit_development'),

    # Rutas para diferentes tipos de propiedades móviles
    path('mobiledDwelling/', views.mobiledDwelling, name='mobiledDwelling'),
    path('mobileBuildings/', views.mobileBuildings, name='mobileBuildings'),
    path('mobileIndustries/', views.mobileIndustries, name='mobileIndustries'),
]

# Si el proyecto está en modo DEBUG (entorno de desarrollo), permitir el acceso a archivos multimedia estáticos
if settings.DEBUG:
    # Esto servirá archivos multimedia desde la ruta MEDIA_URL y los almacenará en MEDIA_ROOT
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
