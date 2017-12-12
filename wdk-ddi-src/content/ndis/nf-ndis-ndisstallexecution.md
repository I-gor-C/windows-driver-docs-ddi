---
UID: NF.ndis.NdisStallExecution
title: NdisStallExecution macro
author: windows-driver-content
description: The NdisStallExecution function stalls the caller on the current processor for a given interval.
old-location: netvista\ndisstallexecution.htm
old-project: netvista
ms.assetid: 590f5a1a-fd78-408e-b4f0-555f08694c43
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisStallExecution
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisStallExecution (NDIS 5.1))   in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisStallExecution (NDIS 5.1))   in Windows XP.
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
---

# NdisStallExecution macro



## -description
The 
  <b>NdisStallExecution</b> function stalls the caller on the current processor for a given interval.



## -syntax

````
VOID NdisStallExecution(
  [in] UINT MicrosecondsToStall
);
````


## -parameters

### -param MicrosecondsToStall [in]

The number of microseconds to delay. A driver should specify no more than 50 microseconds.


## -remarks
<b>NdisStallExecution</b> is a processor-dependent function that busy-waits for at least the specified
    number of microseconds, but not significantly longer.

This function should be called by drivers that must wait for an interval of more than a few
    instructions but less than 50 microseconds. Drivers that call this routine should minimize the number of
    microseconds that they specify.

If a driver must wait for an interval longer than 50 microseconds, it should call the 
    <a href="netvista.ndismsleep">NdisMSleep</a> function. Note that callers of 
    <b>NdisMSleep</b> run at IRQL &lt; DISPATCH_LEVEL.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff554783">NdisStallExecution (NDIS 5.1)</a>)
   in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisStallExecution (NDIS 5.1)</b>)
   in Windows XP.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.ndis_ndisstallexecution_delay">NdisStallExecution_Delay</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_reset.md">MiniportResetEx</a>
</dt>
<dt>
<a href="netvista.ndissettimerobject">NdisSetTimerObject</a>
</dt>
<dt>
<a href="netvista.ndismsleep">NdisMSleep</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisStallExecution macro%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

