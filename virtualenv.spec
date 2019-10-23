#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : virtualenv
Version  : 16.7.7
Release  : 77
URL      : https://files.pythonhosted.org/packages/e7/80/15d28e5a075fb02366ce97558120bb987868dab3600233ec7be032dc6d01/virtualenv-16.7.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/e7/80/15d28e5a075fb02366ce97558120bb987868dab3600233ec7be032dc6d01/virtualenv-16.7.7.tar.gz
Summary  : Virtual Python Environment builder
Group    : Development/Tools
License  : MIT
Requires: virtualenv-bin = %{version}-%{release}
Requires: virtualenv-license = %{version}-%{release}
Requires: virtualenv-python = %{version}-%{release}
Requires: virtualenv-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy-python
BuildRequires : util-linux

%description
virtualenv
==========
A tool for creating isolated 'virtual' python environments.

%package bin
Summary: bin components for the virtualenv package.
Group: Binaries
Requires: virtualenv-license = %{version}-%{release}

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
Requires: virtualenv-python3 = %{version}-%{release}

%description python
python components for the virtualenv package.


%package python3
Summary: python3 components for the virtualenv package.
Group: Default
Requires: python3-core

%description python3
python3 components for the virtualenv package.


%prep
%setup -q -n virtualenv-16.7.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571846316
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/virtualenv
cp %{_builddir}/virtualenv-16.7.7/LICENSE.txt %{buildroot}/usr/share/package-licenses/virtualenv/2e754399255de49ca03cd159799837bf3b94f1ff
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/virtualenv

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/virtualenv/2e754399255de49ca03cd159799837bf3b94f1ff

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
