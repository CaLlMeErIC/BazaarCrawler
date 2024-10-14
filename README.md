# BazaarCrawler
用于恶意软件样本下载，从MalwareBazaar上爬取数据

直接运行BazaarCrawler即可，其中fam_name是需要下载的恶意软件家族名

downloader是根据sha256下载样本文件

queryer是根据输入标签/家族名 批量获取sha256用于下载
其他细节在博客里：https://blog.csdn.net/qq_43199509/article/details/137021258

# 更多的api编写细节:

https://bazaar.abuse.ch/api/ 和 https://bazaar.abuse.ch/browse/
