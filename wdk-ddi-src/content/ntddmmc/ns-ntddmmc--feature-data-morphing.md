---
UID: NS.ntddmmc._FEATURE_DATA_MORPHING
title: FEATURE_DATA_MORPHING
author: windows-driver-content
description: The FEATURE_DATA_MORPHING structure contains information about the morphing feature.
old-location: storage\feature_data_morphing.htm
old-project: storage
ms.assetid: b3eaabdf-0163-4679-9b22-d8ec53abed59
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: FEATURE_DATA_MORPHING, FEATURE_DATA_MORPHING, *PFEATURE_DATA_MORPHING
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddmmc.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FEATURE_DATA_MORPHING
req.alt-loc: ntddmmc.h
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

# FEATURE_DATA_MORPHING structure



## -description
<p>The FEATURE_DATA_MORPHING structure contains information about the morphing feature.</p>


## -syntax

````
typedef struct _FEATURE_DATA_MORPHING {
  FEATURE_HEADER Header;
  UCHAR          Asynchronous  :1;
  UCHAR          OCEvent  :1;
  UCHAR          Reserved01  :6;
  UCHAR          Reserved2[3];
} FEATURE_DATA_MORPHING, *PFEATURE_DATA_MORPHING;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>Contains a <a href="..\ntddmmc\ns-ntddmmc--feature-header.md">FEATURE_HEADER</a> structure with header information for this feature descriptor. </p>
</dd>

### -field <b>Asynchronous</b>

<dd>
<p>Indicates, when set to 1, that the initiator can request device status asynchronously. If set to zero, the initiator must use polling to request status. </p>
</dd>

### -field <b>OCEvent</b>

<dd></dd>

### -field <b>Reserved01</b>

<dd></dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved. </p>
</dd>
</dl>

## -remarks
<p>This structure holds data for the feature named "Morphing" by the <i>MMC-3 </i>specification. Devices that support this feature can notify the initiator of operational changes and allow the initiator to prevent operational changes. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddmmc.h (include Ntddcdrm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddmmc\ns-ntddmmc--feature-header.md">FEATURE_HEADER</a>
</dt>
<dt>
<a href="..\ntddmmc\ne-ntddmmc--feature-number.md">FEATURE_NUMBER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20FEATURE_DATA_MORPHING structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
