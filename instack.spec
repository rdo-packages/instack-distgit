%global commit0 c9a6516ad4d9140dc3806fdb997de5bff3f7843b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%{!?upstream_version: %global upstream_version %{version}}
%global repo_name instack

Name:			instack
Version:		0.0.8
Release:		1%{?dist}
Summary:		OpenStack installation tool for diskimage-builder style elements
Group:			Development/Languages
License:		ASL 2.0
URL:			https://github.com/agroup/instack
# Once we have stable branches and stable releases we can go back to using release tarballs
Source0:  https://github.com/openstack/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildArch:		noarch
BuildRequires:      git
BuildRequires:		python-setuptools
BuildRequires:		python2-devel
BuildRequires:		python-d2to1
BuildRequires:		python-pbr

Requires:		python-argparse
Requires:		diskimage-builder

%description
Instack is an installation tool for diskimage-builder style elements. It
installs the the elements onto the running system, and can be used to install
OpenStack locally from both diskimage-builder elements and
openstack-tripleo-image-elements.

%prep
%autosetup -n %{name}-%{commit0} -S git

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.md
%doc LICENSE
%{_bindir}/instack
%{python2_sitelib}/instack
%{python2_sitelib}/*.egg-info

%changelog
* Mon Oct 19 2015 John Trowbridge <trown@redhat.com> - 0.0.8-1
- Use a source tarball for a git hash that has passed delorean CI for liberty release

* Wed Oct 15 2014 James Slagle <jslagle@redhat.com> 0.0.6-1
- Bump to  0.0.6

* Mon Sep 29 2014 James Slagle <jslagle@redhat.com> 0.0.5-1
- Release 0.0.5

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 08 2014 James Slagle <jslagle@redhat.com> 0.0.4-2
- Build with tito

* Tue Apr 08 2014 James Slagle <jslagle@redhat.com> 0.0.4-1
- Bump to 0.0.4

* Wed Mar 19 2014 James Slagle <jslagle@redhat.com> 0.0.3-1
- Bump to 0.0.3

* Tue Mar 18 2014 James Slagle <jslagle@redhat.com> 0.0.2-3
- Switch to using agroup github repo for the source

* Wed Mar 12 2014 James Slagle <jslagle@redhat.com> 0.0.2-2
- Switch __python to __python2 macro
- Switch python_sitelib to python2_sitelib macro

* Mon Feb 24 2014 James Slagle <jslagle@redhat.com> 0.0.2-1
- Don't use shortcommit
- Bump version to 0.0.2

* Tue Feb 18 2014 James Slagle <jslagle@redhat.com> 0.0.1-1
- Initial rpm build.
