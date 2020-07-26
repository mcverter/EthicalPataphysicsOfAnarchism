#!/usr/bin/perl

open DEBUG_LOG, ">>c:\\EtymologicalEmpiricism\\PERLScripts\\log.txt" or die "could not open debug log";


########################################
#
#
#
#   Package EtymologyDatabaseHandle
#
#
#
#######################################

package EtymologyDatabaseHandle ;

use strict;
use DatabaseHandle;

BEGIN {
    use Exporter   ();
    use vars       qw(@ISA @EXPORT @EXPORT_OK %EXPORT_TAGS);
    
    @ISA         = qw(Exporter DatabaseHandle);
    @EXPORT      = qw(&dbInsertWord);
}
use vars      @EXPORT_OK;



####################################
#
#  METHOD: new  
#  PRECONDITIONS: 
#  POSTCONDITIONS:  
#  SUMMARY:  creates a new object that passes etymology-specific
#              directives to an etymological dictionary
#  VARIABLES
#
###################################
sub new
{
#DATABASE

    my $class = shift;
    my $self = $class->SUPER::new
	('DBI:mysql:roadrunner_re', 'roadrunner' ,'eldritch' );
    bless ($self, $class);
}

####################################
#
#  METHOD:  updateOnlineEtymology
#  PRECONDITIONS: 
#  POSTCONDITIONS:
#
#  VARIABLES
#
###################################

####################################
#
#  METHOD:  updateMWEtymology
#  PRECONDITIONS: 
#  POSTCONDITIONS:
#
#  VARIABLES
#
###################################

sub updateMWEtymology
{
    my $self = shift;
    my $cognate = shift;
    my $MWtym = shift;

    $self->dbInsertLookupValue ( 'tlkpMWEtymology',  
			      'tblword',         
			      'Etymology',
			      'MWEtymology',		   
			      'EnglishCognate',
			      $cognate,
			      $MWtym);

}

sub updateOnlineEtymology
{
    my $self = shift;
    my $cognate = shift;
    my $oetym = shift;

    $self->dbInsertLookupValue ( 
				 'tlkpetymology',  
				 'tblword',         
				 'Etymology',
			      'OnlineEtymology',		   
			      'EnglishCognate',
			      $cognate,
			      $oetym);

}

####################################
#
#  METHOD:  getWordData
#  PRECONDITIONS: 
#  POSTCONDITIONS:
#
#  VARIABLES
#
###################################
sub getWordData
{
    print "\n###########################\nGETWORDDATA\n#################\n";
    my $self = shift;
    my $inputWord = shift;

    $self->selectItemsFromTable ("tblword", "FrenchWord, EnglishCognate,Etymology",
				 "FrenchWord = \'$inputWord\'");

}

sub selectFrequencyOfWord
{
    my $self = shift;
    my $wordID = shift;
    my $sth = $self->selectItemsFromTable ("tlkpbook", 
				 "Year, FullTitle",
				 "",
				  "Year");

    return $sth;
}
sub selectEtymRadicalsFromWord
{
    my $self = shift;
    my $wordID = shift;
    my $sth = $self->selectItemsFromTable ("tblradical, trelwordradical", 
				 "tblradical.RadicalID, RadicalWord, Language, Meaning",
				 "WordID = $wordID AND tblradical.RadicalID = trelwordradical.RadicalID");

    return $sth;
}

sub selectSemCategoriesFromWord
{
    my $self = shift;
    my $wordID = shift;
    my $sth = $self->selectItemsFromTable ("tblsemanticcategory, trelwordsemantic", 
				 "tblsemanticcategory.SemanticID, SemanticCategory",
				 "WordID = $wordID AND tblsemanticcategory.SemanticID = trelwordsemantic.SemanticID");

    return $sth;
}

sub selectWordsFromEtymRadical
{
    my $self = shift;
    my $radicalID = shift;
    my $sth = $self->selectItemsFromTable ("tblword, trelwordradical", 
				  "tblword.WordID, Word",
				 "RadicalID = $radicalID AND tblword.WordID = trelwordradical.WordID");

    return $sth;
}

sub selectWordsFromSemanticCategory
{
    my $self = shift;
    my $semanticID = shift;
    my $sth = $self->selectItemsFromTable ("tblword, trelwordsemantic", 
				  " tblword.WordID, Word ",
				 " SemanticID = $semanticID AND tblword.WordID = trelwordsemantic.WordID ");

    return $sth;
}

sub selectEtymRadicalInfo
{
    my $self = shift;
    my $radicalID = shift;
    print DEBUG_LOG "In select ETymRadInfo.  RadicalID = $radicalID";
    my $sth = $self->selectItemsFromTable ("tblradical", 
				 "RadicalWord, Language, Meaning",
				 "RadicalID = $radicalID");
  
    return $sth;
}
sub selectEtymologiesFromWord
{
    my $self = shift;
    my $wordID = shift;
    $self->selectItemsFromTable ("tlkpMWEtymology, tblword", "MWEtymologyValue",				 "WordID = $wordID");
    #   select  from  where tlkpMWEtymology.MWEtymologyCode = tblword.MWEtymologyCode AND WordID = $wordID;
}



sub getCategoryID 
{
    my $self = shift;
    my $category = shift;
    my $sth = $self->selectItemsFromTable (" tblsemanticcategory ",
				 " SemanticID " , 
				 " SemanticCategory = \'$category\' ");
    my $arrayRef = $self->getNext($sth);
    return $arrayRef->[0];
}


sub getAllSimilarWords 
{
    my $self = shift;
    my $similarityTest = shift;

    my $sth = $self->selectItemsFromTable (" tblword ", 
					   " WordID, Word " ,
					   " Word LIKE \'$similarityTest\' ");
    return $sth;


}


sub getAllMWEtymologies 
{
    my $self = shift;
    my $sth = $self->selectItemsFromTable ("tlkpMWEtymology", 
				 "MWEtymologyID, MWEtymologyValue");
    
}
####################################
#
#  METHOD:  getAllCognates
#  PRECONDITIONS: 
#  POSTCONDITIONS:
#
#  VARIABLES
#
#####################################

sub getAllCognates
{

    my $self = shift; 
    my $sth = $self->selectItemsFromTable ("tblword" , "WordID, EnglishCognate",
				 "EnglishCognate NOT IN (\'NO_COGNATE\', \'NO_TRANSLATION\')");

}


####################################
#
#  METHOD:  getAllWordsWithEtymologies
#  PRECONDITIONS: 
#  POSTCONDITIONS:
#
#  VARIABLES
#
#####################################

sub getAllWordsWithEtymologies
{
    print DEBUG_LOG "in get words with etymologies\n";
    my $self = shift; 
    
    my $sth = $self->selectItemsFromTable (" tblword, trelwordradical " , 
					   " Distinct tblword.WordID, Word ",
					   " tblword.WordID = trelwordradical.WordID ",
					   " Word" );
    
}


sub getAllWordInformation 
{
    print DEBUG_LOG "in get all word info\n";
    my $self = shift; 
    my $wordID = shift;
    print DEBUG_LOG "in gawi.  WordID = $wordID\n";
    my $sth = $self->selectItemsFromTable ("tblword" , "*",
					   "WordID = $wordID");
    my $arrayRef = $self->getNext($sth);
    return $arrayRef
}


sub getEtymology 
{
    my $self = shift; 
    my $etymID = shift;

    my $sth = $self->selectItemsFromTable ("tlkpetymology, tlkpdictionary" , 
					   "Value, DictionaryName, DictionaryDomain",
					   "EtymologyID = $etymID AND  tlkpetymology.DictionaryID = tlkpdictionary.DictionaryID");
    my $arrayRef = $self->getNext($sth);
}

###################################
#
#  METHOD:  getAllWords
#  PRECONDITIONS: 
#  POSTCONDITIONS:
#
#  VARIABLES
#
###################################

sub getOEID 
{
    my $self = shift;
    my $sth = $self->selectItemsFromTable ("tblword", "Word, WordID, MWEtymologyID", "WordID = 5");
    return $sth;
}
sub getAllWords
{
    print DEBUG_LOG "in get all words\n";
    my $self = shift;
    my $sth = $self->selectItemsFromTable ("tblword", "WordID, Word");
    return $sth;
}

###################################
#
#  METHOD:  getAllWords
#  PRECONDITIONS: 
#  POSTCONDITIONS:
#
#  VARIABLES
#
###################################


sub getAllEtymologies
{
    my $self = shift;
    my $sth = $self->selectItemsFromTable ("tlkpetymology", "etymologyID, Value");
    return $sth;
}


####################################
#
#  METHOD:  getAllTranslatedWords
#  PRECONDITIONS: 
#  POSTCONDITIONS:
#
#  VARIABLES
#
###################################
sub getAllTranslatedWords
{
    my $self = shift;

    my $sth = $self->selectItemsFromTable ("tblword" , "EnglishCognate",
				 "EnglishCognate NOT IN (\'NO_COGNATE\', \'NO_TRANSLATION\')");
}

####################################
#
#  METHOD:  getAllRoots
#  PRECONDITIONS: 
#  POSTCONDITIONS:
#
#  VARIABLES
#
###################################

sub getAllRoots
{

    my $self = shift;
    my $sth = $self->selectItemsFromTable ("tblradical", "RadicalID, RadicalWord",
					   "","RadicalWord");
    return $sth;
}


####################################
#
#  METHOD:  getAllRoots
#  PRECONDITIONS: 
#  POSTCONDITIONS:
#
#  VARIABLES
#
###################################

sub getAllSem
{

    my $self = shift;
    my $sth = $self->selectItemsFromTable ("tblsemanticcategory", 
					   "SemanticID, SemanticCategory",
					   "","SemanticCategory");
    return $sth;
}

####################################
#
#  METHOD:  dbGetIndexAndInsertWord
#  PRECONDITIONS: 
#  POSTCONDITIONS:
#
#  VARIABLES
#
###################################

sub dbInsertWord
{
    my ($self, $frenchWord) = @_;


    return $self->getIndexOrInsert ("tblword", "WordID",
				    "null, \'$frenchWord\', \'Fr\',null,null,null,null,null,null",
				    "Word = \'$frenchWord\'");
}


sub getEtymologyID
{
    my ($self, $etymology, $dictID) = @_;

    return $self->getIndexOrInsert ("tlkpetymology", "EtymologyID", 
			     "null, \'$etymology\', \'$dictID\'",
			     "Value = \'$etymology\'");

}

####################################
#
#  METHOD:  addXtoY
#  PRECONDITIONS: 
#  POSTCONDITIONS:
#
#  VARIABLES
#
###################################

sub addLanguageToWord 
{
    my $self = shift;
    my $wordID = shift;
    my $language = shift;
    
    $self->updateTableSetFieldValueWhere ("tblword", "Language", 
					  $language, " wordID = $wordID");
}

sub addCognateToWord
{
    my $self = shift;
    my $wordID = shift;
    my $cognate = shift;

    $self->updateTableSetFieldValueWhere ("tblword", "EnglishCognate",
					  $cognate, " wordID = $wordID");
}
sub setEtymologyValue
{
    my $self = shift;
    my $etymID = shift;
    my $value = shift;

    $self->updateTableSetFieldValueWhere ("tlkpetymology", "Value",
					  $value, " etymologyID = $etymID");

}

sub addMWEtymologyToWord
{
    my $self = shift;
    my $wordID = shift;
    my $etymologyID = shift;
    $self->updateTableSetFieldValueWhere ("tblword", "MWEtymologyID", 
					  $etymologyID, " wordID = $wordID");
 }

sub addTLFiEtymologyToWord
{
    my $self = shift;
    my $wordID = shift;
    my $etymologyID = shift;
    $self->updateTableSetFieldValueWhere ("tblword", "FrenchEtymologyID", 
					  $etymologyID, " wordID = $wordID");
 }

sub addOnlineEtymologyToWord
{
    my $self = shift;
    my $wordID = shift;
    my $etymologyID = shift;
    $self->updateTableSetFieldValueWhere ("tblword", "OnlineEtymologyID", 
					  $etymologyID, " wordID = $wordID");
 }
sub addWordTypeToWord
{
    my $self = shift;
    my $wordID = shift;
    my $wordType = shift;

    $self->updateTableSetFieldValueWhere ("tblword", "wordType", 
					  $wordType, " wordID = $wordID");
}
sub addFrequencyToWord
{
    my $self = shift;
    my $wordID = shift;
    my $frequency = shift;
    
    $self->updateTableSetFieldValueWhere ("tblword", "Frequency",
					  $frequency, " wordID = $wordID");
}
####################################
#
#  METHOD:  dbInsertWordType
#  PRECONDITIONS: 
#  POSTCONDITIONS:
#
#  VARIABLES
#
###################################

sub dbInsertWordType
{
    my ($self, $wordTypeID, $partOfSpeech, $gender, $declension,  
	$tense, $person) = @_;
    
    my $sth = insertValuesIntoTable("tblwordtype",  
				    "NULL, \'$partOfSpeech\', \'$gender\', \'$declension\', \'NULL\', \'NULL\'");
}

####################################
#
#  METHOD:  dbInsertRadical 
#  PRECONDITIONS: 
#  POSTCONDITIONS:
#
#  VARIABLES
#
###################################

sub dbInsertRadical 
{
    my ($self, $radicalID, $radicalWord, $language, $meaning) = @_;

    my $sth = insertValuesIntoTable("tblradical",  
				    "NULL, \'$radicalWord\', \'$language\', \'$meaning\'");
} 

####################################
#
#  METHOD:  getRootIndex
#  PRECONDITIONS: 
#  POSTCONDITIONS:
#
#  VARIABLES
#
###################################
sub addRadical
{
    my $self = shift;
    my $radical = shift;
    my $language = shift;
    my $radicalCode = $self->getIndexOrInsert ("tblradical", "RadicalID", 
						"null, \'$radical\', $language, null",
					       "RadicalWord = \'$radical\'");
    return $radicalCode;
}


sub addWordSemanticRelation
{
    my $self = shift;
    my $wordID = shift;
    my $semanticID = shift;
    
    $self->insertValuesIntoTable (" trelwordsemantic ", " $wordID, $semanticID ");
}


sub addRadicalEtymologyRelation 
{
    my $self = shift;
    my $radicalCode = shift;
    my $etymologyCode = shift;
    my $source = shift;

    $self->insertValuesIntoTable ("trelEtymologyRadical", 
				  "$radicalCode, $etymologyCode, \'$source\'");
}

sub addMoreAt
{
    my $self = shift;
    my $etymologyCode = shift;
    my $moreAtWord = shift;
    my $moreAtEtym = shift;


    my $moreCode = $self->getIndexOrInsert ("tblmoreat", "MoreAtID", 
						"RootWord", $moreAtWord, 
						"null, \'$moreAtWord\', \'moreAtEtym\', null");
#    $self->addRadicalToEtymology($radicalCode, $etymologyCode); 
}


####################################
#
#  METHOD:  getRootIndex
#  PRECONDITIONS: 
#  POSTCONDITIONS:
#
#  VARIABLES
#
###################################

sub getRootIndex
{
    my $self = shift;
    my $root = shift;
    my $allValues = "\\N, \'$root\', \\N, \\N";

    my $rootIndex = $self->getIndexOrInsert 
	("tblradical", "RadicalID", $allValues,
	 "RadicalID = \'$root\'"); 

    return $rootIndex;
       
}





END { }       # module clean-up code here (global destructor)


1;

#+-------------------------------+
# Tables_in_dbradicalempiricism #
#+-------------------------------+
# tblmoreat                     # 
# tblradical                    # 
# tblword                       # 
# tblwordtype                   # 
# tlkpbook                      # 
# tlkpdictionary                # 
# tlkpetymology                 # 
# tlkplanguage                  # 
# tlkpmwetymology               # 
# trelfrequency                 # 
# trelradicalsubradical         # 
# trelwordradical               # 
#+-------------------------------+

