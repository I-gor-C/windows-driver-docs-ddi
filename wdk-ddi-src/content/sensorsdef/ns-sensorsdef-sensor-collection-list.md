---
UID: NS.sensorsdef.SENSOR_COLLECTION_LIST
title: SENSOR_COLLECTION_LIST
author: windows-driver-content
description: This structure contains a list of all SENSOR_VALUE_PAIR structures for each sensor. This structure is returned by calling ReadFile.
old-location: sensors\sensor_collection_list.htm
old-project: sensors
ms.assetid: B842C707-C6E0-4C56-986E-35BFD32F265D
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: SENSOR_COLLECTION_LIST, SENSOR_COLLECTION_LIST, *PSENSOR_COLLECTION_LIST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: sensorsdef.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SENSOR_COLLECTION_LIST
req.alt-loc: Sensorsdef.h
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

# SENSOR_COLLECTION_LIST structure



## -description
<p>This structure contains a list of all <a href="..\sensorsdef\ns-sensorsdef-sensor-value-pair.md">SENSOR_VALUE_PAIR</a> structures for each sensor. This structure is returned by calling ReadFile.</p>


## -syntax

````
typedef struct _SENSOR_COLLECTION_LIST {
  ULONG             AllocatedSizeInBytes;
  ULONG             Count;
  SENSOR_VALUE_PAIR List[1];
} SENSOR_COLLECTION_LIST, *PSENSOR_COLLECTION_LIST;
````


## -struct-fields
<dl>

### -field <b>AllocatedSizeInBytes</b>

<dd>
<p>Represents the number of elements allocated in List.</p>
</dd>

### -field <b>Count</b>

<dd>
<p>Represents the number of used entries in List.</p>
</dd>

### -field <b>List</b>

<dd>
<p>A list of <a href="..\sensorsdef\ns-sensorsdef-sensor-value-pair.md">SENSOR_VALUE_PAIR</a> structures.</p>
</dd>
</dl>

## -remarks
<p>The SENSOR_COLLECTION_LIST structure works with the following helper functions:</p>

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
<dt>Sensorsdef.h</dt>
</dl>
</td>
</tr>
</table>