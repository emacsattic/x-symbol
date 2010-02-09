Summary:     X-Symbol package for XEmacs (semi WYSIWYG for LaTeX, HTML)
Name:        x-symbol
Version:     4.5
Release:     3
Copyright:   GPL
Group:       Applications/Publishing
Source:      %{name}-%{version}-src.tar.gz
URL:         http://x-symbol.sourceforge.net/
BuildArch:   noarch
BuildRoot:   %{_tmppath}/%{name}-%{version}-buildroot
BuildPrereq: xemacs perl
Requires:    xemacs

%description
X-Symbol is a package for XEmacs which provide some WYSIWYGness in an area
where it greatly enhance the readability of your LaTeX or HTML source: using
"real" characters for "tokens" like \oplus or &#trade;.

#---------------------------------------------------------------------
%prep
%setup -q -n x-symbol

#---------------------------------------------------------------------
%build
make -k binkit BUILD_MULE=t \
	STAGING=${RPM_BUILD_ROOT}%{_libdir}/xemacs/xemacs-packages

# %patch -p1 
#---------------------------------------------------------------------
%clean

# be paranoid
[ "${RPM_BUILD_ROOT}" != "/" ] && rm -rf ${RPM_BUILD_ROOT}

#---------------------------------------------------------------------
%files 
%defattr(-,root,root)
%doc README ChangeLog
%dir %{_libdir}/xemacs/xemacs-packages/etc/x-symbol
%{_libdir}/xemacs/xemacs-packages/etc/x-symbol/*
%{_libdir}/xemacs/xemacs-packages/info/*
%dir %{_libdir}/xemacs/xemacs-packages/lisp/x-symbol
%{_libdir}/xemacs/xemacs-packages/lisp/x-symbol/*
%dir %{_libdir}/xemacs/xemacs-packages/man/x-symbol
%{_libdir}/xemacs/xemacs-packages/man/x-symbol/*
%{_libdir}/xemacs/xemacs-packages/pkginfo/*

#---------------------------------------------------------------------
%changelog
* Wed Oct 23 2002 Ryurick M. Hristev <ryurick.hristev@canterbury.ac.nz>
- get rid of the '/usr/local/bin/perl' patch, no longer required

* Sat Oct 19 2002 Ryurick M. Hristev <ryurick.hristev@canterbury.ac.nz>
- up2date for 4.43
- minor fixes and improvements

* Mon Sep 3 2001 Ryurick M. Hristev <r.hristev@phys.canterbury.ac.nz>
- wrote first spec file

