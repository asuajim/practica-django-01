Curso Django - Proyecto 2: Web de Empresa
==========================================

Primeros pasos
===============

# Acceder a la carpeta del curso Udemy
cd Udemy

# Activar el entorno virtual
source py36/bin/activate

# Crear proyecto Django
django-admin startproject webempresa

# Establecer idioma a español
Establecer en settings.py: LANGUAGE_CODE = 'es'

# Establecer base de datos
Establecer en settings.py en el diccionario DATABASES. Por defecto se utilizará la base de datos SQLite

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

Para otras bases de datos consultar: 
https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# Aplicar migraciones pendientes
python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK


Crear una app (core)
--------------------

Con el proyecto detenido y el espacio virtual activo para crear el siguiente la app ejecutar:

python3 manage.py startapp core

Este comando creará la carpeta "core" que contiene la carpeta "migrations" y los archivos de la app: __init__.py, admin.py, apps.py, models.py, tests.py y views.py.

Crear vista/s de la app core
-----------------------------

Abrir el archivo views.py de la carpeta core y añadir a la línea del import el método "HttpResponse", crear la vistas de cada página y el código HTML que muestra el texto común en todas las páginas:

from django.shortcuts import render, HttpResponse

html_base = """<h2>L'autentico caffè d'italia</h2>
<h1>La Caffettiera</h1>
<ul>
    <li><a href='/'>INICIO</a></li>
    <li><a href='/about/'>HISTORIA</a></li>
    <li><a href='/services/'>SERVICIOS</a></li>
    <li><a href='/store/'>VISITANOS</a></li>
    <li><a href='/contact/'>CONTACTO</a></li>
    <li><a href='/blog/'>BLOG</a></li>
</ul>"""

# Create your views here.
def home(request):
    return HttpResponse(html_base + "<h1>Inicio</h1>")

def about(request):
    return HttpResponse(html_base + "<h1>Historia</h1>")

def services(request):
    return HttpResponse(html_base + "<h1>Servicios</h1>")

def store(request):
    return HttpResponse(html_base + "<h1>Visítanos</h1>")

def contact(request):
    return HttpResponse(html_base + "<h1>Contacto</h1>")

def blog(request):
    return HttpResponse(html_base + "<h1>Blog</h1>")

def sample(request):
    return HttpResponse(html_base + "<h1>Ejemplos</h1>")


Asociar a cada vista su correspondiente URL
--------------------------------------------

Después de crear las vistas es necesario establecer en Django las URL en las que se mostrará el código html. 

Para ello, una vez creada las vistas abrir el archivo urls.py que se encuentra en la carpeta webempresa/webempresa y añadir la siguiente línea de import para importar la app core (debajo las líneas de import existentes):

from core import views

(Este comando importa de la app core su archivo views.py)

Después, añadiremos las url a la lista de patrones de urls llamada urlpatterns:

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('store/', views.store, name='store'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('sample/', views.sample, name='sample'),
    path('admin/', admin.site.urls),
]

Finalmente, después de guardar probaremos el resultado:
source py36/bin/activate
cd webempresa
python3 manage.py runserver


Optimizando la definición de las URLs
--------------------------------------

Es posible optimizar las declaraciones de las URLs creando dentro de cada aplicación un archivo 'urls.py' únicamente con las definiciones de cada app.

Por ejemplo, en la app 'core' podemos crear un archivo 'url.py' con el siguiente contenido:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('store/', views.store, name='store'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('sample/', views.sample, name='sample'),
]

Básicamente, lo que se ha hecho es importar las vistas de la app y declarar únicamente las URL de dicha app, descartándose en este caso la URL que hace referencia al panel de administración ya que esa se mantendrá en el archivo 'urls.py' del proyecto.

En el archivo 'urls.py' del proyecto se eliminará el import de las vistas de 'core'; en el import 'django.urls' se añadirá la función 'include' que se usará en la lista 'urlpatters' para incluir las rutas declaradas en el archivo 'urls.py' de la app 'core':

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]

Fusionando el frontend con el backend
======================================

Crear en la carpeta 'webempresa/core' las siguientes carpetas:

- templates
- templates/core
- static
- static/core

Del frontend copiar los archivos .HTML a la carpeta 'templates/core' y las carpetas 'css', 'img' y 'vendor' a la carpeta 'static/core'.

Renombrar el archivo 'index.html' del template por 'home.html' para que se llame igual que su vista.

Agregar la app 'core' a la lista INSTALLED_APPS del archivo 'settings.py':

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

Incorporar el renderizado de los templates
-------------------------------------------

En lugar de la función HttpResponse() utilizar la función render() para renderizar los templates en el archivo 'views.py de la app 'core':

from django.shortcuts import render

html_base = """<h2>L'autentico caffè d'italia</h2>
<h1>La Caffettiera</h1>
<ul>
    <li><a href='/'>INICIO</a></li>
    <li><a href='/about/'>HISTORIA</a></li>
    <li><a href='/services/'>SERVICIOS</a></li>
    <li><a href='/store/'>VISITANOS</a></li>
    <li><a href='/contact/'>CONTACTO</a></li>
    <li><a href='/blog/'>BLOG</a></li>
</ul>"""

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def store(request):
    return render(request, 'core/store.html')

def contact(request):
    return render(request, 'core/contact.html')

def blog(request):
    return render(request, 'core/blog.html')

def sample(request):
    return render(request, 'core/sample.html')


Cargar archivos estáticos en 'home.html' y sustituir referencias
-----------------------------------------------------------------

Se trata de incorporar en el 'home.html' después del título la etiqueta de plantilla {% load static %} y sustituir todas las referencias a archivos estáticos (imágenes, .css y .jsp) con la etiqueta de platilla {% static 'core/ruta/archivo' %}.

Como el archivo 'home.html' tiene una parte común con el resto de plantillas renombrar 'home.html' como 'base.html' para que esa parte podamos incorporarla con una etiqueta de bloque en el resto de plantillas y asimismo eliminar el código redundante del resto.

