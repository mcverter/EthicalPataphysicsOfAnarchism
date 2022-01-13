#!C:\bin\perl

use strict;
use Carp;
use LWP;

open (IN, "OTB_WordIndex.txt") or die "Could not open Word Index";
open (OUT, ">EtymologicalEmpiricism.txt") or die "Could not open OUT file";

my $line;



while ($line = <IN>)
{
    $line =~ /(.*?)\s*(\d.+)/;
    my $word = $1;
    my $pageNums = $2;

    #Create NEW Term
    $word =~ s/\*//g;
    $word =~ s/\W/\+/g;
    my $term = new Term;
    $term->frenchTerm($word);

    my $lookupEnglishEtymology = "$word#http://www.etymonline.com/index.php?search=$lookupWord&searchmode=none";
    my $lookupEnglishDictionary="http://www.m-w.com/dictionary/$lookupWord";

#########################################################
#
#  LWP FUNCTION
#
#
#########################################################
    my $headers = new HTTP::Headers(Accept => 'text/plain');
    my $req = new HTTP::Request("GET", $lookupEnglishDictionary, $headers);
    my $ua = new LWP::UserAgent;

    my $resp = $ua->request($req);
    my $content;
    my $etymology;

    if (! $resp->is_success)
    {
	print $resp->message;
    }
    else 
    {
	$content = $resp->as_string;

	{
	    $line = shift(@content);
	}
	if ($line =~ /Etymology/)
	{
	    $etymology = $line;
	    chomp $etymology;
	    print "Etymology is $etymology\n";

	}
    }

###############################################
#
#
#  LWP FUNCTION
#
#############################################





#    print OUT "$word\t$lookupEnglishEtymology\t$lookupEnglishDictionary\t$pageNums\n";

}


package Term;
#CONSTRUCTION

sub new {
    my $self = {
	_frenchTerm => undef,
	_englishTerm => undef,
	_englishDef => undef,
	_frenchDef => undef,
	_englishEty => undef,
	_frenchDef =>
    };
    bless $self 'WordEntry';
    return $self;
}

1;

package FileGrabber;
