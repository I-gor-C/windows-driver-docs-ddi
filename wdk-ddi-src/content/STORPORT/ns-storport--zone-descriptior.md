---
UID: NS.storport._ZONE_DESCRIPTIOR
title: ZONE_DESCRIPTIOR
author: windows-driver-content
description: Note  This structure is for internal use only and should not be called from your code. .
old-location: storage\zone_descriptior.htm
ms.assetid: 8326f683-3952-486e-b322-80ce96759366
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: storport.h
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
req.irql: 
ms.keywords: ZONE_DESCRIPTIOR, ZONE_DESCRIPTIOR, *PZONE_DESCRIPTIOR
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

### -field <b>ZoneType</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>Reset</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>Non_Seq</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>ZoneCondition</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>Reserved3</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>ZoneLength</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>ZoneStartLBA</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>WritePointerLBA</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>Reserved4</b>

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