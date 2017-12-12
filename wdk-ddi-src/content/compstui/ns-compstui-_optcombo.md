---
UID: NS.COMPSTUI._OPTCOMBO
title: _OPTCOMBO
author: windows-driver-content
description: .
old-location: print\optcombo.htm
old-project: print
ms.assetid: B1F5A79A-8F64-4B7B-ADB4-BDD8EC17F22E
ms.author: windowsdriverdev
ms.date: 12/9/2017
ms.keywords: _OPTCOMBO, *POPTCOMBO, OPTCOMBO
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
---

# _OPTCOMBO structure



## -description




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

### -field cbSize


### -field Flags


### -field cListItem


### -field pListItem


### -field Sel


### -field dwReserved


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Compstui.h</dt>
</dl>
</td>
</tr>
</table>