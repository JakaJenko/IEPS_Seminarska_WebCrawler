from datetime import datetime

class PageInfo():
    id = None

    def __init__(self, site_id, url, id=None, page_type_code=None, html_content=None, http_status_code=None, accessed_time=None, linksTo=None, linksFrom=None):
        if id is not None:
            self.id = id
            self.site_id = site_id
            self.page_type_code = page_type_code
            self.url = url
            self.html_content = html_content
            self.http_status_code = http_status_code
            self.accessed_time = accessed_time

            if linksTo is None:
                self.linksTo = []
            else:
                self.linksTo = linksTo

            if linksTo is None:
                self.linksFrom = []
            else:
                self.linksFrom = linksFrom
        else:
            self.site_id = site_id
            self.url = url
            self.page_type_code = "FRONTIER"
            self.html_content = "None"
            self.http_status_code = 0
            self.accessed_time = datetime.now()
            self.linksTo = []
            self.linksFrom = []

    def BindData(self, page_type_code, html_content, http_status_code):
        self.page_type_code = page_type_code
        self.html_content = html_content
        self.http_status_code = http_status_code
        self.accessed_time = datetime.now()

    def AddPagesTo(self, pages):
        for page in pages:
            self.linksTo.append(page.id)
            self.linksTo = list(set(self.linksTo))

    def AddPagesFrom(self, pages):
        for page in pages:
            self.linksFrom.append(page.id)
            self.linksFrom = list(set(self.linksFrom))

    def AddLinksTo(self, links):
        self.linksTo.extend(links)
        self.linksTo = list(set(self.linksTo))

    def AddLinksFrom(self, links):
        self.linksFrom.extend(links)
        self.linksFrom = list(set(self.linksFrom))