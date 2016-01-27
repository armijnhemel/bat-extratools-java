Summary: A collection of extra Java tools for the Binary Analysis Tool
Name: bat-extratools-java
Version: 24.0
Release: 1
License: BSD, public domain
Source: %{name}-%{version}.tar.gz
Group: Development/Tools
Packager: Armijn Hemel <armijn@binaryanalysis.org>
BuildRequires: ant, java-devel, jpackage-utils
Requires: java, jpackage-utils

%description
A collection of extra Java tools for the Binary Analysis Tool.

%prep
%setup -q
%build
ant
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dedexer/bat-ddx.jar $RPM_BUILD_ROOT%{_javadir}/bat-ddx.jar
cp -p jdeserialize/bat-jdeserialize.jar $RPM_BUILD_ROOT%{_javadir}/bat-jdeserialize.jar
%files
%{_javadir}/bat-ddx.jar
%{_javadir}/bat-jdeserialize.jar
