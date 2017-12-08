---
UID: NS.NTDDSTOR._STORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR
title: _STORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR
author: windows-driver-content
description: The output buffer for the StorageDeviceIoCapabilityProperty as defined in STORAGE_PROPERTY_ID.
old-location: storage\storage_device_io_capability_descriptor.htm
old-project: storage
ms.assetid: 98377F8F-62C8-4E8F-838B-A63DC63E4A0C
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: _STORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR, STORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR, *PSTORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR
req.alt-loc: ntddstor.h
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
---

# _STORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR structure



## -description
The output buffer for the StorageDeviceIoCapabilityProperty as defined in <a href="storage.storage_property_id">STORAGE_PROPERTY_ID</a>.


## -syntax

````
typedef struct _STORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR {
  ULONG Version;
  ULONG Size;
  ULONG LunMaxIoCount;
  ULONG AdapterMaxIoCount;
} STORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR, *PSTORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR;
````


## -struct-fields

### -field Version

The version of this structure. The Size serves as the version.

### -field Size

The size of this structure.

### -field LunMaxIoCount

The logical unit number (LUN) max outstanding I/O count.

### -field AdapterMaxIoCount

The adapter max outstanding I/O count.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Client
</th>
<td width="70%">
Windows 10
</td>
</tr>
<tr>
<th width="30%">
Server
</th>
<td width="70%">
Windows Server 2016
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntddstor.h</dt>
</dl>
</td>
</tr>
</table>