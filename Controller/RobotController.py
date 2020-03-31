import urllib.robotparser
from urllib.parse import urlparse
import requests as req
import requests
import tika
from tika import parser, detector
from robotexclusionrulesparser import RobotExclusionRulesParser

class RobotController:
    def InitRobotForSite(self, url):
        rp = urllib.robotparser.RobotFileParser()

        parsed_uri = urlparse(url)
        robots_url = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri) + 'robots.txt'

        rpe = RobotExclusionRulesParser()
        rpe.fetch(robots_url)

        return rpe


    def CheckIfSiteRobotsAllow(self, site, url):
        try:
            return site._robot.is_allowed("*", url)
        except:
            return True

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
        contentType = r.headers['Content-Type']
        if contentType.startswith("text/html"):
            return ("HTML", 0)
        elif contentType.startswith("application/vnd.openxmlformats-officedocument.wordprocessingml.document"):
            return ("BINARY", "DOCX")
        elif contentType.startswith("application/msword"):
            return ("BINARY", "DOC")
        elif contentType.startswith('application/pdf'):
            return ("BINARY", "PDF")
        elif contentType.startswith("application/vnd.ms-powerpoint"):
            return ("BINARY", "PPT")
        elif contentType.startswith("application/vnd.openxmlformats-officedocument.presentationml.presentation"):
            return ("BINARY", "PPTX")
        elif contentType.startswith("application/vnd.ms-excel"):
            return ("BINARY", "XLS")
        elif contentType.startswith("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"):
            return ("BINARY", "XLSX")
        elif contentType.startswith("application/zip"):
            return ("BINARY", "ZIP")
        #if content type is not correct we use tika to try and detect
        try:
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
            else:
                type = "UNKNOWN"
            return ("BINARY", type)
        except:
            return ("BINARY", "UNKNOWN")
