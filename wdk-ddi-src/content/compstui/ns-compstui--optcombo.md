---
UID: NS.compstui._OPTCOMBO
title: OPTCOMBO
author: windows-driver-content
description: .
old-location: print\optcombo.htm
old-project: print
ms.assetid: B1F5A79A-8F64-4B7B-ADB4-BDD8EC17F22E
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: OPTCOMBO, OPTCOMBO, *POPTCOMBO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: compstui.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OPTCOMBO
req.alt-loc: Compstui.h
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

# OPTCOMBO structure



## -description
<p></p>


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

<dd></dd>

### -field <b>Flags</b>

<dd></dd>

### -field <b>cListItem</b>

<dd></dd>

### -field <b>pListItem</b>

<dd></dd>

### -field <b>Sel</b>

<dd></dd>

### -field <b>dwReserved</b>

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
<dt>Compstui.h</dt>
</dl>
</td>
</tr>
</table>