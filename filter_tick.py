import sys
import datetime

def combine_date_time(date_str, time_str) :
    x=datetime.datetime.strptime(date_str+time_str, "%Y%m%d%H%M%S")
    return x.strftime("%Y/%m/%d,%H:%M:%S")

if len(sys.argv) < 2 :
    print("Usage: exe file contract_type")

file = open(sys.argv[1], 'r', encoding='big5')
contract_type_str = sys.argv[2]
contract_month_str = ""
prev_tick_price = 0

while True:
    line = file.readline()
    if not line :
        break

    i = line.strip();
    t=i.split(',')
    if contract_type_str == t[1].strip() :
        if contract_month_str == "" and t[2].strip().find('W') == -1:
            contract_month_str = t[2].strip()

        if contract_month_str == t[2].strip() and prev_tick_price != t[4].strip() :
            prev_tick_price = t[4].strip()
            date_time_str=combine_date_time(t[0].strip(), t[3].strip())
            print("{0},{1},{1},{1},{1},0,{2},{3}".format(date_time_str, t[4].strip(), contract_type_str, contract_month_str))

