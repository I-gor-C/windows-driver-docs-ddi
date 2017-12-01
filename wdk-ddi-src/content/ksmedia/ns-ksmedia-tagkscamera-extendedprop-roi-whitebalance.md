---
UID: NS.ksmedia.tagKSCAMERA_EXTENDEDPROP_ROI_WHITEBALANCE
title: tagKSCAMERA_EXTENDEDPROP_ROI_WHITEBALANCE
author: windows-driver-content
description: This structure contains the ROI info structure for white balance.
old-location: stream\kscamera_extendedprop_roi_whitebalance.htm
old-project: stream
ms.assetid: 16BDC61E-390C-4D79-A8D0-049404974733
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagKSCAMERA_EXTENDEDPROP_ROI_WHITEBALANCE, KSCAMERA_EXTENDEDPROP_ROI_WHITEBALANCE, *PKSCAMERA_EXTENDEDPROP_ROI_WHITEBALANCE
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
req.alt-api: KSCAMERA_EXTENDEDPROP_ROI_WHITEBALANCE
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

# tagKSCAMERA_EXTENDEDPROP_ROI_WHITEBALANCE structure



## -description
<p>This structure contains the ROI info structure for white balance.</p>


## -syntax

````
typedef struct tagKSCAMERA_EXTENDEDPROP_ROI_WHITEBALANCE {
  KSCAMERA_EXTENDEDPROP_ROI_INFO ROIInfo;
  ULONGLONG                      Reserved;
} KSCAMERA_EXTENDEDPROP_ROI_WHITEBALANCE, *PKSCAMERA_EXTENDEDPROP_ROI_WHITEBALANCE;
````


## -struct-fields
<dl>

### -field <b>ROIInfo</b>

<dd>
<p>See the <a href="stream.kscamera_extendedprop_roi_info">KSCAMERA_EXTENDEDPROP_ROI_INFO</a> structure for more information.</p>
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