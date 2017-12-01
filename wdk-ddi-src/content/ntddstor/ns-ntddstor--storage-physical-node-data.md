---
UID: NS.ntddstor._STORAGE_PHYSICAL_NODE_DATA
title: STORAGE_PHYSICAL_NODE_DATA
author: windows-driver-content
description: Specifies the physical device data of a storage node.
old-location: storage\storage_physical_node_data.htm
old-project: storage
ms.assetid: F6C1EE86-FB1C-467D-9E03-B238CB132D1A
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_PHYSICAL_NODE_DATA, STORAGE_PHYSICAL_NODE_DATA, *PSTORAGE_PHYSICAL_NODE_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_PHYSICAL_NODE_DATA
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

# STORAGE_PHYSICAL_NODE_DATA structure



## -description
<p>Specifies the physical device data of a storage node.</p>


## -syntax

````
typedef struct _STORAGE_PHYSICAL_NODE_DATA {
  ULONG NodeId;
  ULONG AdapterCount;
  ULONG AdapterDataLength;
  ULONG AdapterDataOffset;
  ULONG DeviceCount;
  ULONG DeviceDataLength;
  ULONG DeviceDataOffset;
  ULONG Reserved[3];
} STORAGE_PHYSICAL_NODE_DATA, *PSTORAGE_PHYSICAL_NODE_DATA;
````


## -struct-fields
<dl>

### -field <b>NodeId</b>

<dd>
<p>The hardware ID of the storage node.</p>
</dd>

### -field <b>AdapterCount</b>

<dd>
<p>A value of 0 or 1 that indicates the adapter count in the storage node.</p>
</dd>

### -field <b>AdapterDataLength</b>

<dd>
<p>The data length of the storage adapter in the storage node,  in units of kilobytes (1024 bytes).</p>
</dd>

### -field <b>AdapterDataOffset</b>

<dd>
<p>The data offset from the beginning of the data structure. The buffer contains an array of <a href="..\ntddstor\ns-ntddstor--storage-physical-adapter-data.md">STORAGE_PHYSICAL_ADAPTER_DATA</a>.</p>
</dd>

### -field <b>DeviceCount</b>

<dd>
<p>A value less than or equal to 1.</p>
</dd>

### -field <b>DeviceDataLength</b>

<dd>
<p>The data length of the storage device in the storage node,  in units of kilobytes (1024 bytes).</p>
</dd>

### -field <b>DeviceDataOffset</b>

<dd>
<p>The data offset from the beginning of the data structure. The buffer contains an array of <a href="..\ntddstor\ns-ntddstor--storage-physical-device-data.md">STORAGE_PHYSICAL_DEVICE_DATA</a>.</p>
</dd>

### -field <b>Reserved[3]</b>

<dd>
<p>Specifies if the storage adapter is reserved.</p>
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