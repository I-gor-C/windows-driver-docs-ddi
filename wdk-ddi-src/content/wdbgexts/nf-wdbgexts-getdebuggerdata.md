---
UID: NF.wdbgexts.GetDebuggerData
title: GetDebuggerData
author: windows-driver-content
description: The GetDebuggerData function retrieves information stored in a data block.
old-location: debugger\getdebuggerdata.htm
old-project: debugger
ms.assetid: a07afa2e-1f7d-4685-9ede-8b7805dd6583
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: GetDebuggerData
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
req.alt-api: GetDebuggerData
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

# GetDebuggerData function



## -description
<p>The <b>GetDebuggerData</b> function retrieves information stored in a data block.</p>


## -syntax

````
ULONG GetDebuggerData(
   ULONG Tag,
   PVOID Buf,
   ULONG Size
);
````


## -parameters
<dl>

### -param <i>Tag</i> 

<dd>
<p>This should be set equal to KDBG_TAG. (This value is specified in wdbgexts.h.)</p>
</dd>

### -param <i>Buf</i> 

<dd>
<p>Points to the debugger data block.</p>
</dd>

### -param <i>Size</i> 

<dd>
<p>Specifies the size of the data block, including the header.</p>
</dd>
</dl>

## -returns
<p>If the data block is found, the return value is <b>TRUE</b>; otherwise, it is <b>FALSE</b>.</p>

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