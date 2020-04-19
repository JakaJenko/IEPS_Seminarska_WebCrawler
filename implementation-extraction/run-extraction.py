import sys
import requests


page_paths = [
    'overstock.com/jewelry01.html',
    'overstock.com/jewelry02.html',
    'rtvslo.si/Audi A6 50 TDI quattro_ nemir v premijskem razredu - RTVSLO.si.html',
    'rtvslo.si/Volvo XC 40 D4 AWD momentum_ suvereno med najboljše v razredu - RTVSLO.si.html'
]

if __name__ == "__main__":
    mode = sys.argv[1]
    pages_contents = []
    for page_path in page_paths:
        pageContent = open('../input-extraction/'+page_path, 'rb').read()
        pages_contents.append(pageContent)

    if mode == 'A':  # regular expressions
        pass
    elif mode == 'B':  # XPath
        pass
    elif mode == 'C':  # RoadRunner-like implementation
        pass