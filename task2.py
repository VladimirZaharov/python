seconds = int(input('Введите количество секунд: '))
minutes = 0
hours = 0
if seconds >= 60:
    minutes = seconds // 60
    seconds = seconds % 60
if minutes >= 60:
    hours = minutes // 60
    minutes = minutes % 60

print(f'Время {hours}:{minutes}:{seconds}')
