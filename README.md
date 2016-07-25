# adk2

install rpmbuild:
-----------------
udo yum install rpm-build -y 

create folders:
---------------
mkdir -p ~/rpmbuild/SOURCES  
 
mkdir -p ~/rpmbuild/SPECS



#for not the test one is working.
put the files under 
~/rpmbuild/SOURCE/
put spec file under ../SPECS/

run 
rpmbuild -ba test-1.0.spec 


