class OverstockItems():
    # OverstockItems is list of OverstockItem
    def __init__(self, OverstockItems):
        self.OverstockItems = OverstockItems

    class OverstockItem():
        def __init__(self, Title, Price, ListPrice, Content, Saving, SavingPercent):
            self.Title = Title
            self.Price = Price
            self.ListPrice = ListPrice
            self.Content = Content
            self.Saving = Saving
            self.SavingPercent = SavingPercent
