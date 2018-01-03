Name:		texlive-savetrees
Version:	2.4
Release:	1
Summary:	Pack as much as possible onto each page of a LaTeX document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/savetrees
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/savetrees.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/savetrees.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/savetrees.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The goal of the savetrees package is to pack as much text as
possible onto each page of a LaTeX document. Admittedly, this
makes the document far less attractive. Nevertheless, savetrees
is a simple way to save paper when printing draft copies of a
document. It can also be useful when trying to meet a tight
page-length requirement for a conference or journal submission.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/savetrees
%{_texmfdistdir}/tex/latex/savetrees
%doc %{_texmfdistdir}/doc/latex/savetrees
#- source
%doc %{_texmfdistdir}/source/latex/savetrees

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
