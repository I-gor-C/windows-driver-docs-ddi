---
UID: NF.dbgeng.IDebugControl3.GetInterruptTimeout
title: IDebugControl3::GetInterruptTimeout
author: windows-driver-content
description: The GetInterruptTimeout method returns the number of seconds that the engine will wait when requesting a break into the debugger.
old-location: debugger\getinterrupttimeout.htm
old-project: debugger
ms.assetid: 8faf167e-3110-453f-8234-32dfa543b520
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugControl3, GetInterruptTimeout, IDebugControl3::GetInterruptTimeout
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
req.alt-api: IDebugControl.GetInterruptTimeout,IDebugControl2.GetInterruptTimeout,IDebugControl3.GetInterruptTimeout
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

# IDebugControl3::GetInterruptTimeout method



## -description
<p>The <b>GetInterruptTimeout</b> method returns the number of seconds that the engine will wait when requesting a break into the debugger.</p>


## -syntax

````
HRESULT GetInterruptTimeout(
  [out] PULONG Seconds
);
````


## -parameters
<dl>

### -param Seconds [out]

<dd>
<p>Receives the number of seconds that the engine will wait for the target when requesting a break into the debugger.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The engine requests a break into the debugger when <a href="debugger.setinterrupt">SetInterrupt</a> is called with DEBUG_INTERRUPT_ACTIVE.  If this interrupt times out, the engine will generate a synthetic exception event.  This event will be sent to <a href="debugger.using_callback_objects#event_callbacks#event_callbacks">event callback objects</a>'s <a href="debugger.idebugeventcallbacks_exception">IDebugEventCallbacks::Exception</a> method.</p>

<p>Most targets do not support interrupt time-outs.  Live user-mode debugging is one of the targets that does support them.</p>

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
<a href="debugger.idebugeventcallbacks_exception">IDebugEventCallbacks::Exception</a>
</dt>
<dt>
<a href="debugger.setinterrupt">SetInterrupt</a>
</dt>
<dt>
<a href="debugger.setinterrupttimeout">SetInterruptTimeout</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::GetInterruptTimeout method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
