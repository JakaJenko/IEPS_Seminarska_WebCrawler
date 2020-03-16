import concurrent.futures
import threading
import pathlib
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Business.Page.PageBusinessController import PageBusinessController
from Controller.LinkController import LinkController

THREADS = 5
TIMEOUT = 5
MAX_DEPTH = 2

SEEDs = [("http://gov.si", 2),
         ("http://evem.gov.si", 1),
         ("http://e-uprava.gov.si", 2),
         ("http://e-prostor.gov.si", 2)]

frontier = []

linkCtrl = LinkController()


def main():
    lock = threading.Lock()

    global frontier
    frontier = SEEDs
    history = set()


    pathHere = pathlib.Path().absolute()
    WEB_DRIVER_LOCATION = str(pathHere) + "\..\chromedriver.exe"

    chrome_options = Options()
    # If you comment the following line, a browser will show ...
    chrome_options.add_argument("--headless")

    # Adding a specific user agent
    chrome_options.add_argument("user-agent=fri-ieps-CoronaBojz123")

    driver = webdriver.Chrome(WEB_DRIVER_LOCATION, options=chrome_options)


    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        while len(frontier) != 0:
            future = []

            for _ in range(THREADS):
                address, depth = None, None

                with lock:
                    if len(frontier) != 0:
                        address, depth = frontier.pop()
                        history.add(address)

                if address is not None:
                    if depth < MAX_DEPTH:
                        future.append(executor.submit(GetPageData, driver, address, depth))


            # WAIT
            concurrent.futures.wait(future, timeout=None, return_when=concurrent.futures.ALL_COMPLETED)

            # remove duplicates from frontier
            frontier = list(dict.fromkeys(frontier))

            # remove history from list
            frontier = [(address, depth) for address, depth in frontier if address not in history]

            # WAIT
            concurrent.futures.wait(future, timeout=None, return_when=concurrent.futures.ALL_COMPLETED)


def GetPageData(driver, address, depth):
    global frontier

    print("Started:", address)
    head = requests.head(address)
    print(head.headers, head.history, head.is_redirect)

    driver.get(address)

    # Timeout needed for Web page to render (read more about it)
    time.sleep(TIMEOUT)

    print("Finished:", address)

    links = [(link, depth+1) for link in linkCtrl.GetAllLinks(driver)]
    frontier.extend(links)


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