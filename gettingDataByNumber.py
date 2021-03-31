import requests
import json

#n = "AE0807OA"


def parseNumber(number):
    url = "https://baza-gai.com.ua/nomer/{}".format(number)

    try:
        r = requests.get(url, headers={"Accept": "application/json"})
        data = r.json()

        for item in data['operations']:

            if data['stolen']:
                statusStolen = '❌ Да ❌'
            else:
                statusStolen = '✅ Нет ✅'

            operation = (
                'Производитель: ' + item['vendor'] + '\n'
                'Модель: ' + item['model'] + '\n'
                'Год: ' + str(item['modelYear']) + '\n'
                'Приметы: ' + item['notes'] + '\n'
                'Врозыске: ' + statusStolen + '\n'                              
                'Операция: ' + item['operation'] + '\n'
                'Дата: ' + str(item['regAt']) + '\n'                                  
                'Адрес: ' + item['address']
            )

    except KeyError:
        operation = '⛔Номер не найден⛔'

    return operation


