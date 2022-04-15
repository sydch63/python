#duration = int(input("Введите продолжительность времени: "))
duration = 78
second = 1
minutes = 60
hours = 3600
day = 86400

if duration <= minutes:
    print(duration, 'сек')
elif duration > minutes and duration <= hours:
    duration_minut = duration // minutes
    duration_sec = duration % minutes
    print(duration_minut, 'мин', duration_sec, 'сек')
elif duration > hours and duration < day:
    duration_hours = duration // hours
    duration_minut = (duration - hours) // minutes
    duration_sec = duration % minutes
    print(duration_hours,'час', duration_minut, 'мин', duration_sec, 'сек')
elif duration >= day:
    duration_day = duration // day
    duration_hours_remain = duration - day * duration_day
    duration_hours = duration_hours_remain // hours
    duration_minuts_remain = duration_hours_remain - duration_hours * hours
    duration_minut = duration_minuts_remain // minutes
    duration_sec = duration_minuts_remain - duration_minut * minutes
    print(duration_day,'дн',duration_hours,'час', duration_minut, 'мин', duration_sec, 'сек')
