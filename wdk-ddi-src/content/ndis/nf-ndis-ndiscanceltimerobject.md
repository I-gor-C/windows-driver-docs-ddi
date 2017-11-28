---
UID: NF.ndis.NdisCancelTimerObject
title: NdisCancelTimerObject
author: windows-driver-content
description: The NdisCancelTimerObject function cancels a timer object that is associated with a previous call to the NdisSetTimerObject function.
old-location: netvista\ndiscanceltimerobject.htm
old-project: netvista
ms.assetid: b66652b7-2e02-49f5-a7e3-60ff35363a19
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisCancelTimerObject
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
req.alt-api: NdisCancelTimerObject
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Timer_Function, PeriodicTimer
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: See Remarks section
req.iface: 
---

# NdisCancelTimerObject function



## -description
<p>The 
  <b>NdisCancelTimerObject</b> function cancels a timer object that is associated with a previous call to the 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff564563">NdisSetTimerObject</a> function.</p>


## -syntax

````
BOOLEAN NdisCancelTimerObject(
  _In_ NDIS_HANDLE TimerObject
);
````


## -parameters
<dl>

### -param <i>TimerObject</i> [in]

<dd>
<p>A handle to a timer object that NDIS provides when a driver calls the 
     <a href="..\ndis\nf-ndis-ndisallocatetimerobject.md">
     NdisAllocateTimerObject</a> function.</p>
</dd>
</dl>

## -returns
<p><b>NdisCancelTimerObject</b> returns <b>TRUE</b> if the specified timer object is in the system timer queue;
     otherwise, it returns <b>FALSE</b>.</p>

## -remarks
<p>A call to 
    <b>NdisCancelTimerObject</b> cancels execution of a 
    <a href="..\ndis\nc-ndis-ndis-timer-function.md">NetTimerCallback</a> function, provided
    that the last specified timeout interval has not yet expired.</p>

<p>NDIS drivers should call 
    <b>NdisCancelTimerObject</b> first when they are halting or unloading to ensure that a 
    <i>NetTimerCallback</i> function does not attempt to access resources that the driver has already
    released.</p>

<p>If a nonzero value was specified in the 
    <i>MillisecondsPeriod</i> parameter of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564563">NdisSetTimerObject</a> function, the timer is known as a <i>periodic timer</i>. If a zero value was specified in the <i>MillisecondsPeriod</i> parameter, the timer is known as a <i>one-shot timer</i>. The following points apply to canceling both types of timers:</p>

<p>If  the caller of
    <b>NdisCancelTimerObject</b> is canceling a periodic timer, it must be running at IRQL = PASSIVE_LEVEL. Otherwise, the caller of 
    <b>NdisCancelTimerObject</b> should be running at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>If  the caller of
    <b>NdisCancelTimerObject</b> is canceling a periodic timer, <b>NdisCancelTimerObject</b> calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff552050">KeFlushQueuedDpcs</a> to ensure that the timer is not currently running. Therefore, the caller is not required to have a separate synchronization mechanism to ensure that the timer is not currently being executed on another processor.</p>

<p>If  the caller of
    <b>NdisCancelTimerObject</b> is canceling a one-shot timer, the caller is required to have a separate synchronization mechanism to ensure the timer is not currently running on another processor. For example, the caller could call <a href="https://msdn.microsoft.com/library/windows/hardware/ff567897">NDIS_WAIT_FOR_MUTEX</a> in order to wait for the timer thread to signal a mutex object when the thread is about to complete.</p>

<p>For more information, see <a href="NULL">Synchronization and Notification in Network Drivers</a>.</p>

<p>A call to 
    <b>NdisCancelTimerObject</b> cancels execution of a 
    <a href="..\ndis\nc-ndis-ndis-timer-function.md">NetTimerCallback</a> function, provided
    that the last specified timeout interval has not yet expired.</p>

<p>NDIS drivers should call 
    <b>NdisCancelTimerObject</b> first when they are halting or unloading to ensure that a 
    <i>NetTimerCallback</i> function does not attempt to access resources that the driver has already
    released.</p>

<p>If a nonzero value was specified in the 
    <i>MillisecondsPeriod</i> parameter of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564563">NdisSetTimerObject</a> function, the timer is known as a <i>periodic timer</i>. If a zero value was specified in the <i>MillisecondsPeriod</i> parameter, the timer is known as a <i>one-shot timer</i>. The following points apply to canceling both types of timers:</p>

<p>If  the caller of
    <b>NdisCancelTimerObject</b> is canceling a periodic timer, it must be running at IRQL = PASSIVE_LEVEL. Otherwise, the caller of 
    <b>NdisCancelTimerObject</b> should be running at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>If  the caller of
    <b>NdisCancelTimerObject</b> is canceling a periodic timer, <b>NdisCancelTimerObject</b> calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff552050">KeFlushQueuedDpcs</a> to ensure that the timer is not currently running. Therefore, the caller is not required to have a separate synchronization mechanism to ensure that the timer is not currently being executed on another processor.</p>

<p>If  the caller of
    <b>NdisCancelTimerObject</b> is canceling a one-shot timer, the caller is required to have a separate synchronization mechanism to ensure the timer is not currently running on another processor. For example, the caller could call <a href="https://msdn.microsoft.com/library/windows/hardware/ff567897">NDIS_WAIT_FOR_MUTEX</a> in order to wait for the timer thread to signal a mutex object when the thread is about to complete.</p>

<p>For more information, see <a href="NULL">Synchronization and Notification in Network Drivers</a>.</p>

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
<p>See Remarks section</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548019">Irql_Timer_Function</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550378">PeriodicTimer</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561618">NdisAllocateTimerObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564563">NdisSetTimerObject</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-ndis-timer-function.md">NetTimerCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisCancelTimerObject function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
