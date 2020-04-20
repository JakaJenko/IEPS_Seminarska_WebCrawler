import sys
import requests
from RegexExtraction import RegexExtraction
from XPathExtraction import XPathExtraction
from RoadRunnerExtraction import RoadRunnerExtraction

rtvslo_paths = [
    '../input-extraction/rtvslo.si/Audi A6 50 TDI quattro_ nemir v premijskem razredu - RTVSLO.si.html',
    '../input-extraction/rtvslo.si/Volvo XC 40 D4 AWD momentum_ suvereno med najboljše v razredu - RTVSLO.si.html']
overstock_paths = [
    '../input-extraction/overstock.com/jewelry01.html',
    '../input-extraction/overstock.com/jewelry02.html']
mimovrste_paths = []

regexExtractor = RegexExtraction(rtvslo_paths, overstock_paths, mimovrste_paths)
xpathExtractor = XPathExtraction(rtvslo_paths, overstock_paths, mimovrste_paths)
roadrunnerExtractor = RoadRunnerExtraction(rtvslo_paths, overstock_paths, mimovrste_paths)

regexExtractor.RtvsloExtraction()


if __name__ == "__main__":
    mode = 'A' #sys.argv[1]

    if mode == 'A':  # regular expressions
        pass
    elif mode == 'B':  # XPath
        pass
    elif mode == 'C':  # RoadRunner-like implementation
        pass