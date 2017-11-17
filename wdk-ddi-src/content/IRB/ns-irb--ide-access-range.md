---
UID: NS.irb._IDE_ACCESS_RANGE
title: IDE_ACCESS_RANGE
author: windows-driver-content
description: The IDE_ACCESS_RANGE structure contains the address ranges allocated for an IDE controller.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ide_access_range.htm
ms.assetid: e81441a2-0659-4d32-97f4-415abef6c87a
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: irb.h
req.include-header: Irb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDE_ACCESS_RANGE
req.alt-loc: irb.h
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
ms.keywords: IDE_ACCESS_RANGE, IDE_ACCESS_RANGE, *PIDE_ACCESS_RANGE
req.iface: 
---

# IDE_ACCESS_RANGE structure



## -description
<p>The IDE_ACCESS_RANGE structure contains the address ranges allocated for an IDE controller.</p>


## -syntax

````
typedef struct _IDE_ACCESS_RANGE {
  IDE_PHYSICAL_ADDRESS RangeStart;
  IDE_PHYSICAL_ADDRESS PhysicalRangeStart;
  ULONG                RangeLength;
  BOOLEAN              InMemory;
  UCHAR                Bar;
} IDE_ACCESS_RANGE, *PIDE_ACCESS_RANGE;
````


## -struct-fields
<dl>

### -field <b>RangeStart</b>

<dd>
<p>Contains the logical starting address of the address range.</p>
</dd>

### -field <b>PhysicalRangeStart</b>

<dd>
<p>Contains the physical starting address of the address range.</p>
</dd>

### -field <b>RangeLength</b>

<dd>
<p>Contains the size, in bytes, of the range.</p>
</dd>

### -field <b>InMemory</b>

<dd>
<p>Flag that indicates if this is a memory mapped resource. If cleared, this is an I/O port resource.</p>
</dd>

### -field <b>Bar</b>

<dd>
<p>The number of the PCI Base Address Range that this resource was found in.</p>
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
<dt>Irb.h (include Irb.h)</dt>
</dl>
</td>
</tr>
</table>