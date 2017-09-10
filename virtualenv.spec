#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6E3CBCE93372DCFA (donald@stufft.io)
#
Name     : virtualenv
Version  : 15.1.0
Release  : 27
URL      : http://pypi.debian.net/virtualenv/virtualenv-15.1.0.tar.gz
Source0  : http://pypi.debian.net/virtualenv/virtualenv-15.1.0.tar.gz
Source99 : http://pypi.debian.net/virtualenv/virtualenv-15.1.0.tar.gz.asc
Summary  : Virtual Python Environment builder
Group    : Development/Tools
License  : MIT
Requires: virtualenv-bin
Requires: virtualenv-legacypython
Requires: virtualenv-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
==========

%package bin
Summary: bin components for the virtualenv package.
Group: Binaries

%description bin
bin components for the virtualenv package.


%package legacypython
Summary: legacypython components for the virtualenv package.
Group: Default

%description legacypython
legacypython components for the virtualenv package.


%package python
Summary: python components for the virtualenv package.
Group: Default
Requires: virtualenv-legacypython

%description python
python components for the virtualenv package.


%prep
%setup -q -n virtualenv-15.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505073453
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1505073453
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/virtualenv

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
