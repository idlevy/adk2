Name:           redis-ply 
Version:        3.2.1
Release:        0.2
Summary:        to be added 
Group:          DEvops
License:        GPL
Source:         redis-3.2.1.tar.gz
Prefix:         PlyMedia
Packager: 	Idol
#BuildRoot:      %{_tmppath}/%{name}-root
BuildRoot:      /var

%description
bla bla bla

%prep
%setup  -c redis

%install 
mkdir -p /var/tmp/redis-new/
cp -r  redis  /var/tmp/redis-new/
cp -r  redis.* /var/tmp/redis-new/

cp -p  redis.conf /etc/
cp -p  redis.service /etc/systemd/system/
cp -rp redis/ /opt/

#%files
#/redis/redis.service
#/redis.conf

%post


	







