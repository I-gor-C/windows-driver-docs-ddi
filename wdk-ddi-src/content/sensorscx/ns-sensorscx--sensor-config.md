---
UID: NS.sensorscx._SENSOR_CONFIG
title: SENSOR_CONFIG
author: windows-driver-content
description: This structure contains information that the sensor driver passes to the class extension about each sensor.
old-location: sensors\sensor_config.htm
old-project: sensors
ms.assetid: E21E2FEC-8733-4A8A-A0C4-899F10824F9B
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: SENSOR_CONFIG, SENSOR_CONFIG, *PSENSOR_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: sensorscx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SENSOR_CONFIG
req.alt-loc: SensorsCx.h
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
req.product: Windows 10 or later.
---

# SENSOR_CONFIG structure



## -description
<p>This structure contains information that the sensor driver passes to the class extension about each sensor.</p>


## -syntax

````
typedef struct _SENSOR_CONFIG {
  ULONG                   Size;
  PSENSOR_COLLECTION_LIST pEnumerationList;
} SENSOR_CONFIG, *PSENSOR_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The allocated size of this structure (in bytes).</p>
</dd>

### -field <b>pEnumerationList</b>

<dd>
<p>The list of enumerations. For more information, see <a href="..\sensorsdef\ns-sensorsdef-sensor-collection-list.md">SENSOR_COLLECTION_LIST</a>.</p>
</dd>
</dl>

## -remarks
<p>The SENSOR_CONFIG structure works with the following helper function:</p>

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
<dt>SensorsCx.h</dt>
</dl>
</td>
</tr>
</table>