%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global repo_name instack

Name:			instack
Version:		8.1.0
Release:		1%{?dist}
Summary:		OpenStack installation tool for diskimage-builder style elements
Group:			Development/Languages
License:		ASL 2.0
URL:			https://github.com/openstack/instack
Source0:		https://tarballs.openstack.org/%{repo_name}/%{repo_name}-%{upstream_version}.tar.gz

BuildArch:		noarch
BuildRequires:		git
BuildRequires:		python2-setuptools
BuildRequires:		python2-devel
BuildRequires:		python2-pbr
%if 0%{?fedora} > 0
BuildRequires:		python2-d2to1
%else
BuildRequires:		python-d2to1
%endif

Requires:		diskimage-builder >= 1.1.2
Requires:		python2-pbr >= 2.0.0
Requires:		python2-babel >= 2.3.4

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
* Thu Mar 08 2018 RDO <dev@lists.rdoproject.org> 8.1.0-1
- Update to 8.1.0

