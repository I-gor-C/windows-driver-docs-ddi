---
UID: NS.ksmedia.tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER
title: tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER
author: windows-driver-content
description: This structure contains the header information for ROI capabilities.
old-location: stream\kscamera_extendedprop_roi_configcapsheader.htm
old-project: stream
ms.assetid: E915BF71-F29C-440B-9A56-50389AA8A9CF
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER, KSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER, *PKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER
req.alt-loc: Ksmedia.h
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

# tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER structure



## -description
<p>This structure contains the header information for ROI capabilities.</p>


## -syntax

````
typedef struct tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER {
  ULONG     Size;
  ULONG     ConfigCapCount;
  ULONGLONG Reserved;
} KSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER, *PKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of this header and all <a href="https://msdn.microsoft.com/library/windows/hardware/dn925154">KSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS</a> structures that follow.</p>
</dd>

### -field <b>ConfigCapCount</b>

<dd>
<p>Contains the number of <b>KSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS</b> structures that follow.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>