Name:		texlive-texlive-scripts-extra
Version:	62517
Release:	1
Summary:	TeX Live scripts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texlive-scripts-extra
License:	
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
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/texconfig
%{_texmfdistdir}/texmf-dist/texconfig/x
%{_texmfdistdir}/texmf-dist/texconfig/x/xterm
%{_texmfdistdir}/texmf-dist/texconfig/v
%{_texmfdistdir}/texmf-dist/texconfig/v/vt100
%{_texmfdistdir}/texmf-dist/texconfig/tcfmgr.map
%{_texmfdistdir}/texmf-dist/texconfig/tcfmgr
%{_texmfdistdir}/texmf-dist/texconfig/g
%{_texmfdistdir}/texmf-dist/texconfig/g/generic
%{_texmfdistdir}/texmf-dist/texconfig/README
%{_texmfdistdir}/texmf-dist/scripts
%{_texmfdistdir}/texmf-dist/scripts/texlive-extra
%{_texmfdistdir}/texmf-dist/scripts/texlive-extra/texlinks.sh
%{_texmfdistdir}/texmf-dist/scripts/texlive-extra/texconfig.sh
%{_texmfdistdir}/texmf-dist/scripts/texlive-extra/texconfig-sys.sh
%{_texmfdistdir}/texmf-dist/scripts/texlive-extra/texconfig-dialog.sh
%{_texmfdistdir}/texmf-dist/scripts/texlive-extra/pslatex.sh
%{_texmfdistdir}/texmf-dist/scripts/texlive-extra/ps2frag.sh
%{_texmfdistdir}/texmf-dist/scripts/texlive-extra/kpsewhere.sh
%{_texmfdistdir}/texmf-dist/scripts/texlive-extra/kpsetool.sh
%{_texmfdistdir}/texmf-dist/scripts/texlive-extra/e2pall.pl
%{_texmfdistdir}/texmf-dist/scripts/texlive-extra/dvired.sh
%{_texmfdistdir}/texmf-dist/scripts/texlive-extra/dvi2fax.sh
%{_texmfdistdir}/texmf-dist/scripts/texlive-extra/allneeded.sh
%{_texmfdistdir}/texmf-dist/scripts/texlive-extra/allcm.sh
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/texlinks.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/texlinks.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/texconfig.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/texconfig.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/texconfig-sys.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/texconfig-sys.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pslatex.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pslatex.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/ps2frag.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/ps2frag.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/mkofm.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/mkofm.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/mkocp.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/mkocp.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/kpsexpand.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/kpsexpand.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/kpsewhere.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/kpsewhere.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/kpsetool.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/kpsetool.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/kpsepath.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/kpsepath.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/e2pall.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/e2pall.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/dvired.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/dvired.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/dvi2fax.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/dvi2fax.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/allneeded.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/allneeded.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/allec.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/allec.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/allcm.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/allcm.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
