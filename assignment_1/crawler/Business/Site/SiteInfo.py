from Controller.RobotController import RobotController

class SiteInfo():
    id = None

    def __init__(self, domain, id=None, robots_content=None, sitemap_content=None):
        if id is not None:
            self.id = id
            self.domain = domain
            self.robots_content = robots_content
            self.sitemap_content = sitemap_content
            self.BindData(domain)
        else:
            self.BindData(domain)


    def BindData(self, domain):
        if domain == "OUTSIDE":
            self.domain = domain
            self.robots_content = "None"
            self.sitemap_content = "None"
            return

        robotsCtrl = RobotController()

        if self.id is None:
            self.domain = domain
            self.robots_content = robotsCtrl.GetRobotsContent(domain)
            self.sitemap_content = robotsCtrl.GetSitemapContent(domain)

        self._robot = robotsCtrl.InitRobotForSite(domain)
