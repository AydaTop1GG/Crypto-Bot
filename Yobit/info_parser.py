import requests

def get_info():
    response = requests.get(url="https://yobit.net/api/3/info") # Получаем инфу по парам

    with open("output_data/Yobit_data/info.txt", "w") as file:
        file.write(response.text)

    return response.text


def get_ticker(coin1="btc", coin2="usd"): # Статистика за последние 24 часа
    response = requests.get(url=f"https://yobit.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1") # /Перечисляем пару   ?ignore_invalid=1 если какой-то пары нет, то вместо ошибки выдаст то, что есть

    with open("output_data/Yobit_data/ticker.txt", "w") as file:
        file.write(response.text)

    return response.text



def get_depth(coin1="btc", coin2="usd", limit=50): # Список активных ордеров  limit - глубина для выводa(150 дефолт, 2000 макс)
    response = requests.get(url=f"https://yobit.net/api/3/depth/{coin1}_{coin2}?limit={limit}?ignore_invalid=1") # /Перечисляем пару   ?ignore_invalid=1 если какой-то пары нет, то вместо ошибки выдаст то, что есть


    with open("output_data/Yobit_data/depth.txt", "w") as file:
        file.write(response.text)


    """        Список предложений на покупку         """
    
    bids = response.json()[f"{coin1}_{coin2}"]["bids"] # Отсеиваем ненужное и оставляем нужный список предложений на покупку с ценой и количеством 

    total_bids_amount = 0
    for item in bids: # (цена1 * количество1) + (цена2 * количество2) +... не понял для чего это
        price = item[0]
        coin_amount = item[1]
        total_bids_amount += price * coin_amount

    # Минимальная цена с количеством
    min_bid_price = bids[0][0]
    min_bid_amount = bids[0][1]


    '''        Список предложений на продажу         '''

    asks = response.json()[f"{coin1}_{coin2}"]["asks"] # Отсеиваем ненужное и оставляем нужный список предложений на продажу с ценой и количеством 

    total_asks_amount = 0
    for item in asks: # (цена1 * количество1) + (цена2 * количество2) +... не понял для чего это
        price = item[0]
        coin_amount = item[1]
        total_asks_amount += price * coin_amount

    # Минимальная цена с количеством
    min_ask_price = asks[0][0]
    min_ask_amount = asks[0][1]

    # Визуальное оформление валюты результата
    if coin2 == "usd":
        currency = "$"
    elif coin2 == "rur":
        currency = "₽"
    
    return f"\nTotal bids: {total_bids_amount} {currency}\nMin bid price: {min_bid_price} {currency}\nAmount: {min_bid_amount}\n\nTotal asks: {total_asks_amount} {currency}\nMin ask price: {min_ask_price} {currency}\nAmount: {min_ask_amount}"




def get_trades(coin1="btc", coin2="usd", limit=150): # Инфа о последних сделках указанных пар
    response = requests.get(url=f"https://yobit.net/api/3/trades/{coin1}_{coin2}?limit={limit}?ignore_invalid=1") # /Перечисляем пару   ?ignore_invalid=1 если какой-то пары нет, то вместо ошибки выдаст то, что есть


    with open("output_data/Yobit_data/trades.txt", "w") as file:
        file.write(response.text)


    total_trade_ask = 0
    total_trade_bid = 0

    for item in response.json()[f"{coin1}_{coin2}"]:
        if item["type"] == "ask":
            total_trade_ask += item["price"] * item["amount"]
        else:
            total_trade_bid += item["price"] * item["amount"]

    info = f"[-] TOTAL {coin1} SELL: {round(total_trade_ask, 2)} $\n[+] TOTAL {coin1} BUY: {round(total_trade_bid, 2)} $"

    return info


def main():
    coin1 = input("Введите криптовалюту: ")
    coin2 = input("Введите желаемую валюту: ")
    #print(get_info())
    #print(get_ticker())
    #print(get_ticker(coin1="eth", coin2=coin2))
    print(get_depth(coin1=coin1, coin2=coin2))
    #print(get_depth(coin1="doge"))
    #print(get_depth(coin1="doge", limit=2000))
    #print(get_trades(coin1=coin1, coin2=coin2))



if __name__== "__main__":
    main()