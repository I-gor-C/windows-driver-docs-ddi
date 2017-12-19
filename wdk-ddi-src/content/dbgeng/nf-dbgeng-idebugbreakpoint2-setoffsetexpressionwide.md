---
UID: NF.dbgeng.IDebugBreakpoint2.SetOffsetExpressionWide
title: IDebugBreakpoint2::SetOffsetExpressionWide method
author: windows-driver-content
description: The SetOffsetExpressionWide methods set an expression string that evaluates to the location that triggers a breakpoint.
old-location: debugger\setoffsetexpressionwide.htm
old-project: Debugger
ms.assetid: 1db89a5a-641b-4fca-bd60-217c9be8f19f
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IDebugBreakpoint2, IDebugBreakpoint2::SetOffsetExpressionWide, SetOffsetExpressionWide
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugBreakpoint2.SetOffsetExpressionWide
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
---

# IDebugBreakpoint2::SetOffsetExpressionWide method



## -description
The <b>SetOffsetExpressionWide</b> methods set an expression string that evaluates to the location that triggers a breakpoint.



## -syntax

````
HRESULT SetOffsetExpressionWide(
  [in] PCWSTR Expression
);
````


## -parameters

### -param Expression [in]

The expression string that evaluates to the location on the target that triggers the breakpoint.  If the engine scannot evaluate the expression (for example, if the expression contains a symbol that cannot be interpreted), the breakpoint is flagged as deferred. (For more information about deferred breakpoints, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff539284">Controlling Breakpoint Flags and Parameters</a>.)  For more information about the expression syntax, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560075">Using Breakpoints</a>.


## -returns

      This method might return one of the following values:
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.

 


## -remarks
For more information about how to use breakpoints, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560075">Using Breakpoints</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>