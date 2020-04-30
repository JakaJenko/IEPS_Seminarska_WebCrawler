import difflib
import codecs
import re
from bs4 import BeautifulSoup, Comment
from lxml import etree
import lxml
import xml.etree.ElementTree as parser
from PageTemplates.RoadRunnerItem import RoadRunnerItems

def GetTagStart(find, line):
    if '<' in line:
        #print(line)
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


def get_parent_map(root):
    return {c:p for p in root.iter() for c in p}

def extract_text_info(root, original_root):
    path_txt = []

    parent_map = get_parent_map(original_root)

    for child in root:
        if child.text is not None and len(child.text.strip()) > 0:
            c = child
            arr = []
            while c != original_root:
                arr.append(c.tag)
                c = parent_map[c]
            arr.append(original_root.tag)

            #print("Path:", '/'.join(arr[::-1]))
            #print("Txt:", child.text.strip())

            path_txt.append(('/'.join(arr[::-1]), child.text.strip()))

        toAppend = extract_text_info(child, original_root)
        if len(toAppend) > 0:
            path_txt.extend(toAppend)

    #print(path_txt)
    return path_txt

def needsFix(s):
    toFix = ["svg"]

    for t in toFix:
        if t in s:
            return True

    return False


def fixXML(xml):

    fixed = []

    for line in xml.split("\n"):
        #print(line.replace(" ", "")[:10])

        if needsFix(line):
            print(line)
            print(line[-2:])
            if line[-2:] != "/>":
                line = line.replace(">", "/>")

        fixed.append(line)

    return "\n".join(fixed)

def findMatchingXPath(line, path_txt):
    #print(path_txt)
    #print(line[1:].strip())
    for path, text in path_txt:
        #print(text)
        if Similar(line[1:].strip(), text) > 0.95:
            return path

    return None


class RoadRunnerExtraction():

    def __init__(self, rtvslo_pages=[], overstock_pages=[], mimovrste_pages=[]):
        self.rtvslo_pages = rtvslo_pages
        self.overstock_pages = overstock_pages
        self.mimovrste_pages = mimovrste_pages

    def ExtractWrappers(self):
        wrappers = []
        for p1, p2 in [self.rtvslo_pages, self.mimovrste_pages, self.overstock_pages]:
            page1 = codecs.open(p1, 'r', encoding='utf-8', errors='ignore').read()
            page2 = codecs.open(p2, 'r', encoding='utf-8', errors='ignore').read()

            #extract only body
            soup1 = BeautifulSoup(page1, 'html.parser')
            body1 = soup1.find('body')
            page1 = BeautifulSoup(str(body1.findChildren(recursive=False)), 'html.parser')
            for script in page1.find_all(['script', 'img', 'iframe', 'style', 'a', 'svg']):
                script.decompose()

            for element in page1(text=lambda text: isinstance(text, Comment)):
                element.extract()

            page1 = BeautifulSoup(str(page1)[3:-1], 'html.parser').prettify()
            page1 = page1.split('\n')

            soup2 = BeautifulSoup(page2, 'html.parser')
            body2 = soup2.find('body')
            page2 = BeautifulSoup(str(body2.findChildren(recursive=False)), 'html.parser')
            for script in page2.find_all(['script', 'img', 'iframe', 'style', 'a', 'svg']):
                script.decompose()

            for element in page2(text=lambda text: isinstance(text, Comment)):
                element.extract()

            page2 = BeautifulSoup(str(page2)[3:-1], 'html.parser').prettify()
            page2 = page2.split('\n')

            #root = parser.fromstring(xml)
            #extract_text_info(root, root)

            #return None
            #print(page1)

            fixedPage1 = []

            for line in page1:
                if len(line) > 0:
                    if line[0] != ",":
                        fixedPage1.append(line)

            fixedPage1 = etree.HTML("\n".join(fixedPage1))
            fixedPage1 = etree.tostring(fixedPage1, pretty_print=False, method="html").decode('UTF-8')

            fixedPage1 = BeautifulSoup(fixedPage1, 'xml')
            fixedPage1 = fixedPage1.prettify()

            #fixedPage1 = fixXML(fixedPage1)

            #print(fixedPage1)

            root = parser.fromstring(fixedPage1)
            path_txt = extract_text_info(root, root)
            #print(path_txt)

            #diff = difflib.ndiff(page1, page2)

            find = ["h1", "h2", "h3", "h4", "h5", "div", "p", "td", "b"]

            blocks = []

            diff = difflib.unified_diff(page1, page2)

            #for i in diff:
            #    print(i)

            inPage1 = []
            inPage2 = []
            tmp = None

            articles = []

            for l in diff:

                if "/article" in l:
                    articles.append("E - " + str(len(blocks)))
                elif "article" in l:
                    articles.append("S - " + str(len(blocks)))

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

            last = ("", "")

            '''
            articlesCleaned = []

            for article in articles:
                article = article.split(" - ")

                if last[0] == "S" and article[0] == "E" and last[1] != article[1]:
                    articlesCleaned.extend([last, article])

                last = article
            '''

            results = []

            for i, (inPage1, inPage2) in enumerate(blocks):
                '''
                for type, row in articlesCleaned:
                    if type == "S" and int(row) == i:
                        print("<article>")
                        break
                '''

                scoreDiff = Similar(inPage1[1], inPage2[1])
                scoreMain = mainScore(inPage1[1], inPage2[1], len(blocks))
                blockFeature = findMatchingXPath(inPage1[1], path_txt)

                results.append((scoreDiff, scoreMain, blockFeature, inPage1[1][:30][1:].strip(), inPage2[1][:30][1:].strip()))

                '''
                print("<" + inPage1[0] + ">")
                print(mainScore(inPage1[1], inPage2[1], len(blocks)))
                print(inPage1[1].replace("-", "\t"))
                print(inPage2[1].replace("+", "\t"))
                print("</" + inPage1[0] + ">")
                '''

                '''
                for type, row in articlesCleaned:
                    if type == "E" and int(row)-1 == i:
                        print("</article>")
                        break
                '''

                #print()

            header = [("scoreDiff", "scoreMain", "blockFeature", "file1", "file2")]
            results = list(set(tuple(result) for result in results))

            header.extend(results)
            results = header

            roadRunnerItems = []

            for result in results:
                new_item = RoadRunnerItems.RoadRunnerItem(result[0], result[1], result[2], result[3], result[4]).__dict__
                roadRunnerItems.append(new_item)

            wrappers.append(roadRunnerItems)

        return wrappers
        '''
        for i, d in enumerate(results):
            line = '|'.join(str(x).ljust(20) for x in d)
            print(line)
            if i == 0:
                print('-' * len(line))
        '''