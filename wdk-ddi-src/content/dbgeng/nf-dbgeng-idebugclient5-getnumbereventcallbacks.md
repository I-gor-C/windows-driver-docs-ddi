---
UID: NF.dbgeng.IDebugClient5.GetNumberEventCallbacks
title: IDebugClient5::GetNumberEventCallbacks method
author: windows-driver-content
description: The GetNumberEventCallbacks method returns the number of event callbacks that are interested in the given events.
old-location: debugger\getnumbereventcallbacks.htm
old-project: Debugger
ms.assetid: 02001bad-bafe-432d-bc07-011cb6981ae6
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IDebugClient5, IDebugClient5::GetNumberEventCallbacks, GetNumberEventCallbacks
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
---

# IDebugClient5::GetNumberEventCallbacks method



## -description
The <b>GetNumberEventCallbacks</b> method returns the number of event callbacks that are interested in the given <a href="debugger.events#events#events">events</a>.



## -syntax

````
HRESULT GetNumberEventCallbacks(
  [in]  ULONG  EventFlags,
  [out] PULONG Count
);
````


## -parameters

### -param EventFlags [in]

Specifies a set of events used to filter out some of the event callbacks; only event callbacks that have indicated an interest in one of the events in <i>EventFlags</i> will be counted.  See <a href="https://msdn.microsoft.com/library/windows/hardware/ff541478">DEBUG_EVENT_XXX</a> for a list of the events.


### -param Count [out]

Receives the number of event callbacks that are interested in at least one of the events in <i>EventFlags</i>.


## -returns
This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.

 


## -remarks
Each client can have at most one event callback registered with it.  When a callback is registered with a client, its <a href="debugger.idebugeventcallbacks_getinterestmask">IDebugEventCallbacks::GetInterestMask</a> method is called to allow the client to specify which events it is interested in.

For more information about callbacks, see <a href="https://msdn.microsoft.com/9090a465-b6ab-4e99-8155-b0abdb729468">Callbacks</a>.


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

## -see-also
<dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient5.md">IDebugClient5</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugeventcallbacks.md">IDebugEventCallbacks</a>
</dt>
<dt>
<a href="debugger.geteventcallbacks">GetEventCallbacks</a>
</dt>
<dt>
<a href="debugger.seteventcallbacks">SetEventCallbacks</a>
</dt>
<dt>
<a href="debugger.getnumberoutputcallbacks">GetNumberOutputCallbacks</a>
</dt>
<dt>
<a href="debugger.getnumberinputcallbacks">GetNumberInputCallbacks</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20IDebugClient5::GetNumberEventCallbacks method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

