#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6E3CBCE93372DCFA (donald@stufft.io)
#
Name     : virtualenv
Version  : 15.1.0
Release  : 24
URL      : http://pypi.debian.net/virtualenv/virtualenv-15.1.0.tar.gz
Source0  : http://pypi.debian.net/virtualenv/virtualenv-15.1.0.tar.gz
Source99 : http://pypi.debian.net/virtualenv/virtualenv-15.1.0.tar.gz.asc
Summary  : Virtual Python Environment builder
Group    : Development/Tools
License  : MIT
Requires: virtualenv-bin
Requires: virtualenv-python
BuildRequires : funcsigs-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : setuptools

%description
virtualenv
==========
A tool for creating isolated 'virtual' python environments.

%package bin
Summary: bin components for the virtualenv package.
Group: Binaries

%description bin
bin components for the virtualenv package.


%package python
Summary: python components for the virtualenv package.
Group: Default

%description python
python components for the virtualenv package.


%prep
%setup -q -n virtualenv-15.1.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489274816
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
export SOURCE_DATE_EPOCH=1489274816
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/virtualenv

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