En 'base.html' incluir un bloque para el título para que aparezca junto al nombre de la empresa el nombre de la página cargada:

    <title>{% block title %}{% endblock %} | La Caffettiera</title>

En 'base.html' suprimir los apartados de la 'Cabecera' y del 'Mensaje' e insertar en su lugar la etiqueta de template de bloque:

    <!-- Contenido -->
    {% block content %}{% endblock %}

En 'home.html' suprimir todos los apartados excepto los de la 'Cabecera' y del 'Mensaje' que son los que NO se repiten en todos los templates. 

(En 'home.html' solo aparecerán las secciones 'Cabecera' y 'Mensaje'; el resto de código por encima y por debajo debe ser eliminado)

Agregar al comienzo de 'home.html' la etiqueta para extender el archivo 'base.html' y la etiqueta de carga de archivo estático; un bloque para el título de la página e incluir la secciones 'Cabecera' y 'Mensaje' dentro un bloque llamado 'content':

{% extends 'core/base.html' %}
{% load static %}

{% block title %}Inicio{% endblock %}

{% block content %}
<!-- Cabecera -->
<section class="page-section clearfix">
  ...
</section>

<!-- Mensaje -->
<section class="page-section cta">
  ...
</section>
{% endblock %}

En 'base.html' en la sección del panel de 'Navegación' sustituir las referencias a páginas .html por las etiquetas de template url: {% url 'nombre-url' %}

A continuación, habría que repetir todo lo hecho en la plantilla 'home.html' en el resto de plantillas.

Cambiar el color de resaltado en el menú de navegación
--------------------------------------------------------

En 'base.html' en la lista html '<li>' del panel de navegación tiene la clase 'nav-item' que 'activa' el color naranja en la opción de inicio. Como este bloque queremos que sea común para todas las páginas incluiremos la siguiente etiqueta condicional de plantilla que activará el color de la opción en la página que esté cargada: '{% if request.path == '/' %}active{% endif %}' indicando en el 'path' el nombre de cada página:

<div class="collapse navbar-collapse" id="navbarResponsive">
    <ul class="navbar-nav mx-auto">
    <li class="nav-item px-lg-4 {% if request.path == '/' %}active{% endif %}">
        <a class="nav-link text-uppercase text-expanded" href="{% url 'home' %}">Inicio</a>
    </li>
    <li class="nav-item px-lg-4 {% if request.path == '/about/' %}active{% endif %}">
        <a class="nav-link text-uppercase text-expanded" href="{% url 'about' %}">Historia</a>
    </li>
    <li class="nav-item px-lg-4 {% if request.path == '/services/' %}active{% endif %}">
        <a class="nav-link text-uppercase text-expanded" href="{% url 'services' %}">Servicios</a>
    </li>
    <li class="nav-item px-lg-4 {% if request.path == '/store/' %}active{% endif %}">
        <a class="nav-link text-uppercase text-expanded" href="{% url 'store' %}">Visítanos</a>
    </li>
    <li class="nav-item px-lg-4 {% if request.path == '/contact/' %}active{% endif %}">
        <a class="nav-link text-uppercase text-expanded" href="{% url 'contact' %}">Contacto</a>
    </li>
    <li class="nav-item px-lg-4">
        <a class="nav-link text-uppercase text-expanded" href="{% url 'blog' %}">Blog</a>
    </li>
    </ul>
</div>


Configurar proyecto para que archivos media funcionen en desarrollo
--------------------------------------------------------------------

1) Ir a la carpeta raíz del proyecto y crear carpeta llamada 'media'.

2) Editar el archivo 'settings.py' y agregar al final la configuración:

# Media config
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

3) Editar el archivo 'urls.py' y agregar al comienzo el 'import' siguiente:

from django.conf import settings

4) En el mismo archivo 'urls.py' agregar al final:

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Crear la app 'services'
------------------------

1) Crear la app 'services' con el proyecto detenido:

python3 manage.py startapp services

2) Editar 'settings.py' y agregar la nueva app a la lista de aplicaciones instaladas:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'services',
]

Crear el modelo para la app 'services'
--------------------------------------

1) Editar el archivo 'models.py' de la app y agregar la clase del modelo:

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to='services')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha edición')

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created']
    
    def __str__(self):
        return self.title

2) Crear una migración completa y aplicarla ejecutando los comandos siguiente en la carpeta del proyecto:

python3 manage.py makemigrations
python3 manage.py migrate

3) Crear superusuario para el panel de administración del proyecto:

python3 manage.py createsuperuser

Nombre de usuario (leave blank to use 'antonio'):
Dirección de correo electrónico: pherkad13@gmail.com
Password: django1234
Password (again): django1234
Superuser created successfully.

4) Para que el modelo de la app 'services' sea accesible desde el panel de administrador editar el archivo 'admin.py' de la app y añadir un nuevo 'import' que importe el modelo, una nueva clase de administración básica estableciendo que los campos 'created' y 'updated' sean de lectura; y al final se registrará dicho modelo con su configuración:

from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)

5) Para traducir el nombre de la app 'services' en el panel de administración editar el archivo 'apps.py' y añadir la variable 'verbose_name' con el nuevo nombre a la clase de configuración:

from django.apps import AppConfig


class ServicesConfig(AppConfig):
    name = 'services'
    verbose_name = 'Gestor de Servicios'

6) Editar el archivo 'settigs.py' y en la variable de Aplicacionmes Instaladas sustituir el nombre de la app 'services' por 'services.apps.ServicesConfig' para que se cargue la configuración extendida de la app.

7) Iniciar el proyecto y acceder al panel de administración

python3 manage.py runserver

Acceder a la URL http://127.0.0.1:8000/admin


Crear vista y plantilla de la app 'services'
--------------------------------------------------- 

1) Crear carpeta 'templates/services' en la app 'services'.

