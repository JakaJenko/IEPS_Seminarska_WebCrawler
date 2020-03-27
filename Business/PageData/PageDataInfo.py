class PageDataInfo():
    id = None

    def __init__(self, page_id, data_type_code, data=None, id=None):
        if id is not None:
            self.id = id
            self.page_id = page_id
            self.data_type_code = data_type_code
            self.data = data
        else:
            self.page_id = page_id
            self.data_type_code = data_type_code
            self.data = 'None'
