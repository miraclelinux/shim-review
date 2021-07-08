This repo is for review of requests for signing shim.  To create a request for review:

- clone this repo
- edit the template below
- add the shim.efi to be signed
- add build logs
- add any additional binaries/certificates/SHA256 hashes that may be needed
- commit all of that
- tag it with a tag of the form "myorg-shim-arch-YYYYMMDD"
- push that to github
- file an issue at https://github.com/rhboot/shim-review/issues with a link to your branch
- approval is ready when you have accepted tag

Note that we really only have experience with using GRUB2 on Linux, so asking
us to endorse anything else for signing is going to require some convincing on
your part.

Here's the template:

-------------------------------------------------------------------------------
What organization or people are asking to have this signed:
-------------------------------------------------------------------------------
Cybertrust Japan Co., Ltd.

-------------------------------------------------------------------------------
What product or service is this for:
-------------------------------------------------------------------------------
MIRACLE LINUX 8

-------------------------------------------------------------------------------
What's the justification that this really does need to be signed for the whole world to be able to boot it:
-------------------------------------------------------------------------------
We have received request from our customer that they wants to enable SecureBoot for OEM computer without indivisual signature from hardware vendor specially.

-------------------------------------------------------------------------------
Who is the primary contact for security updates, etc.
-------------------------------------------------------------------------------
- Name: Haruki TSURUMOTO
- Position: Senior Engineer
- Email address: haruki.tsurumoto@miraclelinux.com
- PGP key, signed by the other security contacts, and preferably also with signatures that are reasonably well known in the Linux community:
https://raw.githubusercontent.com/miraclelinux/shim-review/ml8-shim-15.4-20210629/haruki_tsurumoto_D65234EEE8B6B283.pub

```
$ gpg --fingerprint D65234EEE8B6B283
pub   rsa2048 2017-06-16 [SC]
      FEA2 980F F1B1 FA08 4A8D  FD4E D652 34EE E8B6 B283
uid           [ultimate] Haruki TSURUMOTO <haruki.tsurumoto@miraclelinux.com>
sub   rsa2048 2017-06-16 [E]
```

-------------------------------------------------------------------------------
Who is the secondary contact for security updates, etc.
-------------------------------------------------------------------------------
- Name:Yasuhiro NAKAMURA
- Position: Principal Engineer
- Email address: yasuhiro.nakamura@miraclelinux.com
- PGP key, signed by the other security contacts, and preferably also with signatures that are reasonably well known in the Linux community: https://raw.githubusercontent.com/miraclelinux/shim-review/ml8-shim-15.4-20210629/Yasuhiro_NAKAMURA_18BC698751BE355A.pub

```
$ gpg --fingerprint 18BC698751BE355A
pub   rsa3072 2021-07-01 [SC]
      7006 FB03 02DA 06A6 94A1  205E 18BC 6987 51BE 355A
uid           [ultimate] Yasuhiro NAKAMURA <yasuhiro.nakamura@miraclelinux.com>
sub   rsa3072 2021-07-01 [E]
```

-------------------------------------------------------------------------------
Please create your shim binaries starting with the 15.4 shim release tar file:
https://github.com/rhboot/shim/releases/download/15.4/shim-15.4.tar.bz2

This matches https://github.com/rhboot/shim/releases/tag/15.4 and contains
the appropriate gnu-efi source.
-------------------------------------------------------------------------------
Source is starting from upstream 15.4 release,  
tarball matches with upstream release at level of sha256sum.  
https://github.com/miraclelinux/shim-review/raw/ml8-shim-15.4-20210629/shim-15.4.tar.bz2

-------------------------------------------------------------------------------
URL for a repo that contains the exact code which was built to get this binary:
-------------------------------------------------------------------------------
SRPM of shim-unsigned-x64:  
https://github.com/miraclelinux/shim-review/raw/ml8-shim-15.4-20210629/SRPMS/shim-unsigned-x64-15.4-4.el8.ML.1.src.rpm  
SRPM of grub2:  
https://github.com/miraclelinux/shim-review/raw/ml8-shim-15.4-20210629/SRPMS/grub2-2.02-99.el8.ML.1.src.rpm  


-------------------------------------------------------------------------------
What patches are being applied and why:
-------------------------------------------------------------------------------
For shim:  
0001-Fix-a-broken-file-header-on-ia32.patch  
Why:  
We are inclding same patches as upstream for shim.  
This patch had already merged for rhboot's main branch.  
https://github.com/rhboot/shim/pull/357/commits/1bea91ba72165d97c3b453cf769cb4bc5c07207a

-------------------------------------------------------------------------------
If bootloader, shim loading is, GRUB2: is CVE-2020-14372, CVE-2020-25632,
 CVE-2020-25647, CVE-2020-27749, CVE-2020-27779, CVE-2021-20225, CVE-2021-20233,
 CVE-2020-10713, CVE-2020-14308, CVE-2020-14309, CVE-2020-14310, CVE-2020-14311,
 CVE-2020-15705, and if you are shipping the shim_lock module CVE-2021-3418
------------------------------------------------------------------------------

Yes, fixed.  

-------------------------------------------------------------------------------
What exact implementation of Secureboot in GRUB2 ( if this is your bootloader ) you have ?
* Upstream GRUB2 shim_lock verifier or * Downstream RHEL/Fedora/Debian/Canonical like implementation ?
-------------------------------------------------------------------------------
Yes, it have.  
Downstream RHEL-like implementation.  

