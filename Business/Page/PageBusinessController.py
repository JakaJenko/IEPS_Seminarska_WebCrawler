from Business.AbstractDatabaseBusinessController import AbstractDatabaseBusinessController
from Business.Page.PageInfo import PageInfo


class PageBusinessController(AbstractDatabaseBusinessController):
    def __init__(self):
        super().__init__()

    def Select(self):
        page_infos = []

        cur = self.conn.cursor()
        cur.execute("SELECT * FROM crawldb.page")

        for id, site_id, page_type_code, url, html_content, http_status_code, accessed_time in cur.fetchall():
            page_infos.append(PageInfo(id, site_id, page_type_code, url, html_content, http_status_code, accessed_time))

        cur.close()
        return page_infos


    def SelectById(self, id):
        page_info = None

        cur = self.conn.cursor()
        cur.execute("SELECT * FROM crawldb.page WHERE id=%s", (id,))

        value = cur.fetchone()[0]
        page_info = PageInfo(value.id, value.site_id, value.page_type_code, value.url, value.html_content,
                             value.http_status_code, value.accessed_time)

        cur.close()
        return page_info


    def Insert(self, page_info):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO crawldb.page VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (page_info.id, page_info.site_id, page_info.page_type_code, page_info.url, page_info.html_content,
                     page_info.http_status_code, page_info.accessed_time))
        cur.close()

        return True


    def Update(self, page_info):
        pass

    def UpdateLinks(self, page_info):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO crawldb.link VALUES (%s, %s)",
                    (page_info1.id, page_info2.id))
        cur.close()