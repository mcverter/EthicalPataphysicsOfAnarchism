
CREATE DATABASE RadicalEmpiricism if not exists;

/*************************************************
*
*    DATA TABLES 
*
*************************************************/

CREATE TABLE word if not exists
(
	id INT AUTO_INCREMENT PRIMARY,
	Word TEXT UNIQUE NOT NULL,
	EnglishCognate TEXT,
	Language CHAR (2) ,
	
	EtymologicalRoot TEXT,
	Morphemes  Text[],

	Themes Text[],

	PartOfSpeech TEXT,
	Plural Boolean,
	Gender Text,
	VerbTense Text

	MiriamWebsterDefintion TEXT,
	EtymonlineDefinition TEXT,
 	OnlineEtymologyText	INT,
	FrenchEtymologyText	INT,

	);

/*he idea is this: Emmanuel Levinas is deliberately making a joke in his usage of terms. We want to document the words and their collections as clearly as possible and present a user interface that allows the user to navigate these connections.
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


*/
/*************************************************
*
*    RELATIONSHIP TABLES 
*
*************************************************/

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


/*************************************************
*
*    LOOKUP TABLES 
*
*************************************************/

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


