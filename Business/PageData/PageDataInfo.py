class PageDataInfo():
    id = None

    def __init__(self, id, page_id, data_type_code, data):
        self.id = id
        self.page_id = page_id
        self.data_type_code = data_type_code
        self.data = data

    def __init__(self, page_id, data_type_code):
        self.page_id = page_id
        self.data_type_code = data_type_code
        self.data = 'None'
