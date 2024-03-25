from downloader import pe_downloader
from queryer import query_malware
import os


def download_malware_fam(fam_name="TrickBot", limit=20, save_folder='download',
                         unzip=False):
    """
    根据家族名称
    :param fam_name:要下载的样本家族标签
    :param limit:下载数量，最大1000
    :param save_folder: 保存路径
    :param unzip:是否解压缩
    :return:
    """
    sha256_list = query_malware(query_type='signature', query_string=fam_name, limit=limit)
    save_folder=save_folder+'/'+fam_name
    for each_sha256 in sha256_list:
        print('正在下载：', each_sha256)
        try:
            pe_downloader(sample_sha=each_sha256, save_folder=save_folder, unzip=unzip)
        except Exception as e:
            print(e, "下载失败")


if __name__ == "__main__":
    download_malware_fam(fam_name="Wapomi", limit=20, save_folder='download',
                         unzip=False)
