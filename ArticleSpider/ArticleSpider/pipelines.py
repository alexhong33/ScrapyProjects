# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
# codecs 可以避免很多编码的繁杂工作
import json
import MySQLdb
import MySQLdb.cursors


from scrapy.pipelines.images import ImagesPipeline
# 多种输出格式 包
from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi

class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item

# 自定义json文件的导出
class JsonWithEncodingPipeline(object):
    def __init__(self):
        # w 为写入的模式
        self.file = codecs.open('article.json', 'w', encoding="utf-8")
    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item
    def spider_closed(self, spider):
        self.file.close()

# 使用scrapy JsonExporter的JSON输出
class JsonExporterPipeline(object):
    # 调用scrapy提供的json export导出json文件
    def __init__(self):
        self.file = open('articleexport.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

# 自定义图片输出
class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        # result返回2个值 一个boolean 返回成功, 一个Tulpes 返回一个字典 提取其中的path路径
        for ok, value in results:
            image_file_path = value["path"]
        item["front_image_path"] = image_file_path
        return item
        pass


# 采用同步机制 写入MySQL
class MysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', 'admin', 'article_spider', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into jobbole_article(title, url, create_date, fav_nums)
            VALUES (%s, %s, %s, %s)
        """
        # execute + commit 同步操作, 大数据插入时 会堵塞
        self.cursor.execute(insert_sql, (item["title"], item["url"], item["create_date"], item["fav_nums"]))
        self.conn.commit()


# 采用异步机制 写入MySQL
class MysqlTwistedPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            # 参数名称是固定的
            host=settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            passwd = settings["MYSQL_PASSWORD"],
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

        return cls(dbpool)
        pass

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        # 处理异常
        query.addErrback(self.handle_error)

    def handle_error(self, failure):
        # 处理异步插入的异常
        print(failure)

    def do_insert(self, cursor, item):
        # 执行具体的插入
        insert_sql = """
                    insert into jobbole_article(title, url, create_date, fav_nums)
                    VALUES (%s, %s, %s, %s)
                """
        # execute + commit 同步操作, 大数据插入时 会堵塞
        cursor.execute(insert_sql, (item["title"], item["url"], item["create_date"], item["fav_nums"]))

        pass