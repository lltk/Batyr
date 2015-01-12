# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher

class JsonWriterPipeline(object):

	def __init__(self):
		self.file = open('items.json', 'wb')

	def process_item(self, item, spider):
		line = json.dumps(dict(item)) + "\n"
		self.file.write(line)
		return item

class JsonExportPipeline(object):

	def __init__(self):
		dispatcher.connect(self.spider_opened, signals.spider_opened)
		dispatcher.connect(self.spider_closed, signals.spider_closed)
		self.files = {}

	def spider_opened(self, spider):
		f = open('items.json', 'w+b')
		self.files[spider] = f
		self.exporter = JsonItemExporter(f)
		self.exporter.start_exporting()

	def spider_closed(self, spider):
		self.exporter.finish_exporting()
		f = self.files.pop(spider)
		f.close()

	def process_item(self, item, spider):
		self.exporter.export_item(item)
		return item
