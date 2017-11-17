---
UID: NS.scsi._REPORT_ZONES_DATA
title: REPORT_ZONES_DATA
author: windows-driver-content
description: Note  This structure is for internal use only and should not be called from your code. .
old-location: storage\report_zones_data.htm
ms.assetid: 67785cb0-388c-4348-b32a-99bcd02b7c04
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: scsi.h
req.include-header: Minitape.h, Storport.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: REPORT_ZONES_DATA
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
ms.keywords: REPORT_ZONES_DATA, REPORT_ZONES_DATA, *PREPORT_ZONES_DATA
req.iface: 
req.product: Windows 10 or later.
---

# REPORT_ZONES_DATA structure



## -description
<p>
<div class="alert"><b>Note</b>  This  structure is for internal use only and should not be called from your code.</div>
<div> </div>
</p>


## -syntax

````
typedef struct _REPORT_ZONES_DATA {
  UCHAR            ZoneListLength[4];
  UCHAR            Same  :4;
  UCHAR            Reserved1  :4;
  UCHAR            Reserved2[4];
  UCHAR            MaxLBA[8];
  UCHAR            Reserved3[48];
#ifndef (__midl)
  ZONE_DESCRIPTIOR ZoneDescriptors[ANYSIZE_ARRAY];
#endif 
} REPORT_ZONES_DATA, *PREPORT_ZONES_DATA;
````


## -struct-fields
<dl>

### -field <b>ZoneListLength</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>Same</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>MaxLBA</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>Reserved3</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>ZoneDescriptors</b>

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