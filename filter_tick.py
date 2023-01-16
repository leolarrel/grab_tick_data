import sys
import datetime

if len(sys.argv) < 2 :
    print("Usage: exe file contract_type")

contract_type_str = sys.argv[2]
contract_month_str = ""
prev_tick_price = 0

with open(sys.argv[1], 'r', encoding='big5') as file :
    for line in file :
        i = line.strip().split(',');
        if contract_type_str != i[1].strip() :
            continue

        t = i[2].strip()
        if contract_month_str == "" and \
           'W' not in t and '/' not in t:
               contract_month_str = t

        if contract_month_str == t and prev_tick_price != i[4].strip() :
            prev_tick_price = i[4].strip()
            j = datetime.datetime.strptime(f"{i[0].strip()} {i[3].strip()}", "%Y%m%d %H%M%S")
            k = j.strftime("%Y/%m/%d,%H:%M:%S")
            print(f"{j.strftime('%Y/%m/%d,%H:%M:%S')},{prev_tick_price},{prev_tick_price},{prev_tick_price},{prev_tick_price},0,{contract_type_str},{contract_month_str}")
