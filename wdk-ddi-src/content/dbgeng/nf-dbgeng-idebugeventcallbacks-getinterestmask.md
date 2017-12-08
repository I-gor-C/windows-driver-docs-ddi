---
UID: NF.dbgeng.IDebugEventCallbacks.GetInterestMask
title: IDebugEventCallbacks::GetInterestMask
author: windows-driver-content
description: The GetInterestMask callback method is called to determine which events the IDebugEventCallbacks object is interested in. The engine calls GetInterestMask when the object is registered with a client by using SetEventCallbacks.
old-location: debugger\idebugeventcallbacks_getinterestmask.htm
old-project: debugger
ms.assetid: 165c83cb-c0be-4a09-9220-a5208f660308
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugEventCallbacks, GetInterestMask, IDebugEventCallbacks::GetInterestMask
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
req.alt-api: IDebugEventCallbacks.GetInterestMask
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
req.iface: IDebugEventCallbacks
---

# IDebugEventCallbacks::GetInterestMask method



## -description
<p>The <b>GetInterestMask</b> callback method is called to determine which <a href="debugger.events#events#events">events</a> the <b>IDebugEventCallbacks</b> object is interested in.  The engine calls <b>GetInterestMask</b> when the object is registered with a client by using <a href="debugger.seteventcallbacks">SetEventCallbacks</a>.</p>


## -syntax

````
HRESULT GetInterestMask(
  [out] PULONG Mask
);
````


## -parameters
<dl>

### -param Mask [out]

<dd>
<p>Receives a bitmask that indicates which events the object is interested in.  The engine will call only those methods that correspond to the bit flags set by <b>GetInterestMask</b>.  For a description of the bit flags and their corresponding methods, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541478">DEBUG_EVENT_XXX</a>.</p>
</dd>
</dl>

## -returns
<p>The return value S_OK indicates the method was successful.  All other return values indicate an error occurred,  in which case the <b>SetEventCallbacks</b> call will fail and the callback object will not be used nor will it receive events.</p>

## -remarks
<p>For more information about handling events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.</p>

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