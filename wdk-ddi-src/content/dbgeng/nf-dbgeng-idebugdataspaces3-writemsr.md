---
UID: NF.dbgeng.IDebugDataSpaces3.WriteMsr
title: IDebugDataSpaces3::WriteMsr
author: windows-driver-content
description: The WriteMsr method writes a value to the specified Model-Specific Register (MSR).
old-location: debugger\writemsr2.htm
old-project: debugger
ms.assetid: c9838b9e-b390-455d-98d6-249a49c9165d
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugDataSpaces3, WriteMsr, IDebugDataSpaces3::WriteMsr
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugDataSpaces.WriteMsr,IDebugDataSpaces2.WriteMsr,IDebugDataSpaces3.WriteMsr,IDebugDataSpaces4.WriteMsr
req.alt-loc: Dbgeng.h
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
req.iface: IDebugDataSpaces3
---

# IDebugDataSpaces3::WriteMsr method



## -description
<p>The <b>WriteMsr</b> method writes a value to the specified Model-Specific Register (MSR).</p>


## -syntax

````
HRESULT WriteMsr(
   ULONG   Msr,
   ULONG64 Value
);
````


## -parameters
<dl>

### -param <i>Msr</i> 

<dd>
<p>Specifies the MSR address.</p>
</dd>

### -param <i>Value</i> 

<dd>
<p>Specifies the value to write to the MSR.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p>

## -remarks
<p>This method is only available in kernel-mode debugging.</p>

<p>For details on the addresses and values of MSRs, see the processor documentation.</p>

<p>This method is only available in kernel-mode debugging.</p>

<p>For details on the addresses and values of MSRs, see the processor documentation.</p>

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
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>