2) Mover la plantilla 'services.html' de 'core/templates/core' a la carpeta 'services/templates/services'.

3) Trasladar la vista del fichero 'views.py' de la app 'core' (cortando el código y reescribiendo el path a la plantilla) al archivo 'views.py' de la app 'services':

def services(request):
    return render(request, 'services/services.html')

4) Cortar en el archivo 'urls.py' de 'core' el path que hace referencia a 'services'.

5) Crear el archivo 'urls.py' de 'services' con el path que hace referencia a 'services':

from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
]

6) Configurar para que se cargue la URL anterior en el archivo 'urls.py' global o del proyecto que se encuentra en 'webempresa/wepempresa', añadiendo a la lista de la variable 'urlpatterns' el path de 'services':

urlpatterns = [
    path('', include('core.urls')),
    path('services/', include('services.urls')),    
    path('admin/', admin.site.urls),
]

Fusionar el modelo 'services' con el template 'services.html'
--------------------------------------------------------------

Básicamente, se trata de hacer que el template muestre los registros de la tabla de servicios en vez de la información de ejemplo del frontend.

1) En el archivo 'views.py' de la app 'services' añadir el 'import' del modelo 'Service', declarar una variable que guarde todos los objetos en la clase y se enviará la variable en un diccionario de contexto en render():

from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services':services})

2) Editar el template 'services.html' y agregar el bucle que inserte los registros del modelo borrando primero dos de las tres secciones (que se utilizan para mostrar la información de ejemplo) y a continuación insertar los campos en los lugares que correspondan:

{% extends 'core/base.html' %}

{% load static %}

{% block title %}Servicios{% endblock %}

{% block content %}
  {% for service in services reversed %}
    <section class="page-section">
      <div class="container">
        <div class="product-item">
          <div class="product-item-title d-flex">
            <div class="bg-faded p-5 d-flex mr-auto rounded">
              <h2 class="section-heading mb-0">
                <span class="section-heading-upper">{{service.subtitle}}</span>
                <span class="section-heading-lower">{{service.title}}</span>
              </h2>
            </div>
          </div>
          <img class="product-item-img mx-auto d-flex rounded img-fluid mb-3 mb-lg-0" src="{{service.image.url}}" alt="">
          <div class="product-item-description d-flex ml-auto">
            <div class="bg-faded p-5 rounded">
              <p class="mb-0">{{service.content}}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  {% endfor %}
{% endblock %}


Crear la app 'Blog'
===================

1) Iniciar entorno virtual:

source bin/activate

2) Crear la app blog:

cd webempresa
python3 manage.py startapp blog

3) Editar el archivo 'models.py' y crear los modelos siguientes:

from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha edición')

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['-created']
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha publicación', default=now)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categorías')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha edición')

    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ['-created']
    
    def __str__(self):
        return self.title

4) Agregar la app 'blog' a la lista 'INSTALLED_APP' de 'settings.py'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'core',
    'services.apps.ServicesConfig',
]

5) Preparar migraciones:

python3 manage.py makemigrations blog

6) Aplicar migraciones:

python3 manage.py migrate blog

7) Editar 'admin.py' de la app 'blog' y agregar el 'import' de los modelos 'Category' y 'Post', las clases de administración y los métodos de registro:

from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

8) Iniciar el servidor:

python3 manage.py runserver

9) Acceder al panel del administrador:

http://127.0.0.1:8000/admin

10) Agregar categorías: General, Ofertas

11) Agregar entrada de ejemplo usando las dos categorías anteriores


Personalizar el panel de administración
========================================

Editar 'admin.py' de la app 'blog' y añadir a las clases los atributos siguientes según convengan:

1) Para mostrar en la vista inicial varias columnas:

list_display = ('title', 'author', 'published')

2) Para mostrar en la vista inicial criterios de ordenación:

ordering = ('author', 'published')

3) Para agregar un buscador:

search_fields = ('title', 'author__username', 'categories__name')

4) Ofrecer la posibilidad de acceder por jerarquía de fechas:

date_hierarchy = 'published'

5) Para agregar uno o más filtros:

list_filter = ('author__username', 'categories__name')

6) Para añadir un campo calculado agregar un método a la clase correspondiente:

def post_categories(self, obj):
    return ", ".join([c.name for c in obj.categories.all().order_by('name')])

# Para agregar un nombre corto al método anterior para que se pueda incluir
# en la vista iniciar una columna con dicho nombre:
post_categories.short_description = 'Categorías'

# Para ello, además es necesario agregar dicho campo a 'list_display'
# list_display = ('title', 'author', 'published', 'post_categories')

# Opcionalmente, para añadir código HTML a uno de estos campos calculados:
from django.utils.safestring import mark_safe
def image(self, obj):
    return mark_safe('<image src="%s" />' % obj.image)


Crear vistas del blog
======================

1) Editar el archivo 'views.py' de la app 'core', cortar la vista 'blog' y moverla al archivo 'views.py' de la app 'blog', cambiando la ruta de render():

from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html')

2) Crear en la carpeta de la app 'blog' las carpetas 'templates' y 'templates/blog'.

3) Mover la plantilla 'blog.html' desde la app 'core' a la app 'blog', a su correspondiente carpeta de plantillas 'templates/blog'.

4) Crear un archivo 'urls.py' en la app 'blog' y copiar todo el contenido del archivo 'urls.py' de la app 'core', borrando todos los path excepto el de 'blog' y cambiando la ruta de este último para que apunte a la raíz (''):

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
]

5) Borrar en el archivo 'urls.py' de la app 'core' el path de 'blog'.

6) Editar el arhivo 'urls.py' del proyecto en 'webempresa/webempresa' y agregar el path de blog a la lista 'urlpatterns':

urlpatterns = [
    path('', include('core.urls')),
    path('services/', include('services.urls')),    
    path('blog/', include('blog.urls')),    
    path('admin/', admin.site.urls),
]

7) Guardar y comprobar que funciona.


Fusionar los modelos del 'blog' con los templates
==================================================

