# ScrapyProjects

# Scrapy学习笔记


### Spider架构 
1. Scrapy Engine 引擎
2. Scheduler 调度器
3. Downloader 下载器
4. Spider 爬虫
5. Item Pipeline 管道
6. Downloader MiddleWares 下载中间件
7. Spider MiddleWares Sipder中间件

### 制作Scrapy爬虫4步走
1. 新建项目 (scrapy startproject xxx): 新建一个新的爬虫项目
2. 明确目标 (编写items.py, pipelines.py和setting.py): 明确你想要抓取的目标和进一步处理数据
3. 制作爬虫 (spiders/xxspider.py): 制作爬虫开始爬取网站
4. 存储内容 (pipeline.py): 设计管道存储爬取内容

v1.
1.制作福田表格
2.单链接爬取


v2.
1.多连接一起爬取
2.自动切换表格导入

