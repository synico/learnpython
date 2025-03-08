import requests
from bs4 import BeautifulSoup
import os
import json
import time
import re
import datetime

LOCAL_PATH = "C:/data/"

def get_all_files(url):
    """
    递归获取指定 URL 下所有文件的信息
    :param url: 基础 URL
    :return: 文件信息列表，每个元素为 (文件名, 文件 URL, 修改时间戳, 文件大小)
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        all_files = []
        for tr in soup.find_all('tr')[3:]:  # 跳过表头和前两个导航行
            td_list = tr.find_all('td')
            if len(td_list) >= 4:
                link = td_list[1].find('a')
                if link:
                    filename = link.text
                    if filename.endswith('/'):
                        # 如果是目录，递归获取子目录下的文件
                        for folder in get_target_folder():
                            if folder in url or folder == filename:
                                sub_url = url.rstrip('/') + '/' + filename
                                all_files.extend(get_all_files(sub_url))
                    else:
                        file_url = url.rstrip('/') + '/' + filename
                        date_str = td_list[2].text.strip()
                        size_str = td_list[3].text
                        try:
                            timestamp = time.mktime(time.strptime(date_str, '%Y-%m-%d %H:%M'))
                        except ValueError:
                            timestamp = None
                        try:
                            size = int(re.sub(r'[^\d]', '', size_str))
                        except ValueError:
                            size = None
                        all_files.append((filename, file_url, timestamp, size))
        return all_files
    except requests.RequestException as e:
        print(f"请求出错: {e}")
        return []


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


def download_file(file_url, filename):
    """
    下载文件并保存到本地
    :param file_url: 文件的 URL
    :param filename: 文件名
    """
    try:
        response = requests.get(file_url)
        response.raise_for_status()
        prefix = datetime.datetime.now().strftime("%Y-%m-%d")
        suffix = "@" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        fname, fext = os.path.splitext(filename)
        dt_path = LOCAL_PATH + prefix + "/" + fname + suffix + fext
        with open(dt_path, 'wb') as f:
            f.write(response.content)
        print(f"成功下载文件: {filename}")
        # 获取文件时间戳
        timestamp = None
        for fname, url, ts, _ in get_all_files(os.path.dirname(file_url)):
            if url == file_url:
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
    apache_url = "http://127.0.0.1:11111/image/el/"
    step1_time = time.perf_counter()
    # 加载已下载文件的时间戳
    downloaded_timestamps = load_downloaded_timestamps()
    # 获取所有文件信息
    all_files = get_all_files(apache_url)
    # 根据修改时间对文件进行排序
    sorted_files = sort_files_by_modification_time(all_files)
    # 过滤掉已下载的文件
    filtered_files = []
    for filename, file_url, timestamp, size in sorted_files:
        combine_key = filename + "|" + str(timestamp)
        if combine_key and combine_key not in downloaded_timestamps:
            filtered_files.append((filename, file_url, timestamp, size))
    if filtered_files:
        # 最早生成的文件是排序后列表的最后一个
        earliest_file = filtered_files[-1]
        filename, file_url, _, _ = earliest_file
        download_file(file_url, filename)
    else:
        print("没有新文件可供下载。")
    step2_time = time.perf_counter()
    print(f'step elapsed time: {step2_time - step1_time} s')
    time.sleep(1)