Make sure you have provided the following information:

 - [ ] link to your code branch cloned from rhboot/shim-review in the form user/repo@tag
 - [x] completed README.md file with the necessary information
 - [x] shim.efi to be signed
 - [x] public portion of your certificate(s) embedded in shim (the file passed to VENDOR_CERT_FILE)
 - [ ] binaries, for which hashes are added do vendor_db ( if you use vendor_db and have hashes whitelisted )
 - [x] any extra patches to shim via your own git tree or as files
 - [ ] any extra patches to grub via your own git tree or as files
 - [x] build logs


###### What organization or people are asking to have this signed:
Cybertrust Japan Co.,Ltd.  

###### What product or service is this for:
MIRACLE LINUX V8 Asianux inside  

###### What is the origin and full version number of your shim?
Upstream origin: https://github.com/rhboot/shim/releases/tag/15  
Full version is 15-9.0.3.el8  
https://github.com/miraclelinux/shim-review/blob/MLV8/master/shim-unsigned-x64.spec#L21  
66 patches are applied to tarball.  

###### What's the justification that this really does need to be signed for the whole world to be able to boot it:
Our products and customers needs secure boot.  

###### How do you manage and protect the keys used in your SHIM?
Build environment is located our private network, build system(mock) calls pesign-client.  
Private keys are accessible from only admin and build system.  

###### Do you use EV certificates as embedded certificates in the SHIM?
No.  

###### If you use new vendor_db functionality, are any hashes whitelisted, and if yes: for what binaries ?
No.  

###### Is kernel upstream commit 75b0cea7bf307f362057cc778efe89af4c615354 present in your kernel, if you boot chain includes a linux kernel ?
Yes, nearly fixes are included for our kernel.  

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

###### if SHIM is loading grub2 bootloader, is CVE CVE-2020-10713 fixed ?
Yes. it was fixed at version 15-8.  

##### Did you change your certificate strategy, so that affected by CVE CVE-2020-10713 grub2 bootloaders can not be verified ?
No.  

###### What is the origin and full version number of your bootloader (GRUB or other)?
We use GRUB2 as the bootloader, based and rebuild RHEL's 8.3 grub2, which includes secureboot support.  

###### If your SHIM launches any other components, please provide further details on what is launched
No, only GRUB2.  

###### How do the launched components prevent execution of unauthenticated code?
ditto.  

###### Does your SHIM load any loaders that support loading unsigned kernels (e.g. GRUB)?
Yes.  
In secureboot disabled machine, shim-unsigned launches kernel normally.  

###### What kernel are you using? Which patches does it includes to enforce Secure Boot?
We use Linux kernel based and rebuild RHEL's 8.3 kernel, which includes secureboot support.  

###### What changes were made since your SHIM was last signed?
None.  

###### What is the hash of your final SHIM binary?
```
$ sha256sum shim*.efi
c5668cdfba2d97f2fd4b260737a2b260e2959a0a018b361f6358c086a0cf5377  shimia32.efi
c324a476152980cc770943573fc053209edf4c954422ad1e54489601becdf201  shimx64.efi
```
