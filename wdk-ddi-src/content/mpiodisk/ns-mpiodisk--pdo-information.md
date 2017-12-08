---
UID: NS.mpiodisk._PDO_INFORMATION
title: PDO_INFORMATION
author: windows-driver-content
description: The PDO_INFORMATION structure represents a device-path pairing, which is an instance of a LUN through a particular path.
old-location: storage\pdo_information.htm
old-project: storage
ms.assetid: 26ce460f-b12d-4e5e-994a-047a1853325d
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PDO_INFORMATION, PDO_INFORMATION, *PPDO_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: mpiodisk.h
req.include-header: Mpiowmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PDO_INFORMATION
req.alt-loc: mpiodisk.h
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

# PDO_INFORMATION structure



## -description
<p>The PDO_INFORMATION structure represents a device-path pairing, which is an instance of a LUN through a particular path.</p>


## -syntax

````
typedef struct _PDO_INFORMATION {
  PDOSCSI_ADDR ScsiAddress;
  ULONG        DeviceState;
  ULONGLONG    PathIdentifier;
  ULONG        IdentifierType;
  ULONG        IdentifierLength;
  UCHAR        Identifier[32];
  UCHAR        Pad[4];
} PDO_INFORMATION, *PPDO_INFORMATION;
````


## -struct-fields
<dl>

### -field ScsiAddress

<dd>
<p>A PDOSCSI_ADDR structure that represents the SCSI address of the LUN's instance that corresponds to a particular path.</p>
</dd>

### -field DeviceState

<dd>
<p>An unsigned 32-bitfield that represents whether the path, through which this instance of the LUN was exposed, is usable.</p>
</dd>

### -field PathIdentifier

<dd>
<p>An unsigned 64-bitfield that represents the identifier that is associated with the path through which this instance of the LUN is exposed.</p>
</dd>

### -field IdentifierType

<dd>
<p>An unsigned 32-bitfield that represents the identifier type of the LUN's controller.</p>
</dd>

### -field IdentifierLength

<dd>
<p>An unsigned 32-bitfield that represents the length of the identifier of the LUN's controller.</p>
</dd>

### -field Identifier

<dd>
<p>An unsigned 64-bitfield that represents the identifier that is associated with the path through which this instance of the LUN is exposed.</p>
</dd>

### -field Pad

<dd>
<p>Should be zero.</p>
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
<dt>Mpiodisk.h (include Mpiowmi.h)</dt>
</dl>
</td>
</tr>
</table>