import codecs
import re

from lxml import html
from PageTemplates.OverstockItem import OverstockItems
from PageTemplates.RtvsloItem import RtvsloItem
from PageTemplates.MimovrsteItem import MimovrsteItems

class XPathExtraction():

    def __init__(self, rtvslo_pages=[], overstock_pages=[], mimovrste_pages=[]):
        self.rtvslo_pages = rtvslo_pages
        self.overstock_pages = overstock_pages
        self.mimovrste_pages = mimovrste_pages

    def RtvsloExtraction(self):
        items = []
        for page in self.rtvslo_pages:
            pageContent = codecs.open(page, 'r', encoding='utf-8', errors='ignore').read()
            print(pageContent)
            break
            tree = html.fromstring(pageContent)

            author = str(tree.xpath('//*[@id="main-container"]/div[3]/div/div[1]/div[1]/div/text()')[0])
            #print(author)

            title = str(tree.xpath('//*[@id="main-container"]/div[3]/div/header/h1/text()')[0])
            #print(title)

            publishedTime = str(tree.xpath('//*[@id="main-container"]/div[3]/div/div[1]/div[2]/text()[1]')[0])
            publishedTime = publishedTime.replace("ob", " ")
            publishedTime = re.sub(r"\s", "", publishedTime)
            #print(publishedTime)

            subtitle = str(tree.xpath('//*[@id="main-container"]/div[3]/div/header/div[2]/text()')[0])
            #print(subtitle)

            lead = str(tree.xpath('//*[@id="main-container"]/div[3]/div/header/p//text()')[0])
            #print(lead)

            content = str(tree.xpath('//*[@id="main-container"]/div[3]/div/div[2]/text()')[0])
            #print(content)


            item = RtvsloItem(author, title, publishedTime, subtitle, lead, content)
            items.append(item)
        return items


    def OverstockExtraction(self):
        pages = []

        for page in self.overstock_pages:
            pageContent = codecs.open(page, 'r', encoding='utf-8', errors='ignore').read()
            tree = html.fromstring(pageContent)

            overstock_items = []

            titles = tree.xpath('/html/body/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[2]/a/b/text()')
            #print(titles)

            listPrices = tree.xpath('/html/body/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/s/text()')
            #print(listPrices)

            prices = tree.xpath('/html/body/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/span/b/text()')
            #print(prices)

            savings_percents = tree.xpath('/html/body/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/span/text()')
            #print(savings_percents)

            contents = tree.xpath('/html/body/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/span/text()')
            #print(contents)


            for title, listPrice, price, saving_percent, content in zip(titles, listPrices, prices, savings_percents, contents):
                matches = re.finditer("[\S]+", str(saving_percent))

                matches = [match for match in matches]
                new_item = OverstockItems.OverstockItem(title, price, listPrice, content, matches[0].group(0), matches[1].group(0)).__dict__
                overstock_items.append(new_item)

            pages.append(OverstockItems(overstock_items))

        return pages

    def MimovrsteExtraction(self):
        pages = []

        for page in self.mimovrste_pages:
            pageContent = codecs.open(page, 'r', encoding='utf-8', errors='ignore').read()
            tree = html.fromstring(pageContent)

            mimovrste_items = []

            titles = tree.xpath('/html/body/div[3]/div/div[2]/main/section/section/div/article/div/div/div[1]/h3/a/text()')
            #print(titles)

            listPrices = tree.xpath('/html/body/div[3]/div/div[2]/main/section/section/div/article/div/div/div[2]/del/text()')
            print(listPrices)

            prices = tree.xpath('/html/body/div[3]/div/div[2]/main/section/section/div/article/div/div/div[2]/span/text()')
            #print(prices)

            availabilitys = tree.xpath('/html/body/div[3]/div/div[2]/main/section/section/div/article/div/div/div[3]/div/div/p/text()')
            #print(availabilitys)

            descriptions = tree.xpath('/html/body/div[3]/div/div[2]/main/section/section/div/article/div/div/div[6]/div[1]/p//text()')
            #print(descriptions)

            for title, listPrice, price, availability, description in zip(titles, listPrices, prices, availabilitys, descriptions):
                matches = re.finditer("(.*?)( –)", str(availability))

                if '–' in availability:
                    matches = [match for match in matches]
                    availability = matches[0].group(1)


                new_item = MimovrsteItems.MimovrsteItem(title, price, listPrice, description, availability).__dict__
                mimovrste_items.append(new_item)

            pages.append(MimovrsteItems(mimovrste_items))

        return pages