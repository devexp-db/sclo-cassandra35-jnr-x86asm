%global cluster wmeissner
%global git_commit 78eebb2
%global commit_dl g78eebb2
%global commit_rev 0

Name:           jnr-x86asm
Version:        0.1
Release:        4%{?dist}
Summary:        Pure-java port of asmjit

Group:          Development/Libraries
License:        LGPLv3
URL:            http://github.com/%{cluster}/%{name}
Source0:        %{url}/tarball/%{version}/%{cluster}-%{name}-%{version}-%{commit_rev}-%{commit_dl}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  ant-nodeps
BuildRequires:  java-devel >= 1:1.6.0
BuildRequires:  jpackage-utils
Requires:       java >= 1:1.6.0
Requires:       jpackage-utils

%description
Pure-java port of asmjit (http://code.google.com/p/asmjit/)

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{cluster}-%{name}-%{git_commit}
find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
ant

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_javadir}
cp -p dist/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -p -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -r dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE COPYING*
%{_javadir}/*

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}-%{version}

%changelog
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 24 2010 Mohammed Morsi <mmorsi@redhat.com> - 0.1-2
- fixed macros for consistency
- fixed Source0 url
- corrected license, now LGPLv3
- require jpackage-utils in javadocs package

* Mon Feb 01 2010 Mohammed Morsi <mmorsi@redhat.com> - 0.1-1
- Initial package (needed for jaffl, needed for jruby)
