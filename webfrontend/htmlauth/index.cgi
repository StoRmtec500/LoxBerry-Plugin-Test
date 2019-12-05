#!/usr/bin/perl

use LoxBerry::System;
use LoxBerry::Web;
use LoxBerry::Log;
use Config::Simple;
use HTML::Template;
use CGI;
use warnings;
use strict;
use Data::Dumper;


my $version = "0.1.1";

our $cgi = CGI->new;
$cgi->import_names('R');


#############################
## VAR
#############################

my $lat;

#############################
## Read Settings
#############################
my $myFolder = "$lbpconfigdir";

my $pcfg = new Config::Simple('$lbpconfigdir/solcast.cfg');
print STDERR Dumper($pcfg);
print STDERR "Hallo"; 


##########################################################################
# Template and language settings
##########################################################################
require LoxBerry::Web;
	
	## Logging for serverside webif requests
	my $log = LoxBerry::Log->new (
		name => 'Webinterface',
		filename => "$lbplogdir/webinterface.log",
		stderr => 1,
		loglevel => 7,
		addtime => 1
	);

	LOGSTART "Solcast";
	
	# Init Template
	my $template = HTML::Template->new(
	    filename => "$lbptemplatedir/main.html",
	    global_vars => 1,
	    loop_context_vars => 1,
	    die_on_bad_params => 0,
		associate => $pcfg
	);
	
	print $template->output;
	
	# Print the form
	&form_print();

exit;


##########################################################################
# Form: Log
##########################################################################

sub form_log
{
	$template->param("FORM_LOG", 1);
	$template->param("LOGLIST", LoxBerry::Web::loglist_html());
	return();
}

##########################################################################
# Print Form
##########################################################################

sub form_print
{
	# Navbar
	our %navbar;

$navbar{1}{Name} = "Solcast Forecast";
$navbar{1}{URL} = 'index.cgi';
$navbar{1}{Notify_Package} = $lbpplugindir;
 
$navbar{2}{Name} = "All logfiles";
$navbar{2}{URL} = LoxBerry::Web::loglist_url();
$navbar{2}{target} = "_blank";
 
$navbar{1}{active} = 1;

	
	# Template
	LoxBerry::Web::lbheader("Solcast Forecast", "https://www.loxwiki.eu/x/t4RdAw", "");
	print $template->output();
	LoxBerry::Web::lbfooter();
	
	exit;

}