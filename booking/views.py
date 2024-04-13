# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForms
from django.template import loader
from .models import BookingForm, SubscribeForm
from services.models import Typesofpuja

def my_form_view(request,id):
    if request.method == 'POST':
        form = BookingForms(request.POST)
        if form.is_valid():
            form.save();
            context = {
                'booking_details': form.data
            }
            return render(request, 'booking/booking_success.html', context);
    form = BookingForms()
    festival_puja_d = Typesofpuja.objects.get(id=id)
    context = {'form': form, 'festival_puja_d':festival_puja_d}
    return render(request, 'booking/booking.html', context)


def succsess(request, id):
  booking_details = BookingForm.objects.get(id=id)
  template = loader.get_template('booking/booking_success.html')
  context = {
    'booking_details': booking_details,
  }
  return render(request, template, context);


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save();
            context={
                'succsessfull': 'success'
            }
            return render(request,'base.html',context)
    form = SubscribeForm()
    context = {'form': form}
    return render(request, 'base.html', context)
