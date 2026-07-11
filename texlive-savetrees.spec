%global tl_name savetrees
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4
Release:	%{tl_revision}.1
Summary:	Optimise the use of each page of a LaTeX document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/savetrees
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/savetrees.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/savetrees.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/savetrees.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The goal of the savetrees package is to pack as much text as possible
onto each page of a LaTeX document. Admittedly, this makes the document
far less attractive. Nevertheless, savetrees is a simple way to save
paper when printing draft copies of a document. It can also be useful
when trying to meet a tight page-length requirement for a conference or
journal submission. Most of the package options cover specific
modifications to typesetting rules, but there are also options subtle,
moderate and extreme options for the "broad brush" approach.

