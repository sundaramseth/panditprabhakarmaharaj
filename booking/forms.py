from django.forms import ModelForm
from .models import BookingForm, SubscribeForm


class BookingForms(ModelForm):
    class Meta:
        model = BookingForm
        fields = '__all__'

class Subscribe(ModelForm):

    class Meta:
        model = SubscribeForm
        fields = '__all__'

