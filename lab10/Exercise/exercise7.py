def average_temperature_and_precipitation(data):
    city_data = {}
    for city, city_weather in data.items():
        temperatures = [day['temperature'] for day in city_weather]
        precipitation = [day['precipitation'] for day in city_weather]
        avg_temperature = sum(temperatures) / len(temperatures)
        total_precipitation = sum(precipitation)
        city_data[city] = {'avg_temperature': avg_temperature, 'total_precipitation': total_precipitation}
    return city_data

def min_max_temperature_days(data):
    min_max_days = {}
    for city, city_weather in data.items():
        temperatures = [day['temperature'] for day in city_weather]
        min_temp_day = city_weather[temperatures.index(min(temperatures))]['date']
        max_temp_day = city_weather[temperatures.index(max(temperatures))]['date']
        min_max_days[city] = {'min_temp_day': min_temp_day, 'max_temp_day': max_temp_day}
    return min_max_days

def coldest_and_warmest_cities(data):
    city_temperatures = {city: sum([day['temperature'] for day in city_weather]) / len(city_weather) for city, city_weather in data.items()}
    coldest_city = min(city_temperatures, key=city_temperatures.get)
    warmest_city = max(city_temperatures, key=city_temperatures.get)
    return coldest_city, warmest_city

def print_summary(data):
    avg_temp_precipitation = average_temperature_and_precipitation(data)
    min_max_days = min_max_temperature_days(data)
    coldest_city, warmest_city = coldest_and_warmest_cities(data)

    print("Average Temperature and Total Precipitation:")
    for city, city_data in avg_temp_precipitation.items():
        print(f"{city}: Avg Temp: {city_data['avg_temperature']}, Total Precipitation: {city_data['total_precipitation']}")

    print("\nDays with Minimum and Maximum Temperature:")
    for city, days in min_max_days.items():
        print(f"{city}: Min Temp Day: {days['min_temp_day']}, Max Temp Day: {days['max_temp_day']}")

    print("\nColdest and Warmest Cities:")
    print(f"Coldest City: {coldest_city}")
    print(f"Warmest City: {warmest_city}")

# Пример данных о погоде
weather_data = {
    'City1': [
        {'date': '2024-05-01', 'temperature': 20, 'precipitation': 5},
        {'date': '2024-05-02', 'temperature': 22, 'precipitation': 2},
        {'date': '2024-05-03', 'temperature': 18, 'precipitation': 7}
    ],
    'City2': [
        {'date': '2024-05-01', 'temperature': 15, 'precipitation': 8},
        {'date': '2024-05-02', 'temperature': 17, 'precipitation': 3},
        {'date': '2024-05-03', 'temperature': 14, 'precipitation': 6}
    ]
}
def print_solution():
    print_summary(weather_data)
