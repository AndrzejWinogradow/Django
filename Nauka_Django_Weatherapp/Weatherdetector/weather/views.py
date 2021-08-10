from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=49f203c62bf073a97288a56eb72f0c0f').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + 'E/W  ' +
            str(json_data['coord']['lat'])+'N/S',
            "temp": str(json_data['main']['temp']-273)+'°C',
            "pressure": str(json_data['main']['pressure'])+'hPa',
            "humidity": str(json_data['main']['humidity'])+'%',
            "sunrise": str(json_data['sys']['sunrise']),
            "sunset": str(json_data['sys']['sunset']),
        }

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})