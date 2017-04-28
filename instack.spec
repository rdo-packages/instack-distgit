%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global repo_name instack

Name:			instack
Version:		6.1.0
Release:		1%{?dist}
Summary:		OpenStack installation tool for diskimage-builder style elements
Group:			Development/Languages
License:		ASL 2.0
URL:			https://github.com/openstack/instack
Source0:		https://tarballs.openstack.org/%{repo_name}/%{repo_name}-%{upstream_version}.tar.gz

BuildArch:		noarch
BuildRequires:		git
BuildRequires:		python-setuptools
BuildRequires:		python2-devel
BuildRequires:		python-d2to1
BuildRequires:		python-pbr

Requires:		diskimage-builder

%description
Instack is an installation tool for diskimage-builder style elements. It
installs the elements onto the running system, and can be used to install
OpenStack locally from both diskimage-builder elements and
openstack-tripleo-image-elements.

%prep
%autosetup -n %{name}-%{upstream_version} -S git

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
* Fri Apr 28 2017 rdo-trunk <javier.pena@redhat.com> 6.1.0-1
- Update to 6.1.0

* Thu Feb 16 2017 Alfredo Moralejo <amoralej@redhat.com> 6.0.0-1
- Update to 6.0.0

