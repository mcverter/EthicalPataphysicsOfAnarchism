#!C:\bin\perl

use strict;
use Carp;
use LWP;
use LWP::RobotUA;
use FileHandle;
#use lib  "C:/Documents and Settings/tech/My Documents/AnarchismOfTheOtherMan/EtymologicalEmpiricism";
use DBI;
######################
#
#
#  main 
#
#
######################


my $DEBUG = 1;

#DATABASE

my $dbh;
my $sth;
my $query;

$dbh = DBI->connect ('DBI:mysql:dbRadical_Empiricism',undef ,undef ,{RaiseError =>1});

$sth = $dbh->prepare("SHOW TABLES");
$sth->execute();
while (my @row = $sth->fetchrow_array())
{
    print join ("\t", @row), "\n";

}
$sth->finish();

# IN FILE
my $filename = "FrOutput1.txt";
my $IN = new FileHandle;
$IN->open ($filename) or die "Could not open INFILE $filename";

while (my $line = <$IN>)
{
    my @fields = split /\t/, $line;
    my $frenchWord = $fields[1];
    my $englishCognate = $fields[2];
    my $etymology = $fields[3];
    if ($etymology)
	{
if ($DEBUG)
{
	    print "\nLine 113\nETYMOLOGY  IS $etymology\n";
}    
	    
            my @roots = split /<\/i>/, $etymology;
	    my $baseRoot = $roots[0];
#            $baseRoot =~ /.*?([A-Z].*?) <i>(.*)/;
#	    my $language = $1;
#	    my $meaning = $2;
#            $baseRoot = new Radical ($language, $meaning);

if ($DEBUG)
{
	    print "\nLine 120\nROOT is $baseRoot\n";
}
	    my $rootNum = @roots;
	    $etymology = new Etymology ($frenchWord, $englishCognate, $etymology, $baseRoot);

	    for (my $j = 0;  $j < @roots ; $j++)
	    {
		if (($roots[$j+1]) &&
		    ($roots[$j+1] !~ /\b[A-Z]/))
		{
		    $roots[$j] .= $roots [$j+1];
		    splice @roots, $j+1, 1;
		    $j--;
		}
	    }

	    if ($roots[@roots-1] =~  /more/)
	    {
		my $moreLine = $roots[@roots-1]; 
		$moreLine =~ /(.*)(more.*)/;
		$roots[@roots-2] .= $1;
		my $moreAt = $2;
if ($DEBUG)
{
		print "\nLine 144\nMore at is $moreAt\n";
}

		$moreAt = new MoreAt($moreAt);
if ($DEBUG)
{
		print "\nLine150\nMOREAT is LINE ", $moreAt->{_moreLine}, " and HREF ", $moreAt->{_href}, "\n";
}
		pop @roots;

		
		$etymology->addMoreAt($moreAt);

	    }

	    for (my $i = 0; $i < @roots; $i++)
		{
if ($DEBUG)
{
		    print "Line 163\nRoot NUMBER $i is $roots[$i]. ";
}
		    my $radical = $roots[$i];
###########
#
# DEBUG CODE
#
###########
		    if ($radical =~ /abonder/)
		    {
			1;
		    }

###########
#
# DEBUG CODE
#
###########
		    $radical =~ /.*?([A-Z].*?) <i>(.*)/;
		    my $language = $1;
		    my $meaning = $2;
		    my $root = new Radical ($language, $meaning);
if ($DEBUG)
{
		    print "\nLine 187\nRoot RADICAL has LANGUAGE " , $root->{_sourceLanguage}, " and MEANING ", $root->{_meaning}, "\n";
}

		    $etymology->addRadical($root);
		}

	    $etymology->print();
	    print "\n";
	}
}

1;


########################################
#
#
# package Etymology
#
#
########################################
package Etymology;

sub new {
    my $class = shift;
    my $self = {
	_frenchWord => shift,
	_englishCognate => shift,
	_etymology => shift,
	_baseRoot => shift,
	_moreAt => undef,
	_radicals => [],
    };
    bless $self, $class;
    return $self;
}

sub print {
    my $self = shift;
    my $frenchWord = $self-> {_frenchWord};
    my $englishCognate = $self->{_englishCognate};
    my $etymology = $self-> {_etymology};
    my $baseRoot = $self->{_baseRoot};
    my $moreAt = $self->{_moreAt};
    my @radicals = @{ $self->{_radicals} };

    $baseRoot =~ /.*?([A-Z].*?) <i>(.*)/;
    my $language = $1;
    my $meaning = $2;


    my $baseID = dbInsertEtymBase('NULL', $baseRoot, $language, $meaning, $moreAt);
    


    print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n";

    print "\n\nETYMOLOGY is $etymology.  \n  BASEROOT is $baseRoot.\n  MOREAT is $moreAt\n" ; 

    my $i = 1;
    foreach my $rad (@radicals)
    {
	
	my $language = $$rad{_sourceLanguage};
	my $meaning = $$rad{_meaning};
	print "    $i.  ";
	$$rad->print();
	$i++;
	dbInsertRadical ('NULL', $meaning, $language, $meaning);	
	dbInsertBaseRadicalJunction('NULL', 'LAST_INSERT_ID()', $baseID);
	
	
    }
    print "============================================================\n";
    print "\n\n";

    dbInsertWord ('NULL', $frenchWord, $englishCognate, $etymology, $baseID, $baseID, 0);
 
############
#
# Database code:  add unique to database.  add link to database
#
############

 my ($wordID, $frenchWord , $englishCognate , $etymology,  $frenchRoot, $etymBaseID, $wordTypeID);
my ($wordTypeID, $partOfSpeech, $gender, $declension,  $tense, $person);
my ($etymBaseID, $baseWord, $language, $meaning, $moreAt);          
my ($radicalID, $radicalWord, $language, $meaning);
my ($junctionID, $radicalID, $baseID);

}

sub addRadical {
    my $self = shift;
    my $newRadical = shift;
    my $radicals = $self->{_radicals} ;
    my @radicals = @$radicals;
    push (@$radicals, \$newRadical);
    
}

sub addMoreAt {
    my $self = shift;
    my $moreAt = shift;
    $self->{_etymology} = $moreAt;

}

sub dbInsertWord
{
    my ($wordID, $frenchWord , $englishCognate , 
	$etymology,  $frenchRoot, $etymBaseID, $wordTypeID) = @_;

    $query = "INSERT into tblWord (                                   \
				     WordID,                      \
				     FrenchWord ,                 \
				     EnglishCognate ,             \
				     Etymology,                   \
				     FrenchRoot,                  \
				     EtymBaseID,                  \
				     WordTypeID                   \
                               )                                  \
	      VALUES (($wordID, $frenchWord , $englishCognate ,   \ 
                     $etymology,  $frenchRoot, $etymBaseID, $wordTypeID))";

    $sth = $dbh->prepare($query);
}

sub dbInsertWordType
{
    my ($wordTypeID, $partOfSpeech, $gender, $declension,  
	$tense, $person) = @_;
    $query = "INSERT into tblWordType (                         \
					 WordTypeID,        \
					 PartOfSpeech,      \
					 Gender,	    \
					 Declension,        \
					 Tense,             \
					 Person,            \
					 )                  \
	      VALUES ($wordTypeID, $partOfSpeech, $gender,  \
                      $declension,  $tense, $person)";
    $sth = $dbh->prepare($query);
    $sth->execute()
}

sub dbInsertEtymBase 
{
    my ($etymBaseID, $baseWord, $language, $meaning, $moreAt) = @_;          
    $query = "INSERT into tblEtymBase (                         \
	                 	       EtymBaseID,          \
	                               BaseWord,            \
	                               Language,            \
	                               Meaning,             \
	                               MoreAt,             \
                        	   )                        \   
	      	      VALUES (($etymBaseID, $baseWord,      \
                               $language, $meaning, $moreAt))";
    $sth = $dbh->prepare($query);
    $sth->execute();
    $query = "SELECT LAST_INSERT_ID()";
    $sth = $dbh-> prepare ($query)

}

sub dbInsertRadical 
{
    my ($radicalID, $radicalWord, $language, $meaning) = @_;
    $query = "INSERT into tblRadical (                         \
	                          RadicalID,               \	
	                          RadicalWord,             \
	                          Language,                \
           	                  Meaning,                 \
	                          )                        \
	      VALUES($radicalID, $radicalWord, $language, $meaning)";
    $sth= $dbh->prepare($query);
    $sth->execute();
}

sub dbInsertBaseRadicalJunction
{
    my ($junctionID, $radicalID, $baseID) = @_;
    $query = "INSERT into tblBaseRadicalJunction (             \
	                          JunctionID,              \
	                          RadicalID,               \
	                          BaseID,                  \
	                          )                        \
	      VALUES(($junctionID, $radicalID, $baseID))";
    $sth = $dbh->prepare($query);
    $sth->execute()
}

########################################
#
#
# package MoreAt
#
#
########################################
package MoreAt;

sub new {
    my $class = shift;
    my $moreLine = shift;
    my $hrefIndex = index $moreLine, "href";
    $hrefIndex +=6;

    $moreLine = substr ($moreLine, 0, $hrefIndex) .  "http://www.m-w.com" . substr ($moreLine,  $hrefIndex) ;

    $moreLine =~ /href="(.*?)"/;
    my $href = $1;

    my $self;
    my $self = {
	_moreLine => $moreLine,
	_href => $href,
    };
    bless $self, $class;
    return $self;
}

1;

 ########################################
 #
 #
 # package Radical
 #
 #
 ########################################

package Radical;

sub new {
    my $class = shift;
    my $self = {
	_sourceLanguage => shift,
	_meaning => shift,
    };
    bless $self, $class;
    return $self;
}

sub print {
    my $self = shift;
    my $lang = $self-> {_sourceLanguage};
    my $mean = $self->{_meaning};
    print " RADICAL has LANGUAGE $lang and MEANING $mean\n"; 
}
 1;

#######################################
#
#
# package moreAt
#
#
########################################

package moreAt;

sub new {
    my $self = {
	_moreWord => undef,
	_definition => undef,
    };
    bless $self, 'MoreAt';
    return $self;
}

1;