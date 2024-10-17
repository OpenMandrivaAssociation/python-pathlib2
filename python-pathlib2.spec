%global srcname pathlib2

Name:		python-%srcname
Version:	2.3.5
Release:	3
Summary:	Object-oriented filesystem paths
Group:		Development/Python
License:	BSD
URL:		https://github.com/ipython/%srcname
Source0:	http://pypi.python.org/packages/source/p/%srcname/%{srcname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)

%description
The old pathlib module on bitbucket is in bugfix-only mode. The goal of\
pathlib2 is to provide a backport of standard pathlib module which tracks\
the standard library module, so all the newest features of the standard\
pathlib can be used also on older Python versions.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py_build

%install
%py_install

%files
%doc README.rst CHANGELOG.rst LICENSE.rst
%{python_sitelib}/*.egg-info
%dir %{python_sitelib}/pathlib2
%{python_sitelib}/pathlib2/*
