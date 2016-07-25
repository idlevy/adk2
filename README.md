
##install rpmbuild:
-----------------
udo yum install rpm-build -y 

##create folders:
---------------
mkdir -p ~/rpmbuild/SOURCES  
 
mkdir -p ~/rpmbuild/SPECS



__for now the test one is working__
put the files under 
~/rpmbuild/SOURCE/
put spec file under ../SPECS/

run 
rpmbuild -ba test-1.0.spec 


