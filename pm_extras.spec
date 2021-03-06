########################################
# Derived definitions
########################################
%define __check_files %{nil}
%define name pm_extras
%define version 1.1
%define release 1.el5
%define prefix /usr
%define libdir	%{_libdir}
#
%define ocfdir /usr/lib/ocf/resource.d/heartbeat
%define extdir %{_libdir}/stonith/plugins/external
%define lcrsodir %{_libexecdir}/lcrso
#
#
#
Summary: Extra Tools & Scripts for Pacemaker 
Name: %{name}
Version: %{version}
Release: %{release}
Group: Applications
Source: %{name}-%{version}.tar.gz
License: GPL
Vendor: NIPPON TELEGRAPH AND TELEPHONE CORPORATION
BuildRoot: %{_tmppath}/%{name}-%{version}
BuildRequires: make, pacemaker-libs-devel >= 1.0.9, heartbeat-devel >= 3.0.3, cluster-glue-libs-devel >= 1.0.6, corosynclib-devel >= 1.2.7
Requires: pacemaker >= 1.0.9, resource-agents >= 1.0.3, cluster-glue >= 1.0.6, heartbeat >= 3.0.3

########################################
%description
Extra Scripts 
 for pacemaker 1.0.9 
           and 
     resoucr-agent 1.0.3 
           and 
     cluster-glue 1.0.6

 * 2010/10/6
   * RA NVclient 1.4
   * RA VIPcheck 1.1
   * plugin stonith-helper 1.0
   * tool ifcheckd 1.0 for Heartbeat
   * tool iface_check.lcrso 1.0 for Corosync
    - The use is going to be enabled after corosync-2.0.

########################################
%prep
########################################
rm -rf $RPM_BUILD_ROOT

########################################
%setup -q
########################################

########################################
%build
########################################

########################################
%configure
########################################

########################################
%pre
########################################

########################################
%install
########################################
make DESTDIR=$RPM_BUILD_ROOT install

########################################
%clean
########################################
if
	[ -n "${RPM_BUILD_ROOT}"  -a "${RPM_BUILD_ROOT}" != "/" ]
then
	rm -rf $RPM_BUILD_ROOT
fi
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

########################################
%post
########################################

########################################
%preun
########################################

########################################
%postun
########################################

########################################
%files
########################################
%defattr(-,root,root)

%dir %{ocfdir}
%attr (755, root, root) %{ocfdir}/NVclient
%attr (755, root, root) %{ocfdir}/VIPcheck

%dir %{extdir}
%attr (755, root, root) %{extdir}/stonith-helper

%attr (-,root,haclient) %{_libdir}/heartbeat/ifcheckd
%dir %{lcrsodir}
%attr (755, root, root) %{lcrsodir}/iface_check.lcrso

%doc %{_docdir}/pm_extras/README
%doc %{_docdir}/pm_extras/HowToBuild_pm_extras.txt


########################################
%changelog
########################################
* Fri May 13 2011 Hideo Yamauchi <yamauchi@matrixjpn.com>
* Wed Oct 6 2010 Yuusuke IIDA <iidayuus@intellilink.co.jp>
- initial release
