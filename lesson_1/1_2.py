time = int(input("Введите время в секундах: "))
hours = time // 3600
minutes_plus_seconds = time % 3600
minutes = minutes_plus_seconds // 60
seconds = minutes_plus_seconds % 60

hours = hours if hours > 10 else "0" + str(hours)
minutes = minutes if minutes > 10 else "0" + str(minutes)
seconds = seconds if seconds > 10 else "0" + str(seconds)

print(f"The Time is: {hours}:{minutes}:{seconds}")


