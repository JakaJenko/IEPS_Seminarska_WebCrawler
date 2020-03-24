from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse, urldefrag, urljoin, urlencode
from html import unescape
from url_normalize import url_normalize
from w3lib import url as w3url

class LinkController:
    def GetAllLinks(self, driver):
        links = []

        #Gets [a href] links
        elems = driver.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            links.append(self.CleanLink(elem.get_attribute("href"), driver))

        #Gets onclick links
        elems = driver.find_elements_by_xpath("//*[@onclick]")
        for elem in elems:
            value = elem.get_attribute("onclick")
            if re.match("^(location\.href|document\.location)", value):
                link = value.split("=")[1][1:-1]
                links.append(self.CleanLink(link, driver))

        return links

    def CleanLink(self, link, driver=None):

        normalized_url = url_normalize(link)

        canonized_url = w3url.canonicalize_url(normalized_url)

        return canonized_url


    def GetImageSources(self, driver):
        sources = []

        # Gets [img src] links
        elems = driver.find_elements_by_xpath("//img[@src]")
        for elem in elems:
            sources.append(elem.get_attribute("src"))

        return sources