#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : virtualenv
Version  : 15.2.0
Release  : 43
URL      : http://pypi.debian.net/virtualenv/virtualenv-15.2.0.tar.gz
Source0  : http://pypi.debian.net/virtualenv/virtualenv-15.2.0.tar.gz
Summary  : Virtual Python Environment builder
Group    : Development/Tools
License  : MIT
Requires: virtualenv-bin
Requires: virtualenv-python3
Requires: virtualenv-license
Requires: virtualenv-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy-python
BuildRequires : python3-dev
BuildRequires : setuptools

%description
==========

%package bin
Summary: bin components for the virtualenv package.
Group: Binaries
Requires: virtualenv-license

%description bin
bin components for the virtualenv package.


%package license
Summary: license components for the virtualenv package.
Group: Default

%description license
license components for the virtualenv package.


%package python
Summary: python components for the virtualenv package.
Group: Default
Requires: virtualenv-python3

%description python
python components for the virtualenv package.


%package python3
Summary: python3 components for the virtualenv package.
Group: Default
Requires: python3-core

%description python3
python3 components for the virtualenv package.


%prep
%setup -q -n virtualenv-15.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529116289
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/virtualenv
cp LICENSE.txt %{buildroot}/usr/share/doc/virtualenv/LICENSE.txt
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/virtualenv

%files license
%defattr(-,root,root,-)
/usr/share/doc/virtualenv/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
