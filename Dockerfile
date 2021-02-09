FROM scratch
ADD AXS8shimbuild.tar.gz /
CMD ["/bin/bash"]
COPY shim-unsigned-x64.spec /builddir/build/SPECS/
COPY shim*.efi /
COPY rpmmacros /root/.rpmmacros
COPY asianuxsecureboot001.der /builddir/build/SOURCES/
COPY shim-find-debuginfo.sh /builddir/build/SOURCES/shim-find-debuginfo.sh
COPY dbx.esl *.patch /builddir/build/SOURCES/
COPY shim-15.tar.bz2 /builddir/build/SOURCES/
RUN rpmbuild -ba /builddir/build/SPECS/shim-unsigned-x64.spec --noclean --define 'dist .el8'
RUN sha256sum /builddir/build/BUILDROOT/shim*/usr/share/shim/*/*/shim*.efi
RUN sha256sum /shimx64.efi
RUN sha256sum /shimia32.efi
RUN hexdump -Cv /builddir/build/BUILDROOT/shim*/usr/share/shim/*/*/shimx64.efi > /builtx64.hex
RUN hexdump -Cv /builddir/build/BUILDROOT/shim*/usr/share/shim/*/*/shimia32.efi > /builtia32.hex
RUN hexdump -Cv /shimx64.efi > /origx64.hex
RUN hexdump -Cv /shimia32.efi > /origia32.hex
RUN diff -u /origx64.hex /builtx64.hex
RUN diff -u /origia32.hex /builtia32.hex || true
