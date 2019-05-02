# revision 32550
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langczechslovak
Epoch:		1
Version:	20190228
Release:	1
Summary:	Czech/Slovak
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langczechslovak.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-collection-latex
Requires:	texlive-babel-czech
Requires:	texlive-babel-slovak
Requires:	texlive-cnbwp
Requires:	texlive-cs
Requires:	texlive-csbulletin
Requires:	texlive-cslatex
Requires:	texlive-csplain
Requires:	texlive-cstex
Requires:	texlive-hyphen-czech
Requires:	texlive-hyphen-slovak
Requires:	texlive-vlna
Requires:	texlive-lshort-czech
Requires:	texlive-lshort-slovak
Requires:	texlive-texlive-cz

%description
Support for Czech/Slovak.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
