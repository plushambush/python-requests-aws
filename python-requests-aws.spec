%global dist_raw %(%{__grep} -oP "release \\K[0-9]+\\.[0-9]+" /etc/system-release | tr -d ".")

%if 0%{?el8}
%global el_python3_pkgversion 3
%else
%global el_python3_pkgversion 36
%endif

%define pkgname requests-aws
%global sum AWS authentication for Amazon S3 for the python requests module
%global descr AWS authentication for Amazon S3 for the python requests module

Name:           python-%{pkgname}
Version:        0.1.5
Release:        3.CROC2%{?dist}
Summary:        %{sum}

License:        BSD licence
URL:            https://github.com/tax/python-requests-aws
Source0:        %{pkgname}-%{version}.tar.gz
BuildArch:      noarch

%description
%{descr}

%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{sum}
Requires:       python%{el_python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pkgname}
%{descr}

%prep
%setup -q -n %{pkgname}-%{version}

sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

%build
%{py3_build}

%install
[ %buildroot = "/" ] || rm -rf %buildroot

%{py3_install}

find %buildroot/ -name '*.egg-info' -exec rm -rf -- '{}' '+'

%files -n python%{python3_pkgversion}-%{pkgname}
%defattr(-,root,root,-)
%doc LICENSE.txt README.md
%{python3_sitelib}/*

%changelog
* Mon Jan 16 2023 Ivan Konov <ikonov@croc.ru> - 0.1.5-3.CROC2
- Do not build py2 packages on rhel8+
- Remove py2 support

* Sat Jun 29 2019 Vladislav Odintsov <odivlad@gmail.com> - 0.1.5-2
- Add support for py2/py3 build

* Wed Sep 24 2014 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.1.5-1
- Initial package
