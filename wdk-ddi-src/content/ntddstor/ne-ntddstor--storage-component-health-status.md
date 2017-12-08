---
UID: NE.ntddstor._STORAGE_COMPONENT_HEALTH_STATUS
title: STORAGE_COMPONENT_HEALTH_STATUS
author: windows-driver-content
description: Indicates the health status of a storage device.
old-location: storage\storage_component_health_status.htm
old-project: storage
ms.assetid: 6768C1D7-A964-44A7-A340-98060130FF24
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SERIALPERF_STATS, SERIALPERF_STATS, *PSERIALPERF_STATS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_COMPONENT_HEALTH_STATUS
req.alt-loc: Ntddstor.h
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

# STORAGE_COMPONENT_HEALTH_STATUS enumeration



## -description
<p>Indicates the health status of a storage device.</p>


## -syntax

````
typedef enum _STORAGE_COMPONENT_HEALTH_STATUS { 
  HealthStatusUnknown    = 0, // 0x0
  HealthStatusNormal,
  HealthStatusThrottled,
  HealthStatusWarning,
  HealthStatusDisabled,
  HealthStatusFailed
} STORAGE_COMPONENT_HEALTH_STATUS, *PSTORAGE_COMPONENT_HEALTH_STATUS;
````


## -enum-fields
<dl>

### -field HealthStatusUnknown

<dd>
<p>The storage device health status is unknown.</p>
</dd>

### -field HealthStatusNormal

<dd>
<p>The storage device is operating normally.</p>
</dd>

### -field HealthStatusThrottled

<dd>
<p>The storage device has been throttled.</p>
</dd>

### -field HealthStatusWarning

<dd>
<p>The storage device has issued a warning.</p>
</dd>

### -field HealthStatusDisabled

<dd>
<p>The storage device has been disabled.</p>
</dd>

### -field HealthStatusFailed

<dd>
<p>The storage device has failed.</p>
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
<dt>Ntddstor.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>