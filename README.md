This repo is for review of requests for signing shim.  To create a request for review:

- clone this repo
- edit the template below
- add the shim.efi to be signed
- add build logs
- add any additional binaries/certificates/hashes that may be needed
- commit all of that
- tag it with a tag of the form "myorg-shim-arch-YYYYMMDD"
- push that to github
- file an issue at https://github.com/rhboot/shim-review/issues with a link to your branch
- approval is ready when you have accepted tag

Note that we really only have experience with using grub2 on Linux, so asking
us to endorse anything else for signing is going to require some convincing on
your part.

Here's the template:

-------------------------------------------------------------------------------
What organization or people are asking to have this signed:
-------------------------------------------------------------------------------
Cybertrust Japan Co.,Ltd.

-------------------------------------------------------------------------------
What product or service is this for:
-------------------------------------------------------------------------------
MIRACLE LINUX V8 Asianux inside

-------------------------------------------------------------------------------
What's the justification that this really does need to be signed for the whole world to be able to boot it:
-------------------------------------------------------------------------------
Our products and customers needs secure boot.

-------------------------------------------------------------------------------
Who is the primary contact for security updates, etc.
-------------------------------------------------------------------------------
- Name: Haruki TSURUMOTO
- Position: Engineer
- Email address: haruki.tsurumoto@miraclelinux.com
- PGP key, signed by the other security contacts, and preferably also with signatures that are reasonably well known in the linux community: [haruki_tsurumoto_D65234EEE8B6B283.pub](haruki_tsurumoto_D65234EEE8B6B283.pub)

-------------------------------------------------------------------------------
Who is the secondary contact for security updates, etc.
-------------------------------------------------------------------------------
- Name: YOSHIFUJI Hideaki
- Position: Expert Engineer
- Email address: hideaki.yoshifuji@miraclelinux.com
- PGP key, signed by the other security contacts, and preferably also with signatures that are reasonably well known in the linux community: [hideaki_yoshifuji_177ABBE2344FD295.pub](hideaki_yoshifuji_177ABBE2344FD295.pub)

-------------------------------------------------------------------------------
What upstream shim tag is this starting from:
-------------------------------------------------------------------------------
 https://github.com/rhboot/shim/releases/tag/15  

-------------------------------------------------------------------------------
URL for a repo that contains the exact code which was built to get this binary:
-------------------------------------------------------------------------------
```
 https://github.com/miraclelinux/shim-review/blob/MLV8/master/shimx64.efi  
 https://github.com/miraclelinux/shim-review/blob/MLV8/master/shimia32.efi  
```

-------------------------------------------------------------------------------
What patches are being applied and why:
-------------------------------------------------------------------------------

