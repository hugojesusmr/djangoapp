from django.shortcuts import render
import pandas as pd
from sqlalchemy import create_engine
from django.conf import settings
from  hola_docker.models import SitiosTotales
from  hola_docker.models import Origen_FO
from  hola_docker.models import AGG
from  hola_docker.models import Proyeccion
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)


def index(request):
    return render(request, "index.html")        
 

def listarSitios(request):
    busqueda = request.POST.get("buscar")
    sitios = SitiosTotales.objects.all()

    if busqueda:
        sitios = SitiosTotales.objects.filter(
            Q(ATTID__icontains = busqueda) |
            Q(ESTADO__icontains = busqueda) 
        ).distinct()

    page = request.GET.get('page',1)
    try:
        paginator = Paginator(sitios,5)
        sitios = paginator.page(page)
    except:
        raise Http404
    data = {'entity':sitios,
            'paginator': paginator }

    return render(request, "sitios/listarSitios.html",data)


def cargarSitios(request):
       
    if request.method == 'POST':
        upload_file = request.FILES['file']
            
        df = pd.read_excel(upload_file, engine='openpyxl')
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']
       # engine = create_engine('sqlite:///db.sqlite3')
        database_url = 'mysql://{user}:{password}@localhost:3306/{database_name}'.format(
            user=user,
            password=password,
            database_name=database_name
        )
        engine = create_engine(database_url,echo=False)
        df.to_sql(
                  SitiosTotales._meta.db_table,
                  #if_exists='append', 
                  con=engine,index=False)

    return render(request, "sitios/cargarSitios.html")

def listarFO(request):
    busqueda = request.POST.get("buscar")
    sitios = Origen_FO.objects.all()

    if busqueda:
        sitios = Origen_FO.objects.filter(
            Q(ATTID__icontains = busqueda) |
            Q(ESTADO__icontains = busqueda) 
        ).distinct()

    page = request.GET.get('page',1)
    try:
        paginator = Paginator(sitios,5)
        sitios = paginator.page(page)
    except:
        raise Http404
    data = {'entity':sitios,
            'paginator': paginator }

    return render(request, "sitios/listarFO.html",data)

def cargarFO(request):
       
    if request.method == 'POST':
        upload_file = request.FILES['file']
            
        df = pd.read_excel(upload_file, engine='openpyxl')
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']
        database_url = 'mysql://{user}:{password}@localhost:3306/{database_name}'.format(
            user=user,
            password=password,
            database_name=database_name
        )
        engine = create_engine(database_url,echo=False)
        df.to_sql(
                  Origen_FO._meta.db_table,
                  #if_exists='append', 
                  con=engine,index=False)

    return render(request, "sitios/cargarFO.html")

def cargarAGG(request):
    if request.method == 'POST':
        upload_file = request.FILES['file']
            
        df = pd.read_excel(upload_file, engine='openpyxl')
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']
        database_url = 'mysql://{user}:{password}@localhost:3306/{database_name}'.format(
            user=user,
            password=password,
            database_name=database_name
        )
        engine = create_engine(database_url,echo=False)
        df.to_sql(
                  AGG._meta.db_table,
                  #if_exists='append', 
                  con=engine,index=False)

    return render(request, "sitios/cargarAGG.html")

def cargarProyeccion(request):
    if request.method == 'POST':
        upload_file = request.FILES['file']
            
        df = pd.read_excel(upload_file, engine='openpyxl')
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']
        database_url = 'mysql://{user}:{password}@localhost:3306/{database_name}'.format(
            user=user,
            password=password,
            database_name=database_name
        )
        engine = create_engine(database_url,echo=False)
        df.to_sql(
                  Proyeccion._meta.db_table,
                  #if_exists='replace', 
                  con=engine,index=False)

    return render(request, "sitios/cargarProyeccion.html")







