import time
import os
# from smb.SMBConnection import SMBConnection
import shutil
import datetime
from pathlib import Path

import configparser
config = configparser.ConfigParser()
path = '/home/nvidia/workplace/el_workplace_test/file_watch/code/get_ip_img/config.ini'
config.read(path)
ip = config['adress']['ip']

username = config['adress']['username']
password = config['adress']['password']
root_path = config['adress']['root_path']
sub_path = config['adress']['sub_path']
local_dir = config['adress']['local_dir']


def make_file(local_file):
    today = datetime.datetime.now()
    olddate = today + datetime.timedelta(days=-1)
    olddate_2 = today + datetime.timedelta(days=-2)
    tomorrow = today + datetime.timedelta(days=1)
    localtime = today.strftime("%Y-%m-%d %H:%M:%S")
    tomorrowtime = tomorrow.strftime("%Y-%m-%d %H:%M:%S")
    oldtime = olddate.strftime("%Y-%m-%d %H:%M:%S")
    oldtime_2 = olddate_2.strftime("%Y-%m-%d %H:%M:%S")
    year = localtime[:4]
    month = localtime[5:7]
    day = localtime[8:10]
    hour = localtime[11:13]

    old_year = oldtime[:4]
    old_month = oldtime[5:7]
    old_day = oldtime[8:10]

    old_year_2 = oldtime_2[:4]
    old_month_2 = oldtime_2[5:7]
    old_day_2 = oldtime_2[8:10]

    tomorrow_year = tomorrowtime[:4]
    tomorrow_month = tomorrowtime[5:7]
    tomorrow_day = tomorrowtime[8:10]
    
    new_file_name = year + "_" + month + "/" + month + "_" + day
    old_file_name = old_year + "_" + old_month + "/" + old_month + "_" + old_day
    tomorrow_path = tomorrow_year + "_" + tomorrow_month + "_" + tomorrow_day
    file_name_0 = year + "_" + month + "_" + day
    file_name_1 = old_year + "_" + old_month + "_" + old_day
    file_name_2 = old_year_2 + "_" + old_month_2 + "_" + old_day_2
    if int(hour) >= 8:
        new_day_file = local_file + year + "_" + month + "/" + month + "_" + day
        tomorrow_file = local_file + tomorrow_year + "_" + tomorrow_month + "/" + tomorrow_month + "_" + tomorrow_day
        os.makedirs(Path(new_day_file), exist_ok=True)
        os.makedirs(Path(tomorrow_file), exist_ok=True)
        return new_file_name, file_name_0, file_name_1, tomorrow_path, file_name_2
    else:
        new_day_file = local_file + old_year + "_" + old_month + "/" + old_month + "_" + old_day
        tomorrow_file = local_file + year + "_" + month + "/" + month + "_" + day
        os.makedirs(new_day_file, exist_ok=True)
        os.makedirs(Path(tomorrow_file), exist_ok=True)
        return old_file_name, file_name_0, file_name_1, tomorrow_path, file_name_2

def deleteDirectory(smbclient, root_path, directory):
    try:
        smbclient.deleteDirectory(root_path, directory)
    except Exception as exp:
        print("delete directory failed: %s" % directory)
        pass    
    
while(True):
    try:
        smb_c =  SMBConnection(username, password, "nvidia", "share", is_direct_tcp=True)
        smb_c.connect(ip, port=445)
        local_file_name, file_name_0, file_name_1, tomorrow_path, file_name_2 = make_file(local_dir)
        pathlist0 = smb_c.listPath(root_path, sub_path)
        file_list = []
        for item0 in pathlist0:
            f_name0 = item0.filename
            if (f_name0 != ".") and (f_name0 != ".."):
                file_list.append(f_name0)
        if file_name_2 in file_list:
            #smb_c.deleteDirectory(root_path, sub_path + file_name_2)
            deleteDirectory(smb_c, root_path, sub_path + file_name_2)
        for file_name_item in [file_name_0, file_name_1, tomorrow_path]:
            if file_name_item in file_list:
                pathlist = smb_c.listPath(root_path, sub_path + file_name_item)
                for item in pathlist:
                    f_name = item.filename
                    if (f_name != ".") and (f_name != "..") and (f_name.endswith(".jpg")):
                        img_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        img_sub_name = img_time[:4] + img_time[5:7] + img_time[8:10] + img_time[11:13] + img_time[14:16] + img_time[17:19]
                        # img_sub_name = img_time[-5:-3] + img_time[-2:]
                        img_name = f_name.split(".jpg")[0] + "@" + img_sub_name + ".jpg"
                        tmp_download_path = "tmp.jpg"
                        time.sleep(1)
                        f = open(tmp_download_path, 'wb')
                        download_path = sub_path + file_name_item +  "/" + f_name
                        file_attr, filesize = smb_c.retrieveFile(root_path, download_path, f)
                        f.close()
                        time.sleep(0.5)
                        smb_c.deleteFiles(root_path, download_path)
                        # shutil.copy(tmp_download_path, os.path.join(local_dir, local_file_name, img_name.split(".jpg")[0] +  "_" + str(time.time()) + ".jpg"))
                        shutil.copy(tmp_download_path, os.path.join(local_dir, local_file_name, img_name))
                        os.remove(tmp_download_path)
        #smb_c.close()
    except Exception as exp:
        # print(exp)
        pass
    finally:
        smb_c.close()
        
