---
UID: NS.dbgeng._DEBUG_CACHED_SYMBOL_INFO
title: DEBUG_CACHED_SYMBOL_INFO
author: windows-driver-content
description: Defines information about cached symbols.
old-location: debugger\debug_cached_symbol_info.htm
old-project: debugger
ms.assetid: CC7914B6-DCE1-45D1-84D3-5FF1449AD565
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: DEBUG_CACHED_SYMBOL_INFO, DEBUG_CACHED_SYMBOL_INFO, *PDEBUG_CACHED_SYMBOL_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dbgeng.h
req.include-header: DbgEng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEBUG_CACHED_SYMBOL_INFO
req.alt-loc: DbgEng.h
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
req.iface: IDebugSystemObjects4
---

# DEBUG_CACHED_SYMBOL_INFO structure



## -description
<p>Defines information about cached symbols.</p>


## -syntax

````
typedef struct _DEBUG_CACHED_SYMBOL_INFO {
  ULONG64 ModBase;
  ULONG64 Arg1;
  ULONG64 Arg2;
  ULONG   Id;
  ULONG   Arg3;
} DEBUG_CACHED_SYMBOL_INFO, *PDEBUG_CACHED_SYMBOL_INFO;
````


## -struct-fields
<dl>

### -field <b>ModBase</b>

<dd>
<p>A module base.</p>
</dd>

### -field <b>Arg1</b>

<dd>
<p>An argument value.</p>
</dd>

### -field <b>Arg2</b>

<dd>
<p>An argument value.</p>
</dd>

### -field <b>Id</b>

<dd>
<p>An ID.</p>
</dd>

### -field <b>Arg3</b>

<dd>
<p>An argument value.</p>
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
<dt>DbgEng.h (include DbgEng.h)</dt>
</dl>
</td>
</tr>
</table>