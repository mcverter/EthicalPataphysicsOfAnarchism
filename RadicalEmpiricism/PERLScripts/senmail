package WebCrawl;

use LWP;
use strict;


    BEGIN {
        use Exporter   ();
        use vars       qw(@ISA @EXPORT @EXPORT_OK %EXPORT_TAGS);

        @ISA         = qw(Exporter);
        @EXPORT      = qw(&dbInsertWord);
    }
    use vars      @EXPORT_OK;








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
    
    my $ua;
    my $resp;
    
    $ua = new LWP::UserAgent;
    $resp = $ua->request($req);
        
    my $content;

    if (! $resp->is_success)
    {
	my $message = $resp->message;
	
	print "WARNING:  Response failed: $message." ;
	sleep 300;
	my $newContent = getWebsiteContent ($website);
	return -1;
    }
    else 
    {
	$content = $resp->as_string;
	return $content;
    }
}

sub postWebsiteContent
{
    my $website = shift;
# bad, lazy code.  change it
    my $var1 = shift;
    my $var2 = shift;
    
    my $headers = new HTTP::Headers('Accept' => 'text/plain', 'Content-Length'=>1024);
    my $req = new HTTP::Request("POST", $website, $headers);

#bad, lazy code.  change it.
    if ($var1 && $var2)
    {
	$req->content("$var1=$var2");
    }
    my $ua;
    my $resp;
    
    $ua = new LWP::UserAgent;
    $resp = $ua->request($req);
        
    my $content;

    if (! $resp->is_success)
    {
	my $message = $resp->message;
	
	print "WARNING:  Response failed: $message." ;
#	sleep 60;
#	my $newContent = getWebsiteContent ($website);
	return -1;
    }
    else 
    {
	$content = $resp->as_string;
	return $content;
    }
}

1;


#########################################################
#
#  LWP FUNCTION
#  oldGetWebsiteContent
#  MAYBE DELETE?
#########################################################

sub oldGetWebsiteContent
{
    my $website = shift;
    
    my $headers = new HTTP::Headers(Accept => 'text/plain');
    my $req = new HTTP::Request("GET", $website, $headers);
    
    my $robotCounter++;
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
