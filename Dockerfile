FROM almalinux:9.5
RUN dnf --enablerepo crb install -y \
        binutils gcc gnu-efi gnu-efi-devel make redhat-rpm-config rpm-build yum-utils \
        wget dos2unix elfutils-libelf-devel git openssl openssl-devel pesign
COPY rpmmacros /root/.rpmmacros
RUN mkdir -p /builddir/build/{SOURCES,SPECS}
RUN wget -P /builddir/build/SOURCES https://github.com/rhboot/shim/releases/download/15.8/shim-15.8.tar.bz2
RUN cd /builddir/build/SOURCES && echo "a79f0a9b89f3681ab384865b1a46ab3f79d88b11b4ca59aa040ab03fffae80a9  shim-15.8.tar.bz2" | sha256sum -c -
COPY sbat.ml.csv /builddir/build/SOURCES/
COPY vendordb.esl /builddir/build/SOURCES/
COPY shim-find-debuginfo.sh /builddir/build/SOURCES/
COPY shim.patches /builddir/build/SOURCES/
COPY shim-unsigned-x64.spec /builddir/build/SPECS
RUN rpmbuild -bb /builddir/build/SPECS/shim-unsigned-x64.spec
COPY shimx64.efi /
RUN rpm2cpio /builddir/build/RPMS/x86_64/shim-unsigned-x64-15.8-2.el9.ML.1.x86_64.rpm | cpio -diu
RUN ls -l /*.efi ./usr/share/shim/15.8-2.el9.ML.1/*/shim*.efi
RUN hexdump -Cv ./usr/share/shim/15.8-2.el9.ML.1/x64/shimx64.efi > built-x64.hex
RUN hexdump -Cv /shimx64.efi > orig-x64.hex
RUN objdump -h /usr/share/shim/15.8-2.el9.ML.1/x64/shimx64.efi
RUN diff -u orig-x64.hex built-x64.hex
RUN pesign -h -P -i /usr/share/shim/15.8-2.el9.ML.1/x64/shimx64.efi
RUN pesign -h -P -i /shimx64.efi
RUN sha256sum /usr/share/shim/15.8-2.el9.ML.1/x64/shimx64.efi /shimx64.efi
