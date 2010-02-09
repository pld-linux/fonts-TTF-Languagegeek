Summary:	Free TrueType fonts for Canadian syllabics
Summary(pl.UTF-8):	Wolnodostępne fonty TrueType dla sylabariuszy kanadyjskich
Name:		fonts-TTF-Languagegeek
Version:	9.601
Release:	1
License:	GPL v3
Group:		Fonts
Source0:	http://www.languagegeek.com/font/AboriginalSerif.zip
# Source0-md5:	deb6fcf99db5f9da540fd2a7c255a4f8
Source1:	http://www.languagegeek.com/font/AboriginalSans.zip
# Source1-md5:	3799ae7693a4dafb985b1ee4f047ff05
URL:		http://www.languagegeek.com/font/fontdownload.html
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
Languagegeek provides, free of charge, a number of quality fonts for
native languages across North America and the world. The Aboriginal
Series of fonts contains a full host of characters for languages using
syllabics, Cherokee, and Roman orthography, and was designed
specifically for on-screen viewing.

#%%description -l pl.UTF-8
# TODO

%prep
%setup -q -c -a1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{ttffontsdir}/AboriginalSans*.ttf
%{ttffontsdir}/AboriginalSerif*.ttf
