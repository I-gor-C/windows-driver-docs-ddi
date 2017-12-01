---
UID: NF.ntddk.PsSetCreateProcessNotifyRoutineEx2
title: PsSetCreateProcessNotifyRoutineEx2
author: windows-driver-content
description: The PsSetCreateProcessNotifyRoutineEx2 routine registers or removes a callback routine that notifies the caller when a process is created or deleted.
old-location: kernel\pssetcreateprocessnotifyroutineex2.htm
old-project: kernel
ms.assetid: 25B053C1-E3A3-4002-9355-F3EEA8FECB44
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PsSetCreateProcessNotifyRoutineEx2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Windows 10, version 1703
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsSetCreateProcessNotifyRoutineEx2
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
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

# PsSetCreateProcessNotifyRoutineEx2 function



## -description
<p>The <b>PsSetCreateProcessNotifyRoutineEx2</b> routine registers or removes a callback routine that notifies the caller when a process is created or deleted.</p>


## -syntax

````
NTSTATUS PsSetCreateProcessNotifyRoutineEx2(
  _In_ PSCREATEPROCESSNOTIFYTYPE  NotifyType,
  _In_ PVOID                     NotifyInformation,
  _In_ BOOLEAN                   Remove
);
````


## -parameters
<dl>

### -param <i> NotifyType</i> [in]

<dd>
<p>A <a href="..\ntddk\ne-ntddk--pscreateprocessnotifytype.md">PSCREATEPROCESSNOTIFYTYPE</a>-type value that indicates the type of process notification.</p>
</dd>

### -param <i>NotifyInformation</i> [in]

<dd>
<p>The address of the notification information for the specified type of process notification. If <i>NotifyType</i> is <b>PsCreateProcessNotifySubsystems</b>, <i>NotifyInformation</i> is a  <a href="..\ntddk\nc-ntddk-pcreate-process-notify-routine-ex.md">PCREATE_PROCESS_NOTIFY_ROUTINE_EX</a> that specifies the entry point of the caller-supplied process-creation callback. </p>
</dd>

### -param <i>Remove</i> [in]

<dd>
<p>A Boolean value that specifies whether <b>PsSetCreateProcessNotifyRoutineEx2</b> will add or remove a specified routine from the list of callback routines. If this parameter is <b>TRUE</b>, the specified routine is removed from the list of callback routines. If this parameter is <b>FALSE</b>, the specified routine is added to the list of callback routines. If <i>Remove</i> is <b>TRUE</b>, the system also waits for all in-flight callback routines to complete before returning.</p>
</dd>
</dl>

## -returns
<p><b>PsSetCreateProcessNotifyRoutineEx2</b> returns one of the following NTSTATUS values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The specified  routine is now registered with the operating system. The operating system calls this routine whenever a new process is created.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The specified routine was already registered, or the operating system has reached its limit for registering process-creation callback routines.</p>

<p><i> NotifyType</i> is not <b>PsCreateProcessNotifySubsystems</b>.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The image that contains the callback routine pointer did not have IMAGE_DLLCHARACTERISTICS_FORCE_INTEGRITY set in its image header.</p>

<p> </p>

## -remarks
<p>Drivers can call <b>PsSetCreateProcessNotifyRoutineEx2</b> to register their process-creation notify routines.</p>

<p>After a driver-supplied routine is registered, it is called with the unique ID (indicated by <i>ProcessId</i>) 
        of the created or deleted process.  The <i>ParentId</i> identifies the parent process of the new process (this is the parent used for priority, affinity, quota, token, and handle inheritance, among others) if it was
        created with the inherit handles option.  If it was created without
        the inherit handle options, then the parent process ID is NULL.
        </p>

<p>If the <i>Create</i> value is TRUE, the subsystem process
        was created; FALSE indicates the process was deleted. </p>

<p>When the process is created, the callback function is invoked just after the first thread in the
        process has been created. Conversely, for deletion, the function is invoked after the
        last thread in the process has terminated and the address space is about
        to be deleted. It is possible that the callback is only invoked for deletion without getting a creation
        call in cases where the process was created and deleted
        without a thread ever being created.</p>

<p>A driver must remove any callback function that it registers before it unloads. You can remove the callback by calling <b>PsSetCreateProcessNotifyRoutineEx2</b> with <i>Remove</i> = <b>TRUE</b>.  </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1703</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
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
<a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddk\nf-ntddk-pssetcreateprocessnotifyroutine.md">PsSetCreateProcessNotifyRoutine</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-pssetcreateprocessnotifyroutineex.md">PsSetCreateProcessNotifyRoutineEx</a>
</dt>
<dt>
<a href="..\ntddk\nc-ntddk-pcreate-process-notify-routine-ex.md">PCREATE_PROCESS_NOTIFY_ROUTINE_EX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PsSetCreateProcessNotifyRoutineEx2 routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
