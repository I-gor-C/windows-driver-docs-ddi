---
UID: NS.ntddstor._STORAGE_PHYSICAL_ADAPTER_DATA
title: STORAGE_PHYSICAL_ADAPTER_DATA
author: windows-driver-content
description: Specifies the physical device data of a storage adapter.
old-location: storage\storage_physical_adapter_data.htm
old-project: storage
ms.assetid: 404A7AFC-291E-4056-9076-F9E62A07C9FB
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_PHYSICAL_ADAPTER_DATA, STORAGE_PHYSICAL_ADAPTER_DATA, *PSTORAGE_PHYSICAL_ADAPTER_DATA
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
req.alt-api: STORAGE_PHYSICAL_ADAPTER_DATA
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

# STORAGE_PHYSICAL_ADAPTER_DATA structure



## -description
<p>Specifies the physical device data of a storage adapter.</p>


## -syntax

````
typedef struct _STORAGE_PHYSICAL_ADAPTER_DATA {
  ULONG                           AdapterId;
  STORAGE_COMPONENT_HEALTH_STATUS HealthStatus;
  STORAGE_PROTOCOL_TYPE           CommandProtocol;
  STORAGE_SPEC_VERSION            SpecVersion;
  UCHAR                           Vendor[8];
  UCHAR                           Model[40];
  UCHAR                           FirmwareRevision[16];
  UCHAR                           PhysicalLocation[32];
  BOOLEAN                         ExpandedConnector;
  UCHAR                           Reserved0[3];
  ULONG                           Reserved1[3];
} STORAGE_PHYSICAL_ADAPTER_DATA, *PSTORAGE_PHYSICAL_ADAPTER_DATA;
````


## -struct-fields
<dl>

### -field <b>AdapterId</b>

<dd>
<p>The hardware ID of the storage adapter.</p>
</dd>

### -field <b>HealthStatus</b>

<dd>
<p>Indicates the health status of a storage adapter, of type <a href="..\ntddstor\ne-ntddstor--storage-component-health-status.md">STORAGE_COMPONENT_HEALTH_STATUS</a>.</p>
</dd>

### -field <b>CommandProtocol</b>

<dd>
<p>Specifies the storage command protocols that are used between software and hardware, of type <a href="..\ntddstor\ne-ntddstor--storage-protocol-type.md">STORAGE_PROTOCOL_TYPE</a>.</p>
</dd>

### -field <b>SpecVersion</b>

<dd>
<p>Indicates the specification of the storage adapter, of type <a href="..\ntddstor\ns-ntddstor--storage-spec-version.md">STORAGE_SPEC_VERSION</a>.</p>
</dd>

### -field <b>Vendor[8]</b>

<dd>
<p>The vendor name of the storage adapter.</p>
</dd>

### -field <b>Model[40]</b>

<dd>
<p>The model name of the storage adapter.</p>
</dd>

### -field <b>FirmwareRevision[16]</b>

<dd>
<p>The revision number of the storage adapter.</p>
</dd>

### -field <b>PhysicalLocation[32]</b>

<dd>
<p>This member is reserved for future use.</p>
</dd>

### -field <b>ExpandedConnector</b>

<dd>
<p>Specifies if the storage adapter includes an expanded connector.</p>
</dd>

### -field <b>Reserved0[3]</b>

<dd>
<p>Specifies if the storage adapter is reserved.</p>
</dd>

### -field <b>Reserved1[3]</b>

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