# -*- coding: utf-8 -*-

# Scrapy settings for packt project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'packt'

SPIDER_MODULES = ['packt.spiders']
NEWSPIDER_MODULE = 'packt.spiders'

MAIL_FROM = 'csmartins.ufrj@gmail.com'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'packt (+http://www.yourdomain.com)'
