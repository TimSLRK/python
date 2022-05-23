duration = int(input())
minutes = duration // 60
hour = duration // 3600
day = duration // 86400
if duration < 60:
    print(duration, 'сек')
elif 60 <= duration < 3600:
    print(minutes, 'мин', duration % 60, 'сек')
elif 3600 <= duration < 86400:
    print(hour, 'час', (duration % 3600) // 60, 'мин', duration % 60, 'сек')
else:
    print(day, 'дн', (duration % 86400) // 3600, 'час', (duration % 3600 // 60), 'мин', duration % 60, 'сек' )