Instalar Django con Miniconda en Linux en entorno virtual
==========================================================

Chuleta de comandos en GNU/Linux

# Consultar la versión de Python por defecto
python -V

# Instalar un script bash del directorio actual
sh ./script.sh

# Inyectar la nueva configuración en el .bashrc
source ~/.bashrc

# Crear entorno Conda vacío con Python 3.6
conda create -n py36 python=3.6

# Activar el entorno virtual
source activate py36

# Listar los paquetes instalados en el entorno virtual
(py36) pip list

# Instalar Django en el entorno virtual
(py36) pip install django  # se puede instalar cualquier versión con django==2.0.2 o la que sea

# Crear un proyecto de Django
(py36) django-admin startproject proyecto

# Desinstalar Django del entorno virtual
(py36) pip uninstall django

# Desactivar el entorno virtual
(py36) source deactivate

Instalar Django en Linux en entorno virtual con Venv
=====================================================

# Consultar la versión de Python por defecto
python3 -V
Python 3.6.7

# Consultar la ruta de Python
which python3
/usr/bin/python3

# Instalar en Ubuntu el módulo venv
sudo apt install python3-venv

# Crear entorno virtual vacío
python3 -m venv py36

# Acceder a la carpeta del entorno virtual
cd py36

# Activar el entorno virtual
source bin/activate

# Listar los paquetes instalados (antes)
pip3 list

# Instalar Django
pip3 install django

# Instalar Django versión 2.0.2
pip3 install django==2.0.2

# Instalar pylint-django
pip3 install pylint-django

(Para pylint en Visual Source Code ver Configurar VSC)

# Listar los paquetes instalados (después)
astroid (2.1.0)
Django (2.1.4)
isort (4.3.4)
lazy-object-proxy (1.3.1)
mccabe (0.6.1)
Pillow (5.3.0)
pip (9.0.1)
pkg-resources (0.0.0)
pylint (2.2.2)
pylint-django (2.0.5)
pylint-plugin-utils (0.4)
pytz (2018.7)
setuptools (39.0.1)
six (1.12.0)
typed-ast (1.1.0)
wrapt (1.10.11)

# Consultar la versión Django instalada
python3 -m django --version

# Crear proyecto Django
django-admin startproject proyecto

# Desactivar el entorno virtual
deactivate


Configurar VSC
===============

# Instalar VSC

# Si se ha instalado con usuario distinto a root
sudo chown usuario:usuario -R .vscode/

# Instalar git
sudo apt install git

# Consultar version de git
git --version
git version 2.17.1

# Instalar extesión de idioma español
Control+P: ext install MS-CEINTL.vscode-language-pack-es

Instalas la extensión Django Template

# Para activar Pylint:
Acceder a Menú Archivo, Preferencias, Configuración, buscar "PylintArgs", Extensiones, Python Configuration, python.linting.pylintArgs, Editar en settings.json, Editar (icono lápiz), copiar en configuración y, finalmente, dentro de la lista escribir las siguentes cadenas de texto:

...
"python.linting.pylintArgs": [
    "--errors-only", 
    "--load-plugins", 
    "pylint-django"],
}


Práctica 1. Web Personal
=========================

# Iniciar entorno virtual
cd py36
source bin/activate

(Más adelente, el entorno virtual también se puede activar desde VSC seleccionando el archivo manage.py de un proyecto, con la opción 'Ejecutar archivo Python en la Terminal' de su menú contextual).

# Mover a la carpeta de proyectos
cd ..

# Crear proyecto webpersonal en Django
django-admin startproject webpersonal

# Ejecutar proyecto webpersonal
cd webpersonal
python3 manage.py runserver

# Abrir proyecto accediendo a la URL
http://127.0.0.1:8000
Presionar Control y hacer clic en hipervículo para abrir el proyecto en el navegador Internet predeterminado:

"The install worked successfully! Congratulations!

You are seeing this page because DEBUG=True is in your settings file and you have not configured any URLs."

# Deshabilitar debug con aplicación en producción
En archivo webpersonal/webpersonal/settings.py cambiar a False el valor de la variable DEBUG.

