---
UID: NF.ndis.NdisFreeTimerObject
title: NdisFreeTimerObject function
author: windows-driver-content
description: The NdisFreeTimerObject function frees a timer object that was allocated with the NdisAllocateTimerObject function.
old-location: netvista\ndisfreetimerobject.htm
old-project: netvista
ms.assetid: b3edeebb-7a8f-4cd2-bd52-1b8ce044caa2
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisFreeTimerObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisFreeTimerObject
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Timer_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
---

# NdisFreeTimerObject function



## -description
The 
  <b>NdisFreeTimerObject</b> function frees a timer object that was allocated with the 
  <a href="netvista.ndisallocatetimerobject">
  NdisAllocateTimerObject</a> function.



## -syntax

````
VOID NdisFreeTimerObject(
  _In_ NDIS_HANDLE TimerObject
);
````


## -parameters

### -param TimerObject [in]

A handle to a timer object that NDIS provides when a driver calls the 
     <a href="netvista.ndisallocatetimerobject">
     NdisAllocateTimerObject</a> function.


## -returns
None


## -remarks
To use timer services, an NDIS driver first calls the 
    <a href="netvista.ndisallocatetimerobject">NdisAllocateTimerObject</a> function
    to initialize a timer object. Typically, 
    <b>NdisAllocateTimerObject</b> is called when a driver initializes. The driver must call 
    <b>NdisFreeTimerObject</b> to free the timer object when the timer is no longer required.

To cancel a timer, call the 
    <a href="netvista.ndiscanceltimerobject">NdisCancelTimerObject</a> function. 
    <b>NdisCancelTimerObject</b> dequeues the timer object if it is currently queued.


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
Supported in NDIS 6.0 and later.

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
Library

</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.ndis_irql_timer_function">Irql_Timer_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.ndis_timer_characteristics">NDIS_TIMER_CHARACTERISTICS</a>
</dt>
<dt>
<a href="netvista.ndisallocatetimerobject">NdisAllocateTimerObject</a>
</dt>
<dt>
<a href="netvista.ndiscanceltimerobject">NdisCancelTimerObject</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisFreeTimerObject function%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