Básicamente, se trata de hacer que el template muestre los registros de la tabla de entradas del blog en vez de la información de ejemplo del frontend.

1) En el archivo 'views.py' de la app 'blog' añadir el 'import' del modelo 'Post', en la vista 'blog' declarar una variable que guarde todos los objetos entradas y devolver la variable en un diccionario de contexto con render():

from django.shortcuts import render
from .models import Post

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts':posts})

2) Editar el template 'blog.html' y agregar el bucle que inserte los registros del modelo en el bloque donde debe aparecer el contenido 'content' y a continuación insertar los campos en los lugares que correspondan con su formato:

{% extends 'core/base.html' %}

{% load static %}

{% block title %}Blog{% endblock %}

{% block content %}
  {% for post in posts %}
  <section class="page-section cta">
    <div class="container">
      <div class="row">
        <div class="col-xl-9 mx-auto">
          <div class="cta-innerv text-center rounded">
            <h2 class="section-heading mb-5">
              <span class="section-heading-upper">{{post.published|date:"SHORT_DATE_FORMAT"}}</span>
              <span class="section-heading-lower">{{post.title}}</span>
            </h2>
            <p class="mb-0">
              <img class="mx-auto d-flex rounded img-fluid mb-3 mb-lg-0" src="{{post.image.url}}" alt="">
            </p>
            <p class="mb-0 mbt">{{post.content|linebreaks}}</p>
            <p class="mb-0 mbt">
              <span class="section-heading-under">Publicado por <em><b>{{post.author}}</b></em> en 
              <!-- <em> <a href="#" class="link">General</a>, <a href="#" class="link">Ofertas</a></em> --> 
              {% for category in post.categories.all %}
                 {{category.name}}{% if not forloop.last %},{% endif %}
              {% endfor %}
              </span>
            </p>
          </div>

        </div>
      </div>
    </div>
  </section>
  {% endfor %}
{% endblock %}

3) En el archivo 'views.py' de la app 'blog' añadir el 'import' del modelo 'Category', definir la vista para las categorias con un argumento para el id de su identificador, declarar una variable que guarde una determinada categoría obtenida por su id con get() y devolver la variable en un diccionario de contexto con render():

from django.shortcuts import render
from .models import Post, Category

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts':posts})

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    return render(request, 'blog/category.html', {'category':category})

4) En el archivo 'urls.py' de la app 'blog' añadir el path para las categorías incluyendo el campo dinámico <category_id> como un número entero en la ruta:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<int:category_id>/', views.category, name='category'),
]

5) Crear el nuevo template 'category.html' en la app 'blog' a partir de una copia de 'blog.html'.

6) Probar que accediendo a la url http://127.0.0.1:8000/blog/category/1/ se carga la nueva plantilla 'category.html' aunque no muestre entradas. Si el id 1 que se ha pasado no existe se producirá un error "DoesNotExist". 

Lo recomendable en estos casos es mostrar el error típico 404. Para ello, en 'views.py' de la app blog cargar la función 'get_object_or_404' para usarla en lugar de 'get' en el import del módulo 'django.shortcuts' y sustituir get() por get_object_or_404() añadiendo un primer argumento con el nombre del modelo 'Category' para obtener la categoria que luego utilizaremos en un filtro para acceder a todas las entradas que la tengan:

from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts':posts})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(categories=category)
    return render(request, 'blog/category.html', {'category':category, 'posts':posts})

Este modo de acceder a las categorías es razonable pero con Django podemos utilizar consultar inversas.

Obtener categoría utilizando consultas inversas
------------------------------------------------

7) Editar 'views.py' de la app 'blog' en la vista de categorías suprimir la línea en la que se obtienen las entradas, quitar su clave 'posts' del diccionario de render(),

from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts':posts})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'blog/category.html', {'category':category})

8) Editar la plantilla 'category.html' y cambiar la etiqueta de plantilla 'for' que recorre las entradas por '{% for post in category.post_set.all %}'. Así ya funcionaría.

Otra mejora que facilita la lectura y compresión del código que puede hacerse es agregar en el modelo 'Post' el argumento 'related_name' en la definición del campo 'categories':

categories = models.ManyToManyField(Category, verbose_name='Categorías', related_name='get_posts')

Y cambiar después la etiqueta de plantilla 'for' en la plantilla 'category.html' por '{% for post in category.get_posts.all %}'.


Agregar enlaces a la categorías de las entradas
------------------------------------------------

9) Acceder a la parte final del código de la plantilla 'category.html' y cambiar el código:

<!-- <em> <a href="#" class="link">General</a>, <a href="#" class="link">Ofertas</a></em> -->
{% for category in post.categories.all %}
    {{category.name}}{% if not forloop.last %},{% endif %}
{% endfor %}

por:

<em>
{% for category in post.categories.all %}
    <a href="{% url 'category' category.id %}" class="link">{{category.name}}</a>{% if not forloop.last %},{% endif %}
{% endfor %}
</em>

10) Realizar el mismo cambio anterior en la plantilla 'blog.html'.


Crear app 'social'
===================

Permite configurar las redes sociales vinculadas con la web

1) Crear app 'social':

python3 manage.py startapp social

2) Crear el modelo 'Link':

from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name='Nombre clave', max_length=100, unique=True)
    name = models. CharField(verbose_name='Red social', max_length=200)
    url = models.URLField(verbose_name='Enlace', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha edición')

    class Meta:
        verbose_name = 'enlace'
        verbose_name_plural = 'enlaces'
        ordering = ['name']
    
    def __str__(self):
        return self.name

3) Editar 'apps.py' y agregar a la clase 'SocialConfig' el atributo 'verbose_name' con el texto 'Redes sociales':

from django.apps import AppConfig


class SocialConfig(AppConfig):
    name = 'social'
    verbose_name = 'Redes sociales'

