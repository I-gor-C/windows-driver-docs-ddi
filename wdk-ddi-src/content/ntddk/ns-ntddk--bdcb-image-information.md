---
UID: NS.ntddk._BDCB_IMAGE_INFORMATION
title: BDCB_IMAGE_INFORMATION
author: windows-driver-content
description: The BDCB_IMAGE_INFORMATION structure describes information about a boot-start driver that is about to be initialized, provided by Windows to a boot-start driver's BOOT_DRIVER_CALLBACK_FUNCTION routine.
old-location: kernel\bdcb_image_information.htm
old-project: kernel
ms.assetid: 9D0A4D67-3284-4BCC-AC81-F0BCCC2DB9B7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BDCB_IMAGE_INFORMATION, BDCB_IMAGE_INFORMATION, *PBDCB_IMAGE_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDCB_IMAGE_INFORMATION
req.alt-loc: ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# BDCB_IMAGE_INFORMATION structure



## -description
<p>The <b>BDCB_IMAGE_INFORMATION</b> structure describes information about a boot-start driver that is about to 
    be initialized, provided by Windows to a boot-start driver's 
    <a href="..\ntddk\nf-ntddk-ioregisterbootdrivercallback.md">BOOT_DRIVER_CALLBACK_FUNCTION</a> routine.</p>


## -syntax

````
typedef struct _BDCB_IMAGE_INFORMATION {
  BDCB_CLASSIFICATION Classification;
  ULONG               ImageFlags;
  UNICODE_STRING      ImageName;
  UNICODE_STRING      RegistryPath;
  UNICODE_STRING      CertificatePublisher;
  UNICODE_STRING      CertificateIssuer;
  PVOID               ImageHash;
  PVOID               CertificateThumbprint;
  ULONG               ImageHashAlgorithm;
  ULONG               ThumbprintHashAlgorithm;
  ULONG               ImageHashLength;
  ULONG               CertificateThumbprintLength;
} BDCB_IMAGE_INFORMATION, *PBDCB_IMAGE_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>Classification</b>

<dd>
<p>The classification of the boot start image.</p>
</dd>

### -field <b>ImageFlags</b>

<dd>
<p>Bit flags that describe the image. The following values are defined.
      </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>Bit 0</p>
</td>
<td>
<p>The boot start image is a dependent DLL.</p>
</td>
</tr>
<tr>
<td>
<p>Bit 1</p>
</td>
<td>
<p>The boot start image failed code integrity but load was allowed because of boot policy (code integrity not required on the platform, or code integrity disabled because of boot setting,  debugging, or both).</p>
</td>
</tr>
<tr>
<td>
<p>Bits 2-31</p>
</td>
<td>
<p>Do not use. Reserved.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ImageName</b>

<dd>
<p>The name of the boot-start driver's binary image.</p>
</dd>

### -field <b>RegistryPath</b>

<dd>
<p>The path in the registry where the boot-start driver is registered.</p>
</dd>

### -field <b>CertificatePublisher</b>

<dd>
<p>The publisher of the image's certificate. If the image is not signed, the string is empty ("").</p>
</dd>

### -field <b>CertificateIssuer</b>

<dd>
<p>The issuer of the image's certificate. If the image is not signed, the string is empty ("").</p>
</dd>

### -field <b>ImageHash</b>

<dd>
<p>The Authenticode hash of the image, which can be calculated by  using SignTool.exe (Sign Tool). </p>
</dd>

### -field <b>CertificateThumbprint</b>

<dd>
<p>The hash of the certificate of the signer to be signed. Run <b>certutil –dump x,cer</b> to view this value as  "Signature Hash".</p>
</dd>

### -field <b>ImageHashAlgorithm</b>

<dd>
<p>The algorithm of the image hash. The following values are listed for reference.
      </p>
<table>
<tr>
<th>Value</th>
</tr>
<tr>
<td>
<p>ALG_CLASS_HASH</p>
</td>
</tr>
<tr>
<td>
<p>ALG_CLASS_ANY</p>
</td>
</tr>
<tr>
<td>
<p>ALG_SID_MD5</p>
</td>
</tr>
<tr>
<td>
<p>ALG_SID_SHA1</p>
</td>
</tr>
<tr>
<td>
<p>ALG_SID_SHA_256</p>
</td>
</tr>
<tr>
<td>
<p>ALG_SID_SHA_384</p>
</td>
</tr>
<tr>
<td>
<p>ALG_SID_SHA_512</p>
</td>
</tr>
<tr>
<td>
<p>CALG_MD5</p>
</td>
</tr>
<tr>
<td>
<p>CALG_SHA1</p>
</td>
</tr>
<tr>
<td>
<p>CALG_SHA_256</p>
</td>
</tr>
<tr>
<td>
<p>CALG_SHA_384</p>
</td>
</tr>
<tr>
<td>
<p>CALG_SHA_512</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ThumbprintHashAlgorithm</b>

<dd>
<p>The algorithm of the certificate thumbprint. This member should be ignored if <b>CertificateThumbprint</b> is NULL.</p>
</dd>

### -field <b>ImageHashLength</b>

<dd>
<p>The length of data pointed to by the <b>ImageHash</b> member.</p>
</dd>

### -field <b>CertificateThumbprintLength</b>

<dd>
<p>The length of data pointed to by the <b>CertificateThumbprint</b> member.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with  Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddk\ne-ntddk--bdcb-classification.md">BDCB_CLASSIFICATION</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-ioregisterbootdrivercallback.md">BOOT_DRIVER_CALLBACK_FUNCTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20BDCB_IMAGE_INFORMATION structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
