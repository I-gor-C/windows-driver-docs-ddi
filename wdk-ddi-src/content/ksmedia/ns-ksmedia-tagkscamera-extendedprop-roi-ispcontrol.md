---
UID: NS.ksmedia.tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL
title: tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL
author: windows-driver-content
description: This structure contains information for an ROI ISP control.
old-location: stream\kscamera_extendedprop_roi_ispcontrol.htm
old-project: stream
ms.assetid: 49EAB8F3-35B9-4F99-A7B8-66B582B228B1
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL, KSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL, *PKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL
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
req.alt-api: KSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL
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

# tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL structure



## -description
<p>This structure contains information for an ROI ISP control.</p>


## -syntax

````
typedef struct tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL {
  ULONG ControlId;
  ULONG ROICount;
  ULONG Result;
  ULONG Reserved;
} KSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL, *PKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL;
````


## -struct-fields
<dl>

### -field <b>ControlId</b>

<dd>
<p>The ISP control ID. The following are valid values for this field. These values are defined in ksmedia.h.</p>
<ul>
<li>
<p>KSPROPERTY_CAMERACONTROL_EXTENDED_WHITEBALANCEMODE</p>
</li>
<li>
<p>KSPROPERTY_CAMERACONTROL_EXTENDED_EXPOSUREMODE</p>
</li>
<li>
<p>KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSMODE</p>
</li>
</ul>
</dd>

### -field <b>ROICount</b>

<dd>
<p>The number of ROIs associated with this ISP control.</p>
</dd>

### -field <b>Result</b>

<dd>
<p>The error results of the last SET operation for this ISP control.</p>
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