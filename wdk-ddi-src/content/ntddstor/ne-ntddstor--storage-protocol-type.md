---
UID: NE.ntddstor._STORAGE_PROTOCOL_TYPE
title: STORAGE_PROTOCOL_TYPE
author: windows-driver-content
description: This enumeration is used to define the different storage command protocols that are used between software and hardware.
old-location: storage\storage_protocol_type.htm
ms.assetid: 3CC4DF0A-26F1-4825-AD89-D56B0D5F4AC6
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
ms.keywords: SERIALPERF_STATS, SERIALPERF_STATS, *PSERIALPERF_STATS
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

### -field <a id="ProtocolTypeUnknown"></a><a id="protocoltypeunknown"></a><a id="PROTOCOLTYPEUNKNOWN"></a><b>ProtocolTypeUnknown</b>

<dd>
<p>Unknown protocol type.</p>
</dd>

### -field <a id="ProtocolTypeScsi"></a><a id="protocoltypescsi"></a><a id="PROTOCOLTYPESCSI"></a><b>ProtocolTypeScsi</b>

<dd>
<p>SCSI protocol type.</p>
</dd>

### -field <a id="ProtocolTypeAta"></a><a id="protocoltypeata"></a><a id="PROTOCOLTYPEATA"></a><b>ProtocolTypeAta</b>

<dd>
<p>ATA protocol type.</p>
</dd>

### -field <a id="ProtocolTypeNvme"></a><a id="protocoltypenvme"></a><a id="PROTOCOLTYPENVME"></a><b>ProtocolTypeNvme</b>

<dd>
<p>NVMe protocol type.</p>
</dd>

### -field <a id="ProtocolTypeSd"></a><a id="protocoltypesd"></a><a id="PROTOCOLTYPESD"></a><b>ProtocolTypeSd</b>

<dd>
<p>SD protocol type.</p>
</dd>

### -field <a id="ProtocolTypeUfs"></a><a id="protocoltypeufs"></a><a id="PROTOCOLTYPEUFS"></a><b>ProtocolTypeUfs</b>

<dd>
<p>UFS protocol type.</p>
</dd>

### -field <a id="ProtocolTypeProprietary"></a><a id="protocoltypeproprietary"></a><a id="PROTOCOLTYPEPROPRIETARY"></a><b>ProtocolTypeProprietary</b>

<dd>
<p> Vendor-specific protocol type.</p>
</dd>

### -field <a id="ProtocolTypeMaxReserved"></a><a id="protocoltypemaxreserved"></a><a id="PROTOCOLTYPEMAXRESERVED"></a><b>ProtocolTypeMaxReserved</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>

## -remarks
<p>Protocol types that are 128 (0x80) and above in value are reserved for Microsoft use.</p>

<p>Protocol types that are 128 (0x80) and above in value are reserved for Microsoft use.</p>

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