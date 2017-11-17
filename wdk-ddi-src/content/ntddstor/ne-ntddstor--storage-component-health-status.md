---
UID: NE.ntddstor._STORAGE_COMPONENT_HEALTH_STATUS
title: STORAGE_COMPONENT_HEALTH_STATUS
author: windows-driver-content
description: Indicates the health status of a storage device.
old-location: storage\storage_component_health_status.htm
ms.assetid: 6768C1D7-A964-44A7-A340-98060130FF24
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: Storage
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
ms.keywords: SERIALPERF_STATS, SERIALPERF_STATS, *PSERIALPERF_STATS
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

### -field <a id="HealthStatusUnknown"></a><a id="healthstatusunknown"></a><a id="HEALTHSTATUSUNKNOWN"></a><b>HealthStatusUnknown</b>

<dd>
<p>The storage device health status is unknown.</p>
</dd>

### -field <a id="HealthStatusNormal"></a><a id="healthstatusnormal"></a><a id="HEALTHSTATUSNORMAL"></a><b>HealthStatusNormal</b>

<dd>
<p>The storage device is operating normally.</p>
</dd>

### -field <a id="HealthStatusThrottled"></a><a id="healthstatusthrottled"></a><a id="HEALTHSTATUSTHROTTLED"></a><b>HealthStatusThrottled</b>

<dd>
<p>The storage device has been throttled.</p>
</dd>

### -field <a id="HealthStatusWarning"></a><a id="healthstatuswarning"></a><a id="HEALTHSTATUSWARNING"></a><b>HealthStatusWarning</b>

<dd>
<p>The storage device has issued a warning.</p>
</dd>

### -field <a id="HealthStatusDisabled"></a><a id="healthstatusdisabled"></a><a id="HEALTHSTATUSDISABLED"></a><b>HealthStatusDisabled</b>

<dd>
<p>The storage device has been disabled.</p>
</dd>

### -field <a id="HealthStatusFailed"></a><a id="healthstatusfailed"></a><a id="HEALTHSTATUSFAILED"></a><b>HealthStatusFailed</b>

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