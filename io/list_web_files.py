import requests
from bs4 import BeautifulSoup
import os
import json
import time


def get_all_files(url):
    """
    递归获取指定 URL 下所有文件的 URL 列表
    :param url: 基础 URL
    :return: 文件 URL 列表
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        all_files = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and not href.startswith('/image') and not href.startswith('/el') and not href.startswith('?'):
                if href.endswith('/'):
                    sub_url = url.rstrip('/') + '/' + href
                    all_files.extend(get_all_files(sub_url))
                else:
                    file_url = url.rstrip('/') + '/' + href
                    all_files.append(file_url)
        return all_files
    except requests.RequestException as e:
        print(f"请求出错: {e}")
        return []


def get_file_modification_time(file_url):
    """
    获取文件的修改时间（Unix epoch 格式）
    :param file_url: 文件的 URL
    :return: 文件修改时间的 Unix epoch 时间戳，出错则返回 None
    """
    try:
        response = requests.head(file_url)
        response.raise_for_status()
        last_modified = response.headers.get('Last-Modified')
        if last_modified:
            return time.mktime(time.strptime(last_modified, '%a, %d %b %Y %H:%M:%S %Z'))
        return None
    except requests.RequestException as e:
        print(f"获取文件修改时间出错: {e}")
        return None


def sort_files_by_modification_time(files):
    """
    根据文件修改时间对文件列表进行倒序排序
    :param files: 文件 URL 列表
    :return: 排序后的文件 URL 列表
    """
    file_with_time = [(file, get_file_modification_time(file)) for file in files]
    file_with_time = [(file, time) for file, time in file_with_time if time is not None]
    sorted_files = sorted(file_with_time, key=lambda x: x[1], reverse=True)
    return [file for file, _ in sorted_files]


def load_downloaded_timestamps():
    """
    从文件中加载已下载文件的时间戳
    :return: 已下载文件的时间戳列表
    """
    if os.path.exists('downloaded_timestamps.json'):
        with open('downloaded_timestamps.json', 'r') as f:
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
    downloaded_timestamps = load_downloaded_timestamps()
    if timestamp not in downloaded_timestamps:
        downloaded_timestamps.append(timestamp)
    with open('downloaded_timestamps.json', 'w') as f:
        json.dump(downloaded_timestamps, f)


def download_file(file_url):
    """
    下载文件并保存到本地
    :param file_url: 文件的 URL
    """
    try:
        response = requests.get(file_url)
        response.raise_for_status()
        file_name = os.path.basename(file_url)
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print(f"成功下载文件: {file_name}")
        timestamp = get_file_modification_time(file_url)
        if timestamp:
            save_downloaded_timestamp(timestamp)
    except requests.RequestException as e:
        print(f"下载文件出错: {e}")


if __name__ == "__main__":
    # 请替换为实际的 Web 服务器共享文件夹 URL
    web_server_url = "http://127.0.0.1:11111/image/el"
    # 加载已下载文件的时间戳
    step1_time = time.perf_counter()
    downloaded_timestamps = load_downloaded_timestamps()
    # 获取所有文件
    step2_time = time.perf_counter()
    print(f'step1 elapsed time: {step2_time - step1_time} s')
    all_files = get_all_files(web_server_url)
    # 根据修改时间对文件进行排序
    step3_time = time.perf_counter()
    print(f'step2 elapsed time: {step3_time - step2_time} s')
    sorted_files = sort_files_by_modification_time(all_files)
    step4_time = time.perf_counter()
    print(f'step3 elapsed time: {step4_time - step3_time} s')
    # 过滤掉已下载的文件
    filtered_files = []
    for file in sorted_files:
        timestamp = get_file_modification_time(file)
        if timestamp and timestamp not in downloaded_timestamps:
            filtered_files.append(file)
    step5_time = time.perf_counter()
    print(f'step4 elapsed time: {step5_time - step4_time} s')
    if filtered_files:
        # 最早生成的文件是排序后列表的最后一个
        earliest_file = filtered_files[-1]
        download_file(earliest_file)
    else:
        print("没有新文件可供下载。")