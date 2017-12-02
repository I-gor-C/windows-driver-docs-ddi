---
UID: NF.ndis.NdisAllocateTimerObject
title: NdisAllocateTimerObject
author: windows-driver-content
description: The NdisAllocateTimerObject function allocates and initializes a timer object for use with subsequent NdisXxx timer functions.
old-location: netvista\ndisallocatetimerobject.htm
old-project: netvista
ms.assetid: feb5e4cf-7e23-434e-9dc5-bb445a6f5606
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NdisAllocateTimerObject
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
req.alt-api: NdisAllocateTimerObject
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
req.iface: 
---

# NdisAllocateTimerObject function



## -description
<p>The 
  <b>NdisAllocateTimerObject</b> function allocates and initializes a timer object for use with subsequent 
  <b>Ndis<i>Xxx</i></b> timer functions.</p>


## -syntax

````
NDIS_STATUS NdisAllocateTimerObject(
  _In_  NDIS_HANDLE                 NdisHandle,
  _In_  PNDIS_TIMER_CHARACTERISTICS TimerCharacteristics,
  _Out_ PNDIS_HANDLE                pTimerObject
);
````


## -parameters
<dl>

### -param NdisHandle [in]

<dd>
<p>An NDIS handle that was obtained during caller initialization. For more information about
     obtaining NDIS handles, see 
     <a href="netvista.obtaining_pool_handles">Obtaining Pool Handles</a>.</p>
</dd>

### -param TimerCharacteristics [in]

<dd>
<p>A pointer to a caller-supplied 
     <a href="..\ndis\ns-ndis--ndis-timer-characteristics.md">
     NDIS_TIMER_CHARACTERISTICS</a> structure that specifies the characteristics of the allocated timer
     object.</p>
</dd>

### -param pTimerObject [out]

<dd>
<p>A pointer to an NDIS timer object handle that NDIS provides to identify the timer object in
     subsequent calls to 
     <b>Ndis<i>Xxx</i></b> timer functions.</p>
</dd>
</dl>

## -returns
<p><b>NdisAllocateTimerObject</b> returns one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The timer object was allocated successfully.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>The allocation failed because of insufficient resources.</p><dl>
<dt><b>NDIS_STATUS_BAD_CHARACTERISTICS</b></dt>
</dl><p>The allocation failed because the information in the NDIS_TIMER_CHARACTERISTICS structure is
       invalid.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>None of the preceding status values apply.</p>

<p> </p>

## -remarks
<p>To use timer services, an NDIS driver first calls the 
    <b>NdisAllocateTimerObject</b> function to initialize a timer object. Typically, 
    <b>NdisAllocateTimerObject</b> is called during driver initialization.</p>

<p>To start a timer, call the 
    <a href="..\ndis\nf-ndis-ndissettimerobject.md">NdisSetTimerObject</a> function. Calls to 
    <b>NdisSetTimerObject</b> insert the timer object in the system timer queue. Only one instance of a
    particular timer object can be queued at any given moment.</p>

<p>To cancel a timer, call the 
    <a href="..\ndis\nf-ndis-ndiscanceltimerobject.md">NdisCancelTimerObject</a> function. 
    <b>NdisCancelTimerObject</b> dequeues the timer object if it is currently queued.</p>

<p>To free a timer object, you must call the 
    <a href="..\ndis\nf-ndis-ndisfreetimerobject.md">NdisFreeTimerObject</a> function.</p>

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
<p>Supported in NDIS 6.0 and later.</p>
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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.ndis_irql_timer_function">Irql_Timer_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\ns-ndis--ndis-timer-characteristics.md">NDIS_TIMER_CHARACTERISTICS</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscanceltimerobject.md">NdisCancelTimerObject</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfreetimerobject.md">NdisFreeTimerObject</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndissettimerobject.md">NdisSetTimerObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisAllocateTimerObject function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
