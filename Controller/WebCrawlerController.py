import concurrent.futures
import threading
import pathlib
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Business.Page.PageBusinessController import PageBusinessController
from Controller.LinkController import LinkController
from Controller.RobotController import RobotController
from Controller.SiteController import SiteController
from Business.Site.SiteBusinessController import SiteBusinessController
from Business.Page.PageBusinessController import PageBusinessController
from Business.Site.SiteInfo import SiteInfo
from sys import platform
import sys
import requests
import urllib.robotparser
from urllib.parse import urlparse

siteBusinessCtrl = SiteBusinessController()
pageBusinessCtrl = PageBusinessController()

linkCtrl = LinkController()
robotCtrl = RobotController()


THREADS = 10
TIMEOUT = 5
MAX_DEPTH = 3

SEEDs = [#("http://gov.si/", 1),
         ("http://evem.gov.si/", 1),
         ("http://e-uprava.gov.si/", 3),
         ("http://e-prostor.gov.si/", 3)]

sites = [SiteInfo(seed[0]) for seed in SEEDs]

for site in sites:
    site = siteBusinessCtrl.Insert(site)

siteCtrl = SiteController(sites)

# frontier = [(SiteInfo, depth), ...]
frontier = []
history = set()


def main():
    lock = threading.Lock()

    global frontier
    global history


    pathHere = pathlib.Path().absolute()
    WEB_DRIVER_LOCATION = str(pathHere) + "\..\chromedriver.exe"

    # ChromeDriver for mac users
    if platform == "darwin":
        WEB_DRIVER_LOCATION = str(pathHere) + "/../chromedriver"

    chrome_options = Options()
    # If you comment the following line, a browser will show ...
    chrome_options.add_argument("--headless")

    # Adding a specific user agent
    chrome_options.add_argument("user-agent=fri-ieps-CoronaBojz123")

    #driver = webdriver.Chrome(WEB_DRIVER_LOCATION, options=chrome_options)

    drivers = []
    for i in range(THREADS):
        drivers.append(webdriver.Chrome(WEB_DRIVER_LOCATION, options=chrome_options))
    #driver.set_page_load_timeout(TIMEOUT+5)

    # Add first pages to frontier
    frontier = InitFrontier(drivers[0], sites)

    #sys.exit()

    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        while len(frontier) != 0:
            print("Frontier length:", len(frontier))
            future = []

            for threadNumber in range(THREADS):
                page, depth = None, None

                with lock:
                    while page is None:
                        if len(frontier) != 0:
                            page, depth = frontier.pop()

                            if depth >= MAX_DEPTH:
                                history.add(page.url)
                                page, depth = None, None
                        else:
                            break

                    if page is not None:
                        future.append(executor.submit(GetPageData, drivers[threadNumber], page, depth))

            # WAIT
            print("WAIT!")
            concurrent.futures.wait(future, timeout=None, return_when=concurrent.futures.ALL_COMPLETED)
            # remove duplicates from frontier
            print(len(frontier))
            frontier = RemoveDuplicates(frontier)
            print(len(frontier))

            # remove history from list
            frontier = [(page, depth) for page, depth in frontier if page.url not in history]
            print(len(frontier))

            for i in range(len(frontier)):
                if frontier[i][0].id is None:
                    newTuple = (pageBusinessCtrl.Insert(frontier[i][0]), frontier[i][1])
                    frontier[i] = newTuple

            # WAIT
            #concurrent.futures.wait(future, timeout=None, return_when=concurrent.futures.ALL_COMPLETED)


def GetPageData(driver, page, depth):
    global frontier
    global history

    print("Started:", page.url)

    try:
        requestOriginal = requests.get(page.url)
        driver.get(page.url)

        # Timeout needed for Web page to render (read more about it)
        time.sleep(TIMEOUT)

        requestFinal = requests.get(driver.current_url)
    except:
        history.add(page.url)
        print("Finished:", page.url, "Page ERROR")
        return

    # Če je že v history pomeni da je do tega prišlo po kakem drugem redirectu
    if driver.current_url not in history:
        cleanedFinalUrl = linkCtrl.CleanLink(driver.current_url)

        history.add(page.url)
        history.add(cleanedFinalUrl)

        page.BindData("HTML", "HTML CONTENT", 1)
        pageBusinessCtrl.Update(page)

        # Get links
        links = linkCtrl.GetAllLinks(driver)

        for link in links:
            newPage = siteCtrl.CreateNewPage(link)

            if newPage:
                frontier.append((newPage, depth+1))

        # Get images
        images = [source for source in linkCtrl.GetImageSources(driver)]

        #save to database

    else:
        history.add(page.url)

    print("Finished:", page.url, requestOriginal.status_code, " --> ", cleanedFinalUrl, requestFinal.status_code)


def InitFrontier(driver, sites):
    pageInfos = []

    #najde prve strani, da se dajo v frontier
    for site in sites:
        print("Started:", site.domain)
        driver.get(site.domain)
        time.sleep(1)
        requestFinal = requests.get(driver.current_url)
        print(requestFinal.url)

        page = siteCtrl.CreateNewPage(linkCtrl.CleanLink(requestFinal.url))
        page = pageBusinessCtrl.Insert(page)

        pageInfos.append((page, 1))

    return pageInfos


def RemoveDuplicates(frontier):
    check_val = set()  # Check Flag
    res = []

    for i in frontier:
        if i[0].id is not None:
            res.append(i)
            check_val.add(i[0].url)

    for i in frontier:
        if i[0].url not in check_val:
            res.append(i)
            check_val.add(i[0].url)

    return res



if __name__ == "__main__":
    main()

#Faza 1
#iskanje linkov - href, , src, onclick, location.href, document.location - Julijan
#urejanje linkov (je na slajdih kaj je treba) - Julijan
#Mogoče lahko uporabima request.head za kaj (preusmeritve?...) - Jaka
#Premakni History v GetPageData, tam poglej če je kam preusmeri (lahko si zapomnema samo končno stran, ne cele poti preusmeritev) - Jaka
#Upoštevaj robots.txt - Edn ko ma cajt

#Faza 2
#V GetPageData poglej kake podatke dobiš - recimo če je večje kot 10MB je verjetno kak file

#Faza 3
#Shranjevanje v bazo