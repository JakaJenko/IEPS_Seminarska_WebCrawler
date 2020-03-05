class PageInfo():
    def __init__(self, id, site_id, page_type_code, url, html_content, http_status_code, accessed_time):
        self.id = id
        self.site_id = site_id
        self.page_type_code = page_type_code
        self.url = url
        self.html_content = html_content
        self.http_status_code = http_status_code
        self.accessed_time = accessed_time