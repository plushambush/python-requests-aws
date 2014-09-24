%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}

%define pkgname requests-aws

Name:           python-%{pkgname}
Version:        0.1.5
Release:        1%{?dist}
Summary:        AWS authentication for Amazon S3 for the python requests module

License:        BSD licence
URL:            https://github.com/tax/python-requests-aws
Source0:        %{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools

Requires:       python-requests


%description
AWS authentication for Amazon S3 for the python requests module


%prep
%setup -q -n %{pkgname}-%{version}

sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

find $RPM_BUILD_ROOT/ -name '*.egg-info' -exec rm -rf -- '{}' '+'


%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.md
%{python_sitelib}/*


%changelog
* Wed Sep 24 2014 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.1.5-1
- Initial package
