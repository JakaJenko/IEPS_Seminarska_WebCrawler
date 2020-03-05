from Business.AbstractDatabaseBusinessController import AbstractDatabaseBusinessController
from Business.Site.SiteInfo import SiteInfo


class PageBusinessController(AbstractDatabaseBusinessController):
    def __init__(self):
        super().__init__()

    def Select(self):
        page_infos = []

        cur = self.conn.cursor()
        cur.execute("SELECT * FROM crawldb.site")

        for id, domain, robots_content, sitemap_content in cur.fetchall():
            page_infos.append(SiteInfo(id, domain, robots_content, sitemap_content))

        cur.close()
        return page_infos


    def SelectById(self, id):
        page_info = None

        cur = self.conn.cursor()
        cur.execute("SELECT * FROM crawldb.site WHERE id=%s", (id,))

        value = cur.fetchone()[0]
        page_info = SiteInfo(value.id, value.domain, value.robots_content, value.sitemap_content)

        cur.close()
        return page_info


    def Insert(self, site_info):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO crawldb.site VALUES (%s, %s, %s, %s)",
                    (site_info.id, site_info.domain, site_info.robots_content, site_info.sitemap_content))
        cur.close()

        return True

    def Update(self, site_info):
        pass