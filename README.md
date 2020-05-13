# IEPS Seminarska: Data indexing and retrieval
IEPS Iskanje in ekstrakcija podatkov s spleta - Seminarska 3  
Avtorja: Jaka Jenko, Julijan Jug

## Instructions for running
Python 3 and sqlite is required.

Required libraries:
- bs4
- codecs
- nltk
- psycopg2

Install them with the use of "pip install" or "conda install".  

First create a database and tables using sql script database_creation.sql.  
Then fill the indexing tables by running indexing.py like:
```
python Indexing.py
```
To search for a desired query using inverted index run:
```
python run-sqlite-search.py your query
```
Or for basic search run:
```
python run-basic-search.py your query
```
