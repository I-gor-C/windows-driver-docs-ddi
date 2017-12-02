---
UID: NS.ksmedia.tagKSCAMERA_MAXVIDEOFPS_FORPHOTORES
title: tagKSCAMERA_MAXVIDEOFPS_FORPHOTORES
author: windows-driver-content
description: The KSCAMERA_MAXVIDEOFPS_FORPHOTORES structure contains the property data for maximum frame rate at a particular resolution for a camera supporting preview and capture.
old-location: stream\kscamera_maxvideofps_forphotores.htm
old-project: stream
ms.assetid: 4230F7E1-DC36-4265-9E82-907EE82E9DFF
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagKSCAMERA_MAXVIDEOFPS_FORPHOTORES, KSCAMERA_MAXVIDEOFPS_FORPHOTORES, *PKSCAMERA_MAXVIDEOFPS_FORPHOTORES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSCAMERA_MAXVIDEOFPS_FORPHOTORES
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

# tagKSCAMERA_MAXVIDEOFPS_FORPHOTORES structure



## -description
<p>The <b>KSCAMERA_MAXVIDEOFPS_FORPHOTORES</b> structure contains the property data for maximum frame rate at a particular resolution for a camera supporting preview and capture. This structure is used when setting or retrieving the data for the <b>KSPROPERTY_CAMERACONTROL_EXTENDED_MAXVIDFPS_PHOTORES</b> extended control property.</p>


## -syntax

````
typedef struct _KSCAMERA_MAXVIDEOFPS_FORPHOTORES {
  ULONG PhotoResWidth;
  ULONG PhotoResHeight;
  ULONG PreviewFPSNum;
  ULONG PreviewFPSDenom;
  ULONG CaptureFPSNum;
  ULONG CaptureFPSDenom;
} KSCAMERA_MAXVIDEOFPS_FORPHOTORES, *PKSCAMERA_MAXVIDEOFPS_FORPHOTORES;
````


## -struct-fields
<dl>

### -field PhotoResWidth

<dd>
<p>The photo resolution width in pixels.</p>
</dd>

### -field PhotoResHeight

<dd>
<p>The photo resolution height in pixels.</p>
</dd>

### -field PreviewFPSNum

<dd>
<p>The numerator value of the preview frame rate.</p>
</dd>

### -field PreviewFPSDenom

<dd>
<p>The denominator value of the preview frame rate.</p>
</dd>

### -field CaptureFPSNum

<dd>
<p>The numerator value of the capture frame rate.</p>
</dd>

### -field CaptureFPSDenom

<dd>
<p>The denominator value of the capture frame rate.</p>
</dd>
</dl>

## -remarks
<p>When setting the property, using a KSPROPERTY_TYPE_SET  request, the <b>PhotoResWidth</b> and <b>PhotoResHeight</b> members are  supplied by the application based on the available photo media types.  The camera driver must retain this resolution information internally.  The preview and capture frame rate members must be ignored by the driver on KSPROPERTY_TYPE_SET requests.</p>

<p>For any subsequent KSPROPERTY_TYPE_GET request, the camera driver, based on the resolution provided in the earlier KSPROPERTY_TYPE_SET request, must provide the frame rates for the preview and capture streams.  Also, the camera driver must set the <b>PhotoResWidth</b> and <b>PhotoResHeight</b> to the resolution that was provided with the KSPROPERTY_TYPE_SET request.</p>

<p>If no KSPROPERTY_TYPE_SET request was made for the session, the camera driver set all the members of the <b>KSCAMERA_MAXVIDEOFPS_FORPHOTORES</b> structure to 0.</p>

<p>If preview or capture are not supported, such as the case when the camera is a dual pinned camera with only one video pin, it should use the <b>CaptureFPSNum</b> and <b>CaptureFPSDenom</b> members and set the <b>PreviewFPSNum</b> and <b>PreviewFPSDenom</b> members to 0.</p>

<p>If <b>KSCAMERA_EXTENDEDPROP_PHOTOMODE_SEQUENCE</b> is supported on the <i>Photo Mode Control</i> by the camera driver, this control is mandatory.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>