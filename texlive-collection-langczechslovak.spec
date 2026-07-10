%global tl_name collection-langczechslovak
%global tl_revision 54074

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Czech/Slovak
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-langczechslovak
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langczechslovak.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(babel-czech)
Requires:	texlive(babel-slovak)
Requires:	texlive(cnbwp)
Requires:	texlive(collection-basic)
Requires:	texlive(collection-latex)
Requires:	texlive(cs)
Requires:	texlive(csbulletin)
Requires:	texlive(cslatex)
Requires:	texlive(csplain)
Requires:	texlive(cstex)
Requires:	texlive(hyphen-czech)
Requires:	texlive(hyphen-slovak)
Requires:	texlive(lshort-czech)
Requires:	texlive(lshort-slovak)
Requires:	texlive(texlive-cz)
Requires:	texlive(vlna)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Support for Czech/Slovak.

