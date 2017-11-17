---
UID: NF.wdbgexts.GetInputLine
title: GetInputLine
author: windows-driver-content
description: The GetInputLine function requests an input string from the debugger.
old-location: debugger\getinputline.htm
ms.assetid: 18d4aae5-dd11-4c3a-8088-52121f46d208
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: wdbgexts.h
req.include-header: Wdbgexts.h, Wdbgexts.h, Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GetInputLine
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
ms.keywords: GetInputLine
req.iface: 
req.product: Windows 10 or later.
---

# GetInputLine function



## -description
<p>The <b>GetInputLine</b> function requests an input string from the debugger.</p>


## -syntax

````
__inline ULONG GetInputLine(
   PCSTR Prompt,
   PSTR  Buffer,
   ULONG BufferSize
);
````


## -parameters
<dl>

### -param <i>Prompt</i> 

<dd>
<p>Specifies a prompt to indicate what input is being requested.  The prompt is printed to the debugger's output before the input is gathered.  If <i>Prompt</i> is <b>NULL</b>, no prompt is printed.</p>
</dd>

### -param <i>Buffer</i> 

<dd>
<p>Specifies the buffer to receive the input.</p>
</dd>

### -param <i>BufferSize</i> 

<dd>
<p>Specifies the size, in characters, of the buffer <i>Buffer</i>.</p>
</dd>
</dl>

## -returns
<p><b>GetInputLine</b> returns the size, in characters, of the input returned to the <i>Buffer</i> buffer, or zero, if no input was returned.</p>

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