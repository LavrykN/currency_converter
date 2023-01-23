import json

import requests as requests

ZONE_DOMAIN = {
    "uk": 826, "cz": 203, "it": 978, "es": 978,
    "de": 978, "fr": 978, "pt": 978, "be": 978,
    "fi": 978, "gr": 978, "lt": 978, "lu": 978,
    "mc": 978, "me": 978, "nl": 978, "sk": 978,
    "si": 978, "pl": 985, "bg": 975, "dk": 208,
    "no": 578, "ro": 946, "rs": 941, "se": 752,
    "ch": 756
}


class Currency:
    def __init__(self):
        self.data = {
            "al": 0.34,
            "mk": 0.63,
        }

    def parse_currency(self):
        url_currency = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

        currency_data = json.loads(requests.get(url_currency).content)

        for domain, index_country in ZONE_DOMAIN.items():
            for currency_info in currency_data:
                if currency_info["r030"] == index_country:
                    self.data[domain] = currency_info["rate"]

    @property
    def currency(self) -> dict:
        return self.data


if __name__ == "__main__":
    curr = Currency()
    curr.parse_currency()
    print(curr.currency)
