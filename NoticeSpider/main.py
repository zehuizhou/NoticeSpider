from scrapy import cmdline

# cmdline.execute('scrapy crawl notice_spider'.split())
cmdline.execute("scrapy crawl notice_spider -o info.csv -t csv".split())

