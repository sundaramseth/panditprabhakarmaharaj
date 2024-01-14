from django.http import HttpResponse
from django.template import loader





def about(request):
  template = loader.get_template('about.html')
  context = {
    'name': "about",
  }
  return HttpResponse(template.render(context, request));
  


def service_section(request):
  template = loader.get_template('service.html')
  context = {
    'name': "service_section",
  }
  return HttpResponse(template.render(context, request));

  

def destination_wedding(request):
  template = loader.get_template('destination_wedding.html')
  context = {
    'name': "destination_wedding",
  }
  return HttpResponse(template.render(context, request));


def nri_service(request):
  template = loader.get_template('pandit.html')
  context = {
    'name': "pandit",
  }
  return HttpResponse(template.render(context, request));



def termandservice(request):
  template = loader.get_template('termandservice.html')
  context = {
    'name': "termandservice",
  }
  return HttpResponse(template.render(context, request));


