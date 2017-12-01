---
UID: NE.ntddk._BDCB_CLASSIFICATION
title: BDCB_CLASSIFICATION
author: windows-driver-content
description: The BDCB_CLASSIFICATION enumeration lists different classifications of boot start images.
old-location: kernel\bdcb_classification.htm
old-project: kernel
ms.assetid: 01627E7A-460F-4E49-B98C-0FCCFAB2F8BB
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: FILTER_INITIALIZATION_DATA, FILTER_INITIALIZATION_DATA, *PFILTER_INITIALIZATION_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDCB_CLASSIFICATION
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
req.irql: 
req.iface: 
---

# BDCB_CLASSIFICATION enumeration



## -description
<p>The BDCB_CLASSIFICATION enumeration lists different classifications of boot start images.</p>


## -syntax

````
typedef enum _BDCB_CLASSIFICATION { 
  BdCbClassificationUnknownImage,
  BdCbClassificationKnownGoodImage,
  BdCbClassificationKnownBadImage,
  BdCbClassificationKnownBadImageBootCritical,
  BdCbClassificationEnd
} BDCB_CLASSIFICATION;
````


## -enum-fields
<dl>

### -field <a id="BdCbClassificationUnknownImage"></a><a id="bdcbclassificationunknownimage"></a><a id="BDCBCLASSIFICATIONUNKNOWNIMAGE"></a><b>BdCbClassificationUnknownImage</b>

<dd>
<p>The boot start image has not been inspected by anti-malware or anti-malware does not have enough information to determine whether the binary is malware.</p>
</dd>

### -field <a id="BdCbClassificationKnownGoodImage"></a><a id="bdcbclassificationknowngoodimage"></a><a id="BDCBCLASSIFICATIONKNOWNGOODIMAGE"></a><b>BdCbClassificationKnownGoodImage</b>

<dd>
<p>The boot start image has been inspected by anti-malware and found not to be malware.</p>
</dd>

### -field <a id="BdCbClassificationKnownBadImage"></a><a id="bdcbclassificationknownbadimage"></a><a id="BDCBCLASSIFICATIONKNOWNBADIMAGE"></a><b>BdCbClassificationKnownBadImage</b>

<dd>
<p>The boot start image has been inspected by anti-malware and found to be malware.</p>
</dd>

### -field <a id="BdCbClassificationKnownBadImageBootCritical"></a><a id="bdcbclassificationknownbadimagebootcritical"></a><a id="BDCBCLASSIFICATIONKNOWNBADIMAGEBOOTCRITICAL"></a><b>BdCbClassificationKnownBadImageBootCritical</b>

<dd>
<p>The boot start image has been inspected by anti-malware and found to be malware, but the anti-malware boot-start driver also knows it to be critical to the success of the boot.</p>
</dd>

### -field <a id="BdCbClassificationEnd"></a><a id="bdcbclassificationend"></a><a id="BDCBCLASSIFICATIONEND"></a><b>BdCbClassificationEnd</b>

<dd>
<p>Do not use. Reserved for future use.</p>
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
<a href="..\ntddk\ns-ntddk--bdcb-image-information.md">BDCB_IMAGE_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-ioregisterbootdrivercallback.md">BOOT_DRIVER_CALLBACK_FUNCTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20BDCB_CLASSIFICATION enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
