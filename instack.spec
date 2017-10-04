%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global repo_name instack

Name:			instack
Version:		7.0.1
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

Requires:		diskimage-builder >= 1.1.2
Requires:		python-pbr >= 2.0.0
Requires:		python-babel >= 2.3.4

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
* Wed Oct 04 2017 rdo-trunk <javier.pena@redhat.com> 7.0.1-1
- Update to 7.0.1

* Tue Aug 29 2017 Haikel Guemar <hguemar@fedoraproject.org> 7.0.0-1
- Update to 7.0.0

