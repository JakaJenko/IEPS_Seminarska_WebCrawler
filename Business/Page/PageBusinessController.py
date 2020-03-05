from Business.AbstractDatabaseBusinessController import AbstractDatabaseBusinessController
from Business.Page.PageInfo import PageInfo


class PageBusinessController(AbstractDatabaseBusinessController):
    def __init__(self):
        super().__init__()

    def Select(self):
        page_infos = []

        cur = self.conn.cursor()
        cur.execute("SELECT id, site_id, page_type_code, url, html_content, http_status_code, accessed_time FROM crawldb.page")

        for id, site_id, page_type_code, url, html_content, http_status_code, accessed_time in cur.fetchall():
            page_infos.append(PageInfo(id, site_id, page_type_code, url, html_content, http_status_code, accessed_time))

        cur.close()

        for page_info in page_infos:
            page_info = self.__LoadLinks(page_info)

        return page_infos


    def SelectById(self, id):
        page_info = None

        cur = self.conn.cursor()
        cur.execute("""SELECT id, site_id, page_type_code, url, html_content, http_status_code, accessed_time
                        FROM crawldb.page WHERE id=%s""", (id,))

        value = cur.fetchone()[0]
        page_info = PageInfo(value.id, value.site_id, value.page_type_code, value.url, value.html_content,
                             value.http_status_code, value.accessed_time)

        cur.close()

        page_info = self.__LoadLinks(page_info)
        return page_info


    def Insert(self, page_info):
        cur = self.conn.cursor()
        cur.execute("""INSERT INTO crawldb.page (site_id, page_type_code, url, html_content, http_status_code, accessed_time)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                    (page_info.site_id, page_info.page_type_code, page_info.url, page_info.html_content,
                     page_info.http_status_code, page_info.accessed_time))
        return True

    def Update(self, page_info):
        try:
            cur = self.conn.cursor()
            cur.execute("""UPDATE crawldb.page
                            SET site_id = %s, page_type_code=%s, url=%s, html_content=%s,http_status_code=%s, accessed_time=%s
                            WHERE id = %s""",
                        (page_info.site_id, page_info.page_type_code, page_info.url, page_info.html_content,
                         page_info.http_status_code, page_info.accessed_time, page_info.id))
            cur.close()

            self.__UpdateLinks(page_info)

            return True
        except:
            return False


    def __LoadLinks(self, page_info):
        cur = self.conn.cursor()
        cur.execute("SELECT to_page FROM crawldb.link WHERE from_page = %s", (page_info.id,))

        for to_page in cur.fetchall():
            page_info.links.append(to_page)

        cur.close()
        return page_info


    def __UpdateLinks(self, page_info):
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM crawldb.link WHERE from_page = %s", (page_info.id,))

            for to_page in page_info.links:
                cur.execute("INSERT INTO crawldb.link (from_page, to_page) VALUES (%s, %s)", (page_info.id, to_page))

            cur.close()
            return True
        except:
            return False