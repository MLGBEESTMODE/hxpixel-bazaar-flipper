import math
import time
import requests
from threading import Thread


top_list_lenght = input("Enter the amount of items to show: ")
top_list_lenght = int(top_list_lenght)



class ids:
    def __init__(self, id, sell_price, buy_price, sell_price2, buy_price2, competitivness, competitivness2):
        self.id = id
        self.sell_price = sell_price
        self.buy_price = buy_price
        self.sell_price2 = sell_price2
        self.buy_price2 = buy_price
        self.competitivness = competitivness
        self.competitivness2 = competitivness2


class price:
    def __init__(self,  ratio, name, pot_profit, sell_price, buy_price, other, marketcap):
        self.ratio = ratio
        self.name = name
        self.pot_profit = pot_profit
        self.sell_price = sell_price
        self.buy_price = buy_price
        self.other = other
        self.marketcap = marketcap

item_id_list = []


run_time = time.time()
global counter
counter = 0

api_data = requests.get('https://api.hypixel.net/skyblock/bazaar').json()['products']



item_list = list(api_data.keys())


for a in item_list:
    try:
        k = float(api_data[a]['sell_summary'][0]['pricePerUnit'])
        r = float(api_data[a]['buy_summary'][0]['pricePerUnit'])
        item_id_list.append(ids(a, r, k, r, k, 0, 0))
    except:
        1 + 1
thread_running = True

z = True

def thang():

    global ct
    global api_data
    timer = time.time()
    while thread_running:
        if time.time() >= timer:
            timer = time.time() + 0.7
            time.sleep(0.6)
            try:
                api_data = requests.get('https://api.hypixel.net/skyblock/bazaar').json()['products']
            except:
                1 + 1
            for a in item_id_list:
                try:
                    a.sell_price2 = float(api_data[a.id]['buy_summary'][0]['pricePerUnit'])
                    a.sell_price2 = float(api_data[a.id]['sell_summary'][0]['pricePerUnit'])
                    old_sell_price = a.sell_price
                    old_buy_price = a.buy_price
                    new_sell_price = a.sell_price2
                    new_buy_price = a.buy_price2

                    if old_sell_price  < new_sell_price:
                        a.competitivness += 1
                        a.sell_price = new_sell_price
                    else:
                        a.sell_price = new_sell_price
                    if old_buy_price < new_buy_price:
                        a.competitivness2 += 1
                        a.buy_price = new_buy_price
                    else:
                        a.buy_price = new_buy_price
                except:
                    1 + 1
        else:
            time.sleep(0.1)


list12 = []


def thang2():
    global top_list_lenght
    global thread_running
    timer2 = time.time()
    while thread_running:
        b = api_data
        if timer2 < time.time():
            timer2 = time.time() + 60
            x2 = 0
            while x2 == 0:
                x2 += 1

                def getList(dict):
                    return dict.keys()
                z = []
                fr = []
                x = -1
                d = list(getList(b))
                for a in d:
                    try:
                        buy_volume = b[a]['quick_status']['buyMovingWeek']
                        sell_volume = b[a]['quick_status']['sellMovingWeek']
                        buy_price = float(b[a]['sell_summary'][0]['pricePerUnit'])
                        sell_price = float(b[a]['buy_summary'][0]['pricePerUnit'])
                        market = (buy_volume*buy_price) + (sell_volume*sell_price)

                        if buy_volume < sell_volume:
                            volume = buy_volume/7
                        else:
                            volume = sell_volume/7
                        volume = round(volume)
                        volume2 = (volume*((sell_price-buy_price ) - 1.01125))/1000000
                        if volume2 > 0:
                            ratio = sell_price/buy_price - 1.01125
                            z.append(price(ratio, a, volume2, buy_price , sell_price, 1, market))
                            x += 1
                    except:
                        1 + 1

                def e_sort(thing):
                    return thing.pot_profit
                z2 = 0
                while z2 != 30:
                    print(" ")
                    z2 += 1
                x = 0
                z = sorted(z, key=e_sort, reverse=True)
                space2 = ""
                z3 = 0
                top_list = 0
                top_list_profit = 0
                for a in z:
                    if top_list != top_list_lenght:
                        top_list += 1
                        z3 += 1
                        top_list_profit += a.pot_profit
                        space1 = ""
                        space2 = ' '
                        space3 = ''
                        space4 = ''
                        space5 = ''
                        space6 = ''
                        x = 0
                        y = 0
                        x3 = 0
                        X4 = 0
                        x5 = 0
                        num3 = len(str(round(a.ratio*100, 2)))
                        num2 = len(a.name)
                        num = len(str(round(a.pot_profit/24)))
                        num4 = len(str(a.sell_price))
                        num5 = len(str(a.buy_price))
                        x5 = 13 - num5
                        space6 += ' ' * x5
                        x4 = 12 - num4
                        space5 += ' ' * x4
                        x3 = 5 - num3
                        space4 += ' ' * x3
                        y = 30 - num2
                        space2 += ' ' * y
                        x = 3 - num
                        space3 += ' ' * x
                        x = x - 3
                        space1 += ' ' * x
                        for i1 in item_id_list:

                                if i1.id == a.name:
                                    setattr(a, 'comp', i1.competitivness)
                                    setattr(a, 'comp2', i1.competitivness2)
                                    if i1.competitivness > 0:
                                        setattr(a, "other", a.pot_profit
                                                / i1.competitivness)
                                    break
                                else:
                                    setattr(a, 'comp', "Error")
                                    setattr(a, 'comp2', "Error")
                                    1 + 1

                        ratio2 = str(round(a.ratio*100, 2)) + "%"

                        print(space3 + str(round(a.pot_profit/24)) + "M   " + space1 + a.name + "  "
                              + space2 +  "  Margin"  +ratio2 + "   " + space4 + "  Sell Price " + 
                              str(a.buy_price) + "$" + space5 + "  Buy price " + str(a.sell_price) + "$" + space6 + "        Competitivness:" + str(a.comp + a.comp2) + "   P/C: " + str(round(a.other)))
                profit_potential = 0
                market_worth = 0
                for a in z:
                    profit_potential += a.pot_profit
                    market_worth += a.marketcap
                
                print(" ")
                print("Total Daily Profit Potential Of All Items: " + str(round(profit_potential)) + "M")
                print()
                print("5% Of The Hourly Profit Estimate For Currently showed items: "
                      + str(round(top_list_profit*0.05/7)) + "M")
                print(" ")
                print("Estimated Value Of All Market Transactions Hourly : " + str(round(market_worth/168000000000, 3)) + " Billion")
                print(" ")
                print("Running for " + str(round((time.time() - run_time)/60))
                      + " minutes")


            else:
                1 + 1
            cua = time.time() + 60
            while(cua > time.time()):
                time.sleep(1)
                if thread_running == False:
                    cua = 0
        else:
            1 + 1


def thang3():
    time.sleep(2)
    print(" ")
    input('press a key to end the program otherwise keep the program running: ')


if __name__ == '__main__':
    t1 = Thread(target=thang)
    t2 = Thread(target=thang2)
    t3 = Thread(target=thang3)
    t1.start()
    t2.start()
    t3.start()
    t3.join()
z = False
thread_running = False
print("end")