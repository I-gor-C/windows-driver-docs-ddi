---
UID: NF.wdm.KeSetEvent
title: KeSetEvent
author: windows-driver-content
description: The KeSetEvent routine sets an event object to a signaled state if the event was not already signaled, and returns the previous state of the event object.
old-location: kernel\kesetevent.htm
ms.assetid: a2017660-f001-449c-9c33-e26c2897ead1
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeSetEvent
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: CompletionEventChecking, IoAllocateIrpSignalEventInCompletion, IoBuildDeviceIoControlSetEvent, IoBuildFsdIrpSignalEventInCompletion, IrqlKeSetEvent, SignalEventInCompletion, DoubleKeSetEvent, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: See Remarks section.
ms.keywords: KeSetEvent
req.iface: 
req.product: Windows 10 or later.
---

# KeSetEvent function



## -description
<p>The <b>KeSetEvent</b> routine sets an event object to a signaled state if the event was not already signaled, and returns the previous state of the event object. </p>


## -syntax

````
LONG KeSetEvent(
  _Inout_ PRKEVENT  Event,
  _In_    KPRIORITY Increment,
  _In_    BOOLEAN   Wait
);
````


## -parameters
<dl>

### -param <i>Event</i> [in, out]

<dd>
<p>A pointer to an initialized event object for which the caller provides the storage.</p>
</dd>

### -param <i>Increment</i> [in]

<dd>
<p>Specifies the priority increment to be applied if setting the event causes a wait to be satisfied.</p>
</dd>

### -param <i>Wait</i> [in]

<dd>
<p>Specifies whether the call to <b>KeSetEvent</b> is to be followed immediately by a call to one of the <b>KeWait<i>Xxx</i></b> routines. If <b>TRUE</b>, the <b>KeSetEvent</b> call must be followed by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff553324">KeWaitForMultipleObjects</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff553344">KeWaitForMutexObject</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff553350">KeWaitForSingleObject</a>. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -returns
<p>If the previous state of the event object was signaled, a nonzero value is returned.</p>

## -remarks
<p>Calling <b>KeSetEvent</b> causes the event to attain a signaled state. If the event is a notification event, the system attempts to satisfy as many waits as possible on the event object. The event remains signaled until a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551980">KeClearEvent</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff553176">KeResetEvent</a> clears it. If the event is a synchronization event, one wait is satisfied before the system automatically clears the event.</p>

<p>The <b>KeSetEvent</b> routine might temporarily raise the IRQL. If the <i>Wait</i> parameter is <b>FALSE</b>, the routine, before it returns, restores the IRQL to the original value that it had at the start of the call.</p>

<p>If <i>Wait</i> = <b>TRUE</b>, the routine returns without lowering the IRQL. In this case, the <b>KeSetEvent</b> call must be immediately followed by a <b>KeWait<i>Xxx</i></b> call. By setting <i>Wait</i> = <b>TRUE</b>, the caller can prevent an unnecessary context switch from occurring between the <b>KeSetEvent</b> call and the <b>KeWait<i>Xxx</i></b> call. The <b>KeWait<i>Xxx</i></b> routine, before it returns, restores the IRQL to its original value at the start of the <b>KeSetEvent</b> call. Although the IRQL disables context switches between the two calls, these calls cannot reliably be used as the start and end of an atomic operation. For example, between these two calls, a thread that is running at the same time on another processor might change the state of the event object or of the target of the wait.</p>

<p>A pageable thread or pageable driver routine that runs at IRQL = PASSIVE_LEVEL should never call <b>KeSetEvent</b> with the <i>Wait</i> parameter set to TRUE. Such a call causes a fatal page fault if the caller happens to be paged out between the calls to <b>KeSetEvent</b> and <b>KeWait<i>Xxx</i></b>.</p>

<p>For more information about event objects, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544323">Event Objects</a>.</p>

<p>If <i>Wait</i> is set to <b>FALSE</b>, the caller can be running at IRQL &lt;= DISPATCH_LEVEL. Otherwise, callers of <b>KeSetEvent</b> must be running at IRQL &lt;= APC_LEVEL and in a nonarbitrary thread context.</p>

<p>Calling <b>KeSetEvent</b> causes the event to attain a signaled state. If the event is a notification event, the system attempts to satisfy as many waits as possible on the event object. The event remains signaled until a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551980">KeClearEvent</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff553176">KeResetEvent</a> clears it. If the event is a synchronization event, one wait is satisfied before the system automatically clears the event.</p>

<p>The <b>KeSetEvent</b> routine might temporarily raise the IRQL. If the <i>Wait</i> parameter is <b>FALSE</b>, the routine, before it returns, restores the IRQL to the original value that it had at the start of the call.</p>

<p>If <i>Wait</i> = <b>TRUE</b>, the routine returns without lowering the IRQL. In this case, the <b>KeSetEvent</b> call must be immediately followed by a <b>KeWait<i>Xxx</i></b> call. By setting <i>Wait</i> = <b>TRUE</b>, the caller can prevent an unnecessary context switch from occurring between the <b>KeSetEvent</b> call and the <b>KeWait<i>Xxx</i></b> call. The <b>KeWait<i>Xxx</i></b> routine, before it returns, restores the IRQL to its original value at the start of the <b>KeSetEvent</b> call. Although the IRQL disables context switches between the two calls, these calls cannot reliably be used as the start and end of an atomic operation. For example, between these two calls, a thread that is running at the same time on another processor might change the state of the event object or of the target of the wait.</p>

<p>A pageable thread or pageable driver routine that runs at IRQL = PASSIVE_LEVEL should never call <b>KeSetEvent</b> with the <i>Wait</i> parameter set to TRUE. Such a call causes a fatal page fault if the caller happens to be paged out between the calls to <b>KeSetEvent</b> and <b>KeWait<i>Xxx</i></b>.</p>

<p>For more information about event objects, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544323">Event Objects</a>.</p>

<p>If <i>Wait</i> is set to <b>FALSE</b>, the caller can be running at IRQL &lt;= DISPATCH_LEVEL. Otherwise, callers of <b>KeSetEvent</b> must be running at IRQL &lt;= APC_LEVEL and in a nonarbitrary thread context.</p>

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
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>See Remarks section.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975145">CompletionEventChecking</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975155">IoAllocateIrpSignalEventInCompletion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975163">IoBuildDeviceIoControlSetEvent</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975167">IoBuildFsdIrpSignalEventInCompletion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547835">IrqlKeSetEvent</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975249">SignalEventInCompletion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454215">DoubleKeSetEvent</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551980">KeClearEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552137">KeInitializeEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553089">KeReadStateEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553176">KeResetEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553324">KeWaitForMultipleObjects</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553344">KeWaitForMutexObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553350">KeWaitForSingleObject</a>
</dt>
<dt><a href="https://go.microsoft.com/fwlink/p/?linkid=838602">Specifying Priority Boosts When Completing I/O Requests</a></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeSetEvent routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
