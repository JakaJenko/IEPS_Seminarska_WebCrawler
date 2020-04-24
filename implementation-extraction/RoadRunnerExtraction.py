import difflib
import codecs
from bs4 import BeautifulSoup


class RoadRunnerExtraction():

    def __init__(self, rtvslo_pages=[], overstock_pages=[], mimovrste_pages=[]):
        self.rtvslo_pages = rtvslo_pages
        self.overstock_pages = overstock_pages
        self.mimovrste_pages = mimovrste_pages

    def ExtractWrappers(self):
        wrappers = []
        for p1, p2 in [self.overstock_pages]:#, self.mimovrste_pages, self.overstock_pages]:
            page1 = codecs.open(p1, 'r', encoding='utf-8', errors='ignore').read()
            page2 = codecs.open(p2, 'r', encoding='utf-8', errors='ignore').read()

            #extract only body
            soup1 = BeautifulSoup(page1, 'html.parser')
            body1 = soup1.find('body')
            page1 = BeautifulSoup(str(body1.findChildren(recursive=False)), 'html.parser')
            for script in page1.find_all(['script', 'img', 'iframe', 'style', 'a']):
                script.decompose()
            page1 = BeautifulSoup(str(page1)[3:-1], 'html.parser').prettify()
            page1 = page1.split('\n')

            soup2 = BeautifulSoup(page2, 'html.parser')
            body2 = soup2.find('body')
            page2 = BeautifulSoup(str(body2.findChildren(recursive=False)), 'html.parser')
            for script in page2.find_all(['script', 'img', 'iframe', 'style', 'a']):
                script.decompose()
            page2 = BeautifulSoup(str(page2)[3:-1], 'html.parser').prettify()
            page2 = page2.split('\n')


            diff = difflib.ndiff(page1, page2)

            for l in diff:
                print(l)

        return