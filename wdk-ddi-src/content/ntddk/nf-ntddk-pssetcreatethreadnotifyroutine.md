---
UID: NF.ntddk.PsSetCreateThreadNotifyRoutine
title: PsSetCreateThreadNotifyRoutine
author: windows-driver-content
description: The PsSetCreateThreadNotifyRoutine routine registers a driver-supplied callback that is subsequently notified when a new thread is created and when such a thread is deleted.
old-location: kernel\pssetcreatethreadnotifyroutine.htm
old-project: kernel
ms.assetid: 02c5d325-e0b2-4b0f-b964-7befd1b40cb6
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PsSetCreateThreadNotifyRoutine
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsSetCreateThreadNotifyRoutine
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlPsPassive, PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PsSetCreateThreadNotifyRoutine function



## -description
<p>The <b>PsSetCreateThreadNotifyRoutine</b> routine registers a driver-supplied callback that is subsequently notified when a new thread is created and when such a thread is deleted.</p>


## -syntax

````
NTSTATUS PsSetCreateThreadNotifyRoutine(
  _In_ PCREATE_THREAD_NOTIFY_ROUTINE NotifyRoutine
);
````


## -parameters
<dl>

### -param <i>NotifyRoutine</i> [in]

<dd>
<p>A pointer to the driver's implementation of <a href="https://msdn.microsoft.com/library/windows/hardware/mt764087">PCREATE_THREAD_NOTIFY_ROUTINE</a> routine. </p>
</dd>
</dl>

## -returns
<p><b>PsSetCreateThreadNotifyRoutine</b> either returns STATUS_SUCCESS or it returns STATUS_INSUFFICIENT_RESOURCES if it failed the callback registration.</p>

## -remarks
<p>Highest-level drivers can call <b>PsSetCreateThreadNotifyRoutine</b> to set up their thread-creation notify routines, declared as follows:</p>

<p>For example, an IFS or highest-level system-profiling driver might register such a thread-creation callback to track the system-wide creation and deletion of threads against the driver's internal state.</p>

<p>A driver must remove any callbacks it registers before it unloads. You can remove the callback by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559947">PsRemoveCreateThreadNotifyRoutine</a> routine.</p>

<p>Highest-level drivers can call <b>PsSetCreateThreadNotifyRoutine</b> to set up their thread-creation notify routines, declared as follows:</p>

<p>For example, an IFS or highest-level system-profiling driver might register such a thread-creation callback to track the system-wide creation and deletion of threads against the driver's internal state.</p>

<p>A driver must remove any callbacks it registers before it unloads. You can remove the callback by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559947">PsRemoveCreateThreadNotifyRoutine</a> routine.</p>

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
<dt>Ntddk.h (include Ntddk.h)</dt>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547882">IrqlPsPassive</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559935">PsGetCurrentProcessId</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559937">PsGetCurrentThreadId</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559945">PsIsSystemThread</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559947">PsRemoveCreateThreadNotifyRoutine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559951">PsSetCreateProcessNotifyRoutine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559957">PsSetLoadImageNotifyRoutine</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PsSetCreateThreadNotifyRoutine routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
