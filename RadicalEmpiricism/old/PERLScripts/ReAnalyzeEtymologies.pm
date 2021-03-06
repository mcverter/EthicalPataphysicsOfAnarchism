use EtymologyDBManipulations;
use EtymologyDatabaseHandle;
use strict;
use Carp;

my $eDBh = new EtymologyDatabaseHandle();



my $sth = $eDBh->getAllWords();
my $rowArray;
while (($rowArray = $eDBh->getNextRow($sth)) 
	   && (@$rowArray))
    {
	my $wordID = $rowArray->[0];
	my $word  = $rowArray->[1];


	my $mwe = getMWEtymology($wordID);
	my $oe = getOEEtymology($wordID);
	my $atlife = getATLIFEtymology($wordID);

	if ($mwe || $oe || $atlife)
	{
	    print "$word $mwe $oe $atlife\n";
 	}


	if ($oe)
	{
#	    analyzeOEtymology ($wordID, $oe);
	}
	if ($mwe)
	{
	    analyzeMWEtymology ($wordID, $mwe);
	}
	if ($atlife)
	{
#	    analyzeATLIFEtymology ($wordID, $atlife);
	}
    }


sub insertNewRadical
{
    my $wordID = shift;
    my $foreignWord = shift;
    my $language = shift;
    my $radicalID = $eDBh->addRadical($foreignWord);
    $eDBh->insertValuesIntoTable("trelWordRadical", "$wordID, $radicalID");
    print "inserting $language $foreignWord \n"

}
sub getFullEtymology
{
    my $ID = shift;
    my $sth = $eDBh->selectItemsFromTable("tlkpEtymology", "value", "EtymologyID = $ID");
    $rowArray = $eDBh->getNextRow($sth);
    return $rowArray->[0];
}

sub parseOE 
{
    my $etymology = shift;
    my $wordID = shift;

    my @words = split /\s/, $etymology;
    
    for (my $i = 0; $i < $#words; $i++)
    {
	
	if ($words[$i] =~ /<span/)
	{
	    my $foreignWord = $words[$i+1];
	    $foreignWord =~ />(.*)<\/span>/;
	    $foreignWord = $1;
	    $foreignWord =~ s/,//;
	    my $language;

	    if ($words[$i-3] eq "from")
            {
		$language = $words[$i-2] . " " . $words[$i-1];

            }

	    if ($words[$i-2] eq "from")
            {
		$language = $words[$i-1];
		insertNewRadical($wordID, $foreignWord, $language);
           }
	    if ($words[$i-1] eq "from")
            {
		insertNewRadical($wordID, $foreignWord);
            }

	}
    }
    1;
}

sub parseMW
{

    my $etymology = shift;
    my $wordID = shift;

    my @words = split /\s/, $etymology;
    
    for (my $i = 0; $i < $#words; $i++)
    {
	
	if ($words[$i] =~ /<font/)
	{
	    my $foreignWord = $words[$i+1];
	    $foreignWord =~ /([A-Z]+)/;
	    my $language = "MORE_AT";
	    print $1;
	}
	elsif ($words[$i] =~ /<i>/)
	{

	    my $foreignWord = $words[$i];
	    $foreignWord =~ s/<i>//;
	    $foreignWord =~ s/<\/i>//;
	    $foreignWord =~ s/,//;

	    my $language;
	    if ($words[$i-2] && 
		($words[$i-2] =~ /^[A-Z]/))
	    {
		$language = $words[$i-2] . " " .  $words[$i-1];
		print "MW ETYMOLOGY:  " , $foreignWord, " $language\n";#insertNewRadical($wordID, $foreignWord, $language);

		if (($words[$i+1] !~ /<\/i>/) 
		    && ($words[$i+1] =~ /\w/))
		{
		    print "MW ETYMOLOGY:  " , $words[$i+1], " $language\n";#insertNewRadical($wordID, $words[$i+1], $language);
		}

	    }
	    elsif ($words[$i-1] =~ /^[A-Z]/)
	    {
		$language =  $words[$i-1];
		print "MW ETYMOLOGY:  " , $foreignWord, " $language\n";#insertNewRadical($wordID, $foreignWord, $language);

		if (($words[$i+1] !~ /<\/i>/)
		    && ($words[$i+1] =~ /\w/))
		{
		    print "MW ETYMOLOGY:  " , $words[$i+1], " $language\n";#insertNewRadical($wordID, $words[$i+1] , $language);
		}
	    }
	    elsif (($words[$i-1] =~ /from/) ||
		    ($words[$i-1] =~ /of/) )
	    {
		print "MW ETYMOLOGY:  " , $foreignWord, " $language\n";#insertNewRadical($wordID, $foreignWord, $language);

		if (($words[$i+1] !~ /<\/i>/)
		    && ($words[$i+1] =~ /\w/))
		{
		    print "MW ETYMOLOGY:  " , $words[$i+1], " $language\n";#insertNewRadical($wordID, $words[$i+1], $language);
		}
	    }
	    elsif (($words[$i-1] =~ /\+/))
	    {
		print "MW ETYMOLOGY:  " , $foreignWord, " $language\n";#insertNewRadical($wordID, $foreignWord, $language);
		if (($words[$i+1] !~ /<\/i>/)
		    && ($words[$i+1] =~ /\w/))
		{
		    print "MW ETYMOLOGY:  " , $words[$i+1], " $language\n";#insertNewRadical($wordID, $words[$i+1], $language);
		}
		
	    }
	}
	#print $etymology[$i], "\n";
    }
    1;
}
 
sub  analyzeOEtymology 
    {
	my $wordID = shift;
	my $etymologyID = shift;
	my $etymology = getFullEtymology($etymologyID);
	parseOE ($etymology, $wordID);
	1;
    }

sub  analyzeMWEtymology 
    {
	my $wordID = shift;
	my $etymologyID = shift;
	my $etymology = getFullEtymology($etymologyID);
	parseMW($etymology, $wordID);
	1;

    }
sub  analyzeATLIFEtymology 
    {
	my $wordID = shift;
	my $etymologyID = shift;
	my $etymology = getFullEtymology($etymologyID);
	1;
    }

sub getMWEtymology
{
    my $wordID = shift;
    my $sth = $eDBh->selectItemsFromTable("tblWord", "MWEtymologyID", "WordID = $wordID");
    $rowArray = $eDBh->getNextRow($sth);
    return $rowArray->[0];
}

sub getOEEtymology
{
    my $wordID = shift;
    my $sth = $eDBh->selectItemsFromTable("tblWord", "OnlineEtymologyID", "WordID = $wordID");
    $rowArray = $eDBh->getNextRow($sth);
    return $rowArray->[0];
}

sub getATLIFEtymology
{
    my $wordID = shift;
    my $sth = $eDBh->selectItemsFromTable("tblWord", "FrenchEtymologyID", "WordID = $wordID");
    $rowArray = $eDBh->getNextRow($sth);
    return $rowArray->[0];
}