Following patches are same as RHEL 8.3 and CentOS 8.3.  
Patches are taken from inside of SRPM.   
https://git.centos.org/rpms/shim-unsigned-x64/blob/c8/f/SOURCES  
- 0001-Make-some-things-dprint-instead-of-console_print.patch
- 0002-Makefiles-ensure-m32-gets-propogated-to-our-gcc-para.patch
- 0003-Let-MokManager-follow-a-MokTimeout-var-for-timeout-l.patch
- 0004-httpboot-return-EFI_NOT_FOUND-when-it-fails-to-find-.patch
- 0005-httpboot-print-more-messages-when-it-fails-to-set-IP.patch
- 0006-httpboot-allow-the-IPv4-gateway-to-be-empty.patch
- 0007-httpboot-show-the-error-message-for-the-ChildHandle.patch
- 0008-Fix-typo-in-debug-path-in-shim.h.patch
- 0009-MokManager-Stop-using-EFI_VARIABLE_APPEND_WRITE.patch
- 0010-shim-Extend-invalid-reloc-size-warning-message.patch
- 0011-Add-GRUB-s-PCR-Usage-to-README.tpm.patch
- 0012-Fix-the-compile-error-of-mkdir-wrong-directory.patch
- 0013-shim-Properly-generate-absolute-paths-from-relative-.patch
- 0014-shim-Prevent-shim-to-set-itself-as-a-second-stage-lo.patch
- 0015-Fix-for-Section-0-has-negative-size-error-when-loadi.patch
- 0016-Fix-apparent-typo-in-ARM-32-on-64-code.patch
- 0017-Makefile-do-not-run-git-on-clean-if-there-s-no-.git-.patch
- 0018-Make.default-use-correct-flags-to-disable-unaligned-.patch
- 0019-Cryptlib-fix-build-on-32bit-ARM.patch
- 0020-Make-sure-that-MOK-variables-always-get-mirrored.patch
- 0021-mok-fix-the-mirroring-of-RT-variables.patch
- 0022-mok-consolidate-mirroring-code-in-a-helper-instead-o.patch
- 0023-shim-only-include-shim_cert.h-in-shim.c.patch
- 0024-mok-also-mirror-the-build-cert-to-MokListRT.patch
- 0025-mok-minor-cleanups.patch
- 0026-Remove-call-to-TPM2-get_event_log.patch
- 0027-Make-EFI-variable-copying-fatal-only-on-secureboot-e.patch
- 0028-VLogError-Avoid-NULL-pointer-dereferences-in-V-Sprin.patch
- 0029-Once-again-try-even-harder-to-get-binaries-without-t.patch
- 0030-shim-Rework-pause-functions-and-add-read_counter.patch
- 0031-Hook-exit-when-shim_lock-protocol-installed.patch
- 0032-Work-around-stuff-Waddress-of-packed-member-finds.patch
- 0033-Fix-a-use-of-strlen-instead-of-Strlen.patch
- 0034-MokManager-Use-CompareMem-on-MokListNode.Type-instea.patch
- 0035-OpenSSL-always-provide-OBJ_create-with-name-strings.patch
- 0036-Use-portable-shebangs-bin-bash-usr-bin-env-bash.patch
- 0037-tpm-Fix-off-by-one-error-when-calculating-event-size.patch
- 0038-tpm-Define-EFI_VARIABLE_DATA_TREE-as-packed.patch
- 0039-MokManager-console-mode-modification-for-hi-dpi-scre.patch
- 0040-MokManager-avoid-Werror-address-of-packed-member.patch
- 0041-tpm-Don-t-log-duplicate-identical-events.patch
- 0042-Slightly-better-debugging-messages.patch
- 0043-Actually-check-for-errors-from-set_second_stage.patch
- 0044-translate_slashes-don-t-write-to-string-literals.patch
- 0045-shim-Update-EFI_LOADED_IMAGE-with-the-second-stage-l.patch
- 0046-tpm-Include-information-about-PE-COFF-images-in-the-.patch
- 0047-Fix-the-license-on-our-buildid-extractor.patch
- 0048-Update-README.tpm.patch
- 0049-Check-PxeReplyReceived-as-fallback-in-netboot.patch
- 0050-Remove-a-couple-of-incorrect-license-claims.patch
- 0051-MokManager-fix-uninitialized-value.patch
- 0052-Fix-some-volatile-usage-gcc-whines-about.patch
- 0053-MokManager-fix-a-wrong-allocation-failure-check.patch
- 0054-simple_file-fix-uninitialized-variable-unchecked-ret.patch
- 0055-Fix-a-broken-tpm-type.patch
- 0056-Make-cert.S-not-impossible-to-read.patch
- 0057-Add-support-for-vendor_db-built-in-shim-authorized-l.patch
- 0058-Handle-binaries-with-multiple-signatures.patch
- 0059-Make-openssl-accept-the-right-set-of-KU-EKUs.patch
- 0060-Improve-debug-output-some.patch
- 0061-Also-use-a-config-table-to-mirror-mok-variables.patch
- 0062-Implement-lennysz-s-suggestions-for-MokListRT.patch
- 0063-hexdump.h-fix-arithmetic-error.patch
- 0064-Fix-some-mokmanager-deletion-paths.patch
- 0065-Fix-buffer-overrun-due-DEFAULT_LOADER-length-miscalc.patch

This patch is backported from https://github.com/rhboot/shim/commit/9a2dd0a945720634b9f3608c3b3dfb99fafd4465  
- 1001-MokListRT-Fatal.patch

-------------------------------------------------------------------------------
If bootloader, shim loading is, grub2: is CVE-2020-10713 fixed ?
-------------------------------------------------------------------------------
Yes. it was fixed at version 15-8.  

-------------------------------------------------------------------------------
If bootloader, shim loading is, grub2, and previous shims were trusting affected
by CVE-2020-10713 grub2:
* were old shims hashes provided to Microsoft for verification
  and to be added to future DBX update ?
* Does your new chain of trust disallow booting old, affected by CVE-2020-10713,
  grub2 builds ?
-------------------------------------------------------------------------------
- No, our old shims were not passed shim-review ever.
- In secureboot enabling environment, old shims were disallowed to boot.

-------------------------------------------------------------------------------
If your boot chain of trust includes linux kernel, is
"efi: Restrict efivar_ssdt_load when the kernel is locked down"
upstream commit 1957a85b0032a81e6482ca4aab883643b8dae06e applied ?
Is "ACPI: configfs: Disallow loading ACPI tables when locked down"
upstream commit 75b0cea7bf307f362057cc778efe89af4c615354 applied ?
-------------------------------------------------------------------------------
Yes, nearly fixes are included for our kernel.

[drivers/firmware/efi/efi.c]
```
 244 #if IS_ENABLED(CONFIG_ACPI)
 245 #define EFIVAR_SSDT_NAME_MAX    16
 246 static char efivar_ssdt[EFIVAR_SSDT_NAME_MAX] __initdata;
 247 static int __init efivar_ssdt_setup(char *str)
 248 {
 249         int ret = kernel_is_locked_down("Modifying ACPI tables");
 250 
 251         if (ret)
 252                 return ret;
 253 
 254         if (strlen(str) < sizeof(efivar_ssdt))
 255                 memcpy(efivar_ssdt, str, strlen(str));
 256         else
 257                 pr_warn("efivar_ssdt: name too long: %s\n", str);
 258         return 0;
 259 }
```

[drivers/acpi/acpi_configfs.c]
```
 30 static ssize_t acpi_table_aml_write(struct config_item *cfg,
 31                                     const void *data, size_t size)
 32 {
 33         const struct acpi_table_header *header = data;
 34         struct acpi_table *table;
 35         int ret = kernel_is_locked_down("Modifying ACPI tables");
 36 
 37         if (ret)
 38                 return ret;
 39 
 40         table = container_of(cfg, struct acpi_table, cfg);
```

-------------------------------------------------------------------------------
If you use vendor_db functionality of providing multiple certificates and/or
hashes please briefly describe your certificate setup. If there are whitelisted hashes
please provide exact binaries for which hashes are created via file sharing service,
available in public with anonymous access for verification
-------------------------------------------------------------------------------
Not used.

-------------------------------------------------------------------------------
What OS and toolchain must we use to reproduce this build?  Include where to find it, etc.  We're going to try to reproduce your build as close as possible to verify that it's really a build of the source tree you tell us it is, so these need to be fairly thorough. At the very least include the specific versions of gcc, binutils, and gnu-efi which were used, and where to find those binaries.
If possible, provide a Dockerfile that rebuilds the shim.
-------------------------------------------------------------------------------
You can check it in docker environment.  
This environment can replay our mock build environment. This environment is close to RHEL 8.3.  

Please check in the following way.  

```
 $ git clone https://github.com/miraclelinux/shim-review.git
 $ cd shim-review/
 $ git checkout MLV8/master
 $ cat AXS8shimbuild.tar.gz.* > AXS8shimbuild.tar.gz
 $ docker build .
``` 

`$ podman build .` is also OK.  

-------------------------------------------------------------------------------
Which files in this repo are the logs for your build?   This should include logs for creating the buildroots, applying patches, doing the build, creating the archives, etc.
-------------------------------------------------------------------------------
(build.log)[https://github.com/miraclelinux/shim-review/build.log] is.


-------------------------------------------------------------------------------
Add any additional information you think we may need to validate this shim
-------------------------------------------------------------------------------
```
$ sha256sum shim*.efi
c5668cdfba2d97f2fd4b260737a2b260e2959a0a018b361f6358c086a0cf5377  shimia32.efi
c324a476152980cc770943573fc053209edf4c954422ad1e54489601becdf201  shimx64.efi
