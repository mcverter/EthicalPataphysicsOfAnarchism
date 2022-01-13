#!C:\bin\perl

use strict;
use Carp;
use LWP;
use LWP::RobotUA;
use FileHandle;

###########################
#
# Files
#
###########################
my $OTB_EngWords = "OTB_WordIndex.txt";
my $hanselFrWords = "remainingWords";
my $frenchEtyOutput = "frenchEtymologyOutput.txt";

########################
#
# ELECTRONIC RESOURCES
#
########################

my $EngDic = "http://www.m-w.com/dictionary/";
my $EngEtymDic = "http://www.etymonline.com/index.php?searchmode=none&search=";
my $TransDic = "http://www.wordreference.com/fren/";


sub findEngEtym 
{
    my $english = shift;
    my $content = getWebsiteContent ("$EngDic$english");

    my @content;
    @content = split /\n/, $content;
    my $line = shift(@content);
    my $etymology;

    while ($#content)
    {
	if ($line =~ /Etymology/)
	{
	    $etymology = $line;
	    chomp $etymology;
#	    print "Etymology is $etymology\n";
	    last;
	}
	$line = shift(@content);
    }
    return $etymology;

}
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
#  Main
#
################################

my $IN = new FileHandle;
#my $OUT = new FileHandle;
$IN->open ($hanselFrWords) or die "Could not open INFILE $hanselFrWords";
#$OUT->open( "$frenchEtyOutput", ">>") or die "Could not open OUTFILE $frenchEtyOutput";
#$OUT->printflush();

my $line;
my @terms;

my $continueWord = 'reposant';
my $robotCounter;
my $continueAnalysis = 0;

while ($line = <$IN>)
{
    my $word = $line;
    chop $word;

    $word =~ s/\s//g;
    if ($word eq $continueWord)
    {
	$continueAnalysis = 1;
    }
    $continueAnalysis = 1;
    if ($word && $continueAnalysis)
	{
#	    print $word, "\n";
	    my $term = new Term;
	    $term->setFrenchTerm ($word);
	    my $englishCognate = findEnglishCognate($word);
#	    print "COGNATE is $englishCognate \n";
	    $term->setEnglishTerm ($englishCognate);
	    if (($englishCognate ne "NO_COGNATE") &&
		($englishCognate ne "NO_TRANSLATION"))
	    {
		my $englishEtym = findEngEtym($englishCognate);
		$term ->setEnglishEtymology ($englishEtym);
		$term->print();
	    }
	    else 
	    {
		$term -> print ();
	    }
	}
}


#foreach my $listTerm (@terms)
#{
#    $listTerm->print();
#}


#########################################################
#
#  LWP FUNCTION
#
#
#########################################################

sub getWebsiteContent
{
    my $website = shift;
    
    my $headers = new HTTP::Headers(Accept => 'text/plain');
    my $req = new HTTP::Request("GET", $website, $headers);
    
    $robotCounter++;
    my $ua;
    my $robot_ua;
    my $resp;
    
    if ($robotCounter % 20 != 0)
    {
	$ua = new LWP::UserAgent;
	$resp = $ua->request($req);
    }
    else 
    {
	$robot_ua =  LWP::RobotUA->new 
	    ('mitchbot', 'longditude@yahoo.com');
	$robot_ua->delay (7 / 60);
	if ($robotCounter % 11)
	{
	    $robot_ua->delay (60 / 60);
	}
	if ($robotCounter % 13)
	{
	       $robot_ua->delay (120 / 60);
	}
	$resp = $robot_ua->request($req);
    }

    
    my $content;

    if (! $resp->is_success)
    {
	my $message = $resp->message;
	
	print "Response failed: $message.  Robot Counter is $robotCounter." ;
	sleep 60;
	my $newContent = getWebsiteContent ($website);
	return $newContent;
    }
    else 
    {
	$content = $resp->as_string;
	return $content;
    }
}

########################################
#
#
# package Term
#
#
########################################

package Term;


sub new {
    my $self = {
	_frenchTerm => undef,
	_englishTerm => undef,
	_englishDef => undef,
	_frenchDef => undef,
	_englishEty => undef,
	_frenchDef => undef,
    };
    bless $self, 'Term';
    return $self;
}

sub print {
    my $self = shift;
#    my $OUT = shift;


    my $english = $self->{_englishTerm};
#    if (($english eq "NO_COGNATE") ||
#	($english eq "NO_TRANSLATION"))
#    {
#	return;
#    }
    my $french =  $self->{_frenchTerm};
    my $engEtym = $self->{_englishEty};
    print  "$french\t$english\t$engEtym\n";
#    $OUT->write( "$french\t$english\t$engEtym\n");
#    $OUT->flush();

}

sub setEnglishEtymology {
    my $self = shift;
    $self->{_englishEty} = shift;
}

sub setFrenchTerm {
    my $self = shift;
    $self->{_frenchTerm} = shift;
}

sub setEnglishTerm {
    my $self = shift;
    $self->{_englishTerm} = shift;
}

1;

