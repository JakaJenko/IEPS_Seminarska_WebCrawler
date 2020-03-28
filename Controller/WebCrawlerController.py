import concurrent.futures
import threading
import pathlib
import time
import keyboard
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from Business.Page.PageBusinessController import PageBusinessController
from Business.PageData.PageDataBusinessController import PageDataBusinessController
from Controller.LinkController import LinkController
from Controller.PageController import PageController
from Controller.RobotController import RobotController
from Controller.SiteController import SiteController
from Business.Site.SiteBusinessController import SiteBusinessController
from Business.Page.PageBusinessController import PageBusinessController
from Business.Image.ImageBusinessController import ImageBusinessController
from Business.Site.SiteInfo import SiteInfo
from Controller.StartController import StartController
from Business.Image.ImageInfo import ImageInfo
from sys import platform
import sys
import requests
import os
from Business.PageData.PageDataInfo import PageDataInfo
from Business.PageData.PageDataBusinessController import PageDataBusinessController

#https://e-uprava.gov.si/o-e-upravimailto:ekc@gov.si?view_mode=2

startCtrl = StartController()

siteBusinessCtrl = SiteBusinessController()
pageBusinessCtrl = PageBusinessController()
imageBusinessCtrl = ImageBusinessController()
pageDataBusinessCtrl = PageDataBusinessController()

linkCtrl = LinkController()
robotCtrl = RobotController()
pageCtrl = PageController()


THREADS = 5
TIMEOUT = 5
MAX_DEPTH = 5

# frontier = [(SiteInfo, depth), ...]
sites, frontier, history = startCtrl.FreshStart()
#sites, frontier, history = startCtrl.Continue()

siteCtrl = SiteController(sites)

lastVisitedPages = []
lastRedirects = []

def main():
    lock = threading.Lock()

    global frontier
    global history
    global lastVisitedPages
    global lastRedirects

    pathHere = pathlib.Path().absolute()
    WEB_DRIVER_LOCATION = str(pathHere) + "\..\chromedriver.exe"

    # ChromeDriver for mac users
    if platform == "darwin":
        WEB_DRIVER_LOCATION = str(pathHere) + "/../chromedriver"

    chrome_options = Options()
    # If you comment the following line, a browser will show ...
    chrome_options.add_argument("--headless")

    # Adding a specific user agent
    chrome_options.add_argument("user-agent=fri-ieps-CoronaBojz1235")

    #disabling automatic downloads
    profile = {"download.default_directory": "NUL", "download.prompt_for_download": False, }
    chrome_options.add_experimental_option("prefs", profile)

    #driver = webdriver.Chrome(WEB_DRIVER_LOCATION, options=chrome_options)

    drivers = []
    for i in range(THREADS):
        driver = webdriver.Chrome(WEB_DRIVER_LOCATION, options=chrome_options)
        driver.set_page_load_timeout(TIMEOUT + 5)
        drivers.append(driver)


    # Add first pages to frontier
    if len(frontier) == 0:
        frontier = InitFrontier(drivers[0], sites)

    #sys.exit()

    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        while len(frontier) != 0:
            print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            print("Frontier length:", len(frontier))
            future = []

            for threadNumber in range(THREADS):
                page, depth = None, None

                with lock:
                    while page is None:
                        if len(frontier) != 0:
                            page, depth = frontier.pop()

                            if depth >= MAX_DEPTH:
                                print("Depth max:", page.url)
                                page, depth = None, None
                        else:
                            break

                    if page is not None:
                        future.append(executor.submit(GetPageData, drivers[threadNumber], page, depth))

            # WAIT
            print("WAIT!")
            concurrent.futures.wait(future, timeout=None, return_when=concurrent.futures.ALL_COMPLETED)

            if len(lastRedirects) > 0:
                ManageRedirects(lastRedirects)

            lastRedirects = []

            print(len(frontier))

            # remove and save duplicate urls from frontier
            frontier = RemoveDuplicates(frontier)
            print(len(frontier))

            # remove and save history from list
            #frontier = [(page, depth) for page, depth in frontier if page.url not in history]
            frontier = RemoveHistory(frontier, history)
            print(len(frontier))

            for i in range(len(frontier)):
                if frontier[i][0].id is None:
                    #print("Inserting in DB:", frontier[i][0].id, frontier[i][0].url, "From page id:", frontier[i][0].linksFrom)
                    newTuple = (pageBusinessCtrl.InsertWithDepth(frontier[i][0], frontier[i][1]), frontier[i][1])
                    frontier[i] = newTuple

            if os.name == "nt":
                if keyboard.is_pressed('q'):  # if key 'q' is pressed
                    print('Stop!')
                    sys.exit()

            # WAIT
            #concurrent.futures.wait(future, timeout=None, return_when=concurrent.futures.ALL_COMPLETED)


