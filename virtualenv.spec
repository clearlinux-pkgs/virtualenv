#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : virtualenv
Version  : 20.8.0
Release  : 142
URL      : https://files.pythonhosted.org/packages/39/2f/84439468561782ed91d9f9499738fb52a84e4d65f164849e7050db7834e5/virtualenv-20.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/39/2f/84439468561782ed91d9f9499738fb52a84e4d65f164849e7050db7834e5/virtualenv-20.8.0.tar.gz
Summary  : Virtual Python Environment builder
Group    : Development/Tools
License  : MIT
Requires: virtualenv-bin = %{version}-%{release}
Requires: virtualenv-license = %{version}-%{release}
Requires: virtualenv-python = %{version}-%{release}
Requires: virtualenv-python3 = %{version}-%{release}
Requires: backports.entry_points_selectable
Requires: distlib
Requires: filelock
Requires: pathlib2
Requires: platformdirs
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : distlib
BuildRequires : filelock
BuildRequires : pathlib2
BuildRequires : platformdirs
BuildRequires : pluggy-python
BuildRequires : setuptools_scm
BuildRequires : six

%description
# virtualenv
[![PyPI](https://img.shields.io/pypi/v/virtualenv?style=flat-square)](https://pypi.org/project/virtualenv)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/virtualenv?style=flat-square)](https://pypi.org/project/virtualenv)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/virtualenv?style=flat-square)](https://pypi.org/project/virtualenv)
[![Documentation](https://readthedocs.org/projects/virtualenv/badge/?version=latest&style=flat-square)](http://virtualenv.pypa.io)
[![Discord](https://img.shields.io/discord/803025117553754132)](https://discord.gg/pypa)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/virtualenv?style=flat-square)](https://pypistats.org/packages/virtualenv)
[![PyPI - License](https://img.shields.io/pypi/l/virtualenv?style=flat-square)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/pypa/virtualenv/workflows/check/badge.svg?branch=main&event=push)](https://github.com/pypa/virtualenv/actions?query=workflow%3Acheck)
[![codecov](https://codecov.io/gh/pypa/virtualenv/branch/main/graph/badge.svg)](https://codecov.io/gh/pypa/virtualenv)
[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

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
Provides: pypi(virtualenv)
Requires: pypi(backports.entry_points_selectable)
Requires: pypi(distlib)
Requires: pypi(filelock)
Requires: pypi(platformdirs)
Requires: pypi(six)

%description python3
python3 components for the virtualenv package.


%prep
%setup -q -n virtualenv-20.8.0
cd %{_builddir}/virtualenv-20.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631811685
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/virtualenv
cp %{_builddir}/virtualenv-20.8.0/LICENSE %{buildroot}/usr/share/package-licenses/virtualenv/bcaf1877d014a17d06f0e23264c6429acf921d01
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
/usr/share/package-licenses/virtualenv/bcaf1877d014a17d06f0e23264c6429acf921d01

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
