FROM almalinux:9.6-20250909
RUN dnf --enablerepo crb install -y \
        binutils gcc gnu-efi gnu-efi-devel make redhat-rpm-config rpm-build yum-utils \
        wget dos2unix elfutils-libelf-devel git openssl openssl-devel pesign
COPY rpmmacros /root/.rpmmacros
RUN mkdir -p /builddir/build/{SPECS,SOURCES}
RUN wget -P /builddir/build/SOURCES/ https://github.com/rhboot/shim/releases/download/16.1/shim-16.1.tar.bz2
COPY shim-unsigned-x64.spec /builddir/build/SPECS/
COPY shim.patches shim-find-debuginfo.sh /builddir/build/SOURCES/
COPY sbat.ml.csv /builddir/build/SOURCES/
COPY vendordb.esl /builddir/build/SOURCES/
RUN rpmbuild -bb /builddir/build/SPECS/shim-unsigned-x64.spec
COPY shimx64.efi /
RUN rpm2cpio /builddir/build/RPMS/x86_64/shim-unsigned-x64-16.1-1.el9.ML.1.x86_64.rpm | cpio -diu
RUN ls -l /*.efi ./usr/share/shim/16.1-1.el9.ML.1/*/shim*.efi
RUN hexdump -Cv ./usr/share/shim/16.1-1.el9.ML.1/x64/shimx64.efi > built-x64.hex
RUN hexdump -Cv /shimx64.efi > orig-x64.hex
RUN objdump -h /usr/share/shim/16.1-1.el9.ML.1/x64/shimx64.efi
RUN diff -u orig-x64.hex built-x64.hex
RUN pesign -h -P -i /usr/share/shim/16.1-1.el9.ML.1/x64/shimx64.efi
RUN pesign -h -P -i /shimx64.efi
RUN sha256sum /usr/share/shim/16.1-1.el9.ML.1/x64/shimx64.efi /shimx64.efi
