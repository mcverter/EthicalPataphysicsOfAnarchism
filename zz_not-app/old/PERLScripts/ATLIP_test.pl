  # Create a user agent object
use LWP::UserAgent;
use WebCrawl;

my $headers = new HTTP::Headers(Accept => 'text/plain');
my $website = 'http://atilf.atilf.fr/dendien/scripts/tlfiv4/showps.exe?p=combi.htm;java=no;';
my $req = new HTTP::Request("GET", $website, $headers);
$ua = new LWP::UserAgent;
my $res = $ua->request($req);

my $sessionID;

  # Check the outcome of the response
  if ($res->is_success) {
      my $content = $res->content;
      $content =~ /s=(\d+)/;
      $sessionID = $1;
      my $req = $ua->post("http://atilf.atilf.fr/dendien/scripts/tlfiv5/advanced.exe?8;s=$sessionID;p=assiste.htm;", ['mot'=> 'bonjour', 'target' => '_parent']);
#      my $req = HTTP::Request->new(POST => "http://atilf.atilf.fr/dendien/scripts/tlfiv5/advanced.exe?8;s=$sessionID;p=assiste.htm;" );
 #     $req->content('mot=bonjour');
 #       my $res = $ua->request($req);

      # Check the outcome of the response
      if ($req->is_success) {
	  print $req->content;
	  $ua = LWP::UserAgent->new;
	  my $req = $ua->post("http://atilf.atilf.fr/dendien/scripts/tlfiv5/displayp.exe?14;s=$sessionID;i=ft-1-3.htm;", [ 'target' => '_top']);
	  print $req->content;
	  my $req = $ua->post("http://atilf.atilf.fr/dendien/scripts/tlfiv5/displayp.exe?12;s=$sessionID;i=ft-1-1.htm;", [ 'target' => '_top']);
	  print $req->content;
	  my $req = $ua->post("http://atilf.atilf.fr/dendien/scripts/tlfiv5/displayp.exe?13;s=$sessionID;i=ft-1-2.htm;", [ 'target' => '_top']);
	  print $req->content;
#	  my $req = $ua->get("http://atilf.atilf.fr/dendien/scripts/tlfiv5/displayp.exe?13;s=$sessionID;i=ft-1-3.htm;;");
#	  my $res = $ua->request($req);
#	  print $req->content;
      }
      else {
#	  print $res->status_line, "\n";
      }
  }
  else {
#      print $res->status_line, "\n";
  }