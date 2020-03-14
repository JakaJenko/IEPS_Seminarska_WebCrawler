import concurrent.futures
import threading
import pathlib
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Business.Page.PageBusinessController import PageBusinessController
from Controller.LinkController import LinkController
from sys import platform


THREADS = 5
TIMEOUT = 1 #5
MAX_DEPTH = 3

SEEDs = [("http://gov.si", 1),
         ("http://evem.gov.si", 1),
         ("http://e-uprava.gov.si", 1),
         ("http://e-prostor.gov.si", 1)]

frontier = []

linkCtrl = LinkController()


def main():
    lock = threading.Lock()

    global frontier
    frontier = SEEDs
    history = set()


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
    driver.get(address)

    # Timeout needed for Web page to render (read more about it)
    time.sleep(TIMEOUT)

    print("Finished:", address)

    links = [(link, depth+1) for link in linkCtrl.GetAllLinks(driver)]
    frontier.extend(links)


if __name__ == "__main__":
    main()

#iskanje linkov - href, , src, onclick, location.href, document.location
#urejanje linkov