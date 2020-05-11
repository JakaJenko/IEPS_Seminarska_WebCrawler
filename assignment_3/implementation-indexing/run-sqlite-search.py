# -*- coding: utf-8 -*-
import sys
import psycopg2
from nltk.corpus import stopwords
from nltk import word_tokenize
import time
import codecs
from bs4 import BeautifulSoup

conn = psycopg2.connect(host="localhost", user="postgres", password="root")
conn.autocommit = True
path = "../PA3-data/"

stop_words_slovene = set(stopwords.words("slovene")).union(set(
        ["ter","nov","novo", "nova","zato","še", "zaradi", "a", "ali", "april", "avgust", "b", "bi", "bil", "bila", "bile", "bili", "bilo", "biti",
         "blizu", "bo", "bodo", "bojo", "bolj", "bom", "bomo", "boste", "bova", "boš", "brez", "c", "cel", "cela",
         "celi", "celo", "d", "da", "daleč", "dan", "danes", "datum", "december", "deset", "deseta", "deseti", "deseto",
         "devet", "deveta", "deveti", "deveto", "do", "dober", "dobra", "dobri", "dobro", "dokler", "dol", "dolg",
         "dolga", "dolgi", "dovolj", "drug", "druga", "drugi", "drugo", "dva", "dve", "e", "eden", "en", "ena", "ene",
         "eni", "enkrat", "eno", "etc.", "f", "februar", "g", "g.", "ga", "ga.", "gor", "gospa", "gospod", "h", "halo",
         "i", "idr.", "ii", "iii", "in", "iv", "ix", "iz", "j", "januar", "jaz", "je", "ji", "jih", "jim", "jo",
         "julij", "junij", "jutri", "k", "kadarkoli", "kaj", "kajti", "kako", "kakor", "kamor", "kamorkoli", "kar",
         "karkoli", "katerikoli", "kdaj", "kdo", "kdorkoli", "ker", "ki", "kje", "kjer", "kjerkoli", "ko", "koder",
         "koderkoli", "koga", "komu", "kot", "kratek", "kratka", "kratke", "kratki", "l", "lahka", "lahke", "lahki",
         "lahko", "le", "lep", "lepa", "lepe", "lepi", "lepo", "leto", "m", "maj", "majhen", "majhna", "majhni",
         "malce", "malo", "manj", "marec", "me", "med", "medtem", "mene", "mesec", "mi", "midva", "midve", "mnogo",
         "moj", "moja", "moje", "mora", "morajo", "moram", "moramo", "morate", "moraš", "morem", "mu", "n", "na", "nad",
         "naj", "najina", "najino", "najmanj", "naju", "največ", "nam", "narobe", "nas", "nato", "nazaj", "naš", "naša",
         "naše", "ne", "nedavno", "nedelja", "nek", "neka", "nekaj", "nekatere", "nekateri", "nekatero", "nekdo",
         "neke", "nekega", "neki", "nekje", "neko", "nekoga", "nekoč", "ni", "nikamor", "nikdar", "nikjer", "nikoli",
         "nič", "nje", "njega", "njegov", "njegova", "njegovo", "njej", "njemu", "njen", "njena", "njeno", "nji",
         "njih", "njihov", "njihova", "njihovo", "njiju", "njim", "njo", "njun", "njuna", "njuno", "no", "nocoj",
         "november", "npr.", "o", "ob", "oba", "obe", "oboje", "od", "odprt", "odprta", "odprti", "okoli", "oktober",
         "on", "onadva", "one", "oni", "onidve", "osem", "osma", "osmi", "osmo", "oz.", "p", "pa", "pet", "peta",
         "petek", "peti", "peto", "po", "pod", "pogosto", "poleg", "poln", "polna", "polni", "polno", "ponavadi",
         "ponedeljek", "ponovno", "potem", "povsod", "pozdravljen", "pozdravljeni", "prav", "prava", "prave", "pravi",
         "pravo", "prazen", "prazna", "prazno", "prbl.", "precej", "pred", "prej", "preko", "pri", "pribl.",
         "približno", "primer", "pripravljen", "pripravljena", "pripravljeni", "proti", "prva", "prvi", "prvo", "r",
         "ravno", "redko", "res", "reč", "s", "saj", "sam", "sama", "same", "sami", "samo", "se", "sebe", "sebi",
         "sedaj", "sedem", "sedma", "sedmi", "sedmo", "sem", "september", "seveda", "si", "sicer", "skoraj", "skozi",
         "slab", "smo", "so", "sobota", "spet", "sreda", "srednja", "srednji", "sta", "ste", "stran", "stvar", "sva",
         "t", "ta", "tak", "taka", "take", "taki", "tako", "takoj", "tam", "te", "tebe", "tebi", "tega", "težak",
         "težka", "težki", "težko", "ti", "tista", "tiste", "tisti", "tisto", "tj.", "tja", "to", "toda", "torek",
         "tretja", "tretje", "tretji", "tri", "tu", "tudi", "tukaj", "tvoj", "tvoja", "tvoje", "u", "v", "vaju", "vam",
         "vas", "vaš", "vaša", "vaše", "ve", "vedno", "velik", "velika", "veliki", "veliko", "vendar", "ves", "več",
         "vi", "vidva", "vii", "viii", "visok", "visoka", "visoke", "visoki", "vsa", "vsaj", "vsak", "vsaka", "vsakdo",
         "vsake", "vsaki", "vsakomur", "vse", "vsega", "vsi", "vso", "včasih", "včeraj", "x", "z", "za", "zadaj",
         "zadnji", "zakaj", "zaprta", "zaprti", "zaprto", "zdaj", "zelo", "zunaj", "č", "če", "često", "četrta",
         "četrtek", "četrti", "četrto", "čez", "čigav", "š", "šest", "šesta", "šesti", "šesto", "štiri", "ž", "že",
         "svoj", "jesti", "imeti","\u0161e", "iti", "kak", "www", "km", "eur", "pač", "del", "kljub", "šele", "prek",
         "preko", "znova", "morda","kateri","katero","katera", "ampak", "lahek", "lahka", "lahko", "morati", "torej", '.', ',', '?', '!', "+", '-', '=', ':', ';', '*', '/', '', '(', ')']))

def get_snippet(filepath, indexes):
    result = ""
    file = codecs.open(path + filepath, 'r', encoding='utf-8', errors='ignore')
    contents = file.read()
    cleanedContents = BeautifulSoup(contents, 'html.parser')
    for script in cleanedContents.find_all(['script', 'iframe', 'style']):
        script.decompose()
    text = cleanedContents.get_text()
    tokens = word_tokenize(text)
    locila = {',', '.', '?', "!", '(', ')', '+', '-', ';', ':'}
    for i in indexes:
        i = int(i)
        forward = ""
        range_j = 3
        j = 0
        while j < range_j:
            word = tokens[i+j+1]
            if word not in locila:
                forward += " " + word
            else:
                range_j += 1
            j += 1

        backward = ""
        range_j = 3
        j = 0
        while j < range_j:
            word = tokens[i-j-1]
            if word not in locila:
                backward = word + " " + backward
            else:
                range_j += 1
            j += 1

        result += " ... "+backward+tokens[i]+forward
    return result

def search_database(query):
    results = []
    query = [str(w) for w in query]

    cur = conn.cursor()
    cur.execute(
        """SELECT p.documentname, sum(p.frequency) as frequency, string_agg(p.indexes, ',') AS indexes
            FROM ieps3.indexword  w INNER JOIN ieps3.posting p ON w.word = p.word
            WHERE w.word IN %s
            group by p.documentname
            order by 2 desc
            """, (tuple(query),))

    for document, frequency, indexes in cur.fetchall():
        results.append([document, frequency, indexes])

    cur.close()
    return results

if __name__ == "__main__":
    arguments = sys.argv[1:]
    arguments = " ".join(arguments).replace('"', '')
    arguments = "social services" #only for testing

    tokens = word_tokenize(arguments)
    clean_tokens = []
    for token in tokens:
        token = token.lower()
        if token not in stop_words_slovene:
            clean_tokens.append(token)

    t0 = time.time()
    results = search_database(clean_tokens)
    t1 = time.time()

    execution_time = (t1-t0)*100
    print('Results for a query: "{}"\n'.format(arguments))
    print("  Results found in {:.2f}ms\n".format(execution_time))
    print("  Frequencies Document                                 Snippet")
    print("  ----------- ---------------------------------------- -----------------------------------------------------------------------")
    for result in results:
        snippet = get_snippet(result[0], result[2].split(","))
        print("  {:11s} {:40s} {}".format(str(result[1]), result[0], snippet+" ..."))

