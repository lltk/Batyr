# -*- coding: utf-8 -*-

# Scrapy settings for tatoeba project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tatoeba'

SPIDER_MODULES = ['tatoeba.spiders']
NEWSPIDER_MODULE = 'tatoeba.spiders'

# ITEM_PIPELINES = {
# 	'tatoeba.pipelines.JsonExportPipeline': 100,
# }

DOWNLOAD_DELAY = 2.0

FEED_URI = 'tatoeba/data/%(language)s.json'
FEED_FORMAT = 'json'
FEED_STORE_EMPTY = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tatoeba (+http://www.yourdomain.com)'
