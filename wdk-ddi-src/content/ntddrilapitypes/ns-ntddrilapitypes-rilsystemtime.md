---
UID: NS.ntddrilapitypes.RILSYSTEMTIME
title: RILSYSTEMTIME
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsystemtime.htm
old-project: netvista
ms.assetid: da01963f-a0eb-4222-b0c7-20b924f65f66
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILSYSTEMTIME, RILSYSTEMTIME, *LPRILSYSTEMTIME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILSYSTEMTIME
req.alt-loc: ntddrilapitypes.h
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

# RILSYSTEMTIME structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>