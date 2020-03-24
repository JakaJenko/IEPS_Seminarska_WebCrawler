from datetime import datetime

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
                    VALUES (%s, %s, %s, %s, %s, %s) RETURNING id""",
                    (page_info.site_id, page_info.page_type_code, page_info.url, page_info.html_content,
                     page_info.http_status_code, page_info.accessed_time))

        value = cur.fetchone()[0]
        page_info.id = value
        cur.close()

        if len(page_info.links) > 0:
            self.__UpdateLinksReverse(page_info)

        return page_info

    def Update(self, page_info):
        try:
            cur = self.conn.cursor()
            cur.execute("""UPDATE crawldb.page
                            SET site_id = %s, page_type_code=%s, url=%s, html_content=%s,http_status_code=%s, accessed_time=%s
                            WHERE id = %s""",
                        (page_info.site_id, page_info.page_type_code, page_info.url, page_info.html_content,
                         page_info.http_status_code, page_info.accessed_time, page_info.id))
            cur.close()

            return True
        except:
            return False


    def LoadLinks(self, page_info):
        cur = self.conn.cursor()
        cur.execute("SELECT to_page FROM crawldb.link WHERE from_page = %s", (page_info.id,))

        for to_page in cur.fetchall():
            page_info.links.append(to_page)

        cur.close()
        return page_info

    def GetSimilar(self, page_id, similarity):
        cur = self.conn.cursor()
        cur.execute("""SELECT tmp.id, tmp.sim
                        FROM (SELECT similarity(p1.html_content, p2.html_content) AS sim, p1.url, p2.url, p1.id
                                FROM   crawldb.page p1
                                JOIN   (SELECT page.html_content, page.url FROM crawldb.page WHERE page.id = 23524) p2 ON p1.url <> p2.url
                                WHERE  p1.html_content != 'None'
                                ORDER  BY sim DESC) as tmp
                        WHERE tmp.sim >= %s""", (page_id, similarity))
        similar = []
        for p in cur.fetchall():
            similar.append(p.id)

        cur.close()
        return similar


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


    def __UpdateLinksReverse(self, page_info):
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM crawldb.link WHERE from_page = %s", (page_info.id,))

            for from_page in page_info.links:
                cur.execute("INSERT INTO crawldb.link (from_page, to_page) VALUES (%s, %s)", (from_page, page_info.id))

            cur.close()
            return True
        except:
            return False