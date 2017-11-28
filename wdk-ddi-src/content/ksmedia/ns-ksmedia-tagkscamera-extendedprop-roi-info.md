---
UID: NS.ksmedia.tagKSCAMERA_EXTENDEDPROP_ROI_INFO
title: tagKSCAMERA_EXTENDEDPROP_ROI_INFO
author: windows-driver-content
description: This structure contains information about an ROI.
old-location: stream\kscamera_extendedprop_roi_info.htm
old-project: stream
ms.assetid: DAE013B7-7715-4B03-99F7-807306736C14
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: tagKSCAMERA_EXTENDEDPROP_ROI_INFO, KSCAMERA_EXTENDEDPROP_ROI_INFO, *PKSCAMERA_EXTENDEDPROP_ROI_INFO
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
req.alt-api: KSCAMERA_EXTENDEDPROP_ROI_INFO
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

# tagKSCAMERA_EXTENDEDPROP_ROI_INFO structure



## -description
<p>This structure contains information about an ROI.</p>


## -syntax

````
typedef struct tagKSCAMERA_EXTENDEDPROP_ROI_INFO {
  RECT      Region;
  ULONGLONG Flags;
  LONG      Weight;
  LONG      RegionOfInterestType;
} KSCAMERA_EXTENDEDPROP_ROI_INFO, *PKSCAMERA_EXTENDEDPROP_ROI_INFO;
````


## -struct-fields
<dl>

### -field <b>Region</b>

<dd>
<p>These are the relative coordinates in Q13 format on the frame that face detection is running.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>These are VIDEOPROCFLAG flags that indicate the op mode for the ISP control. For focus ROI, the default value is 0 representing focus region configuration without initiating a focus.</p>
</dd>

### -field <b>Weight</b>

<dd>
<p>This is the weight of the region (0-100).</p>
</dd>

### -field <b>RegionOfInterestType</b>

<dd>
<p>If the region is a face, this value is KSCAMERA_EXTENDEDPROP_ROITYPE_FACE. If the region is anything other than face, this value is KSCAMERA_EXTENDEDPROP_ROITYPE_UNKNOWN. For more information, see the <a href="https://msdn.microsoft.com/library/windows/hardware/dn925151">KSCAMERA_EXTENDEDPROP_ROITYPE</a> enumeration.</p>
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