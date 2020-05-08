CREATE TABLE ieps3.IndexWord (
  word TEXT PRIMARY KEY
);

CREATE TABLE ieps3.Posting (
  word TEXT NOT NULL,
  documentName TEXT NOT NULL,
  frequency INTEGER NOT NULL,
  indexes TEXT NOT NULL,
  PRIMARY KEY(word, documentName),
  FOREIGN KEY (word) REFERENCES ieps3.IndexWord(word)
);
