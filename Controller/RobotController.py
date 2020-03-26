import urllib.robotparser
from urllib.parse import urlparse
import requests as req
import requests
import tika
from tika import parser, detector

class RobotController:
    def InitRobotForSite(self, url):
        rp = urllib.robotparser.RobotFileParser()

        parsed_uri = urlparse(url)
        result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

        rp.set_url(result + "/robots.txt")
        rp.read()

        return rp


    def CheckIfSiteRobotsAllow(self, site, url):
        parsed_uri = urlparse(url)
        result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

        return site._robot.can_fetch("*", result)


    def GetRobotsContent(self, url):
        parsed_uri = urlparse(url)
        robots_url = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri) +'robots.txt'
        robots = req.get(robots_url).text

        return robots

    def GetSitemapContent(self, url):
        parsed_uri = urlparse(url)
        robots_url = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri) +'robots.txt'
        robots = req.get(robots_url).text

        sitemaps = []
        for line in robots.split("\n"):
            splited = line.split(" ")
            if splited[0]=="Sitemap:":
                sitemaps.append(splited[1])

        if len(sitemaps) == 0:
            return ""

        sitemap_url = sitemaps[0]
        # return only the first sitemap
        sitemap = req.get(sitemap_url)

        return sitemap.text

    def GetContentTypeFromRequest(self, r):
        try:
            if r.headers['Content-Type'].startswith("text/html"):
                return ("HTML", 0)
            else:
                type = detector.from_buffer(r.raw.read(2048)).split("/")[1]
                if type == "x-tika-msoffice":
                    if r.url.endswith("doc"):
                        type = "DOC"
                    elif r.url.endswith("ppt"):
                        type = "PPT"
                elif type =='x-tika-ooxml':
                    if r.url.endswith('docx'):
                        type = "DOCX"
                    elif r.url.endswith('pptx'):
                        type = "PPTX"
                elif type == "pdf":
                    type = "PDF"
                return ("BINARY", type)
        except:
            return ("BINARY", 0)

r = requests.get("https://file-examples.com/wp-content/uploads/2017/02/file-sample_1MB.docx", timeout=5, stream=True)

rc = RobotController()
print(rc.GetContentTypeFromRequest(r))
