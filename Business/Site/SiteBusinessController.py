from Business.AbstractDatabaseBusinessController import AbstractDatabaseBusinessController
from Business.Site.SiteInfo import SiteInfo


class SiteBusinessController(AbstractDatabaseBusinessController):
    def __init__(self):
        super().__init__()

    def Select(self):
        site_infos = []

        cur = self.conn.cursor()
        cur.execute("SELECT id, domain, robots_content, sitemap_content FROM crawldb.site")

        for id, domain, robots_content, sitemap_content in cur.fetchall():
            site_infos.append(SiteInfo(id, domain, robots_content, sitemap_content))

        cur.close()
        return site_infos


    def SelectById(self, id):
        page_info = None

        cur = self.conn.cursor()
        cur.execute("SELECT id, domain, robots_content, sitemap_content FROM crawldb.site WHERE id=%s", (id,))

        value = cur.fetchone()[0]
        site_info = SiteInfo(value.id, value.domain, value.robots_content, value.sitemap_content)

        cur.close()
        return site_info


    def Insert(self, site_info):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO crawldb.site (domain, robots_content, sitemap_content) VALUES (%s, %s, %s) RETURNING id",
                    (site_info.domain, site_info.robots_content, site_info.sitemap_content))

        value = cur.fetchone()[0]
        site_info.id = value

        cur.close()
        return site_info

    def Update(self, site_info):
        try:
            cur = self.conn.cursor()
            cur.execute("""UPDATE crawldb.site
                            SET domain = %s, robots_content=%s, url=%s, sitemap_content=%s
                            WHERE id = %s""",
                        (site_info.domain, site_info.robots_content, site_info.sitemap_content, site_info.id))
            cur.close()
            return True
        except:
            return False