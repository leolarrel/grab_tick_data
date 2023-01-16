import sys
import os
import urllib.request
import zipfile
import datetime

trade_url_part = "https://www.taifex.com.tw/file/taifex/Dailydownload/DailydownloadCSV/"

def unzip_grab() :
    print("unzip")
    x = zipfile.ZipFile("grab.zip","r")
    x.extractall(".")
    del x

def grab_hook_progress(block_num, block_size, total_size):
    pass
#   sys.stdout.write('\rDownloading %.1f%%' % (float(block_num * block_size) / float(total_size) * 100.0))
#   sys.stdout.flush()

def grab_trade_data(year, month, day) :
    url = f"{trade_url_part}Daily_{year}_{month}_{day}.zip"
    print(f"grab URL: {url}")

    try :
        a,b = urllib.request.urlretrieve(url, 'grab.zip', grab_hook_progress)
        #print("grab data type is: " + b.get_content_type())
        if 'application/zip' == b.get_content_type() :
            print("grab ok")
            return True
        else :
            raise Exception;

    except urllib.error.URLError as e :
        print(f"URL error {e}")
        return False
    except Exception :
        print("failed")
        return False

def grab_oper(the_d) :
    csv_file_name = "Daily_{0}_{1}_{2}.csv".format(the_d.strftime("%Y"), the_d.strftime("%m"), the_d.strftime("%d"))
    if os.path.exists(csv_file_name) :
        print(f"{csv_file_name} already exists,skip grab")
        return 'Ignore'

    print(f"{csv_file_name} nod found, {the_d.strftime('%A')}")
    if grab_trade_data(the_d.strftime("%Y"), the_d.strftime("%m"), the_d.strftime("%d")) == True :
        unzip_grab()
        return 'Success'
    else :
        return 'Fail'

if __name__ == '__main__' :
    try :
        day_diff = int(sys.argv[1])

    except (IndexError, ValueError) :
        print("usage: grab.py <how much day>")
        exit()

    x = datetime.datetime.now()
    gen = ((x - datetime.timedelta(days=(day_diff - i))) for i in range(day_diff + 1))
    for i in gen :
        grab_oper(i)
