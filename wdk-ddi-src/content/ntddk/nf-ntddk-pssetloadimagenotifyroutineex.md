---
UID: NF.ntddk.PsSetLoadImageNotifyRoutineEx
title: PsSetLoadImageNotifyRoutineEx
author: windows-driver-content
description: The PsSetLoadImageNotifyRoutineEx routine registers a driver-supplied callback that is subsequently notified whenever an image is loaded (or mapped into memory).
old-location: kernel\pssetloadimagenotifyroutineex.htm
old-project: kernel
ms.assetid: 792cdb59-e0c2-4697-9934-b7e45a7a31a8
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PsSetLoadImageNotifyRoutineEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsSetLoadImageNotifyRoutineEx
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode)
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PsSetLoadImageNotifyRoutineEx function



## -description
<p>The <b>PsSetLoadImageNotifyRoutineEx</b> routine registers a driver-supplied callback that is subsequently notified whenever an image is loaded (or mapped into memory).</p>


## -syntax

````
 NTSTATUS  PsSetLoadImageNotifyRoutineEx(
  _In_ PLOAD_IMAGE_NOTIFY_ROUTINE NotifyRoutine,
  _In_ ULONG_PTR                  Flags
);
````


## -parameters
<dl>

### -param <i>NotifyRoutine</i> [in]

<dd>
<p>A pointer to the caller-implemented <a href="https://msdn.microsoft.com/library/windows/hardware/mt764088">PLOAD_IMAGE_NOTIFY_ROUTINE</a> callback routine for load-image notifications.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Supplies a bitmask of flags that control the callback function. Here are the possible values:</p>
<ul>
<li>PS_IMAGE_NOTIFY_CONFLICTING_ARCHITECTURE indicates that the callback routine should be invoked for all potentially executable images, including images that have a different architecture from the native architecture of the operating system.

</li>
</ul>
</dd>
</dl>

## -returns
<dl>
<dt><b>STATUS_SUCCESS </b></dt>
</dl><p>The callback was successfully registered.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_2</b></dt>
</dl><p>Invalid flag was supplied in <i>Flags</i>.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The routine failed allocate a callback block due to lack of resources.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h</dt>
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
<dt>NtosKrnl.exe (kernel mode)</dt>
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