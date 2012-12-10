Name: mcstrans
Version: 0.2.11
Release: %mkrel 3
Summary: SELinux Translation Daemon
License: GPLv2+
Group: System/Servers
Source: http://fedora.redhat.com/projects/%{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: selinux-devel >= 1.30.3-1
BuildRequires: cap-devel 
Requires(pre): rpm-helper
Requires(post): rpm-helper
Provides: setransd = %{version}-%{release}

%description
Security-enhanced Linux is a feature of the Linux® kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These
architectural components provide general support for the enforcement
of many kinds of mandatory access control policies, including those
based on the concepts of Type Enforcement®, Role-based Access
Control, and Multi-level Security.

mcstrans provides an translation daemon to translate SELinux categories 
from internal representations to user defined representation.

%prep
%setup -q

%build
%{make} clean
%{make} CFLAGS="-g %{optflags}"

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std} LIBDIR="%{buildroot}%{_libdir}" SHLIBDIR="%{buildroot}/%{_lib}"

%clean
%{__rm} -rf %{buildroot}

%post
%_post_service mcstrans

%preun
%_preun_service mcstrans

%files
%defattr(-,root,root,0755)
/sbin/mcstransd
%{_initrddir}/mcstrans
%{_mandir}/man8/mcs.8*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.11-3mdv2011.0
+ Revision: 620311
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2.11-2mdv2010.0
+ Revision: 430005
- rebuild

* Fri Aug 01 2008 David Walluck <walluck@mandriva.org> 0.2.11-1mdv2009.0
+ Revision: 260000
- add source
- 0.2.11

* Mon Jul 07 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.7-2mdv2009.0
+ Revision: 232360
- rebuilt against new libcap

* Fri Jan 04 2008 David Walluck <walluck@mandriva.org> 0.2.7-1mdv2008.1
+ Revision: 145562
- import mcstrans


* Mon Oct 30 2007 Steve Conklin <sconklin@redhat.com> - 0.2.7-1
- Folded current patches into tarball

* Thu Oct 25 2007 Steve Conklin <sconklin@redhat.com> - 0.2.6-3
- Fixed a compile problem with max_categories

* Thu Oct 25 2007 Steve Conklin <sconklin@redhat.com> - 0.2.6-2
- Fixed some init script errors

* Thu Sep 13 2007 Dan Walsh <dwalsh@redhat.com> 0.2.6-1
- Check for max_categories and error out

* Thu Mar 1 2007 Dan Walsh <dwalsh@redhat.com> 0.2.5-1
- Fix case where s0=""

* Mon Feb 26 2007 Dan Walsh <dwalsh@redhat.com> 0.2.4-1
- Translate range if fully specified correctly

* Mon Feb 12 2007 Dan Walsh <dwalsh@redhat.com> 0.2.3-1
- Additional fix to handle ssh root/sysadm_r/s0:c1,c2
Resolves: #224637

* Mon Feb 5 2007 Dan Walsh <dwalsh@redhat.com> 0.2.1-1
- Rewrite to handle MLS properly
Resolves: #225355

* Mon Jan 29 2007 Dan Walsh <dwalsh@redhat.com> 0.1.10-2
- Cleanup memory when complete

* Mon Dec 4 2006 Dan Walsh <dwalsh@redhat.com> 0.1.10-1
- Fix Memory Leak
Resolves: #218173

* Thu Sep 21 2006 Dan Walsh <dwalsh@redhat.com> 0.1.9-1
- Add -pie
- Fix compiler warnings
- Fix Memory Leak
Resolves: #218173

* Wed Sep 13 2006 Peter Jones <pjones@redhat.com> - 0.1.8-3
- Fix subsys locking in init script

* Wed Aug 23 2006 Dan Walsh <dwalsh@redhat.com> 0.1.8-1
- Only allow one version to run

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Mon Jun 19 2006 Dan Walsh <dwalsh@redhat.com> 0.1.7-1
- Apply sgrubb patch to only call getpeercon on translations

* Tue Jun 6 2006 Dan Walsh <dwalsh@redhat.com> 0.1.6-1
- Exit gracefully when selinux is not enabled

* Mon May 15 2006 Dan Walsh <dwalsh@redhat.com> 0.1.5-1
- Fix sighup handling

* Mon May 15 2006 Dan Walsh <dwalsh@redhat.com> 0.1.4-1
- Add patch from sgrubb
-         Fix 64 bit size problems
-         Increase the open file limit
-        Make sure maximum size is not exceeded

* Fri May 12 2006 Dan Walsh <dwalsh@redhat.com> 0.1.3-1
- Move initscripts to /etc/rc.d/init.d

* Thu May 11 2006 Dan Walsh <dwalsh@redhat.com> 0.1.2-1
- Drop Privs

* Mon May 8 2006 Dan Walsh <dwalsh@redhat.com> 0.1.1-1
- Initial Version
- This daemon reuses the code from libsetrans
