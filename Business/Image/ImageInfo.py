from datetime import datetime

class ImageInfo():
    id = None

    def __init__(self, id, page_id, filename, content_type, data, accessed_time):
        self.id = id
        self.page_id = page_id
        self.filename = filename
        self.content_type = content_type
        self.data = data
        self.accessed_time = accessed_time

    def __init__(self, page_id, url):
        self.page_id = page_id
        self.filename = url
        self.content_type = url.split('.')[-1]
        self.data = 'None'
        self.accessed_time = datetime.now()