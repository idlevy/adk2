Name:               ply_redis
Version:            3.2.1
Release:           0.1
Summary:         A test package
Group:              Test Packages
License:            GPL
URL:                 http://test.example.com
#Source0:           %{name}-%{version}.tar.gz
Source:           redis-3.2.1.tar.gz 
BuildRoot:        %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:   /bin/rm, /bin/mkdir, /bin/cp
Requires:          /bin/bash, /bin/date

 

%description

Demo package for deployment of one single file

%prerp
%setup 


%install

#make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/*
mkdir -p $RPM_BUILD_ROOT/var/tmp/redis-3.2.1/
cp -r  redis  $RPM_BUILD_ROOT/var/tmp/redis-3.2.1/
cp -r  redis.* $RPM_BUILD_ROOT/var/tmp/redis-3.2.1/



%post
cp -p  /var/tmp/redis-3.2.1/redis.conf /etc/
cp -p  /var/tmp/redis-3.2.1/redis.service /etc/systemd/system/
cp -rp  /var/tmp/redis-3.2.1/redis/ /bin/


%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,vagrant,vagrant,-)
#%doc
%attr(0755,vagrant,vagrant)/var/tmp/redis-3.2.1
%attr(0755,vagrant,vagrant)/var/tmp/redis-3.2.1/redis.service
%attr(0755,vagrant,vagrant)/var/tmp/redis-3.2.1/redis.sh
%attr(0755,vagrant,vagrant)/var/tmp/redis-3.2.1/redis/redis-benchmark
%attr(0755,vagrant,vagrant)/var/tmp/redis-3.2.1/redis/redis-check-aof
%attr(0755,vagrant,vagrant)/var/tmp/redis-3.2.1/redis/redis-check-rdb
%attr(0755,vagrant,vagrant)/var/tmp/redis-3.2.1/redis/redis-cli
%attr(0755,vagrant,vagrant)/var/tmp/redis-3.2.1/redis/redis-sentinel
%attr(0755,vagrant,vagrant)/var/tmp/redis-3.2.1/redis/redis-server
%attr(0755,vagrant,vagrant)/var/tmp/redis-3.2.1/redis.conf
%attr(0755,vagrant,vagrant)/var/tmp/redis-3.2.1/redis.service

%changelog


* Thu Jul 28 2016  ido Levy
- Creation of initial RPM
