# Scrapy settings for euro_million project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import sys

sys.path.append("/var/www/euromillion")

BOT_NAME = 'euro_million'

SPIDER_MODULES = ['euro_million.spiders']
NEWSPIDER_MODULE = 'euro_million.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'euro_million (+http://www.yourdomain.com)'
