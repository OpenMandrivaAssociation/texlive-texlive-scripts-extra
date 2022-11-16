Name:		texlive-texlive-scripts-extra
Version:	62517
Release:	1
Summary:	TeX Live scripts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texlive-scripts-extra
License:	distributable
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-scripts-extra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-scripts-extra.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Miscellaneous scripts maintained as part of TeX Live, but not
important for the infrastructure. Thus, this is not part of
scheme-infraonly or tlcritical, just a normal package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texconfig
%{_texmfdistdir}/scripts/texlive-extra
%doc %{_texmfdistdir}/doc/man/man1/*

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
