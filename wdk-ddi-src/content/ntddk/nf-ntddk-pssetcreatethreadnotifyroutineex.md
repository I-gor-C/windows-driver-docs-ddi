---
UID: NF.ntddk.PsSetCreateThreadNotifyRoutineEx
title: PsSetCreateThreadNotifyRoutineEx function
author: windows-driver-content
description: The PsSetCreateThreadNotifyRoutineEx routine registers a driver-supplied callback that is subsequently notified when a new thread is created and when such a thread is deleted.
old-location: kernel\pssetcreatethreadnotifyroutineex.htm
old-project: kernel
ms.assetid: 586688EC-51B1-488E-BFC6-7796C37593BF
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: PsSetCreateThreadNotifyRoutineEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsSetCreateThreadNotifyRoutineEx
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
---

# PsSetCreateThreadNotifyRoutineEx function



## -description
The <b>PsSetCreateThreadNotifyRoutineEx</b> routine registers a driver-supplied callback that is subsequently notified when a new thread is created and when such a thread is deleted. 



## -syntax

````
NTSTATUS PsSetCreateThreadNotifyRoutineEx(
  _In_ PSCREATETHREADNOTIFYTYPE NotifyType,
  _In_ PVOID                    NotifyInformation
);
````


## -parameters

### -param NotifyType [in]

A <a href="kernel.pscreatethreadnotifytype">PSCREATETHREADNOTIFYTYPE</a> value that   indicates the type of thread notification. 


### -param NotifyInformation [in]

Provides the address of the notification information
        for the specified type of thread notification. 


## -returns
<b>PsSetCreateThreadNotifyRoutineEx</b> either returns STATUS_SUCCESS or it returns STATUS_INSUFFICIENT_RESOURCES if it failed the callback registration.


## -remarks
Highest-level drivers can call <b>PsSetCreateThreadNotifyRoutineEx</b> to set up their thread-creation notify routines.

For example, an IFS or highest-level system-profiling driver might register such a thread-creation callback to track the system-wide creation and deletion of threads against the driver's internal state.

If <i>NotifyType</i> is <b>PsCreateThreadNotifyNonSystem</b>, the  <b>PsSetCreateThreadNotifyRoutineEx</b> routine differs from <a href="kernel.pssetcreatethreadnotifyroutine">PsSetCreateThreadNotifyRoutine</a> in the context in which the callback is executed. With <b>PsSetCreateThreadNotifyRoutine</b>, the callback is executed on the creator thread. With <b>PsSetCreateThreadNotifyRoutineEx</b>, the callback is executed on the newly created thread.

A driver must remove any callback function it registers before it unloads. You can remove the callback by calling the <a href="kernel.psremovecreatethreadnotifyroutine">PsRemoveCreateThreadNotifyRoutine</a> routine.


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
Available starting with Windows 10.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.pssetcreatethreadnotifyroutine">PsSetCreateThreadNotifyRoutine</a>
</dt>
<dt>
<a href="kernel.psremovecreatethreadnotifyroutine">PsRemoveCreateThreadNotifyRoutine</a>
</dt>
<dt>
<a href="kernel.psgetcurrentprocessid">PsGetCurrentProcessId</a>
</dt>
<dt>
<a href="kernel.psgetcurrentthreadid">PsGetCurrentThreadId</a>
</dt>
<dt>
<a href="kernel.psissystemthread">PsIsSystemThread</a>
</dt>
<dt>
<a href="kernel.pssetcreateprocessnotifyroutine">PsSetCreateProcessNotifyRoutine</a>
</dt>
<dt>
<a href="kernel.pssetloadimagenotifyroutine">PsSetLoadImageNotifyRoutine</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PsSetCreateThreadNotifyRoutineEx routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

