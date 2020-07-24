
# IN FILE
my $filename = "FrOutput1.txt";
my $IN = new FileHandle;
$IN->open ($filename) or die "Could not open INFILE $filename";

while (my $line = <$IN>)
{
    my @fields = split /\t/, $line;
    my $frenchWord = $fields[1];
    my $englishCognate = $fields[2];
    my $etymology = $fields[3];


########################################
#
#
# package Etymology
#
#
########################################
package Etymology;

sub new {
    my $class = shift;
    my $self = {
	_frenchWord => shift,
	_englishCognate => shift,
	_etymology => shift,
	_baseRoot => shift,
	_moreAt => undef,
	_radicals => [],
    };
    bless $self, $class;
    return $self;
}


#
#
# package MoreAt
#
#
########################################
package MoreAt;

sub new {
    my $class = shift;
    my $moreLine = shift;
    my $hrefIndex = index $moreLine, "href";
    $hrefIndex +=6;

    $moreLine = substr ($moreLine, 0, $hrefIndex) .  "http://www.m-w.com" . substr ($moreLine,  $hrefIndex) ;

    $moreLine =~ /href="(.*?)"/;
    my $href = $1;

    my $self;
    my $self = {
	_moreLine => $moreLine,
	_href => $href,
    };
    bless $self, $class;
    return $self;
}

1;

 ########################################
 #
 #
 # package Radical
 #
 #
 ########################################

package Radical;

sub new {
    my $class = shift;
    my $self = {
	_sourceLanguage => shift,
	_meaning => shift,
    };
    bless $self, $class;
    return $self;
}



sub getLanguage {
    my $self = shift;

    return $self->{_sourceLanguage};
}

sub getMeaning {
    my $self = shift;

    return $self->{_meaning};
}


sub print {
    my $self = shift;
    my $lang = $self-> {_sourceLanguage};
    my $mean = $self->{_meaning};
    print " RADICAL has LANGUAGE $lang and MEANING $mean\n"; 
}
 1;

#######################################
#
#
# package moreAt
#
#
########################################

package moreAt;

sub new {
    my $self = {
	_moreWord => undef,
	_definition => undef,
    };
    bless $self, 'MoreAt';
    return $self;
}

1;
