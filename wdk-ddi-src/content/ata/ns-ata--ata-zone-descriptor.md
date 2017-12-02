---
UID: NS.ata._ATA_ZONE_DESCRIPTOR
title: ATA_ZONE_DESCRIPTOR
author: windows-driver-content
description: This structure is for internal use only and should not be called from your code.
old-location: storage\ata_zone_descriptor.htm
old-project: storage
ms.assetid: 2e027ac5-7b5d-43cc-8d37-c0a3e77e68c9
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ATA_ZONE_DESCRIPTOR, ATA_ZONE_DESCRIPTOR, *PATA_ZONE_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ata.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ATA_ZONE_DESCRIPTOR
req.alt-loc: Ata.h
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

# ATA_ZONE_DESCRIPTOR structure



## -description
<p>This structure is for internal use only and should not be called from your code.</p>


## -syntax

````
typedef struct _ATA_ZONE_DESCRIPTOR {
  UCHAR     ZoneType  : 4;
  UCHAR     Reserved0  : 4;
  UCHAR     Reset  : 1;
  UCHAR     NonSeq : 1;
  UCHAR     Reserved1  : 2;
  UCHAR     ZoneCondition  : 4;
  UCHAR     Reserved2[6];
  ULONGLONG ZoneLength  : 48;
  ULONGLONG Reserved3  : 16;
  ULONGLONG ZoneStartLBA  : 48;
  ULONGLONG Reserved4  : 16;
  ULONGLONG WritePointerLBA  : 48;
  ULONGLONG Reserved5  : 16;
  UCHAR     Reserved6[32];
} ATA_ZONE_DESCRIPTOR, *PATA_ZONE_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field ZoneType  : 4

<dd>
<p>N/A</p>
</dd>

### -field Reserved0  : 4

<dd>
<p>N/A</p>
</dd>

### -field Reset  : 1

<dd>
<p>N/A</p>
</dd>

### -field NonSeq : 1

<dd>
<p>N/A</p>
</dd>

### -field Reserved1  : 2

<dd>
<p>N/A</p>
</dd>

### -field ZoneCondition  : 4

<dd>
<p>N/A</p>
</dd>

### -field Reserved2

<dd>
<p>N/A</p>
</dd>

### -field ZoneLength  : 48

<dd>
<p>N/A</p>
</dd>

### -field Reserved3  : 16

<dd>
<p>N/A</p>
<p>N/A</p>
</dd>

### -field ZoneStartLBA  : 48

<dd>
<p>N/A</p>
</dd>

### -field Reserved4  : 16

<dd>
<p>N/A</p>
</dd>

### -field WritePointerLBA  : 48

<dd>
<p>N/A</p>
</dd>

### -field Reserved5  : 16

<dd>
<p>N/A</p>
</dd>

### -field Reserved6

<dd>
<p>N/A</p>
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
<dt>Ata.h</dt>
</dl>
</td>
</tr>
</table>