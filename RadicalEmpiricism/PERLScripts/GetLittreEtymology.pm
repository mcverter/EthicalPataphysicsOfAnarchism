use WebCrawl;
use strict;
use EtymologyDatabaseHandle;
use FileHandle;





sub getLittreEtymologyFromWeb
{
    my $word = shift;    
    my $outputLog = shift;

    my $output = WebCrawl::getWebsiteContent 
	("http://francois.gannaz.free.fr/Littre/xmlittre.php?requete=$word&submit=Rechercher");
    if ($output =~ /Erreur/) 
    {
	print $outputLog "yes error for word $word\n";
    }
    else 
    {

	$output =~ /<span class=\"nature\">(.*?)</;
	my $wordType = $1;
	$output =~ /etymologie(.*)/s;
	my $etymology = $1;
	$etymology =~ /nt\">(.*)<a/s;
	$etymology = $1;

	print $outputLog "No error for word $word.  WordType is $wordType.  Etymology is $etymology.\n";
	1;
    }
#    if ($output =~ /<dt class="highlight"><a href="\/index.php\?term=$word">$word.*?(<dd.*?dd>)/s)
1;	
    {
#	my $onlineEtymology =  $1;
#	$onlineEtymology =~ tr/'//d;
#        return $onlineEtymology;
    }
}

my $fh = new FileHandle;

$fh->open ("../WordLists/noms_communs.txt") or die ("could not open wordlist");


my $out = new FileHandle;
$out-> open (">../WordLists/LittreOutput.txt") or die ("could not open output log");
 
while (my $line = <$fh>)
{
    if ($line =~ /\S/)
	{
	    &getLittreEtymologyFromWeb ($line, $out);
	}
}
