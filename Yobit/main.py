import requests
import time
from config import API_KEY, API_SECRET
from urllib.parse import urlencode
import hmac
import hashlib


def get_info(): # Проходим аутентификацию сайта и выводим общую инфу
    values = dict()
    values["method"] = "getInfo"
    values["nonce"] = str(int(time.time()))

    body = urlencode(values).encode("utf-8") # Байт-строка
    sign = hmac.new(API_SECRET.encode("utf-8"), body, hashlib.sha512).hexdigest() # Подпись для прохождения аутентификации
    
    headers = { # Заголовки
        "key": API_KEY,
        "sign": sign
    }


    response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)
    return response.json()


def get_deposit_address(coin_name="btc"): # Запрос адресов наших кошельков
    values = dict()
    values["method"] = "GetDepositAddress"
    values["coinName"] = coin_name
    values["need_new"] = 0
    values["nonce"] = str(int(time.time()))

    # Параметры запроса
    body = urlencode(values).encode("utf-8") # Байт-строка
    sign = hmac.new(API_SECRET.encode("utf-8"), body, hashlib.sha512).hexdigest() # Подпись
    
    # Заголовки
    headers = {
        "key": API_KEY,
        "sign": sign
    }

    # Отправляем запрос
    response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)
    return response.json()



def main():
    coin_name = input("Enter a coin name: ") # Запрашиваем у пользователя монету
    print(get_deposit_address(coin_name=coin_name)) # Печатаем результат
    #print(get_info()) # Получаем общую инфу в консоль


if __name__ == '__main__':
    main()