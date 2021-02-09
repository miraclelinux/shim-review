%global pesign_vre 0.106-1
%global gnuefi_vre 1:3.0.5-6
%global openssl_vre 1.0.2j

%global debug_package %{nil}
%global __debug_package 1
%global _binaries_in_noarch_packages_terminate_build 0
%global __debug_install_post %{SOURCE100} x64 ia32
%undefine _debuginfo_subpackages

%global efidir %(eval echo $(grep ^ID= /etc/os-release | sed -e 's/^ID=//' -e 's/rhel/redhat/'))
%global shimrootdir %{_datadir}/shim/
%global shimversiondir %{shimrootdir}/%{version}-%{release}
%global efiarch x64
%global shimdir %{shimversiondir}/%{efiarch}
%global efialtarch ia32
%global shimaltdir %{shimversiondir}/%{efialtarch}

Name:		shim-unsigned-%{efiarch}
Version:	15
Release:	9.0.3.el8
Summary:	First-stage UEFI bootloader
ExclusiveArch:	x86_64
License:	BSD
URL:		https://github.com/rhboot/shim
Source0:	https://github.com/rhboot/shim/releases/download/%{version}/shim-%{version}.tar.bz2
Source1:	asianuxsecureboot001.der
# currently here's what's in our dbx:
# nothing.
Source2:	dbx.esl

Source100:	shim-find-debuginfo.sh

Patch0001: 0001-Make-some-things-dprint-instead-of-console_print.patch
Patch0002: 0002-Makefiles-ensure-m32-gets-propogated-to-our-gcc-para.patch
Patch0003: 0003-Let-MokManager-follow-a-MokTimeout-var-for-timeout-l.patch
Patch0004: 0004-httpboot-return-EFI_NOT_FOUND-when-it-fails-to-find-.patch
Patch0005: 0005-httpboot-print-more-messages-when-it-fails-to-set-IP.patch
Patch0006: 0006-httpboot-allow-the-IPv4-gateway-to-be-empty.patch
Patch0007: 0007-httpboot-show-the-error-message-for-the-ChildHandle.patch
Patch0008: 0008-Fix-typo-in-debug-path-in-shim.h.patch
Patch0009: 0009-MokManager-Stop-using-EFI_VARIABLE_APPEND_WRITE.patch
Patch0010: 0010-shim-Extend-invalid-reloc-size-warning-message.patch
Patch0011: 0011-Add-GRUB-s-PCR-Usage-to-README.tpm.patch
Patch0012: 0012-Fix-the-compile-error-of-mkdir-wrong-directory.patch
Patch0013: 0013-shim-Properly-generate-absolute-paths-from-relative-.patch
Patch0014: 0014-shim-Prevent-shim-to-set-itself-as-a-second-stage-lo.patch
Patch0015: 0015-Fix-for-Section-0-has-negative-size-error-when-loadi.patch
Patch0016: 0016-Fix-apparent-typo-in-ARM-32-on-64-code.patch
Patch0017: 0017-Makefile-do-not-run-git-on-clean-if-there-s-no-.git-.patch
Patch0018: 0018-Make.default-use-correct-flags-to-disable-unaligned-.patch
Patch0019: 0019-Cryptlib-fix-build-on-32bit-ARM.patch
Patch0020: 0020-Make-sure-that-MOK-variables-always-get-mirrored.patch
Patch0021: 0021-mok-fix-the-mirroring-of-RT-variables.patch
Patch0022: 0022-mok-consolidate-mirroring-code-in-a-helper-instead-o.patch
Patch0023: 0023-shim-only-include-shim_cert.h-in-shim.c.patch
Patch0024: 0024-mok-also-mirror-the-build-cert-to-MokListRT.patch
Patch0025: 0025-mok-minor-cleanups.patch
Patch0026: 0026-Remove-call-to-TPM2-get_event_log.patch
Patch0027: 0027-Make-EFI-variable-copying-fatal-only-on-secureboot-e.patch
Patch0028: 0028-VLogError-Avoid-NULL-pointer-dereferences-in-V-Sprin.patch
Patch0029: 0029-Once-again-try-even-harder-to-get-binaries-without-t.patch
Patch0030: 0030-shim-Rework-pause-functions-and-add-read_counter.patch
Patch0031: 0031-Hook-exit-when-shim_lock-protocol-installed.patch
Patch0032: 0032-Work-around-stuff-Waddress-of-packed-member-finds.patch
Patch0033: 0033-Fix-a-use-of-strlen-instead-of-Strlen.patch
Patch0034: 0034-MokManager-Use-CompareMem-on-MokListNode.Type-instea.patch
Patch0035: 0035-OpenSSL-always-provide-OBJ_create-with-name-strings.patch
Patch0036: 0036-Use-portable-shebangs-bin-bash-usr-bin-env-bash.patch
Patch0037: 0037-tpm-Fix-off-by-one-error-when-calculating-event-size.patch
Patch0038: 0038-tpm-Define-EFI_VARIABLE_DATA_TREE-as-packed.patch
Patch0039: 0039-MokManager-console-mode-modification-for-hi-dpi-scre.patch
Patch0040: 0040-MokManager-avoid-Werror-address-of-packed-member.patch
Patch0041: 0041-tpm-Don-t-log-duplicate-identical-events.patch
Patch0042: 0042-Slightly-better-debugging-messages.patch
Patch0043: 0043-Actually-check-for-errors-from-set_second_stage.patch
Patch0044: 0044-translate_slashes-don-t-write-to-string-literals.patch
Patch0045: 0045-shim-Update-EFI_LOADED_IMAGE-with-the-second-stage-l.patch
Patch0046: 0046-tpm-Include-information-about-PE-COFF-images-in-the-.patch
Patch0047: 0047-Fix-the-license-on-our-buildid-extractor.patch
Patch0048: 0048-Update-README.tpm.patch
Patch0049: 0049-Check-PxeReplyReceived-as-fallback-in-netboot.patch
Patch0050: 0050-Remove-a-couple-of-incorrect-license-claims.patch
Patch0051: 0051-MokManager-fix-uninitialized-value.patch
Patch0052: 0052-Fix-some-volatile-usage-gcc-whines-about.patch
Patch0053: 0053-MokManager-fix-a-wrong-allocation-failure-check.patch
Patch0054: 0054-simple_file-fix-uninitialized-variable-unchecked-ret.patch
Patch0055: 0055-Fix-a-broken-tpm-type.patch
Patch0056: 0056-Make-cert.S-not-impossible-to-read.patch
Patch0057: 0057-Add-support-for-vendor_db-built-in-shim-authorized-l.patch
Patch0058: 0058-Handle-binaries-with-multiple-signatures.patch
Patch0059: 0059-Make-openssl-accept-the-right-set-of-KU-EKUs.patch
Patch0060: 0060-Improve-debug-output-some.patch
Patch0061: 0061-Also-use-a-config-table-to-mirror-mok-variables.patch
Patch0062: 0062-Implement-lennysz-s-suggestions-for-MokListRT.patch
Patch0063: 0063-hexdump.h-fix-arithmetic-error.patch
Patch0064: 0064-Fix-some-mokmanager-deletion-paths.patch
Patch0065: 0065-Fix-buffer-overrun-due-DEFAULT_LOADER-length-miscalc.patch
Patch1001: 1001-MokListRT-Fatal.patch

BuildRequires:	elfutils-libelf-devel
BuildRequires:	git openssl-devel openssl
BuildRequires:	pesign >= %{pesign_vre}
BuildRequires:	gnu-efi >= %{gnuefi_vre}
BuildRequires:	gnu-efi-devel >= %{gnuefi_vre}

# Shim uses OpenSSL, but cannot use the system copy as the UEFI ABI is not
# compatible with SysV (there's no red zone under UEFI) and there isn't a
# POSIX-style C library.
# BuildRequires:	OpenSSL
Provides:	bundled(openssl) = %{openssl_vre}

%global desc \
Initial UEFI bootloader that handles chaining to a trusted full \
bootloader under secure boot environments.
%global debug_desc \
This package provides debug information for package %{expand:%%{name}} \
Debug information is useful when developing applications that \
use this package or when debugging this package.

%description
%desc

%package -n shim-unsigned-%{efialtarch}
Summary:	First-stage UEFI bootloader (unsigned data)
Provides:	bundled(openssl) = %{openssl_vre}

%description -n shim-unsigned-%{efialtarch}
%desc

%package debuginfo
Summary:	Debug information for shim-unsigned-%{efiarch}
Requires:	%{name}-debugsource = %{version}-%{release}
Group:		Development/Debug
AutoReqProv:	0
BuildArch:	noarch

%description debuginfo
%debug_desc

%package -n shim-unsigned-%{efialtarch}-debuginfo
Summary:	Debug information for shim-unsigned-%{efialtarch}
Group:		Development/Debug
Requires:	%{name}-debugsource = %{version}-%{release}
AutoReqProv:	0
BuildArch:	noarch

%description -n shim-unsigned-%{efialtarch}-debuginfo
%debug_desc

%package debugsource
Summary:	Debug Source for shim-unsigned
Group:		Development/Debug
AutoReqProv:	0
BuildArch:	noarch

%description debugsource
%debug_desc

%prep
%autosetup -S git -n shim-%{version}
git config --unset user.email
git config --unset user.name
mkdir build-%{efiarch}
mkdir build-%{efialtarch}

%build
COMMITID=$(cat commit)
MAKEFLAGS="TOPDIR=.. -f ../Makefile COMMITID=${COMMITID} "
MAKEFLAGS+="EFIDIR=%{efidir} PKGNAME=shim RELEASE=%{release} "
MAKEFLAGS+="ENABLE_HTTPBOOT=true ENABLE_SHIM_HASH=true "
MAKEFLAGS+="%{_smp_mflags}"
if [ -s "%{SOURCE1}" ]; then
	MAKEFLAGS="$MAKEFLAGS VENDOR_CERT_FILE=%{SOURCE1}"
fi
if [ -s "%{SOURCE2}" ]; then
	MAKEFLAGS="$MAKEFLAGS VENDOR_DBX_FILE=%{SOURCE2}"
fi

cd build-%{efiarch}
make ${MAKEFLAGS} DEFAULT_LOADER='\\\\grub%{efiarch}.efi' all
cd ..

cd build-%{efialtarch}
setarch linux32 make ${MAKEFLAGS} ARCH=%{efialtarch} DEFAULT_LOADER='\\\\grub%{efialtarch}.efi' all
cd ..

%install
COMMITID=$(cat commit)
MAKEFLAGS="TOPDIR=.. -f ../Makefile COMMITID=${COMMITID} "
MAKEFLAGS+="EFIDIR=%{efidir} PKGNAME=shim RELEASE=%{release} "
MAKEFLAGS+="ENABLE_HTTPBOOT=true ENABLE_SHIM_HASH=true "
if [ -s "%{SOURCE1}" ]; then
	MAKEFLAGS="$MAKEFLAGS VENDOR_CERT_FILE=%{SOURCE1}"
fi
if [ -s "%{SOURCE2}" ]; then
	MAKEFLAGS="$MAKEFLAGS VENDOR_DBX_FILE=%{SOURCE2}"
fi

cd build-%{efiarch}
make ${MAKEFLAGS} \
	DEFAULT_LOADER='\\\\grub%{efiarch}.efi' \
	DESTDIR=${RPM_BUILD_ROOT} \
	install-as-data install-debuginfo install-debugsource
cd ..

cd build-%{efialtarch}
setarch linux32 make ${MAKEFLAGS} ARCH=%{efialtarch} \
	DEFAULT_LOADER='\\\\grub%{efialtarch}.efi' \
	DESTDIR=${RPM_BUILD_ROOT} \
	install-as-data install-debuginfo install-debugsource
cd ..

%files
%license COPYRIGHT
%dir %{shimrootdir}
%dir %{shimversiondir}
%dir %{shimdir}
%{shimdir}/*.efi
%{shimdir}/*.hash

%files -n shim-unsigned-%{efialtarch}
%license COPYRIGHT
%dir %{shimrootdir}
%dir %{shimversiondir}
%dir %{shimaltdir}
%{shimaltdir}/*.efi
%{shimaltdir}/*.hash

%files debuginfo -f build-%{efiarch}/debugfiles.list

%files -n shim-unsigned-%{efialtarch}-debuginfo -f build-%{efialtarch}/debugfiles.list

%files debugsource -f build-%{efiarch}/debugsource.list

%changelog
* Fri Feb 05 2021 Haruki TSURUMOTO <haruki.tsurumoto@miraclelinux.com> - 15-9.0.3
- Remove '-B' option from setarch because it occurs operation error in container build
- Fix bogus date previous changelog

* Thu Feb 04 2021 Haruki TSURUMOTO <haruki.tsurumoto@miraclelinux.com> - 15-9.0.2
- One more rebuild for shim-review

* Wed Jan 27 2021 Haruki TSURUMOTO <haruki.tsurumoto@miraclelinux.com> - 15-9.0.1
- Apply debranding changes

* Thu Sep 17 2020 Peter Jones <pjones@redhat.com> - 15-9.el8
- Fix an incorrect allocation size.
  Related: rhbz#1877253

* Thu Jul 30 2020 Peter Jones <pjones@redhat.com> - 15-8
- Fix a load-address-dependent forever loop.
  Resolves: rhbz#1861977
  Related: CVE-2020-10713
  Related: CVE-2020-14308
  Related: CVE-2020-14309
  Related: CVE-2020-14310
  Related: CVE-2020-14311
  Related: CVE-2020-15705
  Related: CVE-2020-15706
  Related: CVE-2020-15707

* Sat Jul 25 2020 Peter Jones <pjones@redhat.com> - 15-7
- Implement Lenny's workaround
  Related: CVE-2020-10713
  Related: CVE-2020-14308
  Related: CVE-2020-14309
  Related: CVE-2020-14310
  Related: CVE-2020-14311

* Fri Jul 24 2020 Peter Jones <pjones@redhat.com> - 15-5
- Once more with the MokListRT config table patch added.
  Related: CVE-2020-10713
  Related: CVE-2020-14308
  Related: CVE-2020-14309
  Related: CVE-2020-14310
  Related: CVE-2020-14311

* Thu Jul 23 2020 Peter Jones <pjones@redhat.com> - 15-4
- Rebuild for bug fixes and new signing keys
  Related: CVE-2020-10713
  Related: CVE-2020-14308
  Related: CVE-2020-14309
  Related: CVE-2020-14310
  Related: CVE-2020-14311

* Wed Jun 05 2019 Javier Martinez Canillas <javierm@redhat.com> - 15-3
- Make EFI variable copying fatal only on secureboot enabled systems
  Resolves: rhbz#1715878
- Fix booting shim from an EFI shell using a relative path
  Resolves: rhbz#1717064

* Tue Feb 12 2019 Peter Jones <pjones@redhat.com> - 15-2
- Fix MoK mirroring issue which breaks kdump without intervention
  Related: rhbz#1668966

* Fri Jul 20 2018 Peter Jones <pjones@redhat.com> - 15-1
- Update to shim 15

* Tue Sep 19 2017 Peter Jones <pjones@redhat.com> - 13-3
- Actually update to the *real* 13 final.
  Related: rhbz#1489604

* Thu Aug 31 2017 Peter Jones <pjones@redhat.com> - 13-2
- Actually update to 13 final.

* Fri Aug 18 2017 Peter Jones <pjones@redhat.com> - 13-1
- Make a new shim-unsigned-x64 package like the shim-unsigned-aarch64 one.
- This will (eventually) supersede what's in the "shim" package so we can
  make "shim" hold the signed one, which will confuse fewer people.
