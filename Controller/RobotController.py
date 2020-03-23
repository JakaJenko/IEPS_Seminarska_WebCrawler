import urllib.robotparser
from urllib.parse import urlparse


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
        result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

        return "TODO: Robots content"