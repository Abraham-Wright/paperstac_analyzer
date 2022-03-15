import csv
import os
import numpy as np
import matplotlib.pyplot as plt

i_rate = .005/12
managment_fee = 20
buyers_fee = 500

for x in os.listdir():
    if x.endswith(".csv"):
        file_name = x

assets = []
with open(file_name, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        assets.append(row)

first = True
i, n = 0, 0
for asset in assets:
    if first: first = False
    else: 
        i = float(asset[11][0:-1])/1200
        try: n = float(asset[22])
        except: n = '??'
        month_pay = asset[30][1:]
        try: UPB = float(asset[10].replace('$','').replace(',',''))
        except: UPB = 0

        try: list_price = float(asset[5].replace('$','').replace(',',''))
        except: list_price = 0

        try: 
            NPW = (((1+i_rate)**n-1)/(i_rate*(1+i_rate)**n))
            NPW *= (float(month_pay.replace(',','')) - managment_fee)
            NPW -= buyers_fee
        except: NPW = 0

        try: disc = NPW/list_price
        except: disc = 0

        print(f'{NPW:12.2f}     {list_price:12.2f}      {disc:.2f}')
