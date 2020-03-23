SELECT *
FROM crawldb.site
INNER JOIN crawldb.page ON crawldb.site.id = crawldb.page.site_id;