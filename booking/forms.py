from django.forms import ModelForm
from .models import BookingForm


class BookingForms(ModelForm):
    class Meta:
        model = BookingForm
        fields = '__all__'