# Establecer idioma a español
Establecer en settings.py: LANGUAGE_CODE = 'es'
Actualizar página en navegador y aparecerá su contenido en el idioma indicado:

"¡La instalación funcionó con éxito! ¡Felicitaciones!

Estás viendo esta página porque DEBUG=True está en tu archivo de configuración y no has configurado ningún URL."

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
Interrumpir servidor con Control + C y ejecutar el siguiente comando:

python3 manage.py migrate

La salida que se obtiene comienza así:
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  ...

Algunas Apps integradas en Django
----------------------------------

- Admin: gestionar panel del administrador
- Auth: gestionar autenticación
- Contenttypes: tipos de contenidos
- Sessions: sesiones
- etc...

Un proyecto puede contener múltiples apps y una app puede ser incluída en diferentes proyectos.

Las aplicaciones se declaran en el archivo settings.py, en la lista INSTALLED_APPS: 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

Crear una app personal (core)
------------------------------

Con el proyecto detenido y el espacio virtual activo para crear el siguiente la app ejecutar:

python3 manage.py startapp core

Este comando creará la carpeta "core" que contiene la carpeta "migrations" y los archivos de la app: __init__.py, admin.py, apps.py, models.py, tests.py y views.py.

Crear vista/s de la app core
-----------------------------

Abrir el archivo views.py de la carpeta core y añadir a la línea del import el método "HttpResponse" quedando como sigue:

from django.shortcuts import render, HttpResponse

El método HttpResponse permite contestar a una petición devolviendo un código.

Crear vista para la portada del proyecto a continuación:

from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Mi web personal</h1><h2>Portada</h2>")

Asociar a la vista 'home' una URL
------------------------------------

Después de crear la vista es necesario establecer en Django la URL en la que se mostrará el código html. 

Para ello, una vez creada la vista abrir el archivo urls.py que se encuentra en la carpeta webpersonal/webpersonal y añadir la siguiente línea de import para importar la app core (debajo las líneas de import existentes):

from core import views

(Este comando importa de la app core su archivo views.py)

Después, añadiremos la url a la lista de patrones de urls llamada urlpatterns:

path('', views.home, name='home'),

- Las comillas vacías indican que la URL de la vista está en la raíz de la app core.
- views.home indica la función que se ejecutará de views.py
- name='home' da nombre a esta asociación de URL-vista

quedando así:

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
]

Ejecutar el proyecto para comprobar el resultado:

python3 manage.py runserver

Ahora en vez de ver la página predeterminada de Django se mostrará el resultado de renderizar el código HTML que se incluye en la vista home:

"Mi web personal
Portada"

También se podría definir la url indicando en el primer argumento el literal de una ruta como 'home'

path('home', views.home, name='home'),

Pero en este caso para llamar a esta vista desde el navegador tendríamos que acceder a:

http://127.0.0.1:8000/home

en vez de a:

http://127.0.0.1:8000


Crear vista 'about' en la app 'core'
-------------------------------------

Añadir a views.py:

def about(request):
    pagina = "<h1>Mi web personal</h1><h2>Acerca de</h2>"
    pagina+= "<p>Soy Antonio y soy programador</p>"
    return HttpResponse(pagina)

Asociar a la vista 'home' una URL
------------------------------------

Añadir a la lista urlpatterns de urls.py la siguiente url:

path('about/', views.about, name='about'),

Incluyendo un menú y mejorando las vistas
------------------------------------------

Modificar el archivo views.py añadiendo la variable html_base con el código del encabezado y de un menú; y editar las clases para incorparar estos cambios, agregando las vistas que faltan del proyecto:

html_base = """<h1>Mi web personal</h1>
<ul>
    <li><a href='/'>Portada</a></li>
    <li><a href='/portfolio/'>Portfolio</a></li>
    <li><a href='/contact/'>Contacto</a></li>
    <li><a href='/about/'>Acerca de</a></li>
</ul>"""

# Create your views here.
def home(request):
    pagina = html_base + "<h2>Portada</h2>"
    pagina += "<p>Esto es la portada</p>"
    return HttpResponse(pagina)

def portfolio(request):
    pagina = html_base + "<h2>Portfolio</h2>"
    pagina += "<p>Esto es mi portfolio</p>"
    return HttpResponse(pagina)

def contact(request):
    pagina = html_base + "<h2>Contacto</h2>"
    pagina += "<p>Puede contactar enviando correo</p>"
    return HttpResponse(pagina)

def about(request):
    pagina = html_base + "<h2>Acerca de</h2>"
    pagina += "<p>Soy Antonio y soy programador</p>"
    return HttpResponse(pagina)

Añadir a la lista urlpatterns de urls.py las urls restantes y ¡Probar!:

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
]

Templates
----------

Para ser eficientes construyendo las páginas de una app lo recomendable es utilizar plantillas.

Crear la carpeta 'templates' dentro de la carpeta 'core' que pertenece a la app de mismo nombre. Después, crear dentro de ella una nueva carpeta 'core'. La ruta desde 'webpersonal' será: webpersonal/core/templates/core.

A continuación crear dentro un archivo llamado 'base.html' con el código siguiente que es común a todas las páginas y que recoge el título de la web y el menú. (Si escribimos html:5 en VSC y pulsamos return se creará automáticamente la estructura de la página. Después modificar el código de país y el título de la página e incluir en el cuerpo el código del ejemplo)

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{% block titele %}{% endblock %} | Mi web personal</title>
</head>

<body>
    <!-- Cabecera y menú -->
    <h1>Mi web personal</h1>
    <ul>
        <li><a href='/'>Portada</a></li>
        <li><a href='/portfolio/'>Portfolio</a></li>
        <li><a href='/contact/'>Contacto</a></li>
        <li><a href='/about/'>Acerca de</a></li>
    </ul>
    <!-- Contenido -->
    {% block content %}{% endblock %}
</body>

</html>

Con {% block nombre %}{% endblock %} se indica el lugar donde se insertará el contenido diferente que tendrá cada página.

A continuación crear en la misma ubicación de base.html los archivos plantillas para cada página: home.html, contact.html, portfolio.html y about.html con el siguiente código:

home.html:
{% extends 'core/base.html' %}

{% block titele %}Portada{% endblock %}

{% block content %}
<h2>Portada</h2>

<p>Esto es la portada</p>
{% endblock %}


contact.html:
{% extends 'core/base.html' %}

{% block titele %}Contacto{% endblock %}

{% block content %}
<h2>Contacto</h2>

<p>Para contactar llame al videoportero</p>
{% endblock %}


portfolio.html:
{% extends 'core/base.html' %}

{% block titele %}Portfolio{% endblock %}

{% block content %}
<h2>Portfolio</h2>

<p>Estos son mis trabajos más destacados</p>
{% endblock %}

about.html:
{% extends 'core/base.html' %}

{% block titele %}Acerca de{% endblock %}

{% block content %}
<h2>Acerca de</h2>

<p>Esto es mi web personal</p>
{% endblock %}

En views.py modificar las funciones para que hagan un render a las plantillas anteriores, quedando así:

def home(request):
    return render(request, 'core/home.html')

def portfolio(request):
    return render(request, 'core/portfolio.html')

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

Por último, en settings.py agregar la app 'core' a la lista de aplicaciones de INSTALLED_APPS para que Django cargue las plantillas de la aplicación y ver el resultado:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

¡Excepcional!

Sustituyendo URL cruda por tag url
-----------------------------------

Para sustituir en el archivo base.html las URL crudas por etiquetas url incluir la etiqueta {% url 'nombre' %} en cada 'a href' en donde se construye el menú en dicho archivo, siendo 'nombre' el nombre del argumento name de cada path correspondiente de la lista urlpatterns del archivo urls.py:

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{% block titele %}{% endblock %} | Mi web personal</title>
</head>

<body>
    <!-- Cabecera y menú -->
    <h1>Mi web personal</h1>
    <ul>
        <li><a href='{% url 'home' %}'>Portada</a></li>
        <li><a href='{% url 'portfolio' %}'>Portfolio</a></li>
        <li><a href='{% url 'contact' %}'>Contacto</a></li>
        <li><a href='{% url 'about' %}'>Acerca de</a></li>
    </ul>
    <!-- Contenido -->
    {% block content %}{% endblock %}
</body>

</html>

Recomendación: nunca utilizar enlaces en crudo, utilizar siempre la etiqueta de plantilla url.

Etiquetas de plantillas y filtros:
https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#built-in-tag-reference


Uniendo el Frontend con el Backend
----------------------------------- 

Para comenzar abrir el archivo 'index.html' del frontend y guardar como 'index-fusion.html'. Este archivo es el equivalente a 'base.html' del backend. En 'index-fusion.html' insertaremos las templates tags del 'base.html' y realizaremos algunos cambios para unir la lógica de la app con la estética. Finalmente, copiar el código completo de 'index-fusion.html' al archivo 'base.html'.

Es necesario aclarar que el servidor de desarrollo de Django no sirve por defecto los contenidos estáticos. Para que lo haga hay que introducir algunas configuraciones extras:

- En primer lugar crear dentro de la carpeta de la app core una carpeta llamada 'static', y dentro de esta otra llamada 'core' al que copiaremos las carpetas 'css', 'img', 'js' y 'vendor' que contienen los archivos estáticos del ejemplo que proporciona el frontend del ejemplo.

- Después en 'base.html' hay que insertar {% load static %} para que Django realice la carga de los archivos estáticos y pueda servirlos. En este caso la etiqueta la insertaremos al comienzo del código justo después del comentario 'Estilos y fuentes del template'.

- A continuación hay que cambiar el modo de expresar todas las rutas de los archivos estáticos en 'base.html'. Para ello, sustituiremos cada una por la etiqueta {% static 'core/ruta' %}.

- En la línea donde se hace referencia a la imagen 'home-bg.jpg' con {% static 'core/img/home-bg.jpg' %} insertaremos en su lugar una etiqueta de bloque para que cada página carge su propia imagen de fondo: {% block fondo %}{% endblock %}

- En la zona de la cabecera insertaremos el bloque {% block cabeceras %}{% endblock %} en lugar del código: 

<h1>Juan Pérez</h1>
<span class="subheading">Ingeniero Industrial</span>
(Este código pasará a la página home)

- A continuación hay que modifcar los html de las páginas para que incorporen el bloque de la imagen de fondo y el de cabeceras. También, la diferencia que hay entre 'home.html' y el resto de páginas es que 'home' no tiene contenido y las demás páginas sí.

home.html:
{% extends 'core/base.html' %}

{% block titele %}Portada{% endblock %}

{% block fondo %}{% load static %}{% static 'core/img/home-bg.jpg' %}{% endblock %}

{% block cabeceras %}
   <h1>Juan Pérez</h1>
   <span class="subheading">Ingeniero Industrial</span>
{% endblock %}  

{% block content %}
{% endblock %}

about.html:
{% extends 'core/base.html' %}

{% block titele %}Acerca de{% endblock %}

{% block fondo %}{% load static %}{% static 'core/img/about-bg.jpg' %}{% endblock %}

{% block cabeceras %}
<h1>Acerca de</h1>
<span class="subheading">Biografía</span>
{% endblock %}  

{% block content %}
<h2>Acerca de</h2>

<p>Esto es mi web personal</p>
{% endblock %}

- Por último, vemos que después de mostrarse los contenidos de cada página (excepto para la home) aparece una línea horizontal a continuación. Para incorporar esta línea añadir en 'base.html' después del bloque de contenido 'content' el siguiente código:

{% if request.path != '/' %}
<hr>
{% endif %}

Para comprobar el resultado es necesario reiniciar el servidor:

python3 manage.py runserver

A continuación, vamos a trabajar con modelos. Necesitaremos el módulo pillow que nos permite trabajar con imágenes. Para instalar ejecutar en el entorno virtual:

pip install pillow


Modelos
========

Crear una nueva app llamada 'portfolio' dentro del proyecto 'webpersonal' con:

python3 manage.py startapp portfolio

Una vez creada la app abrir el archivo 'models.py' de dicha app y definir el primer modelo para los proyectos creando la siguiente clase:

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

Cada clase de un modelo define los campos de una tabla.

A continuación incorporar la app 'portfolio' a la lista de aplicaciones del proyecto añadiéndola a la variable INSTALLED_APPS del archivo 'settings.py':

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'portfolio',
]

Ahora hay que notificar a Django este último cambio en los modelos de una app del proyecto con:

python3 manage.py makemigrations portfolio

Se obtendrá la siguiente salida:
Migrations for 'portfolio':
  portfolio/migrations/0001_initial.py
    - Create model Project

Finalmente, para aplicar estos cambios ejecutar:

python3 manage.py migrate portfolio

Si todo fue bien se obtendrá la siguiente salida:
Operations to perform:
  Apply all migrations: portfolio
Running migrations:
  Applying portfolio.0001_initial... OK

Para añadir el modelo definido al Panel de Administración abrir el archivo 'admin.py' de la app 'portfolio' y añadir el import del modelo 'Project' y registrar el modelo, quedando el código así:

from django.contrib import admin
from .models import Project

# Register your models here.
admin.site.register(Project)

Antes de acceder al Panel de Administración es necesario  crear la cuenta del superusuario con:

python3 manage.py createsuperuser

Nombre de usuario (leave blank to use 'antonio'):
Dirección de correo electrónico: pherkad13@gmail.com
Password: django1234
Password (again): django1234
Superuser created successfully.

Finalmente, iniciar el proyecto:

python3 manage.py runserver

Y acceder desde el navegador a la ruta:

http://127.0.0.1:8000/admin

Introducir el nombre del superusuario y su contraseña para acceder al panel de administración. En el podremos administrar usuarios y grupos de usuarios del proyecto y mantener datos en la tabla Proyectos que hemos incorporado al panel.

Personalizando el panel de administración
==========================================

Establecer en panel un nombre de app diferente al real
-------------------------------------------------------

Para hacer que una app aparezca con un nombre diferente al que tiene en el panel de administrador abrir el archivo 'apps.py' de la app 'portfolio' y añadir a la clase existente:

verbose_name = 'portafolio'

Quedando así:
from django.apps import AppConfig

class PortfolioConfig(AppConfig):
    name = 'portfolio'
    verbose_name = 'portafolio'

A continuación, acceder al archivo 'settings.py' del proyecto y en la lista de aplicaciones de INSTALLED_APPS sustituir el nombre 'portfolio' por portfolio.apps.PortfolioConfig'.

Establecer en panel un nombre de modelo diferente al real
----------------------------------------------------------

Para hacer que un modelo aparezca con un nombre diferente al que tiene en el panel de administrador abrir el archivo 'models.py' de la app 'portfolio' y añadir a la clase existente 'Project' la subclase 'Meta'. Dentro de ellas se pueden incluir entre otros los atributos 'verbose_name' y 'verbose_name_plural' para establecer el nombre que tendrá el modelo en en el panel y el nombre en plural, respectivamente:

from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'

Establecer en panel un nombre diferente para cada campo
--------------------------------------------------------

Añadir el argumento 'verbose_name' a cada campo del modelo 'Project':

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descriptión')
    image = models.ImageField(verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Editado')

Establecer el orden de los registros de un modelo
-------------------------------------------------------

Para fijar el orden por defecto de los registros de un modelo añadir en el archivo 'models.py' de la app en la clase 'Meta' el atributo 'ordering', al que tendremos que asignarle una lista con los nombres de los campos a ordenar. Si precede el signo '-' nombre de un campo la ordenación será descendente.

Para ordenar los proyectos por las fecha de creación en modo descendente:

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created',]

    def __str__(self):
        return self.title

Establecer la visualización de un campo en la vista previa
--------------------------------------------------------------

Por defecto cuando se accede a un modelo en el panel se muestran en la vista previa entre paréntesis el número de registros existentes. En lugar de esto es posible mostrar el nombre de un campo añadiendo a la clase 'Meta' un método '__str__(self)' que devuelva 'return self.campo' como en el ejemplo:

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created',]

    def __str__(self):
        return self.title

Mostrar los campos 'auto' de un modelo en el panel
---------------------------------------------------

Añadir en 'admin.py' una nueva clase con el atributo 'readonly_fieldas' con la tupla con los nombres de campos a mostrar. Después añadir en el método 'admin.site.register()' otro argumento más con el nombre de la nueva clase 'ProjectAdmin':

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmin)

Crear la carpeta 'media' para la imágenes de un modelo
-------------------------------------------------------

Crear la carpeta 'media' dentro de la carpeta del proyecto 'webpersonal'.

A continuación en el archivo 'settings.py' añadir al final una variable llamada 'MEDIA_URL' con la ruta de la carpeta de las imágenes y otra variable denominada MEDIA_ROOT que indique la ubicación de la carpeta con respecto a la carpeta del proyecto utilizando la función os.path.join() para unir a la ruta del proyecto la carpeta 'media':

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

Después en el modelo 'Project' en la declaración del campo 'image' hay que añadir el argumento 'upload_to' con el nombre de la carpeta 'projects', carpeta que se creará dentro de la carpeta 'media' para cargar las imágenes de los proyectos. Esto es recomendable para separar las imágenes de un modelo con las que puedan tener otros modelos del proyecto:

    image = models.ImageField(verbose_name='Imagen', upload_to='projects')

Ahora cuando se añadan proyectos con imágenes se guardarán en la carpeta:

webpersonal/media/projects

En el modo producción si presionamos sobre el nombre de una imagen de un registro no podremos visualizarla. Para poder ver las imágenes es imprescindible que la depuración esté habilitada, es decir, en 'settings.py' la variable DEBUG debe estar a True. También, es necesario extender la configuración añadiendo al archivo del proyecto 'urls.py' un nuevo import:

from django.conf import settings

Y para terminar añadir al final del archivo 'urls.py' el siguiente código que permite la carga de ficheros estáticos en el panel de administración:

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Ahora si vamos al panel de administración y hacemos clic sobre el nombre de una imagen asociada al registro de un modelo dicha imagen será mostrada.


El patrón MVT (Modelo, Vista y Template
========================================

La vista 'portfolio' de 'views.py' de la app 'core' la podemos trasladar al archivo 'views.py' de la app 'portofolio. El código de la vista es el siguiente:

def portfolio(request):
    return render(request, 'core/portfolio.html')

A continuación, por guardar cierta coherencia, en 'portfolio' podemos hacer lo mismo que hicimos en 'core': crear una carpeta llamada 'templates' que contenga otra llamada 'portofolio' y a esta moveremos el archivo plantilla 'portfolio.html' de 'core/templates/core".

Esto nos obliga a cambiar en 'views.py' de 'porfolio' la ruta del archivo 'portfolio.html' para que lo busque en la nueva ubicación:

def portfolio(request):
    return render(request, 'portfolio/portfolio.html')

Ahora falta realizar algunos cambios en el archivo 'urls.py' del proyecto 'webpersonal'. El primero de ellos consiste en modificar los import actuales redefiniendo el que hace referencia a 'core' y añadiendo uno nuevo para las vistas de la app 'portofolio':

from core import views as core_views
from portfolio import views as portfolio_views

Y después se cambian las referencias a las clases de las vistas utilizadas en la lista de urls de 'urlpatters' por la nuevas. Concretamente, en la de la portada, 'contact' y 'about' se indicará 'core_views' y en 'portfolio', 'portfolio_views', quedando así:

urlpatterns = [
    path('', core_views.home, name='home'),
    path('portfolio/', portfolio_views.portfolio, name='portfolio'),
    path('contact/', core_views.contact, name='contact'),
    path('about/', core_views.about, name='about'),
    path('admin/', admin.site.urls),
]

Y estos cambios ¿Qué justificación tienen?

Bueno, aunque como lo teníamos antes funcionaba bien, con Django con el fin de favorecer la escalabilidad del proyecto es recomendable que cada app tenga sus propios archivos localizados dentro de su carpeta. En este caso la plantilla 'portfolio.html' dentro de la carpeta 'portfolio/templates/portfolio'.

Accediendo a los datos de proyectos de la base de datos
--------------------------------------------------------

En el archivo 'views.py' de 'portfolio' importaremos el modelo 'Project' y haciendo uso de él obtendremos en el método 'portfolio' todos los registros del modelo 'Project' que asignaremos a la variable 'projects' y que incluiremos como argumento en la función 'render()' que se devuelve, quedando así:

from django.shortcuts import render
from .models import Project

# Create your views here.

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects':projects})

Después, editaremos el archivo 'portfolio.html' y en el comienzo del bloque 'content' escribiremos la variable anterior 'projects' entre doble llaves, así:

...
{% block content %}

{{projects}}

<!-- Proyecto -->
...

Ahora con el proyecto en ejecución si refrescamos la página de 'portfolio' se visualizará el siguiente literal:

<QuerySet [<Project: Mi segundo proyecto>, <Project: Mi primer proyecto>]> 

Aparece algo parecido a una lista con los títulos de los proyectos existentes en la base de datos. Esto nos sugiere la posiblidad de iterar la lista de algún modo. Efectivamente, existe un etiqueta de plantilla 'for in' que permite recorrer los registros de la lista y acceder a las distintas columnas o campos.

A continuación en 'portfolio.html' reescribimos el bloque 'content' insertando la etiqueta de plantilla 'for in' para recorrer uno a uno todos los projectos del modelo e insertamos cada campo en los lugares donde deben aparecer en la página, quedando así el código:

...
{% block content %}
    {% for project in projects %}
        <!-- Proyecto -->
        <div class="row project">  	
            <div class="col-lg-3 col-md-4 offset-lg-1">
                <img class="img-fluid" src="{{project.image.url}}" alt="">
            </div>
            <div class="col-lg-7 col-md-8">
                <h2 class="section-heading title">{{project.title}}</h2>   
            <p>{{project.description}}</p>
            <!-- <p><a href="http://google.com">Más información</a></p> -->
            </div>
        </div>
    {% endfor %}
{% endblock %}

Añadir nuevo campo a modelo
--------------------------------------------------

Añadir un campo llamado 'link' de tipo URLfield con argumentos null y blank a True en el archivo 'models.py' de la app 'portfolio'.

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descriptión')
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')
    link = models.URLField(verbose_name='Enlace', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Editado')
   
Para hacer efectivos los cambios en el modelo es necesario detener el servidor y crear las migraciones ejecutando en el Terminal:
$ python3 manage.py makemigrations portfolio
Migrations for 'portfolio':
  portfolio/migrations/0002_auto_20181220_1208.py
    - Change Meta options on project
    - Add field link to project
    - Alter field created on project
    - Alter field description on project
    - Alter field image on project
    - Alter field title on project
    - Alter field updated on project

Después aplicar las migraciones con:
$ python3 manage.py migrate portfolio

Operations to perform:
  Apply all migrations: portfolio
Running migrations:
  Applying portfolio.0002_auto_20181220_1208... OK

Modificar template para que aparezca el nuevo campo
------------------------------------------------------------

Editar 'portfolio.html' en 'portfolio/templates/portfolio' y añadir el campo 'link' en el bloque 'content' para que aparezca el literal "Más información:" acompañado del enlace siempre que exista:

{% if project.link %}
    <p><a href="{{project.link}}">Más información</a></p>
{% endif %}

El bloque 'content' quedaría como sigue:

{% block content %}
    {% for project in projects %}
        <!-- Proyecto -->
        <div class="row project">  	
            <div class="col-lg-3 col-md-4 offset-lg-1">
                <img class="img-fluid" src="{{project.image.url}}" alt="">
            </div>
            <div class="col-lg-7 col-md-8">
                <h2 class="section-heading title">{{project.title}}</h2>   
            <p>{{project.description}}</p>
            {% if project.link %}
                <p><a href="{{project.link}}">Más información</a></p>
            {% endif %}
            </div>
        </div>
    {% endfor %}
{% endblock %}

