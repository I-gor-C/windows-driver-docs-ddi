---
UID: NC.ntddk.PCREATE_THREAD_NOTIFY_ROUTINE
title: PCREATE_THREAD_NOTIFY_ROUTINE
author: windows-driver-content
description: A callback routine implemented by a driver to notify the caller when a thread is created or deleted.
old-location: kernel\pcreate_thread_notify_routine.htm
ms.assetid: AAA62659-D12C-4EEC-8D74-6138B34128CE
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetCreateThreadNotifyRoutine
req.alt-loc: Ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=APC_LEVEL
ms.keywords: FILTER_INITIALIZATION_DATA, FILTER_INITIALIZATION_DATA, *PFILTER_INITIALIZATION_DATA
req.iface: 
---

# PCREATE_THREAD_NOTIFY_ROUTINE callback



## -description
<p>A callback routine implemented by a driver to notify the caller when a thread is created or deleted.</p>


## -prototype

````
PCREATE_THREAD_NOTIFY_ROUTINE SetCreateThreadNotifyRoutine;

void SetCreateThreadNotifyRoutine(
  _In_ HANDLE  ProcessId,
  _In_ HANDLE  ThreadId,
  _In_ BOOLEAN Create
)
{ ... }
````


## -parameters
<dl>

### -param <i>ProcessId</i> [in]

<dd>
<p>The process ID of the process.</p>
</dd>

### -param <i>ThreadId</i> [in]

<dd>
<p>The thread ID of the thread.</p>
</dd>

### -param <i>Create</i> [in]

<dd>
<p>Indicates whether the thread was created (<b>TRUE</b>) or deleted (<b>FALSE</b>).</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>Highest-level drivers can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559954">PsSetCreateThreadNotifyRoutine</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/dn957857">PsSetCreateThreadNotifyRoutineEx</a> to register their thread-creation notify routine.</p>

<p>The driver's thread-notify routine runs at IRQL = PASSIVE_LEVEL or APC_LEVEL. When a thread is created, the thread-notify routine runs in the context of the thread that created the new thread. When a thread is deleted, the thread-notify routine runs in the context of this thread when the thread exits. </p>

<p>Highest-level drivers can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559954">PsSetCreateThreadNotifyRoutine</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/dn957857">PsSetCreateThreadNotifyRoutineEx</a> to register their thread-creation notify routine.</p>

<p>The driver's thread-notify routine runs at IRQL = PASSIVE_LEVEL or APC_LEVEL. When a thread is created, the thread-notify routine runs in the context of the thread that created the new thread. When a thread is deleted, the thread-notify routine runs in the context of this thread when the thread exits. </p>

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
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559954">PsSetCreateThreadNotifyRoutine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn957857">PsSetCreateThreadNotifyRoutineEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PCREATE_THREAD_NOTIFY_ROUTINE callback function%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
