---
UID: NS.sensorsdef.SENSOR_PROPERTY_LIST
title: SENSOR_PROPERTY_LIST
author: windows-driver-content
description: This structure contains a list of all SENSOR_VALUE_PAIR structures for each sensor. This structure is returned by calling ReadFile.
old-location: sensors\sensor_property_list.htm
ms.assetid: 03E03BB9-95DB-49C0-AF14-FFF1998C98A7
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: sensors
req.header: sensorsdef.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SENSOR_PROPERTY_LIST
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
ms.keywords: SENSOR_PROPERTY_LIST, SENSOR_PROPERTY_LIST, *PSENSOR_PROPERTY_LIST
req.iface: 
req.product: Windows 10 or later.
---

# SENSOR_PROPERTY_LIST structure



## -description
<p>This structure contains a list of all <a href="https://msdn.microsoft.com/library/windows/hardware/dn946708">SENSOR_VALUE_PAIR</a> structures for each sensor. This structure is returned by calling ReadFile.</p>


## -syntax

````
typedef struct _SENSOR_PROPERTY_LIST {
  ULONG       AllocatedSizeInBytes;
  ULONG       Count;
  PROPERTYKEY List[1];
} SENSOR_PROPERTY_LIST, *PSENSOR_PROPERTY_LIST;
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
<p>A list of PROPERTYKEY values.</p>
</dd>
</dl>

## -remarks
<p>Note that the <i>List[1]</i> parameter is a variable-sized buffer. The first element is a place-holder and may not accurately the buffer size.</p>

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