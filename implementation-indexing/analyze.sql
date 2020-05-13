-- most common word
SELECT p.word, sum(p.frequency) as freq
FROM ieps3.indexword i
right JOIN ieps3.posting p ON i.word = p.word
group by p.word
order by freq desc;

-- all words
select count(*)
from ieps3.indexword;

-- all tokens 
SELECT sum(p.frequency)as freq
FROM ieps3.indexword i
inner JOIN ieps3.posting p ON i.word = p.word;

-- top number of occurances in a single document
SELECT p.word, p.documentname, sum(p.frequency) as freq
FROM ieps3.indexword i
right JOIN ieps3.posting p ON i.word = p.word
group by p.documentname, p.word
order by freq desc

-- number of documents a word apperas in
SELECT p.word, count(*) as freq
FROM ieps3.indexword i
right JOIN ieps3.posting p ON i.word = p.word
group by p.word
order by freq desc

--document with most diverse vocabulary
SELECT p.documentname, count(p.word) as freq
FROM ieps3.indexword i
right JOIN ieps3.posting p ON i.word = p.word
group by p.documentname
order by freq desc