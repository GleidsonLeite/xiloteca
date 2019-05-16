from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import request
from django.utils import timezone
from .models import madeira, textHome, feedDeNoticias, colaboradores

from .forms import filterWood, searchWoodForm
# Create your views here.

from django.views.generic import ListView

def wood_list(request):
    woods = madeira.objects.order_by('nomeCientifico')
    return render(request, 'wood/wood_list.html', {'woods':woods})

def index(request):
    textoInicial = textHome.objects.all()
    feed = feedDeNoticias.objects.order_by('-created_date')
    return render(request, 'wood/index.html', {'textoInicial':textoInicial, 'feed':feed,})

def search(request):
    woods = filterWood(request.POST, queryset = madeira.objects.all())
    return render(request, 'wood/pesquisa.html', {'woods':woods})

def post_detail(request,pk):
    post = get_object_or_404(feedDeNoticias, pk=pk)
    return render(request,'wood/post_detail.html',{'post':post},)

def about(request):
    colab = colaboradores.objects.order_by('nome')
    return render(request, 'wood/about.html',{'colaboradores':colab})

def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response