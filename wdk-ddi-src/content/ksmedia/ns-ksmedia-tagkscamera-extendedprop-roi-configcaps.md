---
UID: NS.ksmedia.tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS
title: tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS
author: windows-driver-content
description: This structure contains the capabilities for an ROI control.
old-location: stream\kscamera_extendedprop_roi_configcaps.htm
ms.assetid: BAC5B134-22F5-4BC9-BBD6-6AF3C934510B
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS
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
ms.keywords: tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS, KSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS, *PKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS
req.iface: 
---

# tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS structure



## -description
<p>This structure contains the capabilities for an ROI control.</p>


## -syntax

````
typedef struct tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS {
  ULONG     ControlId;
  ULONG     MaxNumberOfROIs;
  ULONGLONG Capability;
} KSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS, *PKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS;
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

### -field <b>MaxNumberOfROIs</b>

<dd>
<p>The maximum ROIs supported for this ISO control.</p>
</dd>

### -field <b>Capability</b>

<dd>
<p>The capabilities for this ISP control.</p>
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