---
UID: NS.ntddmmc._FEATURE_DATA_DVD_CPRM
title: FEATURE_DATA_DVD_CPRM
author: windows-driver-content
description: The FEATURE_DATA_DVD_CPRM structure holds information about the DVD Content Protection for Recorded Media (CPRM) feature.
old-location: storage\feature_data_dvd_cprm.htm
ms.assetid: 060c1e9a-14d3-4f9b-b898-d8042f5efd7e
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddmmc.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FEATURE_DATA_DVD_CPRM
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
ms.keywords: FEATURE_DATA_DVD_CPRM, FEATURE_DATA_DVD_CPRM, *PFEATURE_DATA_DVD_CPRM
req.iface: 
---

# FEATURE_DATA_DVD_CPRM structure



## -description
<p>The FEATURE_DATA_DVD_CPRM structure holds information about the DVD Content Protection for Recorded Media (CPRM) feature. </p>


## -syntax

````
typedef struct _FEATURE_DATA_DVD_CPRM {
  FEATURE_HEADER Header;
  UCHAR          Reserved0[3];
  UCHAR          CPRMVersion;
} FEATURE_DATA_DVD_CPRM, *PFEATURE_DATA_DVD_CPRM;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>Contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a> structure with header information for this feature descriptor. </p>
</dd>

### -field <b>Reserved0</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>CPRMVersion</b>

<dd>
<p>Contains the CPRM version number. Must be set to 1. </p>
</dd>
</dl>

## -remarks
<p>This structure holds data for the feature named "DVD CPRM" by the <i>SCSI Multimedia - 4 (MMC-4)</i> specification. Devices that support this feature can perform DVD Content Protection for Recordable Media (CPRM) authentication and key management. </p>

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
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553850">FEATURE_NUMBER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20FEATURE_DATA_DVD_CPRM structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
