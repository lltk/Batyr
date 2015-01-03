# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from tatoeba.items import TatoebaItem

mapping = {'de' : 'deu', 'nl' : 'nld', 'es' : 'spa', 'en' : 'eng', 'ru' : 'rus', 'fr' : 'fra', 'pt' : 'por', 'eo' : 'epo', 'pl' : 'pol', 'he' : 'heb', 'th' : 'tha', 'ko' : 'kor', 'zh' : 'cmn'}

class AudioSpider(CrawlSpider):

	name = 'TatoebaAudio'
	allowed_domains = ['tatoeba.org']

	def __init__(self, language = 'de', *args, **kwargs):
		super(AudioSpider, self).__init__(*args, **kwargs)
		if language == '*':
			for language in mapping.keys():
				self.start_urls += ['http://tatoeba.org/deu/sentences/with_audio/%s' % (language, )]
		else:
			self.start_urls += ['http://tatoeba.org/deu/sentences/with_audio/%s' % (mapping[language], )]
		self.language = language

	rules = (
		Rule(LinkExtractor(allow = ('page:\d', )), callback = 'parse_items', follow = True),
	)

	def parse_items(self, response):
		for element in response.xpath('//div[contains(@class, "mainSentence")]'):
			item = TatoebaItem()
			item['text'] = ''.join(element.xpath('div/a/text()').extract()).encode('utf-8')
			item['audio'] = ''.join(element.xpath('a/@href').extract()).encode('utf-8')
			item['language'] = ''.join(element.xpath('img/@alt').extract()).encode('utf-8')
			item['id'] = ''.join(element.xpath('img/@id').extract()).replace('flag_', '').encode('utf-8')
			yield item
