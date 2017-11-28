---
UID: NS.gnssdriver.PGNSS_GEOFENCE_CREATE_PARAM
title: PGNSS_GEOFENCE_CREATE_PARAM
author: windows-driver-content
description: This structure defines the parameters for creating a geofence in the GNSS engine.
old-location: sensors\gnss_geofence_create_param.htm
old-project: sensors
ms.assetid: CA517EF6-41EE-4DB0-B628-35902BA34FFB
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: PGNSS_GEOFENCE_CREATE_PARAM, GNSS_GEOFENCE_CREATE_PARAM, *PGNSS_GEOFENCE_CREATE_PARAM
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
req.alt-api: GNSS_GEOFENCE_CREATE_PARAM
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

# PGNSS_GEOFENCE_CREATE_PARAM structure



## -description
<p>This structure defines the parameters for creating a geofence in the GNSS engine.</p>


## -syntax

````
typedef struct {
  ULONG               Size;
  ULONG               Version;
  ULONG               AlertTypes;
  GNSS_GEOFENCE_STATE InitialState;
  GNSS_GEOREGION      Boundary;
  BYTE                Unused[512];
} GNSS_GEOFENCE_CREATE_PARAM, *PGNSS_GEOFENCE_CREATE_PARAM;
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

### -field <b>AlertTypes</b>

<dd>
<p>This is a bitmask that indicates the various alerts for this geofence that the HLOS is interested in. The GNSS engine should not raise any geofence alerts unless specifically requested by the HLOS.</p>
<p>If the HLOS sets only GNSS_GEOFENCEALERTTYPE_ENTRY, the GNSS engine must track the geofence all the time, but raise alert only when the device has entered the geofence. The next alert is expected when the device moves out of the geofence and reenters.</p>
<p>If the HLOS sets only GNSS_GEOFENCEALERTTYPE_EXIT, the GNSS engine must track the geofence all the time, but raise alert only when the device has exit the geofence after entering it previously. The next alert is expected when the device moves inside the geofence and re-exits.</p>
<p>If the HLOS sets both the bitmasks, the GNSS engine must track the geofence all the time, and raise alert as the device moves in and out of the geofence .</p>
<p>In all cases, the GNSS engine must separately raise the global tracking status alert if it is unable to track the geofences (irrespective of their alert settings).</p>
</dd>

### -field <b>InitialState</b>

<dd>
<p>Indicates the initial state of the specific geofence, as seen by the HLOS.  The GNSS engine must use this state as the starting state of the geofence, as opposed always starting from the GNSS_GeofenceState_Unknown state. This allows the GNSS engine to stay in sync with the HLOS in terms of the geofence states and get around any differences in geofence entry or  exit detection logic between the GNSS engine and the HLOS.</p>
<p>As the GNSS engine starts tracking the newly added geofence, if it determines that the geofence is in a different state than this initial state, it should raise the appropriate alert. Conversely, if the states are identical, no alert should be raised.</p>
</dd>

### -field <b>Boundary</b>

<dd>
<p>The actual boundary of the geofence.</p>
</dd>

### -field <b>Unused[512]</b>

<dd>
<p>Padding buffer.</p>
</dd>
</dl>

## -remarks
<p>A geographical shape is used to define a geofence.  Windows 10 currently supports only circular geofences.</p>

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