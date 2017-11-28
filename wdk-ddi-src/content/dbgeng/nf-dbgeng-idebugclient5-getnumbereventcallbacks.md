---
UID: NF.dbgeng.IDebugClient5.GetNumberEventCallbacks
title: IDebugClient5::GetNumberEventCallbacks
author: windows-driver-content
description: The GetNumberEventCallbacks method returns the number of event callbacks that are interested in the given events.
old-location: debugger\getnumbereventcallbacks.htm
old-project: debugger
ms.assetid: 02001bad-bafe-432d-bc07-011cb6981ae6
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugClient5, GetNumberEventCallbacks, IDebugClient5::GetNumberEventCallbacks
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
req.alt-api: IDebugClient5.GetNumberEventCallbacks
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
req.iface: IDebugClient5
---

# IDebugClient5::GetNumberEventCallbacks method



## -description
<p>The <b>GetNumberEventCallbacks</b> method returns the number of event callbacks that are interested in the given <a href="debugger.events#events#events">events</a>.</p>


## -syntax

````
HRESULT GetNumberEventCallbacks(
  [in]  ULONG  EventFlags,
  [out] PULONG Count
);
````


## -parameters
<dl>

### -param <i>EventFlags</i> [in]

<dd>
<p>Specifies a set of events used to filter out some of the event callbacks; only event callbacks that have indicated an interest in one of the events in <i>EventFlags</i> will be counted.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff541478">DEBUG_EVENT_XXX</a> for a list of the events.</p>
</dd>

### -param <i>Count</i> [out]

<dd>
<p>Receives the number of event callbacks that are interested in at least one of the events in <i>EventFlags</i>.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>Each client can have at most one event callback registered with it.  When a callback is registered with a client, its <a href="https://msdn.microsoft.com/library/windows/hardware/ff550737">IDebugEventCallbacks::GetInterestMask</a> method is called to allow the client to specify which events it is interested in.</p>

<p>For more information about callbacks, see <a href="https://msdn.microsoft.com/9090a465-b6ab-4e99-8155-b0abdb729468">Callbacks</a>.</p>

<p>Each client can have at most one event callback registered with it.  When a callback is registered with a client, its <a href="https://msdn.microsoft.com/library/windows/hardware/ff550737">IDebugEventCallbacks::GetInterestMask</a> method is called to allow the client to specify which events it is interested in.</p>

<p>For more information about callbacks, see <a href="https://msdn.microsoft.com/9090a465-b6ab-4e99-8155-b0abdb729468">Callbacks</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550497">IDebugClient5</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550550">IDebugEventCallbacks</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546601">GetEventCallbacks</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556671">SetEventCallbacks</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547931">GetNumberOutputCallbacks</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547923">GetNumberInputCallbacks</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient5::GetNumberEventCallbacks method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
