Confirm the following are included in your repo, checking each box:

 - [x] completed README.md file with the necessary information
 - [x] shim.efi to be signed
 - [x] public portion of your certificate(s) embedded in shim (the file passed to VENDOR_CERT_FILE)
 - [x] binaries, for which hashes are added to vendor_db ( if you use vendor_db and have hashes allow-listed )
 - [x] any extra patches to shim via your own git tree or as files
 - [x] any extra patches to grub via your own git tree or as files
 - [x] build logs
 - [x] a Dockerfile to reproduce the build of the provided shim EFI binaries

*******************************************************************************
### What is the link to your tag in a repo cloned from rhboot/shim-review?
*******************************************************************************
https://github.com/miraclelinux/shim-review/tree/miraclelinux-9-x64-20260226

*******************************************************************************
### What is the SHA256 hash of your final SHIM binary?
*******************************************************************************
```
$ sha256sum shimx64.efi
761a8060037df9ce96febe90c999f9c29a92dbe0f829cf26b4620fc3e289a31d  shimx64.efi
```

```
$ pesign --hash --padding --in=shimx64.efi
43f0666914eef0360cdf2ea9995c61e9eb27a02584613fdf9398968c03e4641d shimx64.efi
```


*******************************************************************************
### What is the link to your previous shim review request (if any, otherwise N/A)?
*******************************************************************************
https://github.com/rhboot/shim-review/issues/421

*******************************************************************************
### If no security contacts have changed since verification, what is the link to your request, where they've been verified (if any, otherwise N/A)?
*******************************************************************************
https://github.com/rhboot/shim-review/issues/421
