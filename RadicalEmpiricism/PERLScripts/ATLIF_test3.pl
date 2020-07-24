  # Create a user agent object
use WebCrawl;
use strict;


getATLIFEtymology
{
    my $output = WebCrawl::postWebsiteContent 
	("http://atilf.atilf.fr/dendien/scripts/tlfiv4/showps.exe?p=combi.htm;java=no;");
    $output =~ /s=(\d+)/;
    my $sessionID = $1;
    WebCrawl::postWebsiteContent 
	("http://atilf.atilf.fr/dendien/scripts/tlfiv5/advanced.exe?8;s=$sessionID;p=assiste.htm;", 'mot', 'bonjour');
    $output = WebCrawl::postWebsiteContent 
	("http://atilf.atilf.fr/dendien/scripts/tlfiv5/displayp.exe?13;s=$sessionID;i=ft-1-2.htm;");
    print $output;

}
getATLIFEtymology();
