class LinkController:
    def GetAllLinks(self, driver):
        links = []

        #Gets [a href] links
        elems = driver.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            links.append(elem.get_attribute("href"))

        return links