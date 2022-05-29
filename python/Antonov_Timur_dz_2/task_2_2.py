forecast = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(forecast)):
    if forecast[i].isdigit():
        forecast[i] = forecast[i].zfill(2)
    if forecast[i].startswith('+'):
        forecast[i] = forecast[i].zfill(3)
print(forecast)
j = 0
while j < len(forecast):
    if forecast[j].isdigit() or forecast[j].startswith('+'):
        forecast.insert(j, '"')
        forecast.insert(j + 2, '"')
        j += 1
    j += 1
print(forecast)
weather = ''
for k in forecast:
    if k.isalpha():
        weather += ''.join(f' {""}{k}{""} ')
    else:
        weather += ''.join(k)
weather = weather.strip()
print(weather)