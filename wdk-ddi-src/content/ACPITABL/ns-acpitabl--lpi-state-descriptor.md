---
UID: NS.acpitabl._LPI_STATE_DESCRIPTOR
title: LPI_STATE_DESCRIPTOR
author: windows-driver-content
description: Defines an LPI state descriptor.
old-location: acpi\lpi_state_descriptor.htm
ms.assetid: B52012DB-922A-43A2-A175-7F7887C290F1
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: acpi
req.header: acpitabl.h
req.include-header: Acpitabl.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: LPI_STATE_DESCRIPTOR
req.alt-loc: acpitabl.h
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
ms.keywords: LPI_STATE_DESCRIPTOR, LPI_STATE_DESCRIPTOR, *PLPI_STATE_DESCRIPTOR
---

# LPI_STATE_DESCRIPTOR structure



## -description
<p>Defines an LPI state descriptor.</p>


## -syntax

````
typedef struct _LPI_STATE_DESCRIPTOR {
  ULONG           Type;
  ULONG           Length;
  USHORT          UniqueId;
  UCHAR           Reserved[2];
  LPI_STATE_FLAGS Flags;
  GEN_ADDR        EntryTrigger;
  ULONG           Residency;
  ULONG           Latency;
  GEN_ADDR        ResidencyCounter;
  ULONGLONG       ResidencyCounterFrequency;
} LPI_STATE_DESCRIPTOR, *PLPI_STATE_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>The type.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>The length.</p>
</dd>

### -field <b>UniqueId</b>

<dd>
<p>A unique ID.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>State flags.</p>
</dd>

### -field <b>EntryTrigger</b>

<dd>
<p>An entry trigger.</p>
</dd>

### -field <b>Residency</b>

<dd>
<p>A residency value.</p>
</dd>

### -field <b>Latency</b>

<dd>
<p>A latency value.</p>
</dd>

### -field <b>ResidencyCounter</b>

<dd>
<p>Residency counter.</p>
</dd>

### -field <b>ResidencyCounterFrequency</b>

<dd>
<p>Residency counter frequency. </p>
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
<dt>Acpitabl.h (include Acpitabl.h)</dt>
</dl>
</td>
</tr>
</table>