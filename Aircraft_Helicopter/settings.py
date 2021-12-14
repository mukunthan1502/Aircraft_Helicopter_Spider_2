
BOT_NAME = 'Aircraft_Helicopter'

SPIDER_MODULES = ['Aircraft_Helicopter.spiders']
NEWSPIDER_MODULE = 'Aircraft_Helicopter.spiders'
# ITEM_PIPELINES={'scrapy.pipelines.images.ImagesPipeline':1}
# add next 2 lines for images
ITEM_PIPELINES = {'Aircraft_Helicopter.pipelines.CustomWikiImagesPipeline': 1}
# folder name to store scraped images
IMAGES_STORE = 'Scraped_Images'

ROBOTSTXT_OBEY = True
