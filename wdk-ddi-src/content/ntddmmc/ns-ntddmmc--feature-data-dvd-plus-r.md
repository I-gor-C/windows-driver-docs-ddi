---
UID: NS.ntddmmc._FEATURE_DATA_DVD_PLUS_R
title: FEATURE_DATA_DVD_PLUS_R
author: windows-driver-content
description: The FEATURE_DATA_DVD_PLUS_R structure contains information about the DVD+R feature.
old-location: storage\feature_data_dvd_plus_r.htm
old-project: storage
ms.assetid: e1501ea9-a55b-4fbc-990b-2172c7369bb1
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: FEATURE_DATA_DVD_PLUS_R, FEATURE_DATA_DVD_PLUS_R, *PFEATURE_DATA_DVD_PLUS_R
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
req.alt-api: FEATURE_DATA_DVD_PLUS_R
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

# FEATURE_DATA_DVD_PLUS_R structure



## -description
<p>The FEATURE_DATA_DVD_PLUS_R structure contains information about the DVD+R feature. </p>


## -syntax

````
typedef struct _FEATURE_DATA_DVD_PLUS_R {
  FEATURE_HEADER Header;
  UCHAR          Write  :1;
  UCHAR          Reserved1  :7;
  UCHAR          Reserved2[3];
} FEATURE_DATA_DVD_PLUS_R, *PFEATURE_DATA_DVD_PLUS_R;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>Contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a> structure with header information for this feature descriptor. </p>
</dd>

### -field <b>Write</b>

<dd>
<p>Indicates, when set to 1, that the device has an ability that was not specified in the DVD-ROM profile, to write to DVD+R discs according to <i>DVD+R 4.7 Gbytes Basic Format Specifications.</i> When set to 0, the device has no extra ability beyond what is specified in the profile. </p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved. </p>
</dd>
</dl>

## -remarks
<p>This structure holds data for the feature named "DVD+R" by the <i>MMC-3 </i>specification. Devices that support this feature can specify whether they are able to perform writes to DVD+R discs, even though this ability was not indicated in the device's DVD-ROM profile.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20FEATURE_DATA_DVD_PLUS_R structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
