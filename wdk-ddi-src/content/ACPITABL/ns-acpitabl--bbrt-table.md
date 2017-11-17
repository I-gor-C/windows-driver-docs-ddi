---
UID: NS.acpitabl._BBRT_TABLE
title: BBRT_TABLE
author: windows-driver-content
description: Defines a Boot Background Resource Table.
old-location: acpi\bbrt_table.htm
ms.assetid: 0FC4D7BA-4292-4D87-8982-D20D267D6FA5
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
req.alt-api: BBRT_TABLE
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
ms.keywords: BBRT_TABLE, BBRT_TABLE, *PBBRT_TABLE
---

# BBRT_TABLE structure



## -description
<p>Defines a Boot Background Resource Table.</p>


## -syntax

````
typedef struct _BBRT_TABLE {
  DESCRIPTION_HEADER Header;
  ULONG              Background;
  ULONG              Foreground;
} BBRT_TABLE, *PBBRT_TABLE;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>A header.</p>
</dd>

### -field <b>Background</b>

<dd>
<p>A background value.</p>
</dd>

### -field <b>Foreground</b>

<dd>
<p>A foreground value. </p>
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