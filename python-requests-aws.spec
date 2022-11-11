%global dist_raw %(%{__grep} -oP "release \\K[0-9]+\\.[0-9]+" /etc/system-release | tr -d ".")

%if 0%{?fedora} > 12 || 0%{?rhel} && 0%{?dist_raw} >= 75
%bcond_without python3
%else
%bcond_with python3
%endif

# centos 7.2 and lower versions don't have %py2_* macros, so define it manually
%if 0%{?rhel} && 0%{?dist_raw} <= 72
%{!?py2_build: %global py2_build %py_build}
%{!?py2_install: %global py2_install %py_install}
%endif

%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

%if 0%{?rhel} && 0%{?rhel} >= 8
%bcond_with python2
%else
%bcond_without python2
%endif

%define pkgname requests-aws
%global sum AWS authentication for Amazon S3 for the python requests module
%global descr AWS authentication for Amazon S3 for the python requests module

Name:           python-%{pkgname}
Version:        0.1.5
Release:        3.CROC1Test1227902%{?dist}
Summary:        %{sum}

License:        BSD licence
URL:            https://github.com/tax/python-requests-aws
Source0:        %{pkgname}-%{version}.tar.gz
BuildArch:      noarch


%description
%{descr}

%if %{with python2}
%package -n python2-%{pkgname}
Summary:        %{sum}
Requires:       python-requests
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
Provides:       python-requests-aws
Obsoletes:      python-requests-aws < 0.1.5-1%{?dist}

%description -n python2-%{pkgname}
%{descr}
%endif

%if %{with python3}
%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{sum}
%if 0%{?rhel} && 0%{?rhel} >= 8
Requires:       python3-requests
%else
Requires:       python36-requests
%endif
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pkgname}
%{descr}
%endif


%prep
%setup -q -n %{pkgname}-%{version}

sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py


%build
%if %{with python2}
%{py2_build}
%endif

%if %{with python3}
%{py3_build}
%endif


%install
[ %buildroot = "/" ] || rm -rf %buildroot

%if %{with python2}
%{py2_install}
%endif

%if %{with python3}
%{py3_install}
%endif

find %buildroot/ -name '*.egg-info' -exec rm -rf -- '{}' '+'

%if %{with python2}
%files -n python2-%{pkgname}
%defattr(-,root,root,-)
%doc LICENSE.txt README.md
%{python2_sitelib}/*
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{pkgname}
%defattr(-,root,root,-)
%doc LICENSE.txt README.md
%{python3_sitelib}/*
%endif


%changelog
* Tue Nov 1 2022 Ivan Konov <ikonov@croc.ru> - 0.1.5-3.CROC2
- Do not build py2 packages on rhel8+

* Sat Jun 29 2019 Vladislav Odintsov <odivlad@gmail.com> - 0.1.5-2
- Add support for py2/py3 build

* Wed Sep 24 2014 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.1.5-1
- Initial package
