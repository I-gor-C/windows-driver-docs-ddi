---
UID: NF.dbgeng.IDebugControl3.AddBreakpoint
title: IDebugControl3::AddBreakpoint
author: windows-driver-content
description: The AddBreakpoint method creates a new breakpoint for the current target.
old-location: debugger\addbreakpoint.htm
ms.assetid: 08452b54-158f-4dca-86d8-34cc3f96bc62
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
req.alt-api: IDebugControl.AddBreakpoint,IDebugControl2.AddBreakpoint,IDebugControl3.AddBreakpoint
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
ms.keywords: IDebugControl3, AddBreakpoint, IDebugControl3::AddBreakpoint
req.iface: IDebugControl3
---

# IDebugControl3::AddBreakpoint method



## -description
<p>The <b>AddBreakpoint</b>  method creates a new breakpoint for the current target.</p>


## -syntax

````
HRESULT AddBreakpoint(
  [in]  ULONG            Type,
  [in]  ULONG            DesiredId,
  [out] IDebugBreakpoint **Bp
);
````


## -parameters
<dl>

### -param <i>Type</i> [in]

<dd>
<p>Specifies the breakpoint type of the new breakpoint.  This can be either of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_BREAKPOINT_CODE</p>
</td>
<td>
<p><a href="debugger.s#software_breakpoint#software_breakpoint"><i>software breakpoint</i></a></p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_BREAKPOINT_DATA</p>
</td>
<td>
<p><a href="debugger.p#processor_breakpoint#processor_breakpoint"><i>processor breakpoint</i></a></p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>DesiredId</i> [in]

<dd>
<p>Specifies the desired ID of the new breakpoint.  If it is DEBUG_ANY_ID, the engine will pick an unused ID.</p>
</dd>

### -param <i>Bp</i> [out]

<dd>
<p>Receives an interface pointer to the new breakpoint.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The breakpoint couldn't be created with the desired ID or the value of <i>Type</i> was not recognized.</p>

<p> </p>

<p>This method may also return other error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p>

## -remarks
<p>If <i>DesiredId</i> is not DEBUG_ANY_ID and another breakpoint already uses the ID <i>DesiredId</i>, these methods will fail.</p>

<p>Breakpoints are created empty and disabled.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff560075">Using Breakpoints</a> for details on configuring and enabling the breakpoint.</p>

<p>The client is saved as the adder of the new breakpoint. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff545576">GetAdder</a>. </p>

<p>If <i>DesiredId</i> is not DEBUG_ANY_ID and another breakpoint already uses the ID <i>DesiredId</i>, these methods will fail.</p>

<p>Breakpoints are created empty and disabled.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff560075">Using Breakpoints</a> for details on configuring and enabling the breakpoint.</p>

<p>The client is saved as the adder of the new breakpoint. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff545576">GetAdder</a>. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550508">IDebugControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550512">IDebugControl2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550519">IDebugControl3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538928">Breakpoints</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560075">Using Breakpoints</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549812">IDebugBreakpoint</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554487">RemoveBreakpoint</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::AddBreakpoint method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
