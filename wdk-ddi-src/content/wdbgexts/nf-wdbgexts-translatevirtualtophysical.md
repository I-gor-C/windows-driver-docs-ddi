---
UID: NF.wdbgexts.TranslateVirtualToPhysical
title: TranslateVirtualToPhysical
author: windows-driver-content
description: The TranslateVirtualToPhysical function translates a virtual memory address into a physical memory address.
old-location: debugger\translatevirtualtophysical.htm
old-project: debugger
ms.assetid: 803f766a-e02f-4b9c-bfe0-6197e0f2855c
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: TranslateVirtualToPhysical
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdbgexts.h
req.include-header: Wdbgexts.h, Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TranslateVirtualToPhysical
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

# TranslateVirtualToPhysical function



## -description
<p>The <b>TranslateVirtualToPhysical</b> function translates a virtual memory address into a physical memory address.</p>


## -syntax

````
__inline BOOL TranslateVirtualToPhysical(
   ULONG64 Virtual,
   ULONG64 *Physical
);
````


## -parameters
<dl>

### -param Virtual 

<dd>
<p>Specifies the virtual memory address to translate.</p>
</dd>

### -param Physical 

<dd>
<p>Receives the physical memory address.</p>
</dd>
</dl>

## -returns
<p>If the function succeeds, the return value is <b>TRUE</b>; otherwise, it is <b>FALSE</b>.</p>

## -remarks
<p>This function is only available in kernel-mode debugging.</p>

<p>If you are writing a WdbgExts extension, include wdbgexts.h. If you are writing a DbgEng extension that calls this function, include wdbgexts.h before dbgeng.h (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561480">Writing DbgEng Extension Code</a> for details.)</p>

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
<dt>Wdbgexts.h (include Wdbgexts.h or Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>