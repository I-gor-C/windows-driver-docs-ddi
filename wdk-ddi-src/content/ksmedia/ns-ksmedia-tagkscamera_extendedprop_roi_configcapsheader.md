---
UID: NS.KSMEDIA.TAGKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER
title: tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER
author: windows-driver-content
description: This structure contains the header information for ROI capabilities.
old-location: stream\kscamera_extendedprop_roi_configcapsheader.htm
old-project: stream
ms.assetid: E915BF71-F29C-440B-9A56-50389AA8A9CF
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER, *PKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER, KSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER
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
---

# tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER structure



## -description
This structure contains the header information for ROI capabilities.


## -syntax

````
typedef struct tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER {
  ULONG     Size;
  ULONG     ConfigCapCount;
  ULONGLONG Reserved;
} KSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER, *PKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER;
````


## -struct-fields

### -field Size

The size of this header and all <a href="stream.kscamera_extendedprop_roi_configcaps">KSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS</a> structures that follow.

### -field ConfigCapCount

Contains the number of <b>KSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS</b> structures that follow.

### -field Reserved

Reserved for future use.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>