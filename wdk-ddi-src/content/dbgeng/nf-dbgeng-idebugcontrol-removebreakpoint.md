---
UID: NF.dbgeng.IDebugControl.RemoveBreakpoint
title: IDebugControl::RemoveBreakpoint
author: windows-driver-content
description: The RemoveBreakpoint method removes a breakpoint.
old-location: debugger\removebreakpoint.htm
old-project: debugger
ms.assetid: ce0f5e42-3f4e-48e1-9e73-96bca96e8e23
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl, RemoveBreakpoint, IDebugControl::RemoveBreakpoint
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
req.alt-api: IDebugControl.RemoveBreakpoint,IDebugControl2.RemoveBreakpoint,IDebugControl3.RemoveBreakpoint
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
req.iface: IDebugControl
---

# IDebugControl::RemoveBreakpoint method



## -description
<p>The <b>RemoveBreakpoint</b>  method removes a breakpoint.</p>


## -syntax

````
HRESULT RemoveBreakpoint(
  [in] PDEBUG_BREAKPOINT Bp
);
````


## -parameters
<dl>

### -param <i>Bp</i> [in]

<dd>
<p>Specifies an interface pointer to breakpoint to remove.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method may also return other error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p>

## -remarks
<p>After <b>RemoveBreakpoint</b> and <b>RemoveBreakpoint2</b> are called, the breakpoint object specified in the <i>Bp</i> parameter must not be used again.</p>

<p>For more details, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560075">Using Breakpoints</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugcontrol.md">IDebugControl</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol2.md">IDebugControl2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugbreakpoint.md">IDebugBreakpoint</a>
</dt>
<dt>
<a href="debugger.addbreakpoint">AddBreakpoint</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::RemoveBreakpoint method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
