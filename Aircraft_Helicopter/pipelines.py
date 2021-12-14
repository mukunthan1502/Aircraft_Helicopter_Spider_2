# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline

# use uuid to create random string to append to image filename
import uuid


class CustomWikiImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None, image_number=None):
        # return request.url.split('/')[-1]
        # final string after last dot in filename is the image format
        image_format = request.url.split(".")[-1]
        # convention for file naming is image_random_string.fileformat
        return f'image_{uuid.uuid4()}.{image_format}'
