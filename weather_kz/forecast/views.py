from datetime import datetime
import requests
from django.shortcuts import render

API_KEY = '88344296624c4734a40103525251510'

def format_time_ru(date_str):
    # Преобразуем строку '2023-10-15 14:00' в объект datetime
    date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
    # Возвращаем в формате '15 окт, 14:00'
    return date_obj.strftime('%d %b, %H:%M')

def weather_view(request):
    city_name = request.POST.get('city', 'Almaty')
    weather_data = None
    hourly_forecast = []
    daily_forecast = []
    error_msg = None

    try:
        api_url = (
            f"http://api.weatherapi.com/v1/forecast.json"
            f"?key={API_KEY}&q={city_name}&days=5&lang=ru"
        )
        response = requests.get(api_url)
        response_json = response.json()

        if response_json.get('error'):
            error_msg = response_json['error']['message']
        else:
            location_info = response_json['location']
            current_weather = response_json['current']
            forecast_days = response_json['forecast']['forecastday']

            weather_data = {
                'city': location_info['name'],
                'temp': current_weather['temp_c'],
                'feels_like': current_weather['feelslike_c'],
                'humidity': current_weather['humidity'],
                'wind': current_weather['wind_kph'],
                'description': current_weather['condition']['text'],
                'icon': 'https:' + current_weather['condition']['icon'],
                'last_updated': format_time_ru(current_weather['last_updated']),
            }

            # Составляем почасовой прогноз на следующие 12 часов, начиная с текущего времени
            all_hours = forecast_days[0]['hour'] + forecast_days[1]['hour']
            current_time = datetime.strptime(current_weather['last_updated'], '%Y-%m-%d %H:%M')

            next_hours = [
                hour for hour in all_hours
                if datetime.strptime(hour['time'], '%Y-%m-%d %H:%M') >= current_time
            ][:12]

            for hour in next_hours:
                time_formatted = datetime.strptime(hour['time'], '%Y-%m-%d %H:%M').strftime('%H:%M')
                hourly_forecast.append({
                    'time': time_formatted,
                    'temp': hour['temp_c'],
                    'description': hour['condition']['text'],
                    'icon': 'https:' + hour['condition']['icon'],
                })

            # Прогноз на ближайшие 5 дней
            for day in forecast_days[:5]:
                day_date = datetime.strptime(day['date'], '%Y-%m-%d').strftime('%d %b')
                daily_forecast.append({
                    'date': day_date,
                    'maxtemp': day['day']['maxtemp_c'],
                    'mintemp': day['day']['mintemp_c'],
                    'description': day['day']['condition']['text'],
                    'icon': 'https:' + day['day']['condition']['icon'],
                })

    except Exception:
        error_msg = "Не удалось получить данные о погоде."

    context = {
        'weather': weather_data,
        'hourly': hourly_forecast,
        'daily': daily_forecast,
        'error': error_msg,
    }

    return render(request, 'forecast/weather.html', context)