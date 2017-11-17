---
UID: NF.dbgeng.IDebugDataSpaces4.EndEnumTagged
title: IDebugDataSpaces4::EndEnumTagged
author: windows-driver-content
description: The EndEnumTagged method releases the resources used by the specified enumeration.
old-location: debugger\endenumtagged.htm
ms.assetid: 6a456b8c-aec6-443d-8db4-21e7715ab818
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugDataSpaces3.EndEnumTagged,IDebugDataSpaces4.EndEnumTagged
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
ms.keywords: IDebugDataSpaces4, EndEnumTagged, IDebugDataSpaces4::EndEnumTagged
req.iface: IDebugDataSpaces4
---

# IDebugDataSpaces4::EndEnumTagged method



## -description
<p>The <b>EndEnumTagged</b> method releases the resources used by the specified enumeration.</p>


## -syntax

````
HRESULT EndEnumTagged(
  [in] ULONG64 Handle
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>Specifies the handle identifying the enumeration.  This is the handle returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff558801">StartEnumTagged</a>.</p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>After a handle has been passed to this method it is no longer valid and must not be used again.</p>

<p>After a handle has been passed to this method it is no longer valid and must not be used again.</p>

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