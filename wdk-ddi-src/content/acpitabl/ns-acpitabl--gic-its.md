---
UID: NS.acpitabl._GIC_ITS
title: GIC_ITS
author: windows-driver-content
description: This topic describes the GIC_ITS structure.
old-location: acpi\gic_its.htm
old-project: acpi
ms.assetid: C0DA1B09-230E-4DE6-98CD-F80243D63B95
ms.author: windowsdriverdev
ms.date: 11/16/2017
ms.keywords: GIC_ITS, GIC_ITS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: acpitabl.h
req.include-header: Acpitabl.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709 and later versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GIC_ITS
req.alt-loc: Acpitabl.h
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

# GIC_ITS structure



## -description
<p>This topic describes the <b>GIC_ITS</b> structure.</p>


## -syntax

````
typedef struct _GIC_ITS {
  UCHAR     Type;
  UCHAR     Length;
  USHORT    Reserved1;
  ULONG     Identifier;
  ULONGLONG PhysicalAddress;
  ULONG     Reserved2;
} GIC_ITS;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>Defines the <b>UCHAR</b> member <b>Type</b>.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>Defines the <b>UCHAR</b> member <b>Length</b>.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>Identifier</b>

<dd>
<p>Defines the <b>ULONG</b> member <b>Identifier</b>.</p>
</dd>

### -field <b>PhysicalAddress</b>

<dd>
<p>Defines the <b>ULONGLONG</b> member <b>PhysicalAddress</b>.</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved for future use.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Windows 10, version 1709 and later versions.</p>
</td>
</tr>
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