from ftplib import FTP
from datetime import datetime

def list_files_recursively(ftp, path='.', parent_path=''):
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
                sub_file_info = list_files_recursively(ftp, f"{path}/{name}", full_path)
                file_info_list.extend(sub_file_info)
            else:
                # 如果是文件，获取其最后修改时间
                try:
                    timestamp = ftp.sendcmd('MDTM ' + f"{path}/{name}").split()[1]
                    last_modified = datetime.strptime(timestamp, '%Y%m%d%H%M%S.%f')
                except Exception as e:
                    print(f"获取文件 {full_path} 的修改时间时出错: {e}")
                    last_modified = None
                file_info = {
                    'filename': name,
                    'last_modified': last_modified,
                    'full_path': full_path
                }
                file_info_list.append(file_info)
    except Exception as e:
        print(f"遍历目录 {path} 时出错: {e}")
    return file_info_list

def main():
    # 配置 FTP 服务器信息
    ftp_host = '127.0.0.1'
    target_directory = '/image/el/'  # 要遍历的目标目录，可根据需要修改

    # 连接到 FTP 服务器
    try:
        ftp = FTP(ftp_host)
        ftp.connect(ftp_host, 21)
        ftp.login()
        # 列出指定目录下的所有文件信息
        file_info_list = list_files_recursively(ftp, target_directory)
        # 输出文件信息
        for info in file_info_list:
            print(f"文件名: {info['filename']}")
            print(f"最后修改时间: {info['last_modified']}")
            print(f"全路径: {info['full_path']}")
            print("-" * 50)
        # 关闭 FTP 连接
        ftp.quit()
    except Exception as e:
        print(f"连接到 FTP 服务器时出错: {e}")

if __name__ == "__main__":
    main()