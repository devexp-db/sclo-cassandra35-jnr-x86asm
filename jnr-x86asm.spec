%global cluster wmeissner
%global git_commit 78eebb2
%global commit_dl g78eebb2
%global commit_rev 0

Name:           jnr-x86asm
Version:        0.1
Release:        6%{?dist}
Summary:        Pure-java port of asmjit

Group:          Development/Libraries
License:        LGPLv3
URL:            http://github.com/%{cluster}/%{name}
Source0:        %{url}/tarball/%{version}/%{cluster}-%{name}-%{version}-%{commit_rev}-%{commit_dl}.tar.gz
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
find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete

%pom_xpath_remove pom:extensions

%build
ant

%install

mkdir -p %{buildroot}%{_javadir}
cp -p dist/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -p -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -r dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE COPYING*
%{_javadir}/*
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE COPYING*
%{_javadocdir}/%{name}

%changelog
* Tue Oct 09 2012 gil cattaneo <puntogil@libero.it> - 0.1-6
- add maven pom
- adapt to current guideline

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

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
