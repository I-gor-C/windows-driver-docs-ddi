---
UID: NE.ntddstor._STORAGE_PROTOCOL_TYPE
title: STORAGE_PROTOCOL_TYPE
author: windows-driver-content
description: This enumeration is used to define the different storage command protocols that are used between software and hardware.
old-location: storage\storage_protocol_type.htm
old-project: storage
ms.assetid: 3CC4DF0A-26F1-4825-AD89-D56B0D5F4AC6
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
req.alt-api: STORAGE_PROTOCOL_TYPE
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

# STORAGE_PROTOCOL_TYPE enumeration



## -description
<p>This enumeration is used to define the different storage command protocols that are used between software and hardware.</p>


## -syntax

````
typedef enum _STORAGE_PROTOCOL_TYPE { 
  ProtocolTypeUnknown      = 0,   // 0x0
  ProtocolTypeScsi,
  ProtocolTypeAta,
  ProtocolTypeNvme,
  ProtocolTypeSd,
  ProtocolTypeUfs,
  ProtocolTypeProprietary  = 126, // 0x7E
  ProtocolTypeMaxReserved  = 127 // 0x7F
} STORAGE_PROTOCOL_TYPE;
````


## -enum-fields
<dl>

### -field ProtocolTypeUnknown

<dd>
<p>Unknown protocol type.</p>
</dd>

### -field ProtocolTypeScsi

<dd>
<p>SCSI protocol type.</p>
</dd>

### -field ProtocolTypeAta

<dd>
<p>ATA protocol type.</p>
</dd>

### -field ProtocolTypeNvme

<dd>
<p>NVMe protocol type.</p>
</dd>

### -field ProtocolTypeSd

<dd>
<p>SD protocol type.</p>
</dd>

### -field ProtocolTypeUfs

<dd>
<p>UFS protocol type.</p>
</dd>

### -field ProtocolTypeProprietary

<dd>
<p> Vendor-specific protocol type.</p>
</dd>

### -field ProtocolTypeMaxReserved

<dd>
<p>Reserved.</p>
</dd>
</dl>

## -remarks
<p>Protocol types that are 128 (0x80) and above in value are reserved for Microsoft use.</p>

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