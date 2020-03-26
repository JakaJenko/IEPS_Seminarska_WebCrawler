from Business.AbstractDatabaseBusinessController import AbstractDatabaseBusinessController
from Business.PageData.PageDataInfo import PageDataInfo


class PageDataBusinessController(AbstractDatabaseBusinessController):
    def __init__(self):
        super().__init__()

    def Select(self):
        page_data_infos = []

        cur = self.conn.cursor()
        cur.execute("SELECT id, page_id, data_type_code, data FROM crawldb.page_data")

        for id, page_id, data_type_code, data in cur.fetchall():
            page_data_infos.append(PageDataInfo(id, page_id, data_type_code, data ))

        cur.close()
        return page_data_infos

    def SelectById(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT id, page_id, data_type_code, data FROM crawldb.page_data WHERE id=%s", (id,))

        value = cur.fetchone()[0]
        page_data_info = PageDataInfo(value.id, value.page_id, value.data_type_code, value.data)
        cur.close()
        return page_data_info

    def Insert(self, page_data_info):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO crawldb.page_data (page_id, data_type_code, data) VALUES (%s, %s, %s)",
                    (page_data_info.page_id, page_data_info.data_type_code, page_data_info.data))
        return True

    def Update(self, page_data_info):
        try:
            cur = self.conn.cursor()
            cur.execute("""UPDATE crawldb.page_data
                            SET page_id = %s, data_type_code=%s data=%s
                            WHERE id = %s""",
                        (page_data_info.page_id, page_data_info.data_type_code, page_data_info.data, page_data_info.id))
            cur.close()
            return True
        except:
            return False

    def DeleteByPageId(self, pageId):
        try:
            cur = self.conn.cursor()
            cur.execute("""DELETE FROM crawldb.page_data
                            WHERE page_id = %s""", (pageId,))
            cur.close()
            return True
        except:
            return False