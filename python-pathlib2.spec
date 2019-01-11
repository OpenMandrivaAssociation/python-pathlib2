%global srcname pathlib2
%global srcversion 2.1.0

Name:           python-%srcname
Version:        2.3.3
Release:        1
Summary:        Object-oriented filesystem paths
Group:          Development/Python
License:        BSD
URL:            http://github.com/ipython/%srcname
Source0:        https://pypi.io/packages/source/p/pathlib2/pathlib2-%{version}.tar.gz
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

%prep
%setup -q -n %{srcname}-%{srcversion}

%apply_patches

cp -a . %py2dir

%build
python setup.py build

pushd %py2dir
python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}

pushd %py2dir
python setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst CHANGELOG.rst LICENSE.rst
%{py3_puresitedir}/*.egg-info
%{py3_puresitedir}/%{srcname}.py

%files -n python2-%srcname
%doc README.rst CHANGELOG.rst LICENSE.rst
%{py_puresitedir}/*.egg-info
%{py_puresitedir}/%{srcname}.py
