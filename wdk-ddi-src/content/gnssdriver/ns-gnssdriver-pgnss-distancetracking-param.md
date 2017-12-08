---
UID: NS.gnssdriver.PGNSS_DISTANCETRACKING_PARAM
title: PGNSS_DISTANCETRACKING_PARAM
author: windows-driver-content
description: This structure defines the parameters for a distance-based tracking fix session.
old-location: sensors\gnss_distancetracking_param.htm
old-project: sensors
ms.assetid: B37B3C59-225C-40BC-BCA4-9ABF2500AFC0
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: PGNSS_DISTANCETRACKING_PARAM, GNSS_DISTANCETRACKING_PARAM, *PGNSS_DISTANCETRACKING_PARAM
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
req.alt-api: GNSS_DISTANCETRACKING_PARAM
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

# PGNSS_DISTANCETRACKING_PARAM structure



## -description
<p>This structure defines the parameters for a distance-based tracking fix session.</p>


## -syntax

````
typedef struct {
  ULONG Size;
  ULONG Version;
  ULONG MovementThreshold;
} GNSS_DISTANCETRACKING_PARAM, *PGNSS_DISTANCETRACKING_PARAM;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>Structure size.</p>
</dd>

### -field Version

<dd>
<p>Version number.</p>
</dd>

### -field MovementThreshold

<dd>
<p>If the device moves beyond this threshold, a fix will be generated/recorded. A value of zero indicates that a fix should be reported whenever the device moves. This value is specified in meters.</p>
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
<dt>Gnssdriver.h</dt>
</dl>
</td>
</tr>
</table>