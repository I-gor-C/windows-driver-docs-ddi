---
UID: NF.wdbgexts.SearchMemory
title: SearchMemory
author: windows-driver-content
description: The SearchMemory function searches the target's virtual memory for a specified pattern of bytes.
old-location: debugger\searchmemory.htm
old-project: debugger
ms.assetid: 7e07c47e-803b-44fa-9d0f-aa86475246d2
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SearchMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdbgexts.h
req.include-header: Wdbgexts.h, Wdbgexts.h, Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SearchMemory
req.alt-loc: wdbgexts.h
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

# SearchMemory function



## -description
<p>The <b>SearchMemory</b> function searches the target's virtual memory for a specified pattern of bytes.</p>


## -syntax

````
__inline VOID SearchMemory(
   ULONG64  SearchAddress,
   ULONG64  SearchLength,
   ULONG    PatternLength,
   PVOID    Pattern,
   PULONG64 FoundAddress
);
````


## -parameters
<dl>

### -param <i>SearchAddress</i> 

<dd>
<p>Specifies the address in the target's virtual memory from which to start the search.</p>
</dd>

### -param <i>SearchLength</i> 

<dd>
<p>Specifies the size, in bytes, of the memory to search.  For a successful match, the pattern must be found before <i>SearchLength</i> bytes have been examined.</p>
</dd>

### -param <i>PatternLength</i> 

<dd>
<p>Specifies the size, in bytes, of the pattern to search for.</p>
</dd>

### -param <i>Pattern</i> 

<dd>
<p>Specifies the pattern to search for.</p>
</dd>

### -param <i>FoundAddress</i> 

<dd>
<p>Receives the location of the pattern, found in the target's virtual memory.  If the pattern was not found, the value in <i>FoundAddress</i> is unchanged by this function.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdbgexts.h (include Wdbgexts.h, Wdbgexts.h, or Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>