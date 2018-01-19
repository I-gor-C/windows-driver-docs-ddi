---
UID : NE:ntddstor._STORAGE_PROTOCOL_TYPE
title : _STORAGE_PROTOCOL_TYPE
author : windows-driver-content
description : This enumeration is used to define the different storage command protocols that are used between software and hardware.
old-location : storage\storage_protocol_type.htm
old-project : storage
ms.assetid : 3CC4DF0A-26F1-4825-AD89-D56B0D5F4AC6
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _STORAGE_PROTOCOL_TYPE, *PSTORAGE_PROTOCOL_TYPE, STORAGE_PROTOCOL_TYPE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ntddstor.h
req.include-header : Ntddstor.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : STORAGE_PROTOCOL_TYPE
req.alt-loc : Ntddstor.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PSTORAGE_PROTOCOL_TYPE, STORAGE_PROTOCOL_TYPE"
---

# _STORAGE_PROTOCOL_TYPE Enumeration
This enumeration is used to define the different storage command protocols that are used between software and hardware.

## Syntax
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

## Constants

<table>

<tr>
<td>ProtocolTypeAta</td>
<td>ATA protocol type.</td>
</tr>

<tr>
<td>ProtocolTypeMaxReserved</td>
<td>Reserved.</td>
</tr>

<tr>
<td>ProtocolTypeNvme</td>
<td>NVMe protocol type.</td>
</tr>

<tr>
<td>ProtocolTypeProprietary</td>
<td>Vendor-specific protocol type.</td>
</tr>

<tr>
<td>ProtocolTypeScsi</td>
<td>SCSI protocol type.</td>
</tr>

<tr>
<td>ProtocolTypeSd</td>
<td>SD protocol type.</td>
</tr>

<tr>
<td>ProtocolTypeUfs</td>
<td>UFS protocol type.</td>
</tr>

<tr>
<td>ProtocolTypeUnknown</td>
<td>Unknown protocol type.</td>
</tr>
</table>

## Remarks

Protocol types that are 128 (0x80) and above in value are reserved for Microsoft use.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddstor.h (include Ntddstor.h) |