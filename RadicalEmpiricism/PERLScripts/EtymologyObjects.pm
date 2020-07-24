
########################################
#
#
# package Word
#
#
########################################
# +-----------------+----------+------+-----+---------+-------+
# | Field           | Type     | Null | Key | Default | Extra |
# +-----------------+----------+------+-----+---------+-------+
# | WordID          | int(11)  | NO   | PRI | 0       |       |
# | Word            | tinytext | NO   |     | NULL    |       |  
# | Language        | int(11)  | YES  |     | NULL    |       | 
# | EnglishCognate  | tinytext | YES  |     | NULL    |       | 
# | MWEtymology     | text     | YES  |     | NULL    |       | 
# | OnlineEtymology | text     | YES  |     | NULL    |       | 
# | FrenchEtymology | text     | YES  |     | NULL    |       | 
# | FrenchRoot      | tinytext | YES  |     | NULL    |       | 
# | WordTypeID      | int(11)  | YES  |     | NULL    |       | 
# +-----------------+----------+------+-----+---------+-------+
############################################################



package Word;

sub new {
    my $class = shift;
    my $self = {
	_frenchWord => shift,
#	_englishCognate => shift,
#	_etymology => shift,
#	_baseRoot => shift,
#	_moreAt => undef,
#	_radicals => [],
    };
    bless $self, $class;
    return $self;
}



###################################
#
#
# SET Methods
#
##################################

sub setWord {
    my $self = shift;
    $self-> {_Word}= shift;
}

sub setLanguage {
    my $self = shift;
    $self-> {_Language}= shift;
}

sub setEnglishCognate {
    my $self = shift;
    $self-> {_EnglishCognate}= shift;
}

sub setMWEtymology {
    my $self = shift;
    $self-> {_MWEtymology}= shift;
}
sub setOnlineEtymology {
    my $self = shift;
    $self-> {_OnlineEtymology}= shift;
}
sub setTLIFEtymology {
    my $self = shift;
    $self-> {_TLIFEtymology}= shift;
}
sub setFrenchRoot {
    my $self = shift;
    $self-> {_FrenchRoot}= shift;
}
sub setWordType {
    my $self = shift;
    $self-> {_WordType}= shift;
}


sub addRadical {
    my $self = shift;
    my $newRadical = shift;
    my $radicals = $self->{_radicals} ;
    my @radicals = @$radicals;
    push (@$radicals, \$newRadical);
    
}

sub addMoreAt {
    my $self = shift;
    my $moreAt = shift;
    $self->{_etymology} = $moreAt;

}



###################################
#
#
# GET Methods
#
##################################

sub getWord {
    my $self = shift;
    return $self-> {_Word};
}

sub getLanguage {
    my $self = shift;
    return $self-> {_Language};
}

sub getEnglishCognate {
    my $self = shift;
    return $self-> {_EnglishCognate};
}

sub getMWEtymology {
    my $self = shift;
    return $self-> {_MWEtymology};
}
sub getOnlineEtymology {
    my $self = shift;
    return $self-> {_OnlineEtymology};
}
sub getTLIFEtymology {
    my $self = shift;
    return $self-> {_TLIFEtymology};
}
sub getFrenchRoot {
    my $self = shift;
    return $self-> {_FrenchRoot};
}
sub getWordType {
    my $self = shift;
    return $self-> {_WordType};
}



sub print {
    my $self = shift;
    my $frenchWord = $self-> {_frenchWord};
    my $englishCognate = $self->{_englishCognate};
    my $etymology = $self-> {_etymology};
    my $baseRoot = $self->{_baseRoot};
    my $moreAt = $self->{_moreAt};
    my @radicals = @{ $self->{_radicals} };

    $baseRoot =~ /.*?([A-Z].*?) <i>(.*)/;
    my $language = $1;
    my $meaning = $2;


    my $baseID = $eDBh->dbInsertEtymBase('NULL', $baseRoot, $language, $meaning, $moreAt);
    


    print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n";

    print "\n\nETYMOLOGY is $etymology.  \n  BASEROOT is $baseRoot.\n  MOREAT is $moreAt\n" ; 

    my $i = 1;
    foreach my $rad (@radicals)
    {
	
	my $language = $$rad->getLanguage();
	my $meaning = $$rad->getMeaning();
	print "    $i.  ";
	$$rad->print();
	$i++;
	my $radicalInsertID = $eDBh->dbInsertRadical ('NULL', $meaning, $language, $meaning);	
	my $baseRadInsertID = $eDBh->dbInsertBaseRadicalJunction('NULL', $radicalInsertID, $baseID);
	
	
    }
    print "============================================================\n";
    print "\n\n";

    my $wordInsertID = $eDBh->dbInsertWord ('NULL', $frenchWord, $englishCognate, $etymology, $baseID, $baseID, 0);
 

}

 ########################################
 #
 #
 # package Radical
 #
 #
 ########################################
# +-------------+----------+------+-----+---------+-------+
# | Field       | Type     | Null | Key | Default | Extra |
# +-------------+----------+------+-----+---------+-------+
# | RadicalID   | int(11)  | NO   | PRI | 0       |       | 
# | RadicalWord | tinytext | NO   |     | NULL    |       | 
# | Language    | tinytext | NO   |     | NULL    |       | 
# | Meaning     | text     | YES  |     | NULL    |       | 
# +-------------+----------+------+-----+---------+-------+
#########################################
package Radical;

sub new {
    my $class = shift;
    my $self = {
	_Radical => shift,
	_Language => undef,
	_Meaning => undef,
    };

    bless $self, $class;
    return $self;
}


###################################
#
#
# GET Methods
#
##################################

sub getRadical {
    my $self = shift;
    return $self->{_Radical};
}

sub getLanguage {
    my $self = shift;
    return $self->{_Language};
}

sub getMeaning {
    my $self = shift;
    return $self->{_Meaning};
}


sub print
{
    my $self = shift;
    my $lang = $self-> {_Language};
    my $mean = $self->{_Meaning};
    print " RADICAL has LANGUAGE $lang and MEANING $mean\n"; 
}
###################################
#
#
# SET Methods
#
##################################

sub setRadical {
    my $self = shift;
    $self-> {_Radical}= shift;
}


sub setLanguage {
    my $self = shift;
    $self-> {_Language}= shift;
}

sub setMeaning {
    my $self = shift;
    $self-> {_Meaning}= shift;
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

########################################
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
#   EtymologyParser
#
#
#
#######################################
#package EtymologyParser;

