from datetime import datetime, timedelta

import json
import requests
import os


class SearchFlight:
    def __init__(self, city, destination, max_price, adults, children, desde, hasta):
        self.FLIGHT_API_ENDPOINT = os.environ.get("FLIGHT_ENDPOINT")
        self.city = city
        self.header = {"apikey": os.environ.get("API_TEQUILA_KEY")}
        # self.tomorrow = datetime.now().strftime("%d/%m/%Y")
        # self.six_months = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")
        self.destination = destination
        self.data = {
            "fly_from": "airport:MAD",
            "fly_to": f"city:{destination}",
            "date_from": desde,
            "date_to": hasta,
            "flight_typ": "round",
            "nights_in_dst_from": 2,
            "nights_in_dst_to": 5,
            "ret_from_diff_city": False,
            "ret_to_diff_city": False,
            "adults": adults,
            "children": children,
            "locale": "es",
            "price_to": max_price,
            "max_stopovers": 0,

        }

        self.response = requests.get(url=self.FLIGHT_API_ENDPOINT, headers=self.header, params=self.data)
        self.response = json.loads(self.response.text)
        # print(json.dumps(self.response, indent=4))

        # print(self.response["data"][0])
        # print(len(self.response["data"]))

    def is_cheap_flight(self):
        if self.response["data"]:
            return True
        else:
            return False

    def create_email(self):
        email = "<html>"
        for i in range(0, len(self.response["data"])):
            with open("static/model_email.html", "r") as f:
                page = f.read()
            departure = self.response["data"][i]["route"][0]["local_departure"][:10:]
            arrival = self.response["data"][i]["route"][1]["local_departure"][:10:]
            price = self.response["data"][i]["price"]
            link = self.response["data"][i]["deep_link"]
            page = page.replace("{destination}", self.city)
            page = page.replace("{departure}", departure)
            page = page.replace("{arrival}", arrival)
            page = page.replace("{link}", link)
            page = page.replace("{price}", str(price))
            email += f"\n{page}"
        email += "<html>"
        # print(email)
        return email

