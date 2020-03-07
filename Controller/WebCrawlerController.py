import concurrent.futures
import threading
import pathlib
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Business.Page.PageBusinessController import PageBusinessController
from Controller.LinkController import LinkController

THREADS = 5
TIMEOUT = 5

SEEDs = ["http://gov.si",
         "http://evem.gov.si",
         "http://e-uprava.gov.si",
         "http://e-prostor.gov.si"]

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
                address = ""

                with lock:
                    if len(frontier) != 0:
                        address = frontier.pop()
                        history.add(address)

                if address != "":
                    future.append(executor.submit(GetPageData, driver, address))

            # WAIT
            concurrent.futures.wait(future, timeout=None, return_when=concurrent.futures.ALL_COMPLETED)

            # remove duplicates from frontier
            frontier = list(dict.fromkeys(frontier))

            # remove histroy from list
            frontier = [i for i in frontier if i not in history]

            # WAIT
            concurrent.futures.wait(future, timeout=None, return_when=concurrent.futures.ALL_COMPLETED)


def GetPageData(driver, address):
    global frontier

    print("Started:", address)
    driver.get(address)

    # Timeout needed for Web page to render (read more about it)
    time.sleep(TIMEOUT)

    print("Finished:", address)

    frontier.extend(linkCtrl.GetAllLinks(driver))


if __name__ == "__main__":
    main()

#iskanje linkov - href, , src, onclick, location.href, document.location
#urejanje linkov