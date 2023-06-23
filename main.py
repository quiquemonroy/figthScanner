from fligths import SearchFlight
from cities import Ciudades
from emails import SendEmail
import schedule
import time, pytz


def run():
    ciudades = Ciudades()
    dict_ciudades = ciudades.get_inputs()

    for i in dict_ciudades:
        print(f'{i}: {dict_ciudades[i]}')
        city = SearchFlight(i, dict_ciudades[i]["code"], dict_ciudades[i]["price"], dict_ciudades[i]["adults"],
                            dict_ciudades[i]["children"], dict_ciudades[i]["desde"], dict_ciudades[i]["hasta"])
        if city.is_cheap_flight():
            mail = SendEmail(city.create_email(), i)
            print("found one flight, email sent")
        else:
            print("Cheap flight not found")


schedule.every().day.at("07:00", "Europe/Amsterdam").do(run)
run()
while True:
    schedule.run_pending()
    time.sleep(1)
# TODO Crear envío de SMS, alomojor.
