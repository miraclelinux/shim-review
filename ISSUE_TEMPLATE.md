Make sure you have provided the following information:

 - [v] link to your code branch cloned from rhboot/shim-review in the form user/repo@tag
 - [ ] completed README.md file with the necessary information
 - [ ] shim.efi to be signed
 - [v] public portion of your certificate(s) embedded in shim (the file passed to VENDOR_CERT_FILE)
 - [ ] binaries, for which hashes are added do vendor_db ( if you use vendor_db and have hashes allow-listed )
 - [v] any extra patches to shim via your own git tree or as files
 - [ ] any extra patches to grub via your own git tree or as files
 - [v] build logs
 - [v] a Dockerfile to reproduce the build of the provided shim EFI binaries

Link to our code branch for review: miraclelinux/shim-review@ml8-shim-15.4-20210629

###### What organization or people are asking to have this signed:
Cybertrust Japan Co., Ltd.  

###### What product or service is this for:
MIRACLE LINUX 8  

###### Please create your shim binaries starting with the 15.4 shim release tar file:
###### https://github.com/rhboot/shim/releases/download/15.4/shim-15.4.tar.bz2
###### This matches https://github.com/rhboot/shim/releases/tag/15.4 and contains
###### the appropriate gnu-efi source.
###### Please confirm this as the origin your shim.
Source is starting from upstream 15.4 release, tarball matches with upstream release at level of sha256sum.  
https://github.com/miraclelinux/shim-review/raw/ml8-shim-15.4-20210629/shim-15.4.tar.bz2

###### What's the justification that this really does need to be signed for the whole world to be able to boot it:
We have received request from our customer that they wants to enable SecureBoot for OEM computer without indivisual signature from hardware vendor specially.  

###### How do you manage and protect the keys used in your SHIM?
Our private key is stored in HSM(Yubikey), this will be only available while speicific package build.(e.g. shim, grub2, kernel, fwupd)  

###### Do you use EV certificates as embedded certificates in the SHIM?
Yes.  

###### If you use new vendor_db functionality, are any hashes allow-listed, and if yes: for what binaries ?
Not applied.  
We don't use vendor_db functionality at present.  

###### Is kernel upstream commit 75b0cea7bf307f362057cc778efe89af4c615354 present in your kernel, if you boot chain includes a Linux kernel ?
This commits(75b0cea7bf307f362057cc778efe89af4c615354) is included for 5.8 version.  
Our kernel is based on linux kernel version 4.18.0.  
Strictly speaking, `75b0cea7bf307f362057cc778efe89af4c615354` is not applied for this reason.  
But nearly fixes are included for our kernel from origin of RHEL.  

###### if SHIM is loading GRUB2 bootloader, are CVEs CVE-2020-14372,
###### CVE-2020-25632, CVE-2020-25647, CVE-2020-27749, CVE-2020-27779,
###### CVE-2021-20225, CVE-2021-20233, CVE-2020-10713, CVE-2020-14308,
###### CVE-2020-14309, CVE-2020-14310, CVE-2020-14311, CVE-2020-15705,
###### ( July 2020 grub2 CVE list + March 2021 grub2 CVE list )
###### and if you are shipping the shim_lock module CVE-2021-3418
###### fixed ?

Yes, these grub2 CVEs were fixed.  


###### "Please specifically confirm that you add a vendor specific SBAT entry for SBAT header in each binary that supports SBAT metadata
###### ( grub2, fwupd, fwupdate, shim + all child shim binaries )" to shim review doc ?
###### Please provide exact SBAT entries for all SBAT binaries you are booting or planning to boot directly through shim

We are planning below SBAT entries.  
For shim:  
```
shim.ML,1,Cybertrust Japan,shim,15.4-4,ml-packager@miraclelinux.com
```

For grub2:  
```
sbat,1,SBAT Version,sbat,1,https://github.com/rhboot/shim/blob/main/SBAT.md
grub,1,Free Software Foundation,grub,2.02,https://www.gnu.org/software/grub/
grub.ML8,1,Cybertrust Japan,grub2,2.02-99.el8.ML.1,mail:ml-packager@miraclelinux.com
```


##### Were your old SHIM hashes provided to Microsoft ?
No, we haven't.  

##### Did you change your certificate strategy, so that affected by CVE-2020-14372, CVE-2020-25632, CVE-2020-25647, CVE-2020-27749,
##### CVE-2020-27779, CVE-2021-20225, CVE-2021-20233, CVE-2020-10713,
##### CVE-2020-14308, CVE-2020-14309, CVE-2020-14310, CVE-2020-14311, CVE-2020-15705 ( July 2020 grub2 CVE list + March 2021 grub2 CVE list )
##### grub2 bootloaders can not be verified ?

Not applied.  
Our previous submission had closed, so we have no old grub2 binary for SecureBoot.  

##### What exact implementation of Secureboot in grub2 ( if this is your bootloader ) you have ?
##### * Upstream grub2 shim_lock verifier or * Downstream RHEL/Fedora/Debian/Canonical like implementation ?
RHEL-like implementation, we are downstream.  

###### What is the origin and full version number of your bootloader (GRUB or other)?
GRUB2's upstream version is `2.02`  
https://git.savannah.gnu.org/gitweb/?p=grub.git;a=tag;h=refs/tags/grub-2.02
Full version number will `2.02-99.0.1.el8.ML.1`.  
This is derived from RHEL with our certfications and SBAT CSV.  

###### If your SHIM launches any other components, please provide further details on what is launched
No, only linux kernel.  

###### If your GRUB2 launches any other binaries that are not Linux kernel in SecureBoot mode,
###### please provide further details on what is launched and how it enforces Secureboot lockdown
Not applied.  

###### If you are re-using a previously used (CA) certificate, you
###### will need to add the hashes of the previous GRUB2 binaries
###### exposed to the CVEs to vendor_dbx in shim in order to prevent
###### GRUB2 from being able to chainload those older GRUB2 binaries. If
###### you are changing to a new (CA) certificate, this does not
###### apply. Please describe your strategy.
Not re-using, we have re-newed certificate in this year March.  

###### How do the launched components prevent execution of unauthenticated code?
By SecureBoot ways.  
Shim, Grub2, Kernel will prevent unauthenticated code in SecureBoot enabled environment.  

###### Does your SHIM load any loaders that support loading unsigned kernels (e.g. GRUB)?
No.  

###### What kernel are you using? Which patches does it includes to enforce Secure Boot?
Our kernel is derived from RHEL.  

###### What changes were made since your SHIM was last signed?
Our previous submission had closed semi-automatic for BootHole vulnerability.  
Therefore, we have no last signed SHIM.  

###### What is the SHA256 hash of your final SHIM binary?
```
$ sha256sum shimia32.efi shimx64.efi
416f59378de5bc6f01ecbb992b4efe23b305711881f6bed9acc668656ee00128  shimia32.efi
7cbecc62764694c1ca279805ebd611b356a481e521561d97a6311aadb839d154  shimx64.efi
```
