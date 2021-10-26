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
    url=trade_url_part + "Daily_{0}_{1}_{2}.zip".format(year, month, day)
    print("will grab Daily_{0}_{1}_{2}.zip\n".format(year, month, day) + "URL:" + url)

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
        print(f"failed")
        return False

if __name__ == '__main__' :
    try :
        prev_day_diff=int(sys.argv[1]) - 1
        x=datetime.date.today()
    except (IndexError, ValueError) :
        print ("usage: grab.py <how much day>")
        exit()

    while prev_day_diff > -1:
        y=datetime.timedelta(days=prev_day_diff)
        prev=x-y

        csv_file_name="Daily_{0}_{1}_{2}.csv".format(prev.strftime("%Y"), prev.strftime("%m"), prev.strftime("%d"))
        if os.path.exists(csv_file_name) :
            print("[" + csv_file_name + "] already exists,skip grab")
        else:
            print("[" + csv_file_name + "] nod found, weekday is " + prev.strftime("%A"))
            if grab_trade_data(prev.strftime("%Y"), prev.strftime("%m"), prev.strftime("%d")) == True :
                unzip_grab()

        prev_day_diff -= 1
        del y
        del prev

