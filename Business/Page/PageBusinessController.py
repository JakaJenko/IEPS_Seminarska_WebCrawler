from Business.AbstractDatabaseBusinessController import AbstractDatabaseBusinessController
from Business.Page.PageInfo import PageInfo


class PageBusinessController(AbstractDatabaseBusinessController):
    def Select(self):
        page_infos = []

        cur = self.conn.cursor()
        cur.execute("SELECT * FROM crawldb.page")

        for id, site_id, page_type_code, url, html_content, http_status_code, accessed_time in cur.fetchall():
            page_infos.append(PageInfo(id, site_id, page_type_code, url, html_content, http_status_code, accessed_time))

        cur.close()
        return page_infos


    def Select(self, id):
        page_info = None

        cur = self.conn.cursor()
        cur.execute("SELECT * FROM crawldb.page WHERE id=%s", (id))

        for id, site_id, page_type_code, url, html_content, http_status_code, accessed_time in cur.fetchall():
            page_info = PageInfo(id, site_id, page_type_code, url, html_content, http_status_code, accessed_time)

        cur.close()
        return page_info

    '''
    def Insert(self, page_info):
        cur = self.conn.cursor()
        cur.execute("INSERT () INTO crawldb.page)

        for id, site_id, page_type_code, url, html_content, http_status_code, accessed_time in cur.fetchall():
            page_info = PageInfo(id, site_id, page_type_code, url, html_content, http_status_code, accessed_time)

        cur.close()
        return page_info
    '''

    def Update(self, page_info):
        pass