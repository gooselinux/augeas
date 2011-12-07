Name:           augeas
Version:        0.7.2
Release:        3%{?dist}
Summary:        A library for changing configuration files

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://augeas.net/
Source0:        http://augeas.net/download/%{name}-%{version}.tar.gz
# Format of the patch name is augeas-VERSION-NUMBER-HASH where VERSION
# gives the first version where this patch was applied, NUMBER orders patches
# against the same version, and HASH is the git commit hash from upstream
Patch0:         augeas-0.7.2-01-0c43ca0f.patch
Patch1:         augeas-0.7.2-02-6c713a08.patch
Patch2:         augeas-0.7.2-03-984ff1b8.patch
Patch3:         augeas-0.7.2-04-218003a8.patch
Patch4:         augeas-0.7.2-05-21d39d66.patch
Patch5:         augeas-0.7.2-06-11b85805.patch
Patch6:         augeas-0.7.2-07-72c636de.patch
Patch7:         augeas-0.7.2-08-0695bdd0.patch
Patch8:         augeas-0.7.2-09-5ee81630.patch
Patch9:         augeas-0.7.2-10-2102a725.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  readline-devel libselinux-devel
Requires:       %{name}-libs = %{version}-%{release}

%description
A library for programmatically editing configuration files. Augeas parses
configuration files into a tree structure, which it exposes through its
public API. Changes made through the API are written back to the initially
read files.

The transformation works very hard to preserve comments and formatting
details. It is controlled by ``lens'' definitions that describe the file
format and the transformation into a tree.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        libs
Summary:        Libraries for %{name}
Group:          System Environment/Libraries

%description    libs
The libraries for %{name}.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/augtool
%{_bindir}/augparse
%{_bindir}/fadot
%doc %{_mandir}/man1/*
%{_datadir}/vim/vimfiles/syntax/augeas.vim
%{_datadir}/vim/vimfiles/ftdetect/augeas.vim

%files libs
%defattr(-,root,root,-)
# %{_datadir}/augeas and %{_datadir}/augeas/lenses are owned
# by filesystem.
%{_datadir}/augeas/lenses/dist
%{_libdir}/*.so.*
%doc AUTHORS COPYING NEWS

%files devel
%defattr(-,root,root,-)
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/augeas.pc

%changelog
* Tue Aug 10 2010 Matthew Booth <mbooth@redhat.com> - 0.7.2-3
- Fix crash when reloading externally modified file. BZ 613967

* Tue Jun 29 2010 David Lutterkort <lutter@redhat.com> - 0.7.2-2
- Patches based on upstream fix for BZ 600141

* Tue Jun 22 2010 David Lutterkort <lutter@redhat.com> - 0.7.2-1
- Fix ownership of /usr/share/augeas. BZ 569393

* Wed Apr 21 2010 David Lutterkort <lutter@redhat.com> - 0.7.1-1
- New version

* Thu Jan 14 2010 David Lutterkort <lutter@redhat.com> - 0.7.0-1
- Install vim syntax files

* Mon Sep 14 2009 David Lutterkort <lutter@redhat.com> - 0.5.3-1
- Remove separate xorg.aug, included in upstream source

* Tue Aug 25 2009 Matthew Booth <mbooth@redhat.com> - 0.5.2-3
- Include new xorg lens from upstream

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 David Lutterkort <lutter@redhat.com> - 0.5.2-1
- New version

* Fri Jun  5 2009 David Lutterkort <lutter@redhat.com> - 0.5.1-1
- Install fadot

* Fri Mar 27 2009 David Lutterkort <lutter@redhat.com> - 0.5.0-2
- fadot isn't being installed just yet

* Tue Mar 24 2009 David Lutterkort <lutter@redhat.com> - 0.5.0-1
- New program /usr/bin/fadot

* Mon Mar  9 2009 David Lutterkort <lutter@redhat.com> - 0.4.2-1
- New version

* Fri Feb 27 2009 David Lutterkort <lutter@redhat.com> - 0.4.1-1
- New version

* Fri Feb  6 2009 David Lutterkort <lutter@redhat.com> - 0.4.0-1
- New version

* Mon Jan 26 2009 David Lutterkort <lutter@redhat.com> - 0.3.6-1
- New version

* Tue Dec 23 2008 David Lutterkort <lutter@redhat.com> - 0.3.5-1
- New version

* Mon Feb 25 2008 David Lutterkort <dlutter@redhat.com> - 0.0.4-1
- Initial specfile