4) Editar 'settings.py' y agregar la app a la lista INSTALLED_APPS utilizando la configuración extendida:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'core',
    'services.apps.ServicesConfig',
    'social.apps.SocialConfig',
]

5) Crear y aplicar migraciones

python3 manage.py makemigrations social
python3 manage.py migrate social

6) Editar 'admin.py' de la app para importar el modelo 'Link' y agregar la clase 'LinkAdmin' estableciendo como campos de solo lectura 'created' y 'updated':

from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Link, LinkAdmin)

7) Ejecutar proyecto, acceder a panel de administración y agregar tres enlaces para Twitter, Facebook e Instagram:

pytho3 manage.py runserver
http://127.0.0.1:8000/admin


Recuperar los enlaces sociales para que aparezcan en todas las páginas
-----------------------------------------------------------------------

(Utilizando procesadores de contexto)

1) Crear archivo 'processors.py' en la app social con el siguiente contenido:

from .models import Link

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx

El ejemplo define una función que crea un diccionario 'ctx' con los enlaces que existan en la tabla del modelo 'Link'-

2) Editar 'settings.py' y agregar a la lista TEMPLATES, a su diccionario 'context_processors' el procesador de contexto creado con anterioridad 'social.processors.ctx_dict':

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.processors.ctx_dict',
            ],
        },
    },
]

Ahora el diccionario se inyectará en el contexto global permitiendo acceder a sus claves desde cualquier template. 

3) Insertar las claves de los enlaces en el código de 'base.html' del pie de página para que se muestren sus valores en todas las plantillas:

      <!-- Pié de página -->
    <footer class="footer text-faded text-center py-5">
      <div class="container">
        <p class="m-0">
          {% if LINK_TWITTER %}
            <a href="{{LINK_TWITTER}}" class="link">
              <span class="fa-stack fa-lg">
                <i class="fa fa-circle fa-stack-2x"></i>
                <i class="fa fa-twitter fa-stack-1x fa-inverse"></i>
              </span>
            </a>
          {% endif %}
          {% if LINK_FACEBOOK %}
            <a href="{{LINK_FACEBOOK}}" class="link">
              <span class="fa-stack fa-lg">
                <i class="fa fa-circle fa-stack-2x"></i>
                <i class="fa fa-facebook fa-stack-1x fa-inverse"></i>
              </span>
            </a>
          {% endif %}
          {% if LINK_INSTAGRAM %}
            <a href="{{LINK_INSTAGRAM}}" class="link">
              <span class="fa-stack fa-lg">
                <i class="fa fa-circle fa-stack-2x"></i>
                <i class="fa fa-instagram fa-stack-1x fa-inverse"></i>
              </span>
            </a>
          {% endif %}
	    </p>
        <p class="m-0 mbt">
        	<a href="sample.html" class="link">Política de privacidad</a> ·
        	<a href="sample.html" class="link">Aviso legal</a> ·
        	<a href="sample.html" class="link">Cookies</a>
		</p>
        <p class="m-0 mbt1">&copy; La Caffettiera 2018</p>
      </div>
	</footer>


Crear app 'Pages'
==================

Para gestionar páginas secundarias: políticas de privacidad, aviso legal, etc.

1) Crear app:

python3 manage.py startapp pages

2) En 'apps.py' agregar un nombre de app personalizado:

from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = 'pages'
    verbose_name = 'Gestor de páginas'

3) En 'settings.py' añadir la app a INSTALLED_APPS:

'pages.apps.PagesConfig',


4) En 'models.py' agregar el modelo 'Page':

from django.db import models

# Create your models here.
class Page(models.Model):
    title = models. CharField(verbose_name='Título', max_length=200)
    content = models.TextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha edición')

    class Meta:
        verbose_name = 'página'
        verbose_name_plural = 'páginas'
        ordering = ['title']
    
    def __str__(self):
        return self.title

5) Editar 'admin.py' y agregar el 'import' del modelo 'Page', la clase de administración y el método de registro:

from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Page, PageAdmin)

6) Preparar migraciones de 'Page' y aplicarlas.

python3 manage.py makemigrations pages
python3 manage.py migrate pages

7) Iniciar proyecto y acceder a panel de administración:

python3 manage.py runserver
http://127.0.0.1:8000/admin

8) Agregar tres registros a la tabla 'Pages': aviso legal, cookies y política de privacidad.

9) Editar 'views.py':

rom django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.
def page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/sample.html', {'page':page})

10) Crear en la carpeta de la app las carpetas 'templates' y 'templates/pages'.

11) Mover el template 'sample.html' de la app 'core' a la app 'pages'

12) Suprimir de 'views.py' de la app 'core' la vista 'sample'.

13) Suprimir de 'urls.py' de la app 'core' el path de 'sample'.

15) Crear 'urls.py' en la app 'pages':

from django.urls import path
from . import views

urlpatterns = [
    path('<int:page_id>/', views.page, name='page'),
]

16) Editar 'urls.py' del proyecto y agregar el path de la app a la lista 'urlpatters':

path('page/', include('pages.urls')),    

17) Insertar los campos en la plantilla 'sample.html':
{% extends 'core/base.html' %}

{% load static %}

{% block title %}Muestra{% endblock %}

{% block content %}
<section class="page-section about-heading">
  <div class="container">
    <div class="about-heading-content mbtm">
      <div class="row">
        <div class="col-xl-9 col-lg-10 mx-auto">
          <div class="bg-faded rounded p-5 forced">
            <h2 class="section-heading mb-4">
              <span class="section-heading-lower">{{page.title}}</span>
            </h2>
            <div class="section-content">{{page.content|linebreaks}}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
{% endblock %}

Modificar los enlaces utilizando Template Tags personalizados. 
------------------------------------------------------------

18) Crear directorio 'templatetags' en la carpeta de la app 'pages'.
    
19) Crear archivo '__init__.py' en la carpeta anterior para indicar a Django que se trata de un paquete.

20) Crear archivo 'pages_extras.py' en la carpeta anterior con el siguiente contenido:

