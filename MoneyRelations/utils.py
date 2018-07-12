import json
from decimal import Decimal
from urllib.request import urlopen
from . import models


def get_currencies():
    with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
        source = response.read()

    data = json.loads(source)

    # print(json.dumps(data, indent=2))

    usd_rates = dict()

    for item in data["list"]["resources"]:
        name = item["resource"]["fields"].get('name')
        price = item["resource"]["fields"].get('price')
        usd_rates[name] = price

    EURpUSD = usd_rates['USD/EUR']
    TRYpUSD = usd_rates['USD/TRY']

    TRYpEUR = Decimal(TRYpUSD) / Decimal(EURpUSD)

    return TRYpEUR, TRYpUSD


def getTotal():
    order_list = models.Expense.objects.all()
    sum = 0
    for item in order_list:
        sum = sum + item.order_total()
