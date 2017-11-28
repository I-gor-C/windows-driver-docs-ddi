---
UID: NF.dbgeng.IDebugDataSpaces3.ReadMsr
title: IDebugDataSpaces3::ReadMsr
author: windows-driver-content
description: The ReadMsr method reads a specified Model-Specific Register (MSR).
old-location: debugger\readmsr2.htm
old-project: debugger
ms.assetid: 3ffe53d9-ea57-4561-a889-e6369ef0d5d3
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugDataSpaces3, ReadMsr, IDebugDataSpaces3::ReadMsr
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
req.alt-api: IDebugDataSpaces.ReadMsr,IDebugDataSpaces2.ReadMsr,IDebugDataSpaces3.ReadMsr,IDebugDataSpaces4.ReadMsr
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
req.iface: IDebugDataSpaces3
---

# IDebugDataSpaces3::ReadMsr method



## -description
<p>The <b>ReadMsr</b> method reads a specified Model-Specific Register (MSR).</p>


## -syntax

````
HRESULT ReadMsr(
  [in]  ULONG    Msr,
  [out] PULONG64 Value
);
````


## -parameters
<dl>

### -param <i>Msr</i> [in]

<dd>
<p>Specifies the MSR address.</p>
</dd>

### -param <i>Value</i> [out]

<dd>
<p>Receives the value of the MSR.</p>
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