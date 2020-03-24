import urllib.robotparser
from urllib.parse import urlparse
import requests as req
from reppy.robots import Robots

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
        rp = Robots.fetch(robots_url)

        sitemaps = rp.sitemaps
        if len(sitemaps) == 0:
            return ""

        sitemap_url = sitemaps[0]
        # return only the first sitemap
        sitemap = req.get(sitemap_url)

        return sitemap.text
