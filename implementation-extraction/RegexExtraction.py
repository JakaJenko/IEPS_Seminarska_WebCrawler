import re
import regex
import codecs
from PageTemplates.OverstockItem import OverstockItems
from PageTemplates.RtvsloItem import RtvsloItem
from PageTemplates.MimovrsteItem import MimovrsteItems

class RegexExtraction():

    def __init__(self, rtvslo_pages=[], overstock_pages=[], mimovrste_pages=[]):
        self.rtvslo_pages = rtvslo_pages
        self.overstock_pages = overstock_pages
        self.mimovrste_pages = mimovrste_pages

    def RtvsloExtraction(self):
        items = []
        for page in self.rtvslo_pages:
            pageContent = open(page, 'r').read()

            title_re = r"<h1>(.*)<\/h1>\s*<div class=\"subtitle\">"
            match = re.compile(title_re).search(pageContent)
            title = match.group(1)

            subtitle_re = r"<div class=\"subtitle\">(.*)<\/div>"
            match = re.compile(subtitle_re).search(pageContent)
            subtitle = match.group(1)

            lead_re = r"<p class=\"lead\">(.*)<\/p>"
            match = re.compile(lead_re).search(pageContent)
            lead = match.group(1)

            author_re = r"<div class=\"author-timestamp\">\s+<strong>(.*)<\/strong>"
            match = re.compile(author_re).search(pageContent)
            author = match.group(1)

            publishedTime_re = r"<div class=\"author-timestamp\">\s+<strong>.*<\/strong>\|\s+(.*:[0-9]{2})[\s\t\S]*"
            match = re.compile(publishedTime_re).search(pageContent)
            publishedTime = match.group(1)



            content_matches = regex.finditer(r'(?<=<article class=\"article\">).*?((<p.*?>)(.*?)(<\/p.*?>).*?)*(?=<\/article>)', str(pageContent), regex.DOTALL)
            content = ""
            for match in content_matches:
                for capture in match.captures(3):
                    content += capture
                    
            item = RtvsloItem(author, title, publishedTime, subtitle, lead, content)
            items.append(item)
        return items

    def OverstockExtraction(self):
        pages = []
        for page in self.overstock_pages:
            pageContent = codecs.open(page, 'r', encoding='utf-8', errors='ignore').read()
            overstock_items = []

            regex = r"<td valign=\"top\">\s*<a.*>\s*<b>(.*)<\/b>[\s\S|.]*?<td align=\"left\" nowrap=\"nowrap\">\s*<s>(.*)<\/s>\s*<\/td>[\s\S|.]*?<span class=\"bigred\">\s*<b>(.*)<\/b>[\s\S|.]*?<span class=\"littleorange\">([$€]\s*[0-9\.,]+) \((.*)\)<\/span>[\s\S|.]*?<span class=\"normal\">([\s\S|.]*?)<br>"
            matches = re.finditer(regex, str(pageContent))
            for match in matches:
                title = match.group(1)
                listPrice = match.group(2)
                price = match.group(3)
                saving = match.group(4)
                savingPercent = match.group(5)
                content = match.group(6)

                new_item = OverstockItems.OverstockItem(title, price, listPrice, content, saving, savingPercent).__dict__
                overstock_items.append(new_item)

            pages.append(OverstockItems(overstock_items))

        return pages

    def MimovrsteExtraction(self):
        pages = []
        for page in self.mimovrste_pages:
            pageContent = codecs.open(page, 'r', encoding='utf-8', errors='ignore').read()
            mimovrste_items = []

            regex = r"class=\"lay-block con-no-decoration\">(.*)</a>[\s\S|.]*?<(del|span) class=\"lst-product-item-price--retail\">(.*)<\/(del|span)>[\s\S|.]*?<span class=\"lst-product-item-price-value\">[\s\S]*?\t\t\t\t\t\t    (.*)\s*<\/span>[\s\S|.]*?<p class=\"lst-product-item-availability con-text--availability text-collapse\">(.*?) – [\s\S|.]*?<div class=\"lst-product-item-description \"><p>(.*?)<\/p>"
            matches = re.finditer(regex, str(pageContent))
            for match in matches:
                title = match.group(1)
                listPrice = match.group(3)
                price = match.group(5)
                availability = match.group(6)
                description = match.group(7)
                new_item = MimovrsteItems.MimovrsteItem(title, price, listPrice, description, availability).__dict__
                mimovrste_items.append(new_item)
            pages.append(MimovrsteItems(mimovrste_items))

        return pages
