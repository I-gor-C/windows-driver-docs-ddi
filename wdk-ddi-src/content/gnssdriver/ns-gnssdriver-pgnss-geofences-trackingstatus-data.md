---
UID: NS.gnssdriver.PGNSS_GEOFENCES_TRACKINGSTATUS_DATA
title: PGNSS_GEOFENCES_TRACKINGSTATUS_DATA
author: windows-driver-content
description: This structure is used by the GNSS engine to notify of any changes in the tracking status while tracking a set of previously created geofences.
old-location: sensors\gnss_geofences_trackingstatus_data.htm
old-project: sensors
ms.assetid: 65E59305-B1D9-4255-926A-A72F3B4887AF
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PGNSS_GEOFENCES_TRACKINGSTATUS_DATA, GNSS_GEOFENCES_TRACKINGSTATUS_DATA, *PGNSS_GEOFENCES_TRACKINGSTATUS_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_GEOFENCES_TRACKINGSTATUS_DATA
req.alt-loc: gnssdriver.h
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

# PGNSS_GEOFENCES_TRACKINGSTATUS_DATA structure



## -description
<p>This structure is used by the GNSS engine to notify of any changes in the tracking status while tracking a set of previously created geofences.</p>


## -syntax

````
typedef struct _GNSS_GEOFENCES_TRACKINGSTATUS_DATA {
  ULONG    Size;
  ULONG    Version;
  NTSTATUS Status;
  FILETIME StatusTimeStamp;
  BYTE     Unused[512];
} GNSS_GEOFENCES_TRACKINGSTATUS_DATA, *PGNSS_GEOFENCES_TRACKINGSTATUS_DATA;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Structure size.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Version number.</p>
</dd>

### -field <b>Status</b>

<dd>
<p>A failure code indicates that the GNSS engine is unable to track the geofences (due to bad signal conditions or other transient errors).</p>
<p>A success code indicates that the GNSS engine was previously unable to track geofences, and is now able to track them.</p>
</dd>

### -field <b>StatusTimeStamp</b>

<dd>
<p>The UTC time of this status.</p>
</dd>

### -field <b>Unused[512]</b>

<dd>
<p>Padding buffer.</p>
</dd>
</dl>

## -remarks
<p>The GNSS engine must not raise  events when it is not tracking any mobile-originated geofences (but tracking network-initiated Geofences), or when the geofence tracking has been reset by the GNSS_ResetGeofenceTracking command.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Gnssdriver.h</dt>
</dl>
</td>
</tr>
</table>