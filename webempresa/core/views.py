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

def store(request):
    return render(request, 'core/store.html')

