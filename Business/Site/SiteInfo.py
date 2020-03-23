from Controller.RobotController import RobotController

class SiteInfo():
    id = None

    def __init__(self, id, domain, robots_content, sitemap_content):
        self.id = id
        self.domain = domain
        self.robots_content = robots_content
        self.sitemap_content = sitemap_content
        self.BindData(domain)

    def __init__(self, domain):
        self.BindData(domain)

    def BindData(self, domain):
        robotsCtrl = RobotController()

        if self.id is None:
            self.domain = domain
            self.robots_content = robotsCtrl.GetRobotsContent(domain)
            self.sitemap_content = "Sitemap"

        self._robot = robotsCtrl.InitRobotForSite(domain)