from django import template
from pages.models import Page

register = template.Library()

@register.simple_tag
def get_pages_list():
    pages = Page.objects.all()
    return pages

21) Reiniciar el servidor de desarrollo
    
22) Editar 'base.html' y comentar el código html donde se encuentran los enlaces de "Política de privacidad", "Aviso legal" y "Cookies" e incluir el  código que sigue que reconstruye los enlaces con la información que se obtiene de la base de datos:

<!-- <a href="sample.html" class="link">Política de privacidad</a> ·
<a href="sample.html" class="link">Aviso legal</a> ·
<a href="sample.html" class="link">Cookies</a> -->
{% load pages_extras %}
{% get_pages_list as pages_list %}
{% for page in pages_list %}
    <a href="{% url 'page' page.id page.title|slugify %}" class="link">{{page.title}}</a> {% if not foorloop.last %}·{% endif %}
{% endfor %}

23) Editar 'urls.py' de la app 'pages' y cambiar el path actual por el siguiente:

path('<int:page_id>/<slug:page_slug>', views.page, name='page'),

24) Editar 'views.py' de la app 'pages' y agregar el argumento 'page_slug' a la vista 'page':

def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/sample.html', {'page':page})

(Sin el argumento 'page.title|slugify' también funcionaría pero en lugar de mostrar un path inteligible se mostrarían solo los 'id' (1,2 y 3) de las urls. Para que funcione quitando dicho argumento habría que recortar en 'urls.py' el path quitando del mismo la parte final '<slug:page_slug>' y suprimir el tercer argumento 'page_slug' de la vista 'page' en 'views.py'. Es otra opción menos vistosa pero funciona igualmente).

25) Detener servidor y reiniciar proyecto.


Ordenación los enlaces a conveniencia
========================================

Los enlaces de la práctica anterior son leídos de la base de datos en el orden del campo 'title'.
Es posible que alguna vez sea necesario establecer un orden que incluso pueda cambiar con el tiempo. Para contar con cierta flexibilidad modificadar el modelo 'pages' y realizar los siguientes cambios:

1) Editar 'models.py' de la app 'pages' y añadir el siguiente campo después de 'content' en el modelo 'Page':

order = models.SmallIntegerField(verbose_name='Orden', default=0)

2) En la clase Meta añadir a lista 'ordering' el campo 'order' como primer elemento por el que hay que ordenar:

ordering = ['order', 'title']

3) A continuación, preparar y aplicar migraciones

python3 manage.py makemigrations pages
python3 manage.py migrate pages

4) Editar 'admin.py' de la app 'pages' y añadir a la clase 'PageAdmin' el atributo 'list_display' con la lista de campos a mostrar en la vista previa del modelo en el panel de administración.

5) Acceder al panel de administración:

python3 manage.py runserver
http://127.0.0.1:8000/admin

6) Cambiar el orden asignando los siguientes valores a los enlaces: Política de Privacidad (0), Cookies (1) y Aviso Legal (2). 

7) Recargar cualquier página para comprobar que ahora los enlaces de las páginas secundarias aparecen en el nuevo orden establecido.


Edición directa de páginas
========================

Esta práctica consiste en incorporar en una página un enlace "Editar" en el caso que un usuario este logado para que pueda modificar su contenido accediendo directamente al panel de administración.

En 'settings.py' en la lista 'TEMPLATES' en la lista de procesadores de contexto 'context_proccesors' aparece por defecto 'django.contrib.auth.context_proccesors.auth' que permite acceder desde las plantillas a informacion de los usuarios y de las sesiones activas del proyecto.

Por ejemplo, la etiqueta {{user}} muestra el nombre del usuario que esté logado (o bien 'AnonymousUser' si no hay ninguno). Y con {% if user.is_authenticated %}{% endif %} es posible comprobrar si un usuario está logado. 

Para incorporar un enlace "Editar" en las páginas secundarias:

1) Editar 'sample.html' de la app 'pages' y después de la etiqueta {{page.content|linebreaks}} que muestra el texto de la página añadir el siguiente código:

{% if user.is_authenticated %}
<p>
<a href="{% url 'admin:pages_page_change' page.id %}">Editar</a>
</p>
{% endif %}

(La url se forma co 'admin:' que hace referencia al panel de administración seguido de la app 'pages_', seguido del modelo 'page_' y seguido en este caso de la acción 'change'. Hay otras acciones como 'add' para añadir registros y 'delete0 para borrar registros).

Más info: <https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#reversing-admin-urls>

Personalizando el panel de administrador
====================================

Añadir editor wysiwyg a los campos de texto:

1) Instalar Djando CKEditor

pip3 install django-ckeditor

(Si es necesario actualizar en entorno virtual 'setuptools' y 'wheel': pip3 install --upgrade setuptools wheel)

2) Una vez instalado editar 'settings.py' y agregar la aplicación a la lista de aplicaciones instaladas 'INSTALLED_APPS': ckeditor

3) Editar el archivo 'models.py' de la app 'pages' y añadir el import de ckeditor y sustituir el tipo del campo 'content' que es 'models.TextField' por el nuevo tipo importado 'RichTextField':
   
from ckeditor.fields import RichTextField
...
...
content = RichTextField(verbose_name='Contenido')

3) Preparar y aplicar migraciones:

python3 manage.py makemigrations pages
python3 manage.py migrate pages

4) Poner el servidor en marcha, acceder al proyecto y editar algún registro para comprobar que la caja de 'content' incorpora la barra de edición de ckeditor:

python3 manage.py runserver

5) Para redefinir la barra de edición de ckeditor editar 'settings.py' e ir al final del archivo e incluir el siguiente código:

# ckeditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Basic',
    }
}

(En este caso se utilizará la barra básica con tres botones. Si en vez de 'Basic' se asigna None se mostrarán  todas las opciones de ckeditor).

También, se puede definir la barra a gusto del desarrollador. 

6) Cambiar la configuración actual por la siguiente:

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink']
        ]
    }
}

Si ahora aplicamos formatos Django en vez de aplicar mostrará el código HTML de cada formato. 

7) Para que el código HTML sea interpretado editar la plantilla 'sample.html' y sustituir la etiqueta             {{page.content|linebreaks}} por {{page.content|safe}} para que se considere el contenido como seguro. 


Crear app 'contact'
==================

Preparar la app
----------------------------

1) Crear app 'contact'

python3 manage.py startapp contact

2) Mover vista 'contact' de 'views.py' de la app 'core' a 'views.py' de la app 'contact':

3) Copiar el archivo 'urls.py' de la app 'core' a la app 'conctact'.

4) Editar el archivo 'urls.py' de la app 'core' y borrar el path de la vista 'contact'.

5) Editar el archivo 'urls.py' de la app 'contact', borrar todos los path excepto el de la vista 'contact' y modificar la ruta:

path('', views.contact, name='contact'),
   
6) Editar el archivo 'urls.py' global de la carpeta 'webempresa' y agregar a la lista 'urlpatterns' el path de 'urls.py' de 'contact':

path('contact/', include('contact.urls')),        

7) Editar 'settings.py' y añadir a INSTALLED_APPS la app 'contact'.

8) Trasladar el template 'contact.html' de la app 'core' a la app 'contact'.

9) Iniciar el proyecto:

python3 manage.py runserver


Crear formulario
------------------------------

1) Crear archivo 'forms.py' en la carpeta de la app 'contact' con el siguiente código:

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True)
    email = forms.EmailField(label='Email', required=True)
    content = forms.CharField(label='Contenido', 
                              required=True,
                              widget=forms.Textarea)

2) Editar la plantilla 'contact.html' y comentar todo el código HTML del formulario.

<!-- Formulario de contacto -->
    <!--
    <form>
    ...
    ...
    </form>
    -->
<!-- Fin formulario de contacto -->

3) Editar el archivo 'views.py' de la app 'contact' y agregar el import del formulario creado en el paso 1), instanciarlo dentro del método 'contact' y enviarlo en render() en un diccionario de contexto:
   
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    return render(request, 'contact/contact.html', {'form':contact_form})

4) Editar la plantilla 'contact.html' y agregar la etiqueta de plantilla '<table>{{form.as_table}}</table>' después del encabezado del formulario para que se interprete el nuevo formulario.

<!-- Formulario de contacto -->
    <table>{{form.as_table}}</table>
    <!--
    <form>
    ...
    ...
    </form>
    -->
<!-- Fin formulario de contacto -->

Un formulario se puede presentar de varios modos:

- {{form}}: campos en la misma línea
- {{form.as_p}}: campos en líneas diferentes
- <ul>{{form.as_ul}}</ul>: campos como una lista
- <table>{{form.as_table}}</table>: campos como una tabla

5) Ejecutar proyecto, acceder al formulario y comprobar que:

- No se muestra ningún botón para enviar los datos del formulario.
- Y si se edita el código de la página las etiquetas típicas de un formulario HTML (<form></form>) no se incluyen.


Procesado y validación
-----------------------------------------

1) Editar 'contact.html' y terminar el formulario incluyendo las etiquetas <form></form>:

<!-- Formulario de contacto -->
    <form action="" method="POST">
    {% csrf_token %}
    <table>{{form.as_table}}</table>
    <input type="submit" value="Enviar" />
    </form>
    <!--
    <form>
    ...
    ...
    </form>
    -->
<!-- Fin formulario de contacto -->

Métodos de envío: 'GET' hace visible la URL con los datos de envío en la barra de dirección mientras que 'POST' los oculta.

La etiqueta {% csrf_token %} permite habilitar el token csfr mediante un campo oculto (ver código fuente) que evita el envío del formulario desde páginas externas al proyecto.

Ejemplo de campo oculto:
<input type='hidden' name='csrfmiddlewaretoken' value='I78NxWBhCnrKqFtjlzYd7E9eJS0GWijV7KwC7pkxLR6lruZA1xWiPqrUv35NDE9w' />

El formulario ya funciona y hace una validación básica.

Ver: {{request.POST}} en template y request.method en vista

2) Editar 'views.py' de app contact y agregar import redirect y reverse, control de método de envío y rellenar plantilla con información enviada en caso de que sea "POST" y, si todo hay ido bien, redireccionar para mostrar mensaje informativo al usuario haciendo uso de la misma plantilla:
   
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
           name = request.POST.get('name')
           email = request.POST.get('email')
           content = request.POST.get('content')
           # suponemos que todo ha ido bien
           return redirect(reverse('contact')+'?ok')

    return render(request, 'contact/contact.html', {'form':contact_form})

1) Editar 'contact.html' y delante del formulario incluir el siguiente código que mostrará un mensaje cuando se realice un envío:

{% if 'ok' in request.GET %}
    <p><b>Su mensaje se ha enviado correctamente</b></p>
{% endif %}

Fusionando el formulario
---------------------------------------------

El formulario que genera Django no es tan vistoso como el del front-end. A continuación, se realiza la fusión del formulario que genera Django con los formatos y estilos del propio front-end:

1) Editar la plantilla 'contact.html' y comentar el formulario de django y descomentar el formulario que proporcionaba el front-end.

<!-- Formulario de contacto -->            
{% if 'ok' in request.GET %}
    <p><b>Su mensaje se ha enviado correctamente</b></p>
{% endif %}
<!--
<form action="" method="POST">
{% csrf_token %}
<table>{{form.as_table}}</table>
<input type="submit" value="Enviar" />
</form>
-->            
<form>
    <div class="form-group">
        <label>Nombre *</label>
        <div class="input-group">
            <input type="text" class="form-control">
        </div>
    </div>
    <div class="form-group">
        <label>Email *</label>
        <div class="input-group">
            <input type="text" class="form-control">
        </div>
        <ul class="errorlist">
            <li>El email no es correcto.</li>
        </ul>
    </div>
    <div class="form-group">
        <label>Mensaje *</label>
        <div class="input-group">
            <textarea class="form-control"></textarea>
        </div>
    </div>
    <div class="text-center">
        <input type="submit" class="btn btn-primary btn-block py-2" value="Enviar">
    </div>
</form>            
<!-- Fin formulario de contacto -->

2) Trasladar del formulario de Django al de front-end la acción y el método del formulario, la etiqueta '{% csrf_token %}' y comentar el siguiente código mensaje de error de ejemplo por no ser necesario:

<!--
<ul class="errorlist">
    <li>El email no es correcto.</li>
</ul>
-->

3) Sustituir 'input' y 'textarea' del formulario del front-end por las etiquetas de los campos del formulario generado por django '{{form.name}}', '{{form.email}}' y {{form.content}}; incluir las etiquetas de control de errores para cada campo {{form.name.errors}}, {{form.email.errors}} y {{form.contact.errors}} situándolas debajo de cada división 'input-group' (estas etiquetas de errores generan listas como la del error comentado en el paso anterior para mostrar los mensajes) y, por último, borrar todo el código comentado en la plantilla:
   
<!-- Formulario de contacto -->            
{% if 'ok' in request.GET %}
    <p><b>Su mensaje se ha enviado correctamente</b></p>
{% endif %}       
<form action="" method="POST">
{% csrf_token %}
    <div class="form-group">
        <label>Nombre *</label>
        <div class="input-group">
            {{form.name}}
        </div>
        {{form.name.errors}}
    </div>
    <div class="form-group">
        <label>Email *</label>
        <div class="input-group">
            {{form.email}}
        </div>
        {{form.email.errors}}
    </div>
    <div class="form-group">
        <label>Mensaje *</label>
        <div class="input-group">
            {{form.content}}
        </div>
        {{form.content.errors}}
    </div>
    <div class="text-center">
        <input type="submit" class="btn btn-primary btn-block py-2" value="Enviar">
    </div>
</form>            
<!-- Fin formulario de contacto -->

El nuevo formulario funciona bien pero la apariencia difiere del que proporciona el front-end que ajusta a ambos márganes las cajas de texto y redondea sus aristas. 

4) Editar 'forms.py' y añadir el argumento 'widget' a cada campo extendiendo cada objeto con el correspondiente control de entrada y con el diccionario de claves que serán incluídas en el código HTML, en este caso, con la clave 'class' con el valor 'form-control' y otros atributos que ajustan el diseño de las entradas al front-end:

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', 
            required=True,
            min_length=3,
            max_length=100,
            widget=forms.TextInput(attrs={'class':'form-control',
             'placeholder':'Escribe nombre'}))
    email = forms.EmailField(label='Email',
            required=True,
            min_length=3,
            max_length=100,
            widget=forms.EmailInput(attrs={'class':'form-control',
             'placeholder':'Escribe correo'}))
    content = forms.CharField(label='Contenido', 
            required=True,                              
            min_length=3,
            max_length=300,
            widget=forms.Textarea(attrs={'class':'form-control',
            'rows':3,
            'placeholder':'Escribe mensaje'}))

Configurando envío por correo 
-----------------------------------------------------

1) Crear una cuenta en Mailtrap utilizando una dirección de correo (p.e. gmail) y acceder a "Demo Inbox" para conocer las credenciales. En este caso seleccionar en la lista de "Integrations" la opción "Django" y copiar la configuración que tendremos que añadir al final del archivo 'settings.py':

EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = '7ec63ec7601a72'
EMAIL_HOST_PASSWORD = '9f8272826f14fe'
EMAIL_PORT = '2525'

1) Editar 'views.py' de la app 'contact' y añadir import y código para construir y enviar mensajes:

from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()   
    if request.method == "POST":
            contact_form = ContactForm(data=request.POST)
            if contact_form.is_valid():
                name = request.POST.get('name')
                email = request.POST.get('email')
                content = request.POST.get('content')
                # Enviamos el correo y redireccionamos
                email = EmailMessage("La Caffettiera: nuevo mensaje",
                                     "De {} <{}>\n\n{}".format(name, email, content),
                                     "no-contestar@inbolx.mailtrap.io",
                                     ["asuajim@gmail.com"],
                                     reply_to=[email])
                try:
                        email.send()
                        return redirect(reverse('contact')+'?ok')
                except:
                        pass
                        # Algo no ha ido bien, redireccionamos a FAIL
                        # return redirect(reverse('contact')+'?fail')
    return render(request, 'contact/contact.html', {'form':contact_form})


Personalizando el panel de administración
===========================================

Grupos y Permisos
-------------------

1) Acceder al panel de administración del proyecto, crear un grupo llamado 'Personal' y asignar todos los permisos para gestionar las app 'blog', 'pages' y 'services'. Para la app 'social' sólo será posible el permiso 'Can change enlace'. 

2) Crear un usuario de pruebas llamado 'test' con la contraseña 'django5678' como 'activo', 'de staff' y asignado al grupo anterior 'Personal'.

3) Iniciar sesión con el usuario 'test' y comprobar que las acciones que puede realizar se corresponden con los permisos asignados.

Establecer campos de sólo lectura en tiempo de ejecución
---------------------------------------------------------

En la tabla 'social' el usuario 'test' puede modificar la información de todos los campos excepto 'created' y 'updated'. 

Para impedir que pueda modificar además los campos 'key' y 'name' editar el archivo 'admin.py' de la app 'social' y definir en la clase existente el método 'get_readonly_fields':

from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
            return ('created', 'updated', 'key', 'name')
        else:
            return ('created', 'updated')

admin.site.register(Link, LinkAdmin)

Si admeás quisieramos omitir la visualización de los campos 'created' y 'updated' al usuario 'test' el método en lugar de devolver:

return ('created', 'updated', 'key', 'name')

debe devolver:

return ('key', 'name')

