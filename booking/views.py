# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForms
from django.template import loader
from .models import BookingForm

def my_form_view(request):
    if request.method == 'POST':
        form = BookingForms(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'book_now/booking_success/')
    form = BookingForms()
    context = {'form': form}
    return render(request, 'booking/booking.html', context)


def succsess(request, id):
  booking_details = BookingForm.objects.get(id=id)
  template = loader.get_template('booking/booking_success.html')
  context = {
    'booking_details': booking_details,
  }
  return HttpResponse(template.render(context, request))