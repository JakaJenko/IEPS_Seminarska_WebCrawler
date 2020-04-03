# IEPS_Seminarska_WebCrawler
IEPS Iskanje in ekstrakcija podatkov s spleta - Seminarska 1 - Web Crawler

## Database
https://we.tl/t-KHuQvPZgdA

# Instructions for running
- In AbstractDatabaseBusinessController set database connection data (host name, user, password).

- In StartController set the SEED pages.

- In WebCrawlerController set the parameters THREADS, TIMEOUT and MAX_DEPTH.

- Comment one of the following lines (probably this is already set so that FreshStart is uncomented, while Continue is comented)
sites, frontier, history = startCtrl.FreshStart()  
sites, frontier, history = startCtrl.Continue()

- Clear the database with following comands.
DELETE FROM crawldb.image;  
DELETE FROM crawldb.link;  
DELETE FROM crawldb.page_data;  
DELETE FROM crawldb.page;  
DELETE FROM crawldb.site;  

- Add following data in to database.
INSERT INTO crawldb.page_type(code)
VALUES ('REDIRECT');

INSERT INTO crawldb.data_type(code)
VALUES ('UNKNOWN');

INSERT INTO crawldb.data_type(code)
VALUES ('XLS');

INSERT INTO crawldb.data_type(code)
VALUES ('XLSX');

INSERT INTO crawldb.data_type(code)
VALUES ('ZIP');

- And then run this (WebCrawlerController) file
