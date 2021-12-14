import scrapy


class AircraftHelicopterSpider(scrapy.Spider):
    name = 'aircraft_helicopter'
    start_urls = [
        'https://commons.wikimedia.org/wiki/Helicopter',
        'https://commons.wikimedia.org/wiki/Category:AH-64_Apache',
        'https://en.wikipedia.org/wiki/Boeing_AH-64_Apache',
        'https://commons.wikimedia.org/wiki/Category:Airbus_Helicopters_H215_Super_Puma',
        'https://en.wikipedia.org/wiki/Eurocopter_AS332_Super_Puma',
        'https://commons.wikimedia.org/wiki/Category:Aircraft',
        'https://en.wikipedia.org/wiki/Boeing_Commercial_Airplanes',
        'https://commons.wikimedia.org/wiki/Category:Boeing_aircraft'
        'https://en.wikipedia.org/wiki/Boeing_787_Dreamliner',
        'https://en.wikipedia.org/wiki/Boeing_747',
        'https://en.wikipedia.org/wiki/Boeing_777',
        'https://en.wikipedia.org/wiki/Airbus_A380',
        'https://en.wikipedia.org/wiki/Airbus_A350',
        'https://en.wikipedia.org/wiki/McDonnell_Douglas_F-15_Eagle',
        'https://commons.wikimedia.org/wiki/McDonnell_Douglas_F-15_Eagle',
        'https://en.wikipedia.org/wiki/McDonnell_Douglas_F-15E_Strike_Eagle',
        'https://military-history.fandom.com/wiki/F-15_Eagle_family',
        'https://en.wikipedia.org/wiki/General_Dynamics_F-16_Fighting_Falcon',
    ]

    def parse(self, response):

        # extract all image
        raw_image_urls = response.css('.image img ::attr(src)').getall()
        clean_image_urls = []

        # I only want to deal with jpg, somehow had issue creating using scrip to create
        # tfRecord file when other formats where present with annotation
        for img_url in raw_image_urls:
            if img_url.split('.')[-1] == 'jpg':
                clean_image_urls.append(response.urljoin(img_url))

        yield {
            'image_urls': clean_image_urls
        }
