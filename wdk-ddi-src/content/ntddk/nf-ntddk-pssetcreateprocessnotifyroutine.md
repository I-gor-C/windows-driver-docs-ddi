---
UID: NF.ntddk.PsSetCreateProcessNotifyRoutine
title: PsSetCreateProcessNotifyRoutine
author: windows-driver-content
description: The PsSetCreateProcessNotifyRoutine routine adds a driver-supplied callback routine to, or removes it from, a list of routines to be called whenever a process is created or deleted.
old-location: kernel\pssetcreateprocessnotifyroutine.htm
old-project: kernel
ms.assetid: eeeea140-e469-476f-adce-4505817bc35e
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PsSetCreateProcessNotifyRoutine
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
req.alt-api: PsSetCreateProcessNotifyRoutine
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

# PsSetCreateProcessNotifyRoutine function



## -description
<p>The <b>PsSetCreateProcessNotifyRoutine</b> routine adds a driver-supplied callback routine to, or removes it from, a list of routines to be called whenever a process is created or deleted.</p>


## -syntax

````
NTSTATUS PsSetCreateProcessNotifyRoutine(
  _In_ PCREATE_PROCESS_NOTIFY_ROUTINE NotifyRoutine,
  _In_ BOOLEAN                        Remove
);
````


## -parameters
<dl>

### -param <i>NotifyRoutine</i> [in]

<dd>
<p>Specifies the entry point of a caller-supplied process-creation callback routine. See <a href="https://msdn.microsoft.com/library/windows/hardware/mt764085">PCREATE_PROCESS_NOTIFY_ROUTINE</a>.</p>
</dd>

### -param <i>Remove</i> [in]

<dd>
<p>Indicates whether the routine specified by <i>NotifyRoutine</i> should be added to or removed from the system's list of notification routines. If <b>FALSE</b>, the specified routine is added to the list. If <b>TRUE</b>, the specified routine is removed from the list.</p>
</dd>
</dl>

## -returns
<p><b>PsSetCreateProcessNotifyRoutine</b> can return one of the following:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The given <i>NotifyRoutine</i> is now registered with the system.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The given <i>NotifyRoutine</i> has already been registered, so this call is a redundant call, or the system has reached its limit for registering process-creation callbacks. </p>

<p> </p>

## -remarks
<p>Highest-level drivers can call <b>PsSetCreateProcessNotifyRoutine</b> to set up their process-creation notify routines implemented as <a href="https://msdn.microsoft.com/library/windows/hardware/mt764085">PCREATE_PROCESS_NOTIFY_ROUTINE</a>.</p>

<p>An IFS or highest-level system-profiling driver might register a process-creation callback to track the system-wide creation and deletion of processes against the driver's internal state. For Windows Vista and later versions of Windows, the system can register up to 64 process-creation callback routines.</p>

<p>A driver must remove any callbacks that it registers before it unloads. You can remove the callback by calling <b>PsSetCreateProcessNotify</b> with <i>Remove</i> = <b>TRUE</b>.</p>

<p>After a driver-supplied routine is registered, it is called with <i>Create</i> set to <b>TRUE</b> just after the initial thread is created within the newly created process designated by the input <i>ProcessId</i> handle. The input <i>ParentId</i> handle identifies the parent process of the newly-created process (this is the parent used for priority, affinity, quota, token, and handle inheritance, among others).</p>

<p>Highest-level drivers can call <b>PsSetCreateProcessNotifyRoutine</b> to set up their process-creation notify routines implemented as <a href="https://msdn.microsoft.com/library/windows/hardware/mt764085">PCREATE_PROCESS_NOTIFY_ROUTINE</a>.</p>

<p>An IFS or highest-level system-profiling driver might register a process-creation callback to track the system-wide creation and deletion of processes against the driver's internal state. For Windows Vista and later versions of Windows, the system can register up to 64 process-creation callback routines.</p>

<p>A driver must remove any callbacks that it registers before it unloads. You can remove the callback by calling <b>PsSetCreateProcessNotify</b> with <i>Remove</i> = <b>TRUE</b>.</p>

<p>After a driver-supplied routine is registered, it is called with <i>Create</i> set to <b>TRUE</b> just after the initial thread is created within the newly created process designated by the input <i>ProcessId</i> handle. The input <i>ParentId</i> handle identifies the parent process of the newly-created process (this is the parent used for priority, affinity, quota, token, and handle inheritance, among others).</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt764085">PCREATE_PROCESS_NOTIFY_ROUTINE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559935">PsGetCurrentProcessId</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559953">PsSetCreateProcessNotifyRoutineEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559954">PsSetCreateThreadNotifyRoutine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559957">PsSetLoadImageNotifyRoutine</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PsSetCreateProcessNotifyRoutine routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