def GetPageData(driver, page, depth):
    global frontier
    global history
    global lastVisitedPages
    global lastRedirects

    print("Started:", page.url)

    #if page.url == "https://www.e-prostor.gov.si/":
    #    a=2

    try:
        requestOriginal = requests.get(page.url, timeout=TIMEOUT, stream=True)
        start_page_type, start_data_type = robotCtrl.GetContentTypeFromRequest(requestOriginal)

        driver.get(page.url)

        # Timeout needed for Web page to render (read more about it)
        time.sleep(TIMEOUT)

        requestFinal = requests.get(driver.current_url, timeout=TIMEOUT, stream=True)
    except:
        print("Added to hitroy:", page.url)
        history.add(page.url)
        print("Finished:", page.url, "Page ERROR")
        return

    cleanedFinalUrl = linkCtrl.CleanLink(driver.current_url)

    # Če je BINARY potem se gleda drugače (binary tudi ne bo kam akj redirecto)
    if start_page_type == "BINARY":  # and page.url not in history: (to tk al tk ne bi smelo bit)
        print("Added to hitroy:", page.url, "BINARY")
        history.add(page.url)

        page_type, data_type = robotCtrl.GetContentTypeFromRequest(requestOriginal)
        page.BindData(page_type, "NULL", requestOriginal.status_code)
        pageBusinessCtrl.Update(page)

        pdInfo = PageDataInfo(page.id, data_type)
        pageDataBusinessCtrl.Insert(pdInfo)

    # Če je že v history pomeni da je do tega prišlo po kakem drugem redirectu
    elif cleanedFinalUrl not in history:
        lastVisitedPages.append(page)
        history.add(page.url)

        print("Added to hitroy:", page.url, "->", cleanedFinalUrl)

        final_page_type, final_data_type = robotCtrl.GetContentTypeFromRequest(requestFinal)

        # če je redirect iz html -> binary
        if final_data_type == "BINARY":
            page.BindData(final_page_type, "NULL", requestFinal.status_code)
            pageBusinessCtrl.Update(page)

            pdInfo = PageDataInfo(page.id, final_data_type)
            pageDataBusinessCtrl.Insert(pdInfo)
        else: #če je redirect html -> html
            # Updates page type, HTML content, status code
            page.BindData(final_page_type, driver.page_source, requestFinal.status_code)
            pageBusinessCtrl.Update(page)

            # Get links
            links = linkCtrl.GetAllLinks(driver)

            for link in links:
                newPage = siteCtrl.CreateNewPage(link)

                if newPage:
                    newPage.AddPagesFrom([page])
                    frontier.append((newPage, depth+1))

            # Get images
            images = [ImageInfo(page.id, source) for source in linkCtrl.GetImageSources(driver)]

            for image in images:
                imageBusinessCtrl.Insert(image)

        # shrani cleanedFinalUrl v bazo, če ni enak page.url. page.url -> REDIRECT -> cleanedFinalUrl
        # page.url -> REDIRECT -> cleanedFinalUrl
        if page.url != cleanedFinalUrl:
            lastRedirects.append((page, cleanedFinalUrl, requestFinal.status_code, depth))

        print("Finished:", page.url, requestOriginal.status_code, " --> ", cleanedFinalUrl, requestFinal.status_code)
    else:
        history.add(page.url)

        finalVisitedPage = pageBusinessCtrl.SelectByUrl(cleanedFinalUrl)
        page.AddLinksTo([finalVisitedPage.id])
        pageBusinessCtrl.Update(page)

        print("Finished:", page.url, "redireted to -> ", driver.current_url, "already visited")



def InitFrontier(driver, sites):
    pageInfos = []

    #TEST
    sites = []
    #TEST

    #najde prve strani, da se dajo v frontier
    for site in sites:
        if site.domain == "OUTSIDE":
            continue

        print("Started - initialize:", site.domain)
        try:
            driver.get(site.domain)
            time.sleep(1)
        except TimeoutException as ex:
            print("Timeuted - initialize:", site.domain)
            continue

        requestFinal = requests.get(driver.current_url)
        print(requestFinal.url)

        page = siteCtrl.CreateNewPage(linkCtrl.CleanLink(requestFinal.url))
        page = pageBusinessCtrl.Insert(page)
        pageInfos.append((page, 1))

        print("Finished - initialize:", site.domain)

    #TEST
    #page = siteCtrl.CreateNewPage(linkCtrl.CleanLink("http://evem.gov.si/info/vec-dogodkov/tiskani-obrazci/"))
    page = siteCtrl.CreateNewPage(linkCtrl.CleanLink("http://evem.gov.si/info/uploads/tx_printforms/0211Podelitev_pooblastila_za_procesna_dejanja_v_postopkih_VEM_0320__002_.docx"))
    page = pageBusinessCtrl.Insert(page)
    pageInfos.append((page, 1))
    #TEST

    return pageInfos


def RemoveDuplicates(frontier):
    print("------------------------Removing duplicates from frontier------------------------")
    check_val = set()  # Check Flag

    #Že vpisan v bazo
    alreadyInDB = set()

    #Ustvarjen, ampak še ni v bazi
    alreadyExists = set()
    res = []

    for i in frontier:
        if i[0].url not in check_val and i[0].id is not None:
            #print("Already in DB-0:", i[0].id, i[0].url)
            #res.append(i)
            check_val.add(i[0].url)
            alreadyInDB.add(i[0].url)
            #frontier.remove(i)

    for i in frontier:
        if i[0].url not in check_val and pageBusinessCtrl.IsUrlInDB(i[0].url):
            #print("Already in DB-1:", i[0].id, i[0].url)
            #res.append(i)
            check_val.add(i[0].url)
            alreadyInDB.add(i[0].url)
            #frontier.remove(i)


    for i in frontier:
        if i[0].url in alreadyInDB:
            #print("Already in DB-2:", i[0].id, i[0].url)
            #duplicates.append(i)

            #print("Fixing duplicate:", i[0].id, i[0].url)
            # load existing page by url
            existingPage = pageBusinessCtrl.SelectByUrl(i[0].url)
            existingPage.AddLinksFrom(i[0].linksFrom)
            pageBusinessCtrl.Update(existingPage)
            res.append((existingPage, i[1]))

        elif i[0].url not in check_val:
            #print("Not duplicated:", i[0].id, i[0].url)
            res.append(i)
            check_val.add(i[0].url)
        else:
            #print("Duplicated:", i[0].id, i[0].url)
            #Če je duplilikat najdi z kom je in mu dej LinksFrom
            for j in res:
                if j[0].url == i[0].url:
                    j[0].AddLinksFrom(i[0].linksFrom)
                    break

    return res


def RemoveHistory(frontier, history):
    print("------------------------Removing duplicates from history------------------------")

    res = []
    duplicates = []
    for i in frontier:
        if i[0].url not in history:
            #print("Not in history:", i[0].id, i[0].url)
            res.append(i)
        else:
            duplicates.append(i)

    for duplicate in duplicates:
        #load existing page by url
        #print("Duplicates in history:", duplicate[0].id, duplicate[0].url)
        existingPage = pageBusinessCtrl.SelectByUrl(duplicate[0].url)
        existingPage.AddLinksFrom(duplicate[0].linksFrom)
        pageBusinessCtrl.Update(existingPage)

    return res


def CombineLastInsertedPages(frontier, lastVisitedPages):
    newFrontier = []

    #page v frontierju ki imajo from_page url removanega
    pageIdsToRemove = []

    #če jih je 10 novih, da jih ne primerja med sabo, ampak posamezno z tem kar je v bazi
    excludeIds = [lastVisitedPage.id for lastVisitedPage in lastVisitedPages]

    for lastVisitedPage in lastVisitedPages:
        similarPageIds = pageBusinessCtrl.GetSimilar(lastVisitedPage.id, 0.95)
        print("Similar to page:", lastVisitedPage.id, "similar ids:", similarPageIds)

        similarPageIds = list(set(similarPageIds)-set(excludeIds))

        if len(similarPageIds) > 0:
            pageIdsToRemove.append(lastVisitedPage.id)

            lastVisitedPage.page_type_code = "DUPLICATE"
            lastVisitedPage.html_content = None
            lastVisitedPage.AddLinksTo(similarPageIds)
            lastVisitedPage.linksFrom = []
            pageBusinessCtrl.Update(lastVisitedPage)

            imageBusinessCtrl.DeleteByPageId(lastVisitedPage.id)
            pageDataBusinessCtrl.DeleteByPageId(lastVisitedPage.id)

        excludeIds.remove(lastVisitedPage.id)

    for page, depth in frontier:
        if page.id not in pageIdsToRemove:
            newFrontier.append((page, depth))

    return newFrontier

def ManageRedirects(redirects):
    print("------------------------Manage redirects------------------------")

    global history

    addedFinalPages = []

    for page, redirectedToUrl, statusCode, depth in redirects:
        redirectedTo = None

        for finalPage in addedFinalPages:
            if finalPage.url == redirectedToUrl:
                redirectedTo = finalPage

        if redirectedTo is None:
            #Mogoče že v bazi
            redirectedTo = pageBusinessCtrl.SelectByUrl(redirectedToUrl)

            if redirectedTo is None:
                redirectedTo = siteCtrl.CreateNewPage(redirectedToUrl, True)

                if redirectedTo:
                    redirectedTo = pageBusinessCtrl.InsertWithDepth(redirectedTo, depth)
                else:
                    print("Cant make page: ", redirectedToUrl)

        if not redirectedTo:  # strani ne smeš obiskat ali je izven domene (zdej načeloma lahk)
            return
        else:
            history.add(redirectedTo.url)

            redirectedTo.linksFrom = [page.id]
            redirectedTo.linksTo = page.linksTo
            redirectedTo.page_type_code = page.page_type_code

            page.linksTo = [redirectedTo.id]

            # preveri če je v bazo vstavljeno kot
            page.html_content = str(depth) + ";" + "None"
            page.page_type_code = "REDIRECT"
            page.http_status_code = statusCode


            addedFinalPages.append(redirectedTo)

            pageBusinessCtrl.Update(redirectedTo)
            pageBusinessCtrl.Update(page)

            pageCtrl.ReplacePageInImagesAndPageDataBecauseOfRedirect(page, redirectedTo)

if __name__ == "__main__":
    main()

#Jaka
#Linke page1 -> page2 in page3 -> page2
#Link DUPLICATE -> HTML
#preveri kako so LinksFrom pa LinksTo (ali dobi page oboje, ali se slučajno LinksFrom prepišejo kje na fg)

#Julijan
#Site map
#Page data - data_type
#Duplikate kk najt