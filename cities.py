import requests
import json
import os


class Ciudades:
    def __init__(self):
        self.cities = {}
        self.bearer_token = os.environ.get("BEARER_TOKEN")
        self.header_sheety = {"Authorization": f"Bearer {self.bearer_token}"}
        self.api_endpoint = os.environ.get("API_ENDPOINT")

        self.response = requests.get(url=self.api_endpoint, headers=self.header_sheety)

        self.response = json.loads(self.response.text)
        # print(self.response["vuelos"])

    def get_inputs(self):
        self.cities = {}
        for i in self.response["vuelos"]:
            # print(i)
            city = i["city"]
            price = int(i["lowestPrice"])
            adults = int(i["adultos"])
            children = int(i["niños"])
            desde = i["desde"]
            hasta = i["hasta"]
            code = i["code"]

            self.cities[city] = {"price": price, "adults": adults, "children": children, "code": code, "desde": desde,
                                 "hasta": hasta}
        return self.cities
