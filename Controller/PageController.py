from Business.Image.ImageBusinessController import ImageBusinessController
from Business.PageData.PageDataBusinessController import PageDataBusinessController


class PageController:
    def ReplacePageInImagesAndPageDataBecauseOfRedirect(self, pageOriginal, pageNew):
        imageBusinessCtrl = ImageBusinessController()
        pageDataBusinessCtrl = PageDataBusinessController()

        for image in imageBusinessCtrl.SelectByPageId(pageOriginal.id):
            image.page_id = pageNew.id
            imageBusinessCtrl.Update(image)

        for pageData in pageDataBusinessCtrl.SelectByPageId(pageOriginal.id):
            pageData.page_id = pageNew.id
            pageDataBusinessCtrl.Update(pageData)