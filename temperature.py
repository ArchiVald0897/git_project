from pyowm import OWM

city = input("Введите город\n")

owm = OWM('edbd35eb868e464c9db0fd2caa8d0bd1')
mgr = owm.weather_manager()

observation = mgr.weather_at_place(city)
w = observation.weather
temperature = w.temperature('celsius')['temp']
print("В городе " + city + " Сейчас температура: " + str(temperature) + " по Цельсию")
