---
UID: NF.dbgeng.IDebugDataSpaces4.StartEnumTagged
title: IDebugDataSpaces4::StartEnumTagged
author: windows-driver-content
description: The StartEnumTagged method initializes a enumeration over the tagged data associated with a debugger session.
old-location: debugger\startenumtagged.htm
old-project: debugger
ms.assetid: b79b1f09-baff-4071-a209-6fc399c9aef9
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugDataSpaces4, StartEnumTagged, IDebugDataSpaces4::StartEnumTagged
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
req.alt-api: IDebugDataSpaces3.StartEnumTagged,IDebugDataSpaces4.StartEnumTagged
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
req.iface: IDebugDataSpaces4
---

# IDebugDataSpaces4::StartEnumTagged method



## -description
<p>The <b>StartEnumTagged</b> method initializes a enumeration over the tagged data associated with a debugger session.</p>


## -syntax

````
HRESULT StartEnumTagged(
  [out] PULONG64 Handle
);
````


## -parameters
<dl>

### -param <i>Handle</i> [out]

<dd>
<p>Receives the handle identifying the enumeration.  This handle can be passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547874">GetNextTagged</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff542978">EndEnumTagged</a>.</p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The resources held by an enumeration created with this method can be released using <a href="https://msdn.microsoft.com/library/windows/hardware/ff542978">EndEnumTagged</a>.</p>

<p>The resources held by an enumeration created with this method can be released using <a href="https://msdn.microsoft.com/library/windows/hardware/ff542978">EndEnumTagged</a>.</p>

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