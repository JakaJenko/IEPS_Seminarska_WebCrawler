from urllib.parse import urlparse
from Business.Page.PageInfo import PageInfo
from Controller.RobotController import RobotController
import socket

robotCtrl = RobotController()


class SiteController:
    def __init__(self, sites):
        self._sites = sites

    def CreateNewPage(self, url, alowOutside = False):
        siteOfUrl = self.SiteOfUrl(url)

        if not siteOfUrl:
            return False

        if siteOfUrl.domain == "OUTSIDE":
            if alowOutside:
                return PageInfo(siteOfUrl.id, url)
            else:
                return False

        if robotCtrl.CheckIfSiteRobotsAllow(siteOfUrl, url):
            return PageInfo(siteOfUrl.id, url)

        return False


    def SiteOfUrl(self, url):
        defaultSite = None

        parsedUrl = urlparse(url)
        urlNetloc = '{uri.netloc}/'.format(uri=parsedUrl)
        urlNetloc = urlNetloc.replace("www.", "")

        for site in self._sites:
            if site.domain == "OUTSIDE":
                defaultSite = site

            parsedDomain = urlparse(site.domain)
            domainNetloc = '{uri.netloc}/'.format(uri=parsedDomain)
            domainNetloc = domainNetloc.replace("www.", "")

            if urlNetloc == domainNetloc:
                return site

        return defaultSite

    def GetIPFromSite(self, site):
        domena = site.domain
        uri = urlparse(domena)
        domain_name = "{uri.netloc}".format(uri=uri)
        ip = socket.gethostbyname(domain_name)
        return ip
