# TODO:
# - apache configuration, relocation to /usr/share
Summary:	Shows the current weather conditions on your Web page
Summary(pl):	Pokazuje aktualn± pogodê na Twojej stronie www
Name:		phpweather
Version:	2.2.0
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/phpweather/%{name}-%{version}.tar.bz2
# Source0-md5:	1ea31c3347b19c2e3d6f2e99894ce305
URL:		http://www.phpweather.net/
Requires:	webserver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpdir	/home/services/httpd/html/phpweather

%description
PHP Weather makes it easy to show the current weather on your Web
page. PHP Weather retrieves the latest METAR (weather) report and
converts this format into both imperial and metric units, caches the
data in a MySQL, PostgreSQL, or DBA database for fast retrieval, and
makes it easily available in PHP scripts. You can display the data in
several languages by using the included translations. You can also
access the information with a WAP-enabled mobile phone.

%description -l pl
PHP Weather u³atwia pokazywanie aktualnej pogody na stronie WWW.
Program pobiera ostatni raport pogodowy METAR i konwertuje jego format
na jednostki zarówno imperialne, jak i metryczne, zapamiêtuje dane w
bazie MySQL, PostgreSQL lub DBA w celu szybkiego odczytywania i czyni
je ³atwo dostêpne dla skryptów PHP. Mo¿na wy¶wietlaæ dane w kilku
jêzykach u¿ywaj±c za³±czonych t³umaczeñ. Mo¿na tak¿e dostaæ siê do
tych informacji przy u¿yciu telefonu komórkowego z obs³ug± WAP.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_phpdir}/{config,db/files,doc,icons,output},%{_sysconfdir}/httpd/%{name}}

install *.php		$RPM_BUILD_ROOT%{_phpdir}
install *.css		$RPM_BUILD_ROOT%{_phpdir}
install *.csv		$RPM_BUILD_ROOT%{_phpdir}
install config/*.php	$RPM_BUILD_ROOT%{_phpdir}/config
install db/*.php	$RPM_BUILD_ROOT%{_phpdir}/db
install db/files/*	$RPM_BUILD_ROOT%{_phpdir}/db/files
install doc/*.html	$RPM_BUILD_ROOT%{_phpdir}/doc/
# info page to install:
#install doc/
install icons/*.gif	$RPM_BUILD_ROOT%{_phpdir}/icons/
install output/*.php	$RPM_BUILD_ROOT%{_phpdir}/output/

touch $RPM_BUILD_ROOT%{_sysconfdir}/httpd/%{name}/defaults.php
ln -s %{_sysconfdir}/httpd/%{name}/defaults.php $RPM_BUILD_ROOT%{_phpdir}/defaults.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog doc/*.{pdf,txt}
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/httpd/%{name}/defaults.php
%dir %{_sysconfdir}/httpd/%{name}
%dir %{_phpdir}
%dir %{_phpdir}/config
%dir %{_phpdir}/db
%dir %{_phpdir}/db/files
%dir %{_phpdir}/doc
%dir %{_phpdir}/icons
%dir %{_phpdir}/output
%{_phpdir}/*.php
%{_phpdir}/*.css
%{_phpdir}/*.csv
%{_phpdir}/config/*.php
%{_phpdir}/db/*.php
%{_phpdir}/db/files/*
%{_phpdir}/doc/*.html
%{_phpdir}/icons/*.gif
%{_phpdir}/output/*.php
