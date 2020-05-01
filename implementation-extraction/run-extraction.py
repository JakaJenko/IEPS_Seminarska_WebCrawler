import sys
import json
from RegexExtraction import RegexExtraction
from XPathExtraction import XPathExtraction
from RoadRunnerExtraction import RoadRunnerExtraction

rtvslo_paths = [
    '../input-extraction/rtvslo.si/Audi A6 50 TDI quattro_ nemir v premijskem razredu - RTVSLO.si.html',
    '../input-extraction/rtvslo.si/Volvo XC 40 D4 AWD momentum_ suvereno med najboljše v razredu - RTVSLO.si.html']
overstock_paths = [
    '../input-extraction/overstock.com/jewelry01.html',
    '../input-extraction/overstock.com/jewelry02.html']
mimovrste_paths = [
    '../input-extraction/mimovrste.si/Grafične kartice _ mimovrste=).htm',
    '../input-extraction/mimovrste.si/Procesorji _ mimovrste=).htm'
]
test_rtvslo_paths = [
'../input-extraction/test_rtvslo.si/page1.txt',
'../input-extraction/test_rtvslo.si/page2.txt'
]

regexExtractor = RegexExtraction(rtvslo_paths, overstock_paths, mimovrste_paths)
xpathExtractor = XPathExtraction(rtvslo_paths, overstock_paths, mimovrste_paths)
roadrunnerExtractor = RoadRunnerExtraction(rtvslo_paths, overstock_paths, mimovrste_paths)

if __name__ == "__main__":
    mode = 'C' #sys.argv[1]

    if mode == 'A':  # regular expressions
        rtvslo_items    = regexExtractor.RtvsloExtraction()
        overstock_items = regexExtractor.OverstockExtraction()
        mimovrste_items = regexExtractor.MimovrsteExtraction()

        for rtvslo_item in rtvslo_items:
            print("RTV SLO:\n%s" % json.dumps(rtvslo_item.__dict__, indent=4, ensure_ascii=False))

        for overstock_item in overstock_items:
            print("Overstock:\n%s" % json.dumps(overstock_item.__dict__, indent=4, ensure_ascii=False))

        for mimovrste_item in mimovrste_items:
            print("Mimovrste:\n%s" % json.dumps(mimovrste_item.__dict__, indent=4, ensure_ascii=False))

    elif mode == 'B':  # XPath
        rtvslo_items    = xpathExtractor.RtvsloExtraction()
        overstock_items = xpathExtractor.OverstockExtraction()
        mimovrste_items = xpathExtractor.MimovrsteExtraction()

        for rtvslo_item in rtvslo_items:
            print("RTV SLO:\n%s" % json.dumps(rtvslo_item.__dict__, indent=4, ensure_ascii=False))

        for overstock_item in overstock_items:
            print("Overstock:\n%s" % json.dumps(overstock_item.__dict__, indent=4, ensure_ascii=False))

        for mimovrste_item in mimovrste_items:
            print("Mimovrste:\n%s" % json.dumps(mimovrste_item.__dict__, indent=4, ensure_ascii=False))

    elif mode == 'C':  # RoadRunner-like implementation
        wrappers = roadrunnerExtractor.ExtractWrappers()


        #for wrapper in wrappers:
        print("Wrappers:\n%s" % json.dumps(wrappers, indent=4, ensure_ascii=False))