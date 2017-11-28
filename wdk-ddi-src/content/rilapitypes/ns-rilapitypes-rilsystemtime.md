---
UID: NS.rilapitypes.RILSYSTEMTIME
title: RILSYSTEMTIME
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsystemtime_2.htm
old-project: netvista
ms.assetid: 436fd67e-6696-4079-9bcf-7260de3bbc00
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILSYSTEMTIME, RILSYSTEMTIME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILSYSTEMTIME
req.alt-loc: rilapitypes.h
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
req.product: Windows 10 or later.
---

# RILSYSTEMTIME structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILSYSTEMTIME {
  WORD  wYear;
  WORD  wMonth;
  WORD  wDayOfWeek;
  WORD  wDay;
  WORD  wHour;
  WORD  wMinute;
  WORD  wSecond;
  WORD  wMilliseconds;
} RILSYSTEMTIME, RILSYSTEMTIME;
````


## -struct-fields
<dl>

### -field <b>wYear</b>

<dd></dd>

### -field <b>wMonth</b>

<dd></dd>

### -field <b>wDayOfWeek</b>

<dd></dd>

### -field <b>wDay</b>

<dd></dd>

### -field <b>wHour</b>

<dd></dd>

### -field <b>wMinute</b>

<dd></dd>

### -field <b>wSecond</b>

<dd></dd>

### -field <b>wMilliseconds</b>

<dd></dd>
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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>