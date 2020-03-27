from Business.AbstractDatabaseBusinessController import AbstractDatabaseBusinessController
from Business.Image.ImageInfo import ImageInfo


class ImageBusinessController(AbstractDatabaseBusinessController):
    def __init__(self):
        super().__init__()

    def Select(self):
        images = []

        cur = self.conn.cursor()
        cur.execute("SELECT id, page_id, filename, content_type, data, accessed_time FROM crawldb.image")

        for id, page_id, filename, content_type, data, accessed_time  in cur.fetchall():
            images.append(ImageInfo(page_id, None, id, filename, content_type, data, accessed_time))

        cur.close()
        return images

    def SelectById(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT id, page_id, filename, content_type, data, accessed_time FROM crawldb.image WHERE id=%s", (id,))

        value = cur.fetchone()[0]
        image_info = ImageInfo(value.page_id, None, value.id, value.filename, value.content_type, value.data, value.accessed_time)
        cur.close()
        return image_info

    def SelectByPageId(self, page_id):
        image_infos = []

        cur = self.conn.cursor()
        cur.execute("SELECT id, page_id, data_type_code, data FROM crawldb.page_data WHERE page_id=%s", (page_id,))

        for id, page_id, filename, content_type, data, accessed_time  in cur.fetchall():
            page_data_info = ImageInfo(page_id, None, id, filename, content_type, data, accessed_time)

        cur.close()
        return image_infos

    def Insert(self, image_info):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO crawldb.image (page_id, filename, content_type, data, accessed_time) VALUES (%s, %s, %s, %s, %s)",
                    (image_info.page_id, image_info.filename, image_info.content_type, image_info.data, image_info.accessed_time))
        return True

    def Update(self, image_info):
        try:
            cur = self.conn.cursor()
            cur.execute("""UPDATE crawldb.image
                            SET page_id = %s, filename=%s, content_type=%s, data=%s, accessed_time=%s
                            WHERE id = %s""",
                        (image_info.page_id, image_info.filename, image_info.content_type, image_info.data, image_info.accessed_time, image_info.id))
            cur.close()
            return True
        except:
            return False

    def DeleteByPageId(self, pageId):
        try:
            cur = self.conn.cursor()
            cur.execute("""DELETE FROM crawldb.image
                            WHERE page_id = %s""", (pageId,))
            cur.close()
            return True
        except:
            return False