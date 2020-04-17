import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityFrom

# Create your views here.


def weather(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=58c4e41bd6b01af1061714aad969ee0d'
    weather_data = []
    err_msg = ''
    message = ''
    msg_class = ''

    if request.method == 'POST':
        form = CityFrom(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            if(City.objects.filter(name=new_city).count() == 0):
                resp = requests.get(url.format(new_city)).json()
                if resp['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'Invalid City'
            else:
                err_msg = 'City already exists'
        if err_msg:
            message = err_msg
            msg_class = 'is-danger'
        else:
            message = 'City added successfully'
            msg_class = 'is-success'
    form = CityFrom()
    err_msg = ''
    cities = City.objects.all()
    for city in cities:
        resp = requests.get(url.format(city.name)).json()
        city_weather = {
            'city': city.name,
            'temperature': resp['main']['temp'],
            'description': resp['weather'][0]['description'],
            'icon': resp['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    print(weather_data)
    info = {
        'weather_data': weather_data,
        'form': form,
        'message': message,
        'msg_class': msg_class
    }
    return render(request, 'weather.html', info)


def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')
