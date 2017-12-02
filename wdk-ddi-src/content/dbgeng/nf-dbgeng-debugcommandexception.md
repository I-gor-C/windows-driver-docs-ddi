---
UID: NF.dbgeng.DebugCommandException
title: DebugCommandException
author: windows-driver-content
description: Specifies a debug command exception.
old-location: debugger\debugcommandexception.htm
old-project: debugger
ms.assetid: 6DC67840-B985-45D0-8E81-671C3DC1EBC2
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DebugCommandException
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DebugCommandException
req.alt-loc: dbgeng.h
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

# DebugCommandException function



## -description
<p>Specifies a debug command exception.</p>


## -syntax

````
void WINAPI DebugCommandException(
   ULONG Command,
   ULONG ArgSize,
   PVOID Arg
);
````


## -parameters
<dl>

### -param Command 

<dd>
<p>A command.</p>
</dd>

### -param ArgSize 

<dd>
<p>The size of the argument.</p>
</dd>

### -param Arg 

<dd>
<p>A pointer to an argument.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>