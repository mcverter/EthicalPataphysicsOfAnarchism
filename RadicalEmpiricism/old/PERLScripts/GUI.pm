#!/usr/bin/perl

use CGI;
use CGI qw/:standard -debug/;
use EtymologyDatabaseHandle;
use InsertStaticTable;
use strict;
open (STDERR, ">&STDOUT");
##############
#
# debug log
#
##############

$| = 1;
open DEBUG_LOG, ">>c:\\EtymologicalEmpiricism\\PERLScripts\\log.txt";

##############
#
# global handles to CGI object 
#   and Database Object
#
##############
my ($cgi) = new CGI;
my $eDBh = new EtymologyDatabaseHandle();



loadPage();


#################################
#
#   METHOD: printMainScreen 
#   PRECONDITIONS: called by loadPage()
#   POSTCONDITIONS: calls 
#                   allWordPanel()
#                   allCognatePanel()
#                   allEtymologicalRoots()
#                   allSemanticCategorys()
#
#
#   SUMMARY: 
#
#   VARIABLES:
# 
##################################

sub printMainScreen
{
    print $cgi->header();
    print $cgi->start_html(
		       -title => "Word Lookup"
		       );
#    &allWordPanel;
#    print "<hr>\n";
    print "<center>\n";
    &allWordsWithEtymologiesPanel;
    print "<hr>\n";

 #   &allCognatesPanel;
 #   print "<hr>\n";
    &allEtymologicalRoots;
    print "<hr>\n";
    &allSemanticCategories;
    print "</center>\n";
    print $cgi->end_html;
}


#################################
#
#   METHOD: printAllWordEtymRoots
#   PRECONDITIONS: called by printWordDetailScreen()
#   POSTCONDITIONS: 
#   SUMMARY: prints all the etymological roots
#              of a given Word
#
#   VARIABLES:  wordID (integer)
# 
##################################

sub printAllWordEtymRoots
{
    my $wordID = shift;
    print <<"=====";
      <table border="1">
	  <caption> <b>ETYMOLOGICAL RADICALS </b></caption>
	  <tr><th>Radical</th><th>Language</th><th>Meaning</th><th>ViewMore</th></tr>
=====
my $sthPtr = $eDBh->selectEtymRadicalsFromWord($wordID);
    my $rootRef;
    while (( $rootRef = $eDBh->getNext($sthPtr))
	   && (@$rootRef))
    {
	my $radicalID = $rootRef->[0];
	my $radical = $rootRef->[1];
	my $lang = $rootRef->[2];
	my $meaning = $rootRef->[3];
	my $view = "<a href=\"GUI.pm?mode=showEtymRadical&etymRoot=$radicalID\">Explore \"$radical\"</a>";
	print "<tr><td>$radical</td><td>$lang</td><td>$meaning</td><td>$view</td></tr>\n";
    }
    print "</table>\n<hr>";
}




#################################
#
#   METHOD: printAllWordSemRoots
#   PRECONDITIONS: called by printWordDetailScreen()
#   POSTCONDITIONS: 
#   SUMMARY: prints all semantic roots of a given word
#
#   VARIABLES: wordID (int)
# 
##################################
sub printAllWordSemRoots
{
    my $wordID = shift;
    print <<"=====";
      <table border="1">
	  <caption> <b>SEMANTIC CATEGORIES </b></caption>
	  <tr><th>Category</th><th>ViewMore</th></tr>
=====
my $sthPtr = $eDBh->selectSemCategoriesFromWord($wordID);
    my $catRef;
    while (( $catRef = $eDBh->getNext($sthPtr))
	   && (@$catRef))
    {
	my $categoryID = $catRef->[0];
	my $category = $catRef->[1];
	my $view = "<a href=\"GUI.pm?mode=showSemCategory&semRoot=$categoryID\">Explore \"$category\"</a>";
	print "<tr><td>$category</td><td>$view</td></tr>\n";
    }
    print "</table>\n<hr>";

}

sub printWordType
{
    my $wordID = shift;
    print <<"=====";
      <table border="1">
	  <caption> <b>WORD TYPE </b></caption>
	  </table>
<hr>
=====
}

sub printFrequency 
{
    my $wordID = shift;
    print <<"=====";
      <table border="1">
	  <caption> <b>Word Frequency </b></caption>
	  <tr><th>Year Published</th><th>Title</th><th>Frequency</th></tr>
=====
    my $sthPtr = $eDBh->selectFrequencyOfWord($wordID);
    my $freqRef;
    while (( $freqRef = $eDBh->getNext($sthPtr))
	   && (@$freqRef))
    {
	my $year = $freqRef->[0];
	my $title = $freqRef->[1];
	my $frequency = $freqRef->[2];
	print "<tr><td>$year</td><td>$title</td><td>$frequency</td></tr>\n";
    }

    print "</table>\n<hr>";
}


#################################
#
#   METHOD: printWordDetailScreen
#   PRECONDITIONS: called by loadPage()
#   POSTCONDITIONS: calls
#                     printAllWordEtymRoots($wordID);
#                     printAllWordSemRoots($wordID);
#                     printWordType();
#                     printFrequency();                      
#                  also calls $eDBh->getAllWordInformation();
#                   and printEtymology()
#   SUMMARY: 
#
#   VARIABLES:
# 
##################################
sub printWordDetailScreen
{
    print DEBUG_LOG "html word info started.\n";

    my $wordID = shift;
    print DEBUG_LOG "html word line 2.\n";
    my $wordArrayRef = $eDBh->getAllWordInformation($wordID); 
    print DEBUG_LOG "html word line 3.\n";
    my $word =  $wordArrayRef->[1];
    my $language = $wordArrayRef->[2];
    my $cognate = $wordArrayRef->[3];
    my $mwEtymologyID = $wordArrayRef->[4];
    my $onlineEtymologyID = $wordArrayRef->[5];
    my $frenchEtymologyID = $wordArrayRef->[6];
    my $frenchRoot = $wordArrayRef->[7];
    my $wordTypeID = $wordArrayRef->[8];
    print DEBUG_LOG "French Etymology ID: $frenchEtymologyID .\n";   
    print $cgi->header();
    print $cgi->start_html(
		       -title => "Information for Word $word"
		       );
    print <<"=====";
    <h2> Information for Word <em>$word</em></h2>
     <br />
    <table border="1">
	<tr><th>Language:</th><td>$language</td></tr>
	<tr><th>English Cognate:</th><td>$cognate</td></tr>
	<tr><th>French Root</th><td>$frenchRoot</td></tr>
    </table>

=====

# I need to redesign database calls to get etymologies 
#  from lookup table in one swoop
beginEtymology();
    print DEBUG_LOG "French $frenchEtymologyID. MW: $mwEtymologyID, online: $onlineEtymologyID .\n";   
    printEtymology($frenchEtymologyID);
    printEtymology($mwEtymologyID);
    printEtymology($onlineEtymologyID);

    endEtymology();

    printAllWordEtymRoots($wordID);
    printAllWordSemRoots($wordID);
    printWordType();
   printFrequency();

    print $cgi->end_html;

    1;
}
#################################
#
#   METHOD:  printEtymology
#   PRECONDITIONS: called by printWordDetailScreen() 
#   POSTCONDITIONS: 
#   SUMMARY:  prints the Etymology in a table
#
#   VARIABLES:
# 
##################################
sub printEtymology 
{
    my $etymologyID = shift;
    print DEBUG_LOG "Print Etymology:  ID =$etymologyID, \n";    
    if ($etymologyID) 
	
    {
	 my $etymRef = $eDBh->getEtymology($etymologyID);
	 my $etymVal = $etymRef->[0];
	 my $etymSource = $etymRef->[1];
	 my $etymURL = $etymRef->[2];
 



    print <<"=====";
	<tr>
	<td>$etymSource <br /> ($etymURL)</td>
	<td>$etymVal</td>
	</tr>
=====
}
}

#################################
#
#   METHOD: 
#   PRECONDITIONS: 
#   POSTCONDITIONS: 
#   SUMMARY: 
#
#   VARIABLES:
# 
##################################
sub beginEtymology
{
    print <<"=====";
    <table border="1">
	<caption><b> ETYMOLOGIES</b></caption>
	<th>Source</th><th>Etymology</th>
=====
}

#################################
#
#   METHOD: 
#   PRECONDITIONS: 
#   POSTCONDITIONS: 
#   SUMMARY: 
#
#   VARIABLES:
# 
##################################
sub endEtymology
{
    print <<"=====";
    </table>
    <hr>
=====
}

#################################
#
#   METHOD: 
#   PRECONDITIONS: 
#   POSTCONDITIONS: 
#   SUMMARY: 
#
#   VARIABLES:
# 
##################################
sub printCognateDetailScreen
{
    my $cognate = shift;
}

#################################
#
#   METHOD: 
#   PRECONDITIONS: 
#   POSTCONDITIONS: 
#   SUMMARY: 
#
#   VARIABLES:
# 
##################################
sub printEtymologicalRootScreen
{
    my $root = shift;

    print $cgi->header();
    print $cgi->start_html(
		       -title => "Information for Etymological Radical $root"
		       );

    printEtymRootDetails($root);
    print DEBUG_LOG "all details printed\n";
    printAllEtymRootWords($root);
    print $cgi->end_html;
}

#################################
#
#   METHOD: 
#   PRECONDITIONS: 
#   POSTCONDITIONS: 
#   SUMMARY: 
#
#   VARIABLES:
# 
##################################
sub     printAllEtymRootWords
{
    my $etymID = shift;
    my $etymWord = shift;
    print <<"=====";
      <table border="1">
	  <caption> Words with the Etymological Root $etymWord</caption>
	  <tr><th>Word</th><th>ViewMore</th></tr>
=====
print DEBUG_LOG "about to select words from database\n";
my $sthPtr = $eDBh->selectWordsFromEtymRadical($etymID);
print DEBUG_LOG "after  selecting words from database\n";
    my $rootRef;
    while (( $rootRef = $eDBh->getNext($sthPtr))
	   && (@$rootRef))
    {
	print DEBUG_LOG "before next root ref\n";
	my $wordID = $rootRef->[0];
	my $word = $rootRef->[1];
	my $view = "<a href=\"GUI.pm?mode=showWord&word=$wordID\">Explore \"$word\"</a>";
	print "<tr><td>$word</td><td>$view</td></tr>\n";
	print DEBUG_LOG "after next root ref\n";
    }
    print "</table>";
    print DEBUG_LOG "at end of print etymologyical root words\n";
}

#################################
#
#   METHOD: 
#   PRECONDITIONS: 
#   POSTCONDITIONS: 
#   SUMMARY: 
#
#   VARIABLES:
# 
##################################
sub printEtymRootDetails
{
    my $etymID = shift;
    my $etymRef = $eDBh->selectEtymRadicalInfo($etymID);
}

#################################
#
#   METHOD: 
#   PRECONDITIONS: 
#   POSTCONDITIONS: 
#   SUMMARY: 
#
#   VARIABLES:
# 
##################################
sub printSemanticCategoryScreen
{
    my $root = shift;
}



#################################
#
#   METHOD: 
#   PRECONDITIONS: 
#   POSTCONDITIONS: 
#   SUMMARY: 
#
#   VARIABLES:
# 
##################################
sub allWordPanel
{    
    
#    my $sth = $eDBh->getAllWords();
#    my $rowArray;
    
    print <<"=====";
    
    <h2> All Words </h2>
	<form action="GUI.pm">
	<input type="hidden" name="mode" value="showWord">
	<select name=word size=10>	    
=====


#    while (($rowArray = $eDBh->getNextRow($sth)) 
#	   && (@$rowArray))
#    {
#	my $wordID = $rowArray->[0];
#	my $word  = $rowArray->[1];
#	print "<option  value=\"$wordID\">$word</option>\n";
#    }
    print <<"=====";
    </select>
	<br />
	<input type="submit" value="Lookup Word Information">
	</form>
    
=====
}


#################################
#
#   METHOD: 
#   PRECONDITIONS: 
#   POSTCONDITIONS: 
#   SUMMARY: 
#
#   VARIABLES:
# 
##################################
sub allWordsWithEtymologiesPanel
{    
    print DEBUG_LOG "allWOrdsWithETymPanel.\n";    
#    my $sth = $eDBh->getAllWordsWithEtymologies();
#    my $rowArray;

    
    print <<"=====";
    
    <h2> All Words with Etymologies</h2>
	<form action="GUI.pm">
	<input type="hidden" name="mode" value="showWord">
	<select name=word size=10>	    
=====
insertWordsWithEtymRoots();
#    while (($rowArray = $eDBh->getNextRow($sth)) 
#	   && (@$rowArray))
#    {
#	my $wordID = $rowArray->[0];
#	my $word  = $rowArray->[1];
#	print "<option  value=\"$wordID\">$word</option>\n";
#    }
    print <<"=====";
    </select>
	<br />
	<input type="submit" value="Lookup Word Information">
	</form>
    
=====
}

#################################
#
#   METHOD: 
#   PRECONDITIONS: 
#   POSTCONDITIONS: 
#   SUMMARY: 
#
#   VARIABLES:
# 
##################################
sub allEtymologicalRoots
{    
    print <<"=====";    
    <h2> All Etymological Roots </h2>
    <form action="GUI.pm">
    <input type="hidden" name="mode" value="showEtymRadical">
    <select name=etymRoot size=10>	        
=====
insertEtymologicalRoots();

#    my $sth = $eDBh->getAllRoots();
#    my $rowArray;
#    while (($rowArray = $eDBh->getNextRow($sth)) 
#	   && (@$rowArray))
#    {
#	my $radID = $rowArray->[0];
#	my $radTerm = $rowArray->[1];
#	print "<option value=\"$radID\">$radTerm</option>\n";
#    }
    print <<"=====";    
    </select>
	<br />
	<input type="submit" value="Lookup Radical Information">
    </form>
=====
}

#################################
#
#   METHOD: 
#   PRECONDITIONS: 
#   POSTCONDITIONS: 
#   SUMMARY: 
#
#   VARIABLES:
# 
##################################
sub allSemanticCategories
{    
    print <<"=====";    
    <h2> All Semantic Categories </h2>
    <form action="GUI.pm">
    <input type="hidden" name="mode" value="showSemCategory">
    <select name=etymRoot size=10>	        
=====
insertSemanticCategories();
#    my $sth = $eDBh->getAllSem();
#    my $rowArray;
#    while (($rowArray = $eDBh->getNextRow($sth)) 
#	   && (@$rowArray))
#    {
#	my $semID = $rowArray->[0];
#	my $semTerm = $rowArray->[1];
#	print "<option value=\"$semID\">$semTerm</option>\n";
#    }
    print <<"=====";    
    </select>
	<br />
	<input type="submit" value="Lookup Category Information">
    </form>
=====
}

#################################
#
#   METHOD: 
#   PRECONDITIONS: 
#   POSTCONDITIONS: 
#   SUMMARY: 
#
#   VARIABLES:
# 
##################################
sub allCognatesPanel
{
    
    print <<"=====";
    
    <h2> All Cognates </h2>
	<form action="GUI.pm">
	<input type="hidden" name="mode" value="showWord">
	<select name=word size=10>	    
=====

    my $sth = $eDBh->getAllCognates();
    
    my $rowArray;
    my $oldCognate;
    
    print "<select>\n";
    while (($rowArray = $eDBh->getNextRow($sth)) 
	   && (@$rowArray))

    {
	my $wordID = $rowArray->[0];
	my $cognate = $rowArray->[1];
	if ($cognate ne $oldCognate)
	{
	    print "<option value=\"$wordID\">$cognate</option>\n";
	    $oldCognate = $cognate;
	}
    }
    print <<"=====";
    </select>
	<br />
	<input type="submit" value="Lookup Cognate Information">
	</form>
    
=====
}





#################################
#
#   METHOD: loadPage
#   PRECONDITIONS: called from main
#   POSTCONDITIONS: depending on the mode, calls either
#                    printMainScreen();
#                    printWordDetailScreen($word);
#                    printCognateDetailScreen($cognate);
#                    printEtymologicalRootScreen($etymRoot);
#                    printSemanticCategoryScreen($semRoot);
#   SUMMARY: 
#
#   VARIABLES: mode -> determines which page to load
# 
##################################
sub loadPage
{
    my $mode = $cgi->param('mode');
    print DEBUG_LOG "in load page Mode = $mode.\n";
   if ((!$mode)   ||
	($mode eq 'main'))
    {
	printMainScreen();
    }
    elsif ($mode eq 'showWord')
    {
	print DEBUG_LOG "in case statment show word.\n";
	my $word = $cgi->param('word');
	printWordDetailScreen($word);
    }
    elsif ($mode eq 'showCognate')
    {
	my $cognate = $cgi->param('cognate');
	printCognateDetailScreen($cognate);
    }

   elsif ($mode eq 'showEtymRadical')
    {
	my $etymRoot =  $cgi->param('etymRoot');
	printEtymologicalRootScreen($etymRoot);
    }
    
    elsif ($mode eq 'showSemCategory')
    {
	my $semRoot =  $cgi->param('semRoot');
	printSemanticCategoryScreen($semRoot);
    }
    
}
