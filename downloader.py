#!/usr/bin/env python3
import requests
import os
import pyzipper

__author__ = "Corsin Camichel"
__copyright__ = "Copyright 2020, Corsin Camichel"
__license__ = "Creative Commons Attribution-ShareAlike 4.0 International License."
__version__ = "1.0"
__email__ = "cocaman@gmail.com"


def pe_downloader(sample_sha: str, save_folder='./', unzip=False):
    """
    根据sha256下载样本，默认zip格式不解压
    :param sample_sha:文件sha256
    :param save_folder:保存的路径
    :param unzip:是否解压
    :return: True/False 表示下载是否成功
    """
    if len(sample_sha) != 64:
        print(sample_sha, "不是sha256")
        return False

    unzip_password = b'infected'
    headers = {'API-KEY': ''}

    if not save_folder.endswith('/'):
        save_folder += '/'

    if not os.path.exists(save_folder):
        # 如果保存目录不存在则创建
        os.makedirs(save_folder)
    data = {
        'query': 'get_file',
        'sha256_hash': sample_sha,
    }
    if os.path.exists(save_folder + sample_sha + '.zip') or os.path.exists(save_folder+sample_sha):
        print("该样本已存在")
        return False

    response = requests.post('https://mb-api.abuse.ch/api/v1/', data=data, timeout=15, headers=headers,
                             allow_redirects=True)
    if 'file_not_found' in response.text:
        print("Error: 未找到样本")
        return False

    open(save_folder + sample_sha + '.zip', 'wb').write(response.content)
    if unzip:
        with pyzipper.AESZipFile(save_folder + sample_sha + ".zip") as zf:
            zf.pwd = unzip_password
            zf.extractall(save_folder)
            print("样本 \"" + sample_sha + "\" 下载解压成功.")
        os.remove(save_folder + sample_sha + '.zip')
    else:
        print("样本 \"" + sample_sha + "\" 下载成功.")

    return True


if __name__ == "__main__":
    pe_downloader("adffd52446d0d94c4f726205482a0c062248d6eb35948df937336957cf747db8",
                  save_folder='testdownload/', unzip=False)
