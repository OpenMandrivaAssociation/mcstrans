Name: mcstrans
Version: 0.2.7
Release: %mkrel 1
Summary: SELinux Translation Daemon
License: GPL
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
%{__mkdir_p} %{buildroot}/%{_lib} 
%{__mkdir_p} %{buildroot}%{_libdir} 
%{makeinstall_std} LIBDIR="%{buildroot}%{_libdir}" SHLIBDIR="%{buildroot}/%{_lib}" install
%{__rm} -f %{buildroot}%{_sbindir}/*
%{__rm} -f %{buildroot}%{_libdir}/*.a

%clean
%{__rm} -rf %{buildroot}

%post 
chkconfig --add mcstrans
if [ -f %{_var}/lock/subsys/mcstransd ]; then
   %{__mv} %{_var}/lock/subsys/mcstransd %{_var}/lock/subsys/mcstrans
fi

%preun
%_preun_service %{name}

%postun 
%postun_service %{name}

%files
%defattr(-,root,root,0755)
/sbin/mcstransd
%{_sysconfdir}/rc.d/init.d/mcstrans
%{_mandir}/man8/mcs.8*

