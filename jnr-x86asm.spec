%global commit_hash 1dead92
%global tag_hash 2a7fb9b

Name:           jnr-x86asm
Version:        1.0.2
Release:        8%{?dist}
Summary:        Pure-java port of asmjit

Group:          Development/Libraries
License:        MIT
URL:            http://github.com/jnr/%{name}/
Source0:        https://github.com/jnr/%{name}/tarball/%{version}/jnr-%{name}-%{version}-0-g%{commit_hash}.tar.gz
Source1:        MANIFEST.MF
Patch0:         add-manifest.patch
BuildArch:      noarch

BuildRequires:  java-devel
BuildRequires:  maven-local

%description
Pure-java port of asmjit (http://code.google.com/p/asmjit/)

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n jnr-%{name}-%{tag_hash}
%patch0
cp %{SOURCE1} .
find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Jun 22 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-8
- Add OSGi MANIFEST.MF.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Alexander Kurtakov <akurtako@redhat.com> 1.0.2-6
- Migrate to install with xmvn.

* Mon Jun 16 2014 Mat Booth <mat.booth@redhat.com> - 1.0.2-5
- Fix FTBFS.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.2-3
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 05 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.2-1
- Updated to version 1.0.2.
- Switch from ant to maven.

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
