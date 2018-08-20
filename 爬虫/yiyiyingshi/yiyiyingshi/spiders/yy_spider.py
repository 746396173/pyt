import scrapy

class YySpoder(scrapy.Spider):
    name = "yy"
    allowed_domains = ['m.22k.im']
    start_urls = [
        "http://m.22k.im/x1y1",
    ]

    def parse(self, response):
        hrefs = ''#视频页面地址
        for res in response.xpath('//*[@id="j1"]/a/@href').extract():
            href = r'http://z.syasn.com/xy/'+str(res)+r'.mp4?end=1080&dz=k.syasn.com'
            hrefs = hrefs+str(href)+'\n'
            #print(hrefs)

        with open("url2","a") as f:
            f.write(hrefs)



if __name__ == "__main__":
    pass