-------------------------------------------------------------------------------
If bootloader, shim loading is, GRUB2, and previous shims were trusting affected
by CVE-2020-14372, CVE-2020-25632, CVE-2020-25647, CVE-2020-27749,
  CVE-2020-27779, CVE-2021-20225, CVE-2021-20233, CVE-2020-10713,
  CVE-2020-14308, CVE-2020-14309, CVE-2020-14310, CVE-2020-14311, CVE-2020-15705,
  and if you were shipping the shim_lock module CVE-2021-3418
  ( July 2020 grub2 CVE list + March 2021 grub2 CVE list )
  grub2:
* were old shims hashes provided to Microsoft for verification
  and to be added to future DBX update ?
* Does your new chain of trust disallow booting old, affected by CVE-2020-14372,
  CVE-2020-25632, CVE-2020-25647, CVE-2020-27749,
  CVE-2020-27779, CVE-2021-20225, CVE-2021-20233, CVE-2020-10713,
  CVE-2020-14308, CVE-2020-14309, CVE-2020-14310, CVE-2020-14311, CVE-2020-15705,
  and if you were shipping the shim_lock module CVE-2021-3418
  ( July 2020 grub2 CVE list + March 2021 grub2 CVE list )
  grub2 builds ?
-------------------------------------------------------------------------------
Not applied for both questions.  


-------------------------------------------------------------------------------
If your boot chain of trust includes linux kernel, is
"efi: Restrict efivar_ssdt_load when the kernel is locked down"
upstream commit 1957a85b0032a81e6482ca4aab883643b8dae06e applied ?
Is "ACPI: configfs: Disallow loading ACPI tables when locked down"
upstream commit 75b0cea7bf307f362057cc778efe89af4c615354 applied ?
-------------------------------------------------------------------------------
These commits are included for 5.4 and later version.  
Our kernel is based on version 4.18.0.  
Strictly speaking, these fixes are not applied for this reason.  
But nearly fixes are included for our kernel from origin of RHEL.  

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
hashes please briefly describe your certificate setup. If there are allow-listed hashes
please provide exact binaries for which hashes are created via file sharing service,
available in public with anonymous access for verification
-------------------------------------------------------------------------------
Not applied,  
since we don't use vendor_db functionality at present.  

-------------------------------------------------------------------------------
If you are re-using a previously used (CA) certificate, you will need
to add the hashes of the previous GRUB2 binaries to vendor_dbx in shim
in order to prevent GRUB2 from being able to chainload those older GRUB2
binaries. If you are changing to a new (CA) certificate, this does not
apply. Please describe your strategy.
-------------------------------------------------------------------------------
Not applied.  

-------------------------------------------------------------------------------
What OS and toolchain must we use to reproduce this build?  Include where to find it, etc.  We're going to try to reproduce your build as close as possible to verify that it's really a build of the source tree you tell us it is, so these need to be fairly thorough. At the very least include the specific versions of gcc, binutils, and gnu-efi which were used, and where to find those binaries.
If the shim binaries can't be reproduced using the provided Dockerfile, please explain why that's the case and the differences would be.
-------------------------------------------------------------------------------
You can check it in docker environment.  
This environment can replay our mock build environment.  
This environment is close to RHEL 8.3.  

Please check in the following way.  
```
 $ git clone https://github.com/miraclelinux/shim-review.git
 $ cd shim-review/
 $ git checkout ml8-shim-15.4-20210629
 $ cat tarball_piece/ML8-shimbuild.tar.gz* > ML8-shimbuild.tar.gz
 $ docker build .
```

`$ podman build . ` is also OK.

FYI: We have splitted tarball to pieces(< 50MB) for the reason of GitHub's large file limit.  
https://docs.github.com/ja/github/managing-large-files/working-with-large-files/conditions-for-large-files  
```
$ split -b 48m ML8-shimbuild.tar.gz "ML8-shimbuild.tar.gz."
```

-------------------------------------------------------------------------------
Which files in this repo are the logs for your build?   This should include logs for creating the buildroots, applying patches, doing the build, creating the archives, etc.
-------------------------------------------------------------------------------
build.log is https://github.com/miraclelinux/shim-review/blob/ml8-shim-15.4-20210629/build.log  
root.log is https://github.com/miraclelinux/shim-review/blob/ml8-shim-15.4-20210629/root.log  
snapshot of rootfs is putted in: https://github.com/miraclelinux/shim-review/tree/ml8-shim-15.4-20210629/tarball_piece

-------------------------------------------------------------------------------
Add any additional information you think we may need to validate this shim
-------------------------------------------------------------------------------
Download links of unsigned binary:  
https://github.com/miraclelinux/shim-review/raw/ml8-shim-15.4-20210629/shimia32.efi  
https://github.com/miraclelinux/shim-review/raw/ml8-shim-15.4-20210629/shimx64.efi  

Checksums:  
```
$ sha256sum shimia32.efi shimx64.efi 
678c2e622dda72d348bf3e028434a11fb55df230d57d6fa74a4ad534b5191383  shimia32.efi
a3f048ea3efda6a18c40c1b79d52c6477a451d0c590d022fe3cd385ae92a1f26  shimx64.efi
```

