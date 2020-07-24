#################################
#
#   METHOD: findEnglishCognate
#   PRECONDITIONS:
#   POSTCONDITIONS: 
#   SUMMARY: 
#
#   VARIABLES:
# 
##################################


sub findEnglishCognate
{
    my $french = shift;

    my $content = getWebsiteContent ("$TransDic$french");
    
    my @content;
    @content = split /\n/, $content;
    my $line = shift(@content);

    my $cognate;
    my $cognateTemp;
    my $cognateScore = 0;
    my $cognateScoreTemp;

    while ($#content)
    {
	$line = shift(@content);
	if ($line =~ /We found no English translations for/)
	{
	    return "NO_TRANSLATION";
	}
	if ($line =~ /<td class=\'ToW\'>(.*?)<\/td>/)
	    {
		$cognateTemp = $1; 
		if ($cognateTemp =~ /(.*?) \(<i/)
		{
		    $cognateTemp = $1;
		}
		$cognateScoreTemp = calculateCognate ($french, $cognateTemp);
		if ($cognateScoreTemp > $cognateScore)
		{
		    $cognateScore = $cognateScoreTemp;
		    $cognate = $cognateTemp;
		}
		$cognateScoreTemp = $cognateTemp = 0;
	    }
	
    }
    if  ($cognateScore < 2)
    {
	return "NO_COGNATE";
    }
    else 
    {
	return $cognate;
    }
}

#################################
#
#   METHOD: normalizeFrench
#   PRECONDITIONS:
#   POSTCONDITIONS: 
#   SUMMARY: 
#
#   VARIABLES:
# 
##################################


sub normalizeFrench 
{
    my $french = shift;
    $french =~ s/ê/e/g;
    $french =~ s/ë/e/g;
    $french =~ s/é/e/g;
    $french =~ s/è/e/g;
    $french =~ s/à/a/g;
    $french =~ s/ù/u/g;
    $french =~ s/ç/c/g;

    return $french;
}

#################################
#
#   METHOD: calculateCognate
#   PRECONDITIONS:
#   POSTCONDITIONS: 
#   SUMMARY: 
#
#   VARIABLES:
# 
##################################


sub calculateCognate 
{
    my $french = shift;
    my $cognate = shift;
    $french = normalizeFrench ($french);
    
    my $score;
    my $stem;
    my $continue = 1;
    my $length = length $french;

    for ($score = 1; (($score <= $length) && ($continue)); $score++)
    {
	$continue = 0;
	$stem = substr $french, 0, $score;
	if ($cognate =~ /^$stem/)
	{
	    $continue = 1;
	}
    }
    

    $score -= 2;

#   print "French is $french, English is $cognate, Score is $score\n";
    return $score;
}
