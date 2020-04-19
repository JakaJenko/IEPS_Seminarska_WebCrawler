from datetime import datetime
from mimetypes import guess_extension, guess_type

class ImageInfo():
    id = None

    def __init__(self, page_id, url=None, id=None, filename=None, content_type=None, data=None, accessed_time=None):
        if id is not None:
            self.id = id
            self.page_id = page_id
            self.filename = filename
            self.content_type = content_type
            self.data = data.decode('ascii')
            self.accessed_time = accessed_time
        else:
            if "base64" in url and "." not in url[-10:]:
                #je base64
                self.filename = "base64"
                self.content_type = guess_extension(guess_type(url)[0])
                self.data = url.encode('ascii')
            else:
                self.content_type = url.split('.')[-1]

                if len(url) > 255:
                    url = "Url too long"

                self.filename = url
                self.data = 'None'.encode('ascii')


            self.page_id = page_id
            self.accessed_time = datetime.now()