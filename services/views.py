from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Typesofpuja

def home(request):
  all_puja = Typesofpuja.objects.all().values()
  template = loader.get_template('home.html')
  context = {
    'name': "about",
    'all_puja': all_puja,
  }
  return HttpResponse(template.render(context, request));


def festive_service(request):
  festival_puja = Typesofpuja.objects.all().values()
  template = loader.get_template('typesofpuja/festival_puja_services.html')
  context = {
    'festival_puja': festival_puja,
  }
  return HttpResponse(template.render(context, request))

def hawan_service(request):
  hawan_service = Typesofpuja.objects.all().values()
  template = loader.get_template('typesofpuja/hawan_service.html')
  context = {
    'hawan_service': hawan_service,
  }
  return HttpResponse(template.render(context, request))


def katha_service(request):
  katha_service = Typesofpuja.objects.all().values()
  template = loader.get_template('typesofpuja/katha_service.html')
  context = {
    'katha_service': katha_service,
  }
  return HttpResponse(template.render(context, request))

def santi_service(request):
  santi_service = Typesofpuja.objects.all().values()
  template = loader.get_template('typesofpuja/santi_service.html')
  context = {
    'santi_service': santi_service,
  }
  return HttpResponse(template.render(context, request))


def sanskar_service(request):
  sanskar_service = Typesofpuja.objects.all().values()
  template = loader.get_template('typesofpuja/sanskar_service.html')
  context = {
    'sanskar_service': sanskar_service,
  }
  return HttpResponse(template.render(context, request))

def sthapan_service(request):
  sthapan_service = Typesofpuja.objects.all().values()
  template = loader.get_template('typesofpuja/sthapan_service.html')
  context = {
    'sthapan_service': sthapan_service,
  }
  return HttpResponse(template.render(context, request))

  
def details(request, id):
  festival_puja_d = Typesofpuja.objects.get(id=id)
  template = loader.get_template('typesofpuja/festive_puja_details.html')
  context = {
    'festival_puja_d': festival_puja_d,
  }
  return HttpResponse(template.render(context, request))
  
def mainservices(request):
  template = loader.get_template('service.html')
  context = {
    'name': "all_services",
  }
  return HttpResponse(template.render(context, request))                 