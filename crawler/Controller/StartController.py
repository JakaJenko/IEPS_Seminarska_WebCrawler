from Business.Site.SiteInfo import SiteInfo
from Business.Site.SiteBusinessController import SiteBusinessController
from Business.Page.PageBusinessController import PageBusinessController


class StartController:
    SEEDs = ["http://gov.si/",
             "http://evem.gov.si/",
             "http://e-uprava.gov.si/",
             "http://e-prostor.gov.si/"]

    def GetSitesFromDB(self):
        siteBusinessCtrl = SiteBusinessController()
        sites = siteBusinessCtrl.Select()
        return sites

    def GetForntierFromDB(self):
        pageBusinessCtrl = PageBusinessController()
        frontier = pageBusinessCtrl.SelectFrontier()
        return frontier

    def GetHistoryFromDB(self):
        pageBusinessCtrl = PageBusinessController()
        history = pageBusinessCtrl.SelectHistory()
        history = set(history)
        return history

    def FreshStart(self):
        siteBusinessCtrl = SiteBusinessController()
        sites = [SiteInfo(seed) for seed in self.SEEDs]

        # Site for pages outside SEED sides
        outsiteSide = SiteInfo("OUTSIDE")
        sites.append(outsiteSide)

        for site in sites:
            site = siteBusinessCtrl.Insert(site)

        return sites, [], set()

    def Continue(self):
        return self.GetSitesFromDB(), self.GetForntierFromDB(), self.GetHistoryFromDB()