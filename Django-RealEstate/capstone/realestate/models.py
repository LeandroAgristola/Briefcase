from django.db import models
import os

# Modelo que representa un proyecto de desarrollo
class development(models.Model):
    # Título del desarrollo, limitado a 50 caracteres
    title = models.CharField(max_length=50)
    
    # Descripción corta o contenido sobre el desarrollo, limitado a 200 caracteres
    content = models.CharField(max_length=200)

    # Imagen asociada con el desarrollo, almacenada en el directorio 'developments'
    image = models.ImageField(upload_to='developments')
    
    # Archivo de folleto o PDF asociado con el desarrollo, almacenado en el directorio 'developments_pdfs/'
    brochurePaper = models.FileField(upload_to='developments_pdfs/')
    
# Marca de tiempo de cuándo se creó el desarrollo, se establece automáticamente al crearse
    created = models.DateTimeField(auto_now_add=True)

    # Marca de tiempo de cuándo se actualizó por última vez el desarrollo, se establece automáticamente al guardarse
    updated = models.DateTimeField(auto_now=True)

    # Opciones meta para el modelo
    class Meta:
        # Nombre singular para el modelo en la interfaz de administración
        verbose_name = 'development'

        # Nombre plural para el modelo en la interfaz de administración
        verbose_name_plural = 'developments'

   # Representación de cadena del modelo, que muestra el título
    def __str__(self):
        return self.title

    # Método de eliminación personalizado para eliminar archivos asociados del sistema de archivos
    def delete(self, *args, **kwargs):
        # Si existe una imagen, eliminarla del sistema de archivos
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)

        # Si existe un archivo de folleto o PDF, eliminarlo del sistema de archivos
        if self.brochurePaper:
            if os.path.isfile(self.brochurePaper.path):
                os.remove(self.brochurePaper.path)

        # Llama al método de eliminación de la clase padre para eliminar la instancia del modelo de la base de datos
        super().delete(*args, **kwargs)
