---
UID: NF.wdbgexts.WriteMsr
title: WriteMsr
author: windows-driver-content
description: The WriteMsr function writes to a Model-Specific Register (MSR).
old-location: debugger\writemsr.htm
ms.assetid: a88c2c74-ab9a-4d9a-aeb7-d08bfe497da4
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
req.alt-api: WriteMsr
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
ms.keywords: WriteMsr
req.iface: 
req.product: Windows 10 or later.
---

# WriteMsr function



## -description
<p>The <b>WriteMsr</b> function writes to a Model-Specific Register (MSR). </p>


## -syntax

````
HRESULT WriteMsr(
  [in] ULONG   MsrReg,
  [in] ULONG64 MsrValue
);
````


## -parameters
<dl>

### -param <i>MsrReg</i> [in]

<dd>
<p>Specifies the ID number of the MSR.</p>
</dd>

### -param <i>MsrValue</i> [in]

<dd>
<p>Specifies the new value of the MSR.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>For a WdbgExts extension, include wdbgexts.h. For a DbgEng extension, include wdbgexts.h before dbgeng.h. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff561480">Writing DbgEng Extension Code</a> for details.</p>

<p>For a WdbgExts extension, include wdbgexts.h. For a DbgEng extension, include wdbgexts.h before dbgeng.h. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff561480">Writing DbgEng Extension Code</a> for details.</p>

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
<dt>Dbgeng.h (include Wdbgexts.h, Wdbgexts.h, or Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>