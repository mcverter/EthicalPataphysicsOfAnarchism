use strict;
use EtymologyDatabaseHandle;

my $eDBh = new EtymologyDatabaseHandle();
cleanEtymologies();

sub cleanWords
{
    my $sth = $eDBh->getAllWords();
    my $rowArray;
    while (($rowArray = $eDBh->getNextRow($sth)) 
	   && (@$rowArray))
    {
	my $wordID  = $rowArray->[0];
	my $word  = $rowArray->[1];
	my $newWord = replaceWithAccents($word);
	if ($word ne $newWord)
	{
	    $eDBh->setWordValue($wordID, $newWord);
	    print "changing word $word to $newWord.  WORDID: $wordID\n";
	}
    }
}

sub cleanEtymologies
{
    my $sth = $eDBh->getAllEtymologies();
    my $rowArray;
    while (($rowArray = $eDBh->getNextRow($sth)) 
	   && (@$rowArray))
    {
	my $etymID  = $rowArray->[0];
	my $etymology  = $rowArray->[1];
	my $newEtym = replaceWithAccents($etymology);
	if ($etymology ne $newEtym)
	{
	    $eDBh->setEtymologyValue($etymID, $newEtym);
	    print "changing word $etymology to $newEtym.  WORDID: $etymID\n";
	}
    }

}


sub replaceWithAccents
{
   my $word = shift;
   my $newWord = $word;
  $newWord =~ s/é/�/g;
  $newWord =~ s/è/�/g;
  $newWord =~ s/ç/�/g;
  $newWord =~ s/î/�/g;
  $newWord =~ s/û/�/g;
  $newWord =~ s/â/�/g;
  $newWord =~ s/ô/�/g;
  $newWord =~ s/ï/�/g;
  $newWord =~ s/à/�/g;
  $newWord =~ s/Ç/�/g;
  $newWord =~ s/ë/�/g;
  $newWord =~ s/ä/�/g;
  $newWord =~ s/Û/�/g;
  return $newWord;
}
sub replaceWithAccentsOLD
{
   my $word = shift;

     if ($word =~ /�/)
	 {
	    if ($word =~ /�/)
	    {
          my $newWord = $word;
          $newWord =~ s/é/�/;
      }
      elsif ($word =~ /�/)
	    {
          my $newWord = $word;
          $newWord =~ s/ê/�/;
         # print "oldWOrd:  $word.  New WOrd: $newWord\n";
      }
      elsif ($word =~ /�/)
	    {
          my $newWord = $word;
          $newWord =~ s/è/�/;
          #print "oldWOrd:  $word.  New WOrd: $newWord\n";
      }
       elsif ($word =~ /�/)
	    {
          my $newWord = $word;
          $newWord =~ s/ç/�/;
          #print "oldWOrd:  $word.  New WOrd: $newWord\n";
      }
      elsif ($word =~ /�/)
	    {
          my $newWord = $word;
          $newWord =~ s/î/�/;
          #print "oldWOrd:  $word.  New WOrd: $newWord\n";
      }
      elsif ($word =~ /�/)
	    {
          my $newWord = $word;
          $newWord =~ s/û/�/;
         #print "oldWOrd:  $word.  New WOrd: $newWord\n";
      }
      elsif ($word =~ /�/)
	    {
          my $newWord = $word;
          $newWord =~ s/â/�/;
    #     print "oldWOrd:  $word.  New WOrd: $newWord\n";
      }
      elsif ($word =~ /�/)
	    {
          my $newWord = $word;
          $newWord =~ s/ô/�/;
         #print "oldWOrd:  $word.  New WOrd: $newWord\n";
      }
      elsif ($word =~ /�/)
	    {
          my $newWord = $word;
          $newWord =~ s/ï/�/;
         #print "oldWOrd:  $word.  New WOrd: $newWord\n";
      }
      elsif ($word =~ /�/)
	    {
          my $newWord = $word;
          $newWord =~ s/à/�/;
         #print "oldWOrd:  $word.  New WOrd: $newWord\n";
      }
      elsif ($word =~ /�/)
	    {
          my $newWord = $word;
          $newWord =~ s/Ç/�/;
         #print "oldWOrd:  $word.  New WOrd: $newWord\n";
      }
      elsif ($word =~ /�/)
	    {
          my $newWord = $word;
          $newWord =~ s/ë/�/;
         #print "oldWOrd:  $word.  New WOrd: $newWord\n";
      }

      elsif ($word =~ /�/)
	    {
          my $newWord = $word;
          $newWord =~ s/ä/�/;
         #print "oldWOrd:  $word.  New WOrd: $newWord\n";
      }
     elsif ($word =~ /�/)
	    {
          my $newWord = $word;
          $newWord =~ s/Û/�/;
        # print "oldWOrd:  $word.  New WOrd: $newWord\n";
      }

      else
      {
         print $word, "\n";
      }
	}
}
