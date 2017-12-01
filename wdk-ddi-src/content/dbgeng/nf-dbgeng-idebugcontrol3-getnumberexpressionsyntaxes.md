---
UID: NF.dbgeng.IDebugControl3.GetNumberExpressionSyntaxes
title: IDebugControl3::GetNumberExpressionSyntaxes
author: windows-driver-content
description: The GetNumberExpressionSyntaxes method returns the number of expression syntaxes that are supported by the engine.
old-location: debugger\getnumberexpressionsyntaxes.htm
old-project: debugger
ms.assetid: eb96dd47-300a-49b7-b3c3-ee3bcb6662ba
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl3, GetNumberExpressionSyntaxes, IDebugControl3::GetNumberExpressionSyntaxes
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
req.alt-api: IDebugControl3.GetNumberExpressionSyntaxes
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
req.iface: IDebugControl3
---

# IDebugControl3::GetNumberExpressionSyntaxes method



## -description
<p>The <b>GetNumberExpressionSyntaxes</b> method returns the number of expression syntaxes that are supported by the engine.</p>


## -syntax

````
HRESULT GetNumberExpressionSyntaxes(
  [out] PULONG Number
);
````


## -parameters
<dl>

### -param <i>Number</i> [out]

<dd>
<p>Receives the number of expression syntaxes.</p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

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
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>
</dt>
<dt>
<a href="debugger.evaluate">Evaluate</a>
</dt>
<dt>
<a href="debugger.getexpressionsyntaxnames">GetExpressionSyntaxNames</a>
</dt>
<dt>
<a href="debugger.setexpressionsyntaxbyname">SetExpressionSyntaxByName</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl3::GetNumberExpressionSyntaxes method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
