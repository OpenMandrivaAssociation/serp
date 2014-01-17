%{?_javapackages_macros:%_javapackages_macros}
Name:          serp
Version:       1.14.2
Release:       0.6.20120406cvs.0%{?dist}
Summary:       Bytecode manipulation framework
License:       BSD
Url:           http://serp.sourceforge.net/
# cvs -d:pserver:anonymous@serp.cvs.sourceforge.net:/cvsroot/serp login
# cvs -z3 -d:pserver:anonymous@serp.cvs.sourceforge.net:/cvsroot/serp  export -r HEAD serp
# tar czf serp-1.14.2-20120406-src-cvs.tar.gz serp
Source0:       serp-1.14.2-20120406-src-cvs.tar.gz
# change 
#  org.codehaus.mojo jxr-maven-plugin in org.apache.maven.plugins maven-jxr-plugin
#  org.codehaus.mojo surefire-report-maven-plugin in org.apache.maven.plugins >maven-surefire-report-plugin
Patch0:        serp-1.13.1-pom_xml.patch

BuildRequires: java-devel

BuildRequires: maven-local
BuildRequires: maven-surefire-provider-junit4

BuildRequires: mvn(junit:junit)

BuildArch:     noarch

%description
The goal of the serp bytecode framework is to tap the full 
power of bytecode modification while lowering its associated
costs. The framework provides a set of high-level APIs for 
manipulating all aspects of bytecode, from large-scale 
structures like class member fields to the individual 
instructions that comprise the code of methods. While in 
order to perform any advanced manipulation, some understanding 
of the class file format and especially of the JVM instruction 
set is necessary, the framework makes it as easy as possible
to enter the world of bytecode development.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}
find . -name "*.class" -delete
find . -name "*.jar" -delete

%patch0 -p0
sed -i "s|pom.version|project.version|" pom.xml

%mvn_file :%{name} %{name}
%mvn_alias :%{name} %{name}:%{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt README.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.2-0.6.20120406cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 02 2013 gil cattaneo <puntogil@libero.it> 1.14.2-0.5.20120406cvs
- build with XMvn
- minor changes to adapt to current guideline

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.2-0.4.20120406cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.14.2-0.3.20120406cvs
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.2-0.2.20120406cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 06 2012 gil cattaneo <puntogil@libero.it> 1.14.2-0.1.20120406cvs
- initial rpm