class MimovrsteItems():
    # MimovrsteItems is list of MimovrsteItem
    def __init__(self, MimovrsteItems):
        self.MimovrsteItems = MimovrsteItems

    class MimovrsteItem():
        def __init__(self, Title, Price, ListPrice, Description, Availability):
            self.Title = Title
            self.Price = Price
            self.ListPrice = ListPrice
            self.Description = Description
            self.Availability = Availability
