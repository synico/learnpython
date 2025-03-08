import requests
from bs4 import BeautifulSoup
import os
import json
import time
import re
import datetime
from ftplib import FTP

LOCAL_PATH = "C:/data/"

def get_all_files(ftp, path='.', parent_path=''):
    """
    递归列出 FTP 服务器上指定目录下的所有文件信息
    :param ftp: FTP 连接对象
    :param path: 当前要遍历的目录路径
    :param parent_path: 父目录路径
    :return: 包含文件信息的列表
    """
    file_info_list = []
    try:
        # 获取当前目录下的所有文件和文件夹
        items = []
        ftp.retrlines('LIST ' + path, items.append)
        for item in items:
            parts = item.split()
            name = ' '.join(parts[8:])
            full_path = f"{parent_path}/{name}" if parent_path else name
            if item.startswith('d'):
                # 如果是目录，递归调用函数继续遍历
                sub_file_info = get_all_files(ftp, f"{path}/{name}", full_path)
                file_info_list.extend(sub_file_info)
            else:
                # 如果是文件，获取其最后修改时间
                try:
                    timestamp = ftp.sendcmd('MDTM ' + f"{path}/{name}").split()[1]
                    last_modified = datetime.datetime.strptime(timestamp, '%Y%m%d%H%M%S.%f')
                except Exception as e:
                    print(f"获取文件 {full_path} 的修改时间时出错: {e}")
                    last_modified = None
                file_info = {
                    'filename': name,
                    'full_path': full_path,
                    'last_modified': last_modified
                }
                file_info_list.append((name, full_path, last_modified))
    except Exception as e:
        print(f"遍历目录 {path} 时出错: {e}")
    return file_info_list


def sort_files_by_modification_time(files):
    """
    根据文件修改时间对文件列表进行倒序排序
    :param files: 文件信息列表
    :return: 排序后的文件信息列表
    """
    return sorted(files, key=lambda x: x[2], reverse=True)


def load_downloaded_timestamps():
    """
    从文件中加载已下载文件的时间戳
    :return: 已下载文件的时间戳列表
    """
    prefix = datetime.datetime.now().strftime("%Y-%m-%d")
    dt_path = LOCAL_PATH + prefix + "/downloaded_timestamps.json"
    try: 
        directory = os.path.dirname(LOCAL_PATH + prefix)
        if directory and not os.path.exists(LOCAL_PATH + prefix):
            os.makedirs(LOCAL_PATH + prefix, exist_ok=True)
    except Exception as ex:
        print(f'初始化目录失败: {ex}')
    if os.path.exists(dt_path):
        with open(dt_path, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_downloaded_timestamp(timestamp):
    """
    将下载文件的时间戳保存到文件
    :param timestamp: 下载文件的时间戳
    """
    prefix = datetime.datetime.now().strftime("%Y-%m-%d")
    dt_path = LOCAL_PATH + prefix + "/downloaded_timestamps.json"
    downloaded_timestamps = load_downloaded_timestamps()
    if timestamp not in downloaded_timestamps:
        downloaded_timestamps.append(timestamp)
    with open(dt_path, 'w') as f:
        json.dump(downloaded_timestamps, f)


def download_file(ftp, file_url):
    """
    下载文件并保存到本地
    :param file_url: 文件的 URL
    :param filename: 文件名
    """
    try:
        prefix = datetime.datetime.now().strftime("%Y-%m-%d")
        suffix = "@" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        fname, fext = os.path.splitext(filename)
        dt_path = LOCAL_PATH + prefix + "/" + fname + suffix + fext
        # 下载文件
        with open(dt_path, 'wb') as local_file:
          ftp.retrbinary(f'RETR {file_url}', local_file.write)
        print(f"成功下载文件: {filename}")
        # 获取文件时间戳
        timestamp = None
        for fname, url, ts in get_all_files(ftp, os.path.dirname(file_url)):
            if url in file_url:
                timestamp = ts
                break
        if timestamp:
            save_downloaded_timestamp(fname + "|" + str(timestamp))
    except requests.RequestException as e:
        print(f"下载文件出错: {e}")

def get_target_folder():
    folders = []
    current_datetime = datetime.datetime.now()
    folders.append(current_datetime.strftime("%Y-%m-%d") + "/")
    if current_datetime.hour <= 8:
        # 需要拿前一天的数据
        yesterday = current_datetime - datetime.timedelta(days=1)
        folders.append(yesterday.strftime("%Y-%m-%d") + "/")
    return folders

while True:
    # 请替换为实际的 Apache 共享文件夹 URL
    ftp_host = '127.0.0.1'
    target_directory = '/image/el/'  # 要遍历的目标目录，可根据需要修改
    step1_time = time.perf_counter()
    # 加载已下载文件的时间戳
    downloaded_timestamps = load_downloaded_timestamps()
    # 获取所有文件信息
    ftp = FTP()
    try:
        ftp.connect(ftp_host, 21)
        ftp.login()
    except Exception as ex:
        print(ex)
    all_files = get_all_files(ftp, target_directory)
    # 根据修改时间对文件进行排序
    sorted_files = sort_files_by_modification_time(all_files)
    # 过滤掉已下载的文件
    filtered_files = []
    for filename, file_url, timestamp in sorted_files:
        combine_key = filename + "|" + str(timestamp)
        if combine_key and combine_key not in downloaded_timestamps:
            filtered_files.append((filename, file_url, timestamp))
    if filtered_files:
        # 最早生成的文件是排序后列表的最后一个
        earliest_file = filtered_files[-1]
        filename, file_url, _ = earliest_file
        download_file(ftp, target_directory + file_url)
    else:
        print("没有新文件可供下载。")
    step2_time = time.perf_counter()
    print(f'step elapsed time: {step2_time - step1_time} s')
    time.sleep(1)