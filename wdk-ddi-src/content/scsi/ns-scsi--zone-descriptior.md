---
UID: NS.scsi._ZONE_DESCRIPTIOR
title: ZONE_DESCRIPTIOR
author: windows-driver-content
description: Note  This structure is for internal use only and should not be called from your code. .
old-location: storage\zone_descriptior.htm
old-project: storage
ms.assetid: 8326f683-3952-486e-b322-80ce96759366
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ZONE_DESCRIPTIOR, ZONE_DESCRIPTIOR, *PZONE_DESCRIPTIOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: scsi.h
req.include-header: Minitape.h, Storport.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZONE_DESCRIPTIOR
req.alt-loc: scsi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ZONE_DESCRIPTIOR structure



## -description
<p>
<div class="alert"><b>Note</b>  This  structure is for internal use only and should not be called from your code.</div>
<div> </div>
</p>


## -syntax

````
typedef struct _ZONE_DESCRIPTIOR {
  UCHAR      ZoneType  :4;
  UCHAR      Reserved1  :4;
  UCHAR  : 1 Reset  :1;
  UCHAR      Non_Seq  :1;
  UCHAR      Reserved2  :2;
  UCHAR      ZoneCondition  :4;
  UCHAR      Reserved3[6];
  UCHAR      ZoneLength[8];
  UCHAR      ZoneStartLBA[8];
  UCHAR      WritePointerLBA[8];
  UCHAR      Reserved4[32];
} ZONE_DESCRIPTIOR, *PZONE_DESCRIPTIOR;
````


## -struct-fields
<dl>

### -field ZoneType

<dd>
<p>N/A</p>
</dd>

### -field Reserved1

<dd>
<p>N/A</p>
</dd>

### -field Reset

<dd>
<p>N/A</p>
</dd>

### -field Non_Seq

<dd>
<p>N/A</p>
</dd>

### -field Reserved2

<dd>
<p>N/A</p>
</dd>

### -field ZoneCondition

<dd>
<p>N/A</p>
</dd>

### -field Reserved3

<dd>
<p>N/A</p>
</dd>

### -field ZoneLength

<dd>
<p>N/A</p>
</dd>

### -field ZoneStartLBA

<dd>
<p>N/A</p>
</dd>

### -field WritePointerLBA

<dd>
<p>N/A</p>
</dd>

### -field Reserved4

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
<dt>Scsi.h (include Minitape.h or Storport.h)</dt>
</dl>
</td>
</tr>
</table>