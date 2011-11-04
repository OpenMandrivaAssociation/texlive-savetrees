# revision 22491
# category Package
# catalog-ctan /macros/latex/contrib/savetrees
# catalog-date 2011-05-15 09:57:20 +0200
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-savetrees
Version:	2.0
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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The goal of the savetrees package is to pack as much text as
possible onto each page of a LaTeX document. Admittedly, this
makes the document far less attractive. Nevertheless, savetrees
is a simple way to save paper when printing draft copies of a
document. It can also be useful when trying to meet a tight
page-length requirement for a conference or journal submission.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/savetrees/savetrees.bst
%{_texmfdistdir}/tex/latex/savetrees/savetrees.sty
%doc %{_texmfdistdir}/doc/latex/savetrees/README
%doc %{_texmfdistdir}/doc/latex/savetrees/savetrees.pdf
#- source
%doc %{_texmfdistdir}/source/latex/savetrees/savetrees.dtx
%doc %{_texmfdistdir}/source/latex/savetrees/savetrees.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
