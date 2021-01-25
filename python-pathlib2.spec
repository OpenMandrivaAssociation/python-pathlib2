%global srcname pathlib2

Name:           python-%srcname
Version:        2.3.5
Release:        1
Summary:        Object-oriented filesystem paths
Group:          Development/Python
License:        BSD
URL:            http://github.com/ipython/%srcname
Source0:        http://pypi.python.org/packages/source/p/%srcname/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:	python-setuptools
BuildRequires:	python-devel

BuildRequires:	python2-setuptools
BuildRequires:	python2-devel

%description
The old pathlib module on bitbucket is in bugfix-only mode. The goal of\
pathlib2 is to provide a backport of standard pathlib module which tracks\
the standard library module, so all the newest features of the standard\
pathlib can be used also on older Python versions.

%package -n python2-%srcname

Summary:	Object-oriented filesystem paths

%description -n python2-%srcname
The old pathlib module on bitbucket is in bugfix-only mode. The goal of\
pathlib2 is to provide a backport of standard pathlib module which tracks\
the standard library module, so all the newest features of the standard\
pathlib can be used also on older Python versions.

%prep
%setup -q -n %{srcname}-%{version}

%autopatch -p1

cp -a . %py2dir

%build
%{__python} setup.py build

pushd %py2dir
%{__python2} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

pushd %py2dir
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}


%files
%doc README.rst CHANGELOG.rst LICENSE.rst
%{python3_sitelib}/*.egg-info
#{python3_sitelib}/%{srcname}.py
#{python3_sitelib}/__pycache__/%{srcname}.cpython-37.*

%files -n python2-%srcname
%doc README.rst CHANGELOG.rst LICENSE.rst
%{python2_sitelib}/*.egg-info
#{python2_sitelib}/%{srcname}.py?
#{python2_sitelib}/%{srcname}.py

