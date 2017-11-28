---
UID: NF.ndis.NdisStallExecution
title: NdisStallExecution
author: windows-driver-content
description: The NdisStallExecution function stalls the caller on the current processor for a given interval.
old-location: netvista\ndisstallexecution.htm
old-project: netvista
ms.assetid: 590f5a1a-fd78-408e-b4f0-555f08694c43
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisStallExecution
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisStallExecution (NDIS 5.1))
   in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisStallExecution (NDIS 5.1))
   in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisStallExecution
req.alt-loc: ndis.h
req.ddi-compliance: NdisStallExecution_Delay
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
req.iface: 
---

# NdisStallExecution function



## -description
<p>The 
  <b>NdisStallExecution</b> function stalls the caller on the current processor for a given interval.</p>


## -syntax

````
VOID NdisStallExecution(
  _In_ UINT MicrosecondsToStall
);
````


## -parameters
<dl>

### -param <i>MicrosecondsToStall</i> [in]

<dd>
<p>The number of microseconds to delay. A driver should specify no more than 50 microseconds.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>NdisStallExecution</b> is a processor-dependent function that busy-waits for at least the specified
    number of microseconds, but not significantly longer.</p>

<p>This function should be called by drivers that must wait for an interval of more than a few
    instructions but less than 50 microseconds. Drivers that call this routine should minimize the number of
    microseconds that they specify.</p>

<p>If a driver must wait for an interval longer than 50 microseconds, it should call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563677">NdisMSleep</a> function. Note that callers of 
    <b>NdisMSleep</b> run at IRQL &lt; DISPATCH_LEVEL.</p>

<p><b>NdisStallExecution</b> is a processor-dependent function that busy-waits for at least the specified
    number of microseconds, but not significantly longer.</p>

<p>This function should be called by drivers that must wait for an interval of more than a few
    instructions but less than 50 microseconds. Drivers that call this routine should minimize the number of
    microseconds that they specify.</p>

<p>If a driver must wait for an interval longer than 50 microseconds, it should call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563677">NdisMSleep</a> function. Note that callers of 
    <b>NdisMSleep</b> run at IRQL &lt; DISPATCH_LEVEL.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff554783">NdisStallExecution (NDIS 5.1)</a>)
   in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisStallExecution (NDIS 5.1)</b>)
   in Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549332">NdisStallExecution_Delay</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-reset.md">MiniportResetEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564563">NdisSetTimerObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563677">NdisMSleep</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisStallExecution function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
