import difflib
import codecs
import re
from bs4 import BeautifulSoup


def GetTagStart(find, line):
    if '<' in line:
        # print("Line:", line)
        tag = re.finditer('(<([^\/\s]*) *.*>)', line)
        tag = [t for t in tag]

        tag = tag[0].group(2)
        # print("Tag:", tag)

        if len(tag) == 0:
            return None

        if tag in find:
            # print("OK tag")
            return tag

    return None


def Similar(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()

def IsOK(line):
    line = line.replace(" ", "")
    line = line.replace("-", "")
    line = line.replace("+", "")

    if len(line) < 2:
        return False

    if line[0] == "<" and line[-1] == ">":
        return False

    return True

def mainScore(s1, s2, blocks):
    #returns mainscore FOR S1!
    sim = Similar(s1, s2)
    diffs1 = 1-sim
    return (diffs1*len(s1)) / blocks

class RoadRunnerExtraction():

    def __init__(self, rtvslo_pages=[], overstock_pages=[], mimovrste_pages=[]):
        self.rtvslo_pages = rtvslo_pages
        self.overstock_pages = overstock_pages
        self.mimovrste_pages = mimovrste_pages

    def ExtractWrappers(self):
        wrappers = []
        for p1, p2 in [self.mimovrste_pages]:#, self.mimovrste_pages, self.overstock_pages]:
            print("as")

            page1 = codecs.open(p1, 'r', encoding='utf-8', errors='ignore').read()
            page2 = codecs.open(p2, 'r', encoding='utf-8', errors='ignore').read()

            #extract only body
            soup1 = BeautifulSoup(page1, 'html.parser')
            body1 = soup1.find('body')
            page1 = BeautifulSoup(str(body1.findChildren(recursive=False)), 'html.parser')
            for script in page1.find_all(['script', 'img', 'iframe', 'style', 'a']):
                script.decompose()
            page1 = BeautifulSoup(str(page1)[3:-1], 'html.parser').prettify()
            page1 = page1.split('\n')

            soup2 = BeautifulSoup(page2, 'html.parser')
            body2 = soup2.find('body')
            page2 = BeautifulSoup(str(body2.findChildren(recursive=False)), 'html.parser')
            for script in page2.find_all(['script', 'img', 'iframe', 'style', 'a']):
                script.decompose()
            page2 = BeautifulSoup(str(page2)[3:-1], 'html.parser').prettify()
            page2 = page2.split('\n')


            #diff = difflib.ndiff(page1, page2)

            find = ["h1", "h2", "h3", "h4", "h5", "div", "p", "td", "b"]

            blocks = []

            diff = difflib.unified_diff(page1, page2)

            #for i in diff:
            #    print(i)

            inPage1 = []
            inPage2 = []
            tmp = None

            for l in diff:
                #if "article" in l:
                #    print("ARTICE")

                #print("TAG")
                newTag = GetTagStart(find, l)
                #print("\TAG")

                if newTag is not None:
                    tmp = newTag
                    #print("New tmp:", tmp)

                if "-" == l[0]:
                    if not IsOK(l):
                        continue

                    #print("Tmp:", tmp)
                    #print("Line:", l)
                    if len(inPage1) == 0:
                        inPage1.append(tmp)

                    inPage1.append(l)
                elif "+" == l[0]:
                    if not IsOK(l):
                        continue

                    if len(inPage2) == 0:
                        if len(inPage1) == 0:
                            continue

                        inPage2.append(inPage1[0])

                    inPage2.append(l)
                else:
                    if len(inPage1) > 0 and len(inPage2) > 0:
                        #print("Page1:", inPage1)
                        #print("Page2:", inPage2)
                        if inPage1[0] is not None:
                            blocks.append((inPage1, inPage2))
                        #print()

                    inPage1 = []
                    inPage2 = []


            differentBlocks = []

            for inPage1, inPage2 in blocks:
                #print(inPage1[1])
                #print(inPage2[1])
                differScore = Similar(inPage1[1], inPage2[1])
                #print(differScore)

                if differScore < 0.6:
                    differentBlocks.append((inPage1, inPage2))

            #print("|||||||||||||||||||||||||||||||||||||||||||||")

            for inPage1, inPage2 in blocks:
                print("<" + inPage1[0] + ">")
                print(inPage1[1].replace("-", "\t"))
                print(inPage2[1].replace("+", "\t"))
                print("</" + inPage1[0] + ">")
                print()
