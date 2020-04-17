from django.forms import ModelForm, TextInput
from .models import City


class CityFrom(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(
            attrs={'class': 'input', 'placeholer': 'City Name'})}
