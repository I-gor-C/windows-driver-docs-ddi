---
UID: NS.compstui._OPTCOMBO
title: OPTCOMBO
author: windows-driver-content
description: TBD.
old-location: print\optcombo.htm
ms.assetid: B1F5A79A-8F64-4B7B-ADB4-BDD8EC17F22E
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: print
req.header: compstui.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OPTCOMBO
req.alt-loc: 
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
ms.keywords: OPTCOMBO, OPTCOMBO, *POPTCOMBO
req.iface: 
---

# OPTCOMBO structure



## -description
<p>TBD</p>


## -syntax

````
typedef struct _OPTCOMBO {
  WORD      cbSize;
  BYTE      Flags;
  WORD      cListItem;
  POPTPARAM pListItem;
  LONG      Sel;
  LONG      dwReserved[3];
} OPTCOMBO, *POPTCOMBO;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>cListItem</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>pListItem</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>Sel</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>dwReserved</b>

<dd>
<p>TBD</p>
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
<dt>Compstui.h</dt>
</dl>
</td>
</tr>
</table>