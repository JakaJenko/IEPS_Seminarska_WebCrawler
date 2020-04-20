import re
import codecs
from PageTemplates.OverstockItem import OverstockItem
from PageTemplates.RtvsloItem import RtvsloItem

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

            # content_re = r"<div class=\"article-body\">\s+([\s\S]*|.*)\s{3}<\/div>\s+<div class=\"article-column\">"
            # match = re.compile(content_re).search(pageContent)
            content = match.group(1)

            item = RtvsloItem(author, title, publishedTime, subtitle, lead, content)
            items.append(item)
        return items

    def OverstockExtraction(self):
        page_items = []
        for page in self.rtvslo_pages:
            pageContent = codecs.open(self.overstock_pages[1], 'r', encoding='utf-8', errors='ignore').read()
            items = []

            regex = r"<td valign=\"top\">\s*<a.*>\s*<b>(.*)<\/b>[\s\S|.]*?<td align=\"left\" nowrap=\"nowrap\">\s*<s>(.*)<\/s>\s*<\/td>[\s\S|.]*?<span class=\"bigred\">\s*<b>(.*)<\/b>[\s\S|.]*?<span class=\"littleorange\">([$€]\s*[0-9\.,]+) \((.*)\)<\/span>[\s\S|.]*?<span class=\"normal\">([\s\S|.]*?)<br>"
            matches = re.finditer(regex, str(pageContent))
            for match in matches:
                title = match.group(1)
                listPrice = match.group(2)
                price = match.group(3)
                saving = match.group(4)
                savingPercent = match.group(5)
                content = match.group(6)
                new_item = OverstockItem(title, price, listPrice, content, saving, savingPercent)
                items.append(new_item)
            page_items.append(items)

        return page_items

    def MimovrsteExtraction(self):
        return
