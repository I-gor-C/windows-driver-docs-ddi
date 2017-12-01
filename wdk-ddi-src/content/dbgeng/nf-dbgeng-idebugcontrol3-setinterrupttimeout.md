---
UID: NF.dbgeng.IDebugControl3.SetInterruptTimeout
title: IDebugControl3::SetInterruptTimeout
author: windows-driver-content
description: The SetInterruptTimeout method sets the number of seconds that the debugger engine should wait when requesting a break into the debugger.
old-location: debugger\setinterrupttimeout.htm
old-project: debugger
ms.assetid: 93bc2a07-a6f7-45df-945d-81c6c53adb47
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl3, SetInterruptTimeout, IDebugControl3::SetInterruptTimeout
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
req.alt-api: IDebugControl.SetInterruptTimeout,IDebugControl2.SetInterruptTimeout,IDebugControl3.SetInterruptTimeout
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

# IDebugControl3::SetInterruptTimeout method



## -description
<p>The <b>SetInterruptTimeout</b> method sets the number of seconds that the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a> should wait when requesting a break into the debugger.</p>


## -syntax

````
HRESULT SetInterruptTimeout(
  [in] ULONG Seconds
);
````


## -parameters
<dl>

### -param <i>Seconds</i> [in]

<dd>
<p>Specifies the number of seconds that the engine should wait for the target when requesting a break into the debugger.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The engine requests a break into the debugger when <a href="debugger.setinterrupt">SetInterrupt</a> is called with the DEBUG_INTERRUPT_ACTIVE flag.  </p>

<p>If an interrupt times out, the engine will generate a synthetic exception event.  This event will be sent to <a href="debugger.using_callback_objects#event_callbacks#event_callbacks">event callback objects</a>'s <a href="debugger.idebugeventcallbacks_exception">IDebugEventCallbacks::Exception</a> method.</p>

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
<a href="debugger.getinterrupttimeout">GetInterruptTimeout</a>
</dt>
<dt>
<a href="debugger.idebugeventcallbacks_exception">IDebugEventCallbacks::Exception</a>
</dt>
<dt>
<a href="debugger.setinterrupt">SetInterrupt</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::SetInterruptTimeout method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
