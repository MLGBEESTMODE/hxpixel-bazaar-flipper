import math
import time
import requests
from threading import Thread

print("After setting list lenght and refresh time you can change settings")
print("press 0 to end the program, and to sort the list press 1 by potential profit, 2 name, 3 margin, 4 sell price, 5 buy price")
print("6 volume, 7 by competitivness and 8 for P/C, also type 1 after the first number too sort backward and 1 too sort forward")

print(" ")
setting_loop = True
while(setting_loop):
    try:
        top_list_lenght = int(input("Enter the amount of items to show: "))
        setting_loop = False
    except:
        print("entered wrong format")

while(setting_loop != True):
    try:
        refresh = int(input("Enter the amount seconds to wait before refreshing list: "))
        setting_loop = True
    except:
        print("entered wrong format")

setting = 1
setting1 = 1
def e_sort(thing):
    if(setting == 1):
        return thing.pot_profit
    elif(setting == 2):
        return thing.name
    elif(setting == 3):
          return thing.ratio
    elif(setting == 4):
          return thing.sell_price  
    elif(setting == 5):
        return thing.buy_price
    elif(setting == 6):
        return thing.volume    
    elif(setting == 7):
        return thing.comp3         
    elif(setting == 8):
        return thing.p_c 
# def e_sort(thing):
#     return thing.pot_profit





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
    def __init__(self,  ratio, name, pot_profit, sell_price, buy_price, other, marketcap, comp, comp2, comp3, p_c, volume):
        self.ratio = ratio
        self.name = name
        self.pot_profit = pot_profit
        self.sell_price = sell_price
        self.buy_price = buy_price
        self.other = other
        self.marketcap = marketcap
        self.comp = comp
        self.comp2 = comp2
        self.comp3 = comp3
        self.p_c = p_c
        self.volume = volume

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
            timer2 = time.time() + refresh
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
                            z.append(price(ratio, a, volume2, buy_price , sell_price, 1, market, 0, 0, 0, 0, volume))
                            x += 1
                    except:
                        1 + 1

                z2 = 0
                while z2 != 30:
                    print(" ")
                    z2 += 1
                x = 0

                z = sorted(z, key=e_sort, reverse=setting1)
                space2 = ""
                z3 = 0
                top_list = 0
                top_list_profit = 0
                print("Potential profit")
                for a in z:
                    if top_list != top_list_lenght:
                        top_list += 1
                        z3 += 1
                        top_list_profit += a.pot_profit
                        ratio2 = str(round(a.ratio*100, 2)) + "%"
                        space1 = ' ' * ( 10 - len(str(round(a.pot_profit/24))))
                        space2 = ' ' * ( 30 - len(a.name))
                        space3= ' ' * ( 8 - len(str(ratio2)))
                        space4= ' ' * ( 10 - len(str(round(a.buy_price))))
                        space5= ' ' * ( 10 - len(str(round(a.sell_price))))
                        space6= ' ' * ( 5 - len(str(round(a.volume))))
                        space7= ' ' * ( 10 - len(str(round(a.comp3))))
                        space8 = ' ' * ( 10 - len(str(round(a.p_c))))
                        for i1 in item_id_list:
                            if i1.id == a.name:
                                a.comp = i1.competitivness
                                a.comp2 = i1.competitivness2
                                a.comp3 = a.comp + a.comp2
                                if i1.competitivness > 0:
                                    a.p_c = a.pot_profit/ a.comp3
                        print("  " + str(round(a.pot_profit/24)) + "M   "  + space1  + a.name + "  " + space2+  "  Margin"   + ratio2 + "   " + space3 + "  Sell Price " + str(a.buy_price) + "$"  + space4  + "  Buy price " + str(a.sell_price) + "$"      +space5 + "  volume: " + str(a.volume)  + space6 +   "        Competitivness: " + str(a.comp3) + space7 + "   P/C: " + str(round(a.p_c)) + space8)
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
            cua = time.time() + refresh
            while(cua > time.time()):
                time.sleep(1)
                if thread_running == False:
                    cua = 0
        else:
            1 + 1


def thang3():
    global setting
    global setting1
    time.sleep(2)
    print(" ")
    while(True):
        try:
            a = input("Enter numbers to change settings or exit: ")
            if(a[0] == '0'):
                break
            x = 0
            if(int(a[0]) < 8 or int(a[0]) > 0):
                setting = int(a[0])
                x += 1
                if(int(a[1]) == 0 or int(a[1]) == 1):
                    setting1 = int(a[1])
                    x += 2
                else:
                    print("entered wrong number or format")
            else:
                print("entered wrong number or format")
            if(x == 1):
                print("First Setting Change")
            if(x == 2):
                print("Second Setting Changed")
            if(x == 3):
                print("Both Setting Changed")
        except:
            print("entered wrong number or format")
            




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