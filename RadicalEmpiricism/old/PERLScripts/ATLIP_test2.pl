  # Create a user agent object
use LWP::UserAgent;
use WebCrawl;
use strict;

sub getATLIFEtymology
{
    my $headers = new HTTP::Headers(Accept => 'text/plain');
    my $website = 'http://atilf.atilf.fr/dendien/scripts/tlfiv4/showps.exe?p=combi.htm;java=no;';
    my $req = new HTTP::Request("GET", $website, $headers);
    my $ua = new LWP::UserAgent;
    my $res = $ua->request($req);

    my $sessionID;

    # Check the outcome of the response
    if ($res->is_success) {
	my $content = $res->content;
	$content =~ /s=(\d+)/;
	$sessionID = $1;
	my $req = $ua->post("http://atilf.atilf.fr/dendien/scripts/tlfiv5/advanced.exe?8;s=$sessionID;p=assiste.htm;", ['mot'=> 'bonjour']);
	
	# Check the outcome of the response
	if ($req->is_success) {
	    $ua = LWP::UserAgent->new;
	    my $req = $ua->post("http://atilf.atilf.fr/dendien/scripts/tlfiv5/displayp.exe?13;s=$sessionID;i=ft-1-2.htm;");
	    print $req->content;
	}
    }
}
getATLIFEtymology();
