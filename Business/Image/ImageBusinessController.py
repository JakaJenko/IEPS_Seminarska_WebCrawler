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
            images.append(ImageInfo(id, page_id, filename, content_type, data, accessed_time ))

        cur.close()
        return images

    def SelectById(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT id, page_id, filename, content_type, data, accessed_time FROM crawldb.image WHERE id=%s", (id,))

        value = cur.fetchone()[0]
        image_info = ImageInfo(value.id, value.page_id, value.filename, value.content_type, value.data, value.accessed_time)
        cur.close()
        return image_info

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