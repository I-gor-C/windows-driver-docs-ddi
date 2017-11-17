---
UID: NC.ntddk.PCREATE_PROCESS_NOTIFY_ROUTINE_EX
title: PCREATE_PROCESS_NOTIFY_ROUTINE_EX
author: windows-driver-content
description: A callback routine implemented by a driver to notify the caller when a process is created or exits.
old-location: kernel\pcreate_process_notify_routine_ex.htm
ms.assetid: 071BD24F-AA58-4A39-8059-CEF6D7105DB6
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
req.alt-api: SetCreateProcessNotifyRoutineEx
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
req.irql: PASSIVE_LEVEL
ms.keywords: FILTER_INITIALIZATION_DATA, FILTER_INITIALIZATION_DATA, *PFILTER_INITIALIZATION_DATA
req.iface: 
---

# PCREATE_PROCESS_NOTIFY_ROUTINE_EX callback



## -description
<p>A callback routine implemented by a driver to notify the caller when a process is created or exits.</p>


## -prototype

````
PCREATE_PROCESS_NOTIFY_ROUTINE_EX SetCreateProcessNotifyRoutineEx;

void SetCreateProcessNotifyRoutineEx(
  _In_        HANDLE                 ParentId,
  _In_        HANDLE                 ProcessId,
  _Inout_opt_ PPS_CREATE_NOTIFY_INFO CreateInfo
)
{ ... }
````


## -parameters
<dl>

### -param <i>ParentId</i> [in]

<dd>
<p>The process ID of the parent process.</p>
</dd>

### -param <i>ProcessId</i> [in]

<dd>
<p>The process ID of the process.</p>
</dd>

### -param <i>CreateInfo</i> [in, out, optional]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff559960">PS_CREATE_NOTIFY_INFO</a> structure that contains information about the new process. </p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>Highest-level drivers call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559953">PsSetCreateProcessNotifyRoutineEx</a> to register their implementation of  <i>PCREATE_PROCESS_NOTIFY_ROUTINE_EX</i> routine. An installable file system (IFS) or highest-level system-profiling driver might register a process-creation callback routine to track which processes are created and deleted against the driver's internal state across the system. </p>

<p>Highest-level drivers call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559953">PsSetCreateProcessNotifyRoutineEx</a> to register their implementation of  <i>PCREATE_PROCESS_NOTIFY_ROUTINE_EX</i> routine. An installable file system (IFS) or highest-level system-profiling driver might register a process-creation callback routine to track which processes are created and deleted against the driver's internal state across the system. </p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559953">PsSetCreateProcessNotifyRoutineEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt805891">PsSetCreateProcessNotifyRoutineEx2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PCREATE_PROCESS_NOTIFY_ROUTINE_EX callback function%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
