#!C:\perl\bin\perl

use EtymologyDatabaseHandle;
use strict;

my $eDBh = new EtymologyDatabaseHandle();

sub addSemanticToSimilarWords
{
    my $category = shift;
    my $similarityTest = shift;


    my $categoryID = $eDBh->getCategoryID($category);
    if ($categoryID < 0)
    {
	die ("Could not find ID for Category $category in addSemanticToSimilarWords\n");
    }

    my $sth = $eDBh->getAllSimilarWords($similarityTest);
    my $rowArray;
    
    while (($rowArray = $eDBh->getNextRow($sth)) 
	   && (@$rowArray))
    {
	my $wordID = $rowArray->[0];
	my $word  = $rowArray->[1];
 	$eDBh->addWordSemanticRelation($wordID, $categoryID);	
    }



}


# main function
my $category = $ARGV[0];
my $similarityTest = $ARGV[1];   

addSemanticToSimilarWords($category, $similarityTest);