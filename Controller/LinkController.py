from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse, urldefrag, urljoin, urlencode
from html import unescape


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
        #change realtive links to absolute
        if not link.startswith('http'):
            base_url = urljoin(driver.current_url, '.')
            link = base_url[:-1] + link

        # Removes # fragments
        link, frag = urldefrag(link)

        #remove port number
        re.sub(":80/", "", link)

        #remove index.html
        re.sub("index\.html$", "", link)

        #decode encoded characters
        link = unescape(link)

        #encode neccesery characters (spaces)
        link = link.replace(" ", "%20")

        if link[-1] != "/":
            if link.count("/") == 2:
                link = link + "/"
            elif "." not in link.split("/")[-1]:
                link = link + "/"

        return link

    def GetImageSources(self, driver):
        sources = []

        # Gets [img src] links
        elems = driver.find_elements_by_xpath("//img[@src]")
        for elem in elems:
            sources.append(elem.get_attribute("src"))

        return sources