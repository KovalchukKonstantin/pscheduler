#
# RPM Spec for Python Module
#

%define short	pyjq
Name:		python-%{short}
Version:	2.1.0
Release:	1%{?dist}
Summary:	Python bindings to JQ
BuildArch:	%(uname -m)
License:	BSD 2-Clause
Group:		Development/Libraries

Provides:	%{name} = %{version}-%{release}
Prefix:		%{_prefix}

Vendor:		OMOTO Kenji
URL:		https://github.com/doloopwhile/pyjq

Source:		%{short}-%{version}.tar.gz
Patch0:		%{name}-%{version}-00-nodownloads.patch
Patch1:		%{name}-%{version}-01-librarypath.patch
Patch2:		%{name}-%{version}-02-exception.patch

Requires:       python
Requires:       jq >= 1.5
Requires:       oniguruma >= 5.9

BuildRequires:  python
BuildRequires:  python-setuptools
BuildRequires:  Cython >= 0.19
BuildRequires:  jq-devel >= 1.5
BuildRequires:  oniguruma-devel >= 5.9

%description
Python bindings to JQ



# Don't do automagic post-build things.
%global              __os_install_post %{nil}


%prep
%setup -q -n %{short}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1


%build

#rpmbuild/BUILD/pyjq-2.1.0/MEMO.txt:We must run ``cython _pyjq.pyx`` before to run ``python setup.py xxx``.
#rpmbuild/BUILD/pyjq-2.1.0/MEMO.txt:Of course, ``Cython.Build.cythonize`` enable to automatically compile .pyx to .c

cythonize _pyjq.pyx
python setup.py build


%install
python setup.py install --root=$RPM_BUILD_ROOT -O1  --record=INSTALLED_FILES


%clean
rm -rf $RPM_BUILD_ROOT


%files -f INSTALLED_FILES
%defattr(-,root,root)
