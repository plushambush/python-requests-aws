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

%define pkgname requests-aws
%global sum AWS authentication for Amazon S3 for the python requests module
%global descr AWS authentication for Amazon S3 for the python requests module

Name:           python-%{pkgname}
Version:        0.1.5
Release:        2%{?dist}
Summary:        %{sum}

License:        BSD licence
URL:            https://github.com/tax/python-requests-aws
Source0:        %{pkgname}-%{version}.tar.gz
BuildArch:      noarch


%description
%{descr}


%package -n python2-%{pkgname}
Summary:        %{sum}
Requires:       python2-requests
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
Provides:       python-requests-aws
Obsoletes:      python-requests-aws < 0.1.5-1%{?dist}

%description -n python2-%{pkgname}
%{descr}


%if %{with python3}
%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{sum}
Requires:       python%{python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pkgname}
%{descr}
%endif


%prep
%setup -q -n %{pkgname}-%{version}

sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py


%build
%{py2_build}

%if %{with python3}
%{py3_build}
%endif


%install
[ %buildroot = "/" ] || rm -rf %buildroot

%{py2_install}

%if %{with python3}
%{py3_install}
%endif

find %buildroot/ -name '*.egg-info' -exec rm -rf -- '{}' '+'


%files -n python2-%{pkgname}
%defattr(-,root,root,-)
%doc LICENSE.txt README.md
%{python2_sitelib}/*

%if %{with python3}
%files -n python%{python3_pkgversion}-%{pkgname}
%defattr(-,root,root,-)
%doc LICENSE.txt README.md
%{python3_sitelib}/*
%endif


%changelog
* Sat Jun 29 2019 Vladislav Odintsov <odivlad@gmail.com> - 0.1.5-2
- Add support for py2/py3 build

* Wed Sep 24 2014 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.1.5-1
- Initial package
