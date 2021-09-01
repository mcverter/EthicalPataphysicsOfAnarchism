CREATE DATABASE RadicalEmpiricism if not exists;
/*************************************************
 *
 *    DATA TABLES 
 *
 *************************************************/
CREATE TABLE if not exists sentences  (
	id SERIAL PRIMARY KEY,
	English TEXT NOT NULL,
	French TEXT NOT NULL,
	Book TEXT
);

CREATE TABLE french_word if not exists(
	id id INT AUTO_INCREMENT PRIMARY,
	original TEXT UNIQUE NOT NULL,
	sans_diacritics TEXT,
	english_cognate TEXT,
);

CREATE TABLE lingis_word if not exists(
	id id INT AUTO_INCREMENT PRIMARY,
	lingis TEXT NOT NULL,
);

CREATE TABLE french_lingis_correspondence if not exists ();

CREATE TABLE morphologies if not exists (
		cnrtl TEXT,
);

CREATE TABLE etymologies if not exists ();

CREATE TABLE semantics IF NOT EXISTS ();

CREATE TABLE definitions if not exists (
	littre TEXT,
	cnrtl TEXT,
	academie9 TEXT,
	miriam_webster TEXT,
);


CREATE TABLE word_frequencies if not exists();


CREATE TABLE book (
	BookID INT AUTO_INCREMENT,
	Abrev TINYTEXT NOT NULL,
	FullTitle TEXT,
	Year INT,
	BibliographicalInfo TEXT,
	TotalWords INT,
	PRIMARY KEY (BookID)
);
/*
 CREATE TABLE word if not exists (
 EtymologicalRoot TEXT,
 Morphemes Text [],
 Themes Text [],
 PartOfSpeech TEXT,
 Plural Boolean,
 Gender Text,
 VerbTense Text MiriamWebsterDefintion TEXT,
 EtymonlineDefinition TEXT,
 OnlineEtymologyText INT,
 FrenchEtymologyText INT,
 The idea is this: Emmanuel Levinas is deliberately making a joke in his usage of terms. We want to document the words and their collections as clearly as possible and present a user interface that allows the user to navigate these connections.
 The linguistic connections are various:
 (1) etymological : "institution" "destitution" "institution" "hypostasist" (ETYMOLOGICAL ROOT: STA, to stand)
 (2) thematic: "maternity" "fraternity" "paternity". "father", "midwife" "orphan"
 (3) Grammatical Form (verb, noun, adjective, adverb)
 (4) Verb tense and voice and mood
 (5) Noun declension (if this is applicable in french)
 6 ) Gender
 (7) Plural
 */
/*CREATE TABLE tblWordType
 (
 WordTypeID 	INT		AUTO_INCREMENT ,
 PartOfSpeech	VARCHAR (32) 	UNIQUE NOT NULL,
 PRIMARY KEY (WordTypeID)	
 );
 
 
 CREATE TABLE tblRadical
 (
 RadicalID       INT		AUTO_INCREMENT ,
 RadicalWord	VARCHAR (32)	UNIQUE NOT NULL,
 Language	TEXT	,
 Meaning		TEXT,
 PRIMARY KEY (RadicalID)	
 );
 
 CREATE TABLE tblSemanticCategory
 (
 SemanticID       INT		AUTO_INCREMENT ,
 SemanticCategory	VARCHAR (64)	UNIQUE NOT NULL,
 PRIMARY KEY (SemanticID)	
 );
 
 CREATE TABLE tblMoreAt
 (
 MoreAtID 	INT	AUTO_INCREMENT,
 RootWord	VARCHAR (16),
 EtymologyID	INT,	
 DomainID	INT,
 PRIMARY KEY (MoreAtID)
 );
 
 
 CREATE TABLE trelFrequency 
 (
 BookID INT,
 WordID INT,
 Occurences INT,
 PRIMARY KEY (WordID, BookID)
 );
 
 
 CREATE TABLE trelWordRadical
 (
 WordID 	INT,
 RadicalID INT,
 PRIMARY KEY (WordID, RadicalID)	
 );
 
 CREATE TABLE trelWordSemantic
 (
 WordID 	INT,
 SemanticID INT,
 PRIMARY KEY (WordID, SemanticID)	
 );
 
 
 
 CREATE TABLE trelRadicalSubradical
 (
 RadicalID INT,
 SubradicalID INT,
 PRIMARY KEY (RadicalID, SubradicalID)
 
 );
 
 CREATE TABLE trelSemanticSubsemantic
 (
 SemanticID 	INT,
 SubsemanticID INT,
 PRIMARY KEY (SemanticID, SubsemanticID)	
 );
 
 CREATE TABLE trelRadicalSemantic
 (
 RadicalID INT,
 SemanticID 	INT,
 PRIMARY KEY (RadicalID, SemanticID)	
 );
 
 
 
 CREATE TABLE tlkpBook 
 (
 BookID  INT AUTO_INCREMENT,
 Abrev TINYTEXT NOT NULL,
 FullTitle TEXT,
 Year INT,
 BibliographicalInfo TEXT,	
 TotalWords INT,
 PRIMARY KEY (BookID)
 );
 
 
 CREATE TABLE tlkpLanguage
 (
 LanguageID CHAR (3),
 LanguageValue VARCHAR (16) NOT NULL UNIQUE,
 PRIMARY KEY (LanguageID)
 
 );
 
 CREATE TABLE tlkpEtymology
 (
 EtymologyID INT    AUTO_INCREMENT,
 Value BLOB NOT NULL,
 DictionaryID CHAR(4),
 PRIMARY KEY (EtymologyID)	
 );
 
 CREATE TABLE tlkpDictionary (
 DictionaryID	CHAR (4),
 DictionaryName	VARCHAR (32),
 DictionaryDomain	VARCHAR (32),
 DictionarySearchAddress	VARCHAR (16),
 PRIMARY KEY (DictionaryID)
 );
 
 
 LOAD DATA LOCAL INFILE "/home/roadrunner/public_html/RadicalEmpiricism/DBScripts/BookDataFile.txt" INTO TABLE tlkpBook;
 LOAD DATA LOCAL INFILE "/home/roadrunner/public_html/RadicalEmpiricism/DBScripts/DictionaryDataFile.txt" INTO TABLE tlkpDictionaryg;
 
 
 */