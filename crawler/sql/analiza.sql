--število pageov v bazi
select count(*) as st_pages
from crawldb.page p
where p.page_type_code !='FRONTIER'

--Število pageov v vsaki domeni
select count(*) as st_pages, s.domain, s.id
from crawldb.site s
inner join crawldb.page p on p.site_id = s.id
where p.page_type_code != 'FRONTIER'
group by s.id

--število binarnih datotek
select count(*) as st_datotek
from crawldb.page_data p1

-- število binarnih datotek po tipu
select count(*) as st_datotek, p1.data_type_code
from crawldb.page_data p1
group by p1.data_type_code

--število binarnih datotek po domenah /lahko tudi tipi po domenah
select count(*) as st_datotek, s.domain--, pd.data_type_code
from crawldb.page_data pd
inner join crawldb.page p on p.id = pd.page_id
inner join crawldb.site s on s.id = p.site_id
group by s.domain-- pd.data_type_code
order by s.domain

-- število slik v celotni bazi
select count(*) as st_slik
from crawldb.image i

--število slik po tipu
select count(*) as st_slik, i.content_type
from crawldb.image i
group by i.content_type

--povprečno število slik na page v celotni bazi
select count(*)::decimal / count(distinct i.page_id) as povprecje_slik
from crawldb.image i

--število slik na posamezni domeni
select count(*) as st_slik, s.domain
from crawldb.image i
inner join crawldb.page p on p.id = i.page_id
inner join crawldb.site s on s.id = p.site_id
group by s.id
--za povprečje ročno deli z številom pageov na domeni

--število linkov
select count(*) as st_linkov
from crawldb.link l

--število linkov
select count(*) as st_linkov, s.domain
from crawldb.link l
inner join crawldb.page p on p.id = l.from_page
inner join crawldb.site s on s.id = p.site_id
group by s.id

--top 5 strani z največ linki 
select count(*) as st_linkov, p.url 
from crawldb.link l
inner join crawldb.page p on p.id = l.from_page
group by p.id
order by st_linkov desc
limit 5

--top 5 strani na katere kaže največ linkov
select count(*) as st_linkov, p.url 
from crawldb.link l
inner join crawldb.page p on p.id = l.to_page
where p.page_type_code != 'FRONTIER'
group by p.id
order by st_linkov desc
limit 5

--duplikatov
SET pg_trgm.similarity_threshold = 0.8;

SELECT similarity(p1.html_content, p2.html_content) AS sim, p1.id, p2.id
FROM   crawldb.page p1
JOIN   crawldb.page p2 ON p1.html_content <> p2.html_content
               AND  p1.html_content % p2.html_content
ORDER  BY sim DESC
limit 10



