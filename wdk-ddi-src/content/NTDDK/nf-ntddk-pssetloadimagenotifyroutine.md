---
UID: NF.ntddk.PsSetLoadImageNotifyRoutine
title: PsSetLoadImageNotifyRoutine
author: windows-driver-content
description: The PsSetLoadImageNotifyRoutine routine registers a driver-supplied callback that is subsequently notified whenever an image is loaded (or mapped into memory).
old-location: kernel\pssetloadimagenotifyroutine.htm
ms.assetid: e90bc043-1b92-474c-b6c7-7e510271118b
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsSetLoadImageNotifyRoutine
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
ms.keywords: PsSetLoadImageNotifyRoutine
req.iface: 
---

# PsSetLoadImageNotifyRoutine function



## -description
<p>The <b>PsSetLoadImageNotifyRoutine</b> routine registers a driver-supplied callback that is subsequently notified whenever an image is loaded (or mapped into memory).</p>


## -syntax

````
NTSTATUS PsSetLoadImageNotifyRoutine(
  _In_ PLOAD_IMAGE_NOTIFY_ROUTINE NotifyRoutine
);
````


## -parameters
<dl>

### -param <i>NotifyRoutine</i> [in]

<dd>
<p>A pointer to the caller-implemented <a href="https://msdn.microsoft.com/library/windows/hardware/mt764088">PLOAD_IMAGE_NOTIFY_ROUTINE</a> callback routine for load-image notifications.</p>
</dd>
</dl>

## -returns
<p><b>PsSetLoadImageNotifyRoutine</b> either returns STATUS_SUCCESS or it returns STATUS_INSUFFICIENT_RESOURCES if it failed the callback registration.</p>

## -remarks
<p>Highest-level system-profiling drivers can call <b>PsSetLoadImageNotifyRoutine</b> to set up their load-image notify routines (see <a href="https://msdn.microsoft.com/library/windows/hardware/mt764088">PLOAD_IMAGE_NOTIFY_ROUTINE</a>).</p>

<p>The maximum number of drivers that can be simultaneously registered to receive load-image notifications is eight. If the maximum number of load-image notify routines is already registered when a driver calls <b>PsSetLoadImageNotifyRoutine</b> to try to register an additional notify routine, <b>PsSetLoadImageNotifyRoutine</b> fails and returns STATUS_INSUFFICIENT_RESOURCES.</p>

<p><b>Notes</b></p>

<p>A driver must remove any callbacks it registers before it unloads. You can remove the callback by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559949">PsRemoveLoadImageNotifyRoutine</a> routine.</p>

<p>Highest-level system-profiling drivers can call <b>PsSetLoadImageNotifyRoutine</b> to set up their load-image notify routines (see <a href="https://msdn.microsoft.com/library/windows/hardware/mt764088">PLOAD_IMAGE_NOTIFY_ROUTINE</a>).</p>

<p>The maximum number of drivers that can be simultaneously registered to receive load-image notifications is eight. If the maximum number of load-image notify routines is already registered when a driver calls <b>PsSetLoadImageNotifyRoutine</b> to try to register an additional notify routine, <b>PsSetLoadImageNotifyRoutine</b> fails and returns STATUS_INSUFFICIENT_RESOURCES.</p>

<p><b>Notes</b></p>

<p>A driver must remove any callbacks it registers before it unloads. You can remove the callback by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559949">PsRemoveLoadImageNotifyRoutine</a> routine.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt764088">PLOAD_IMAGE_NOTIFY_ROUTINE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559935">PsGetCurrentProcessId</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559949">PsRemoveLoadImageNotifyRoutine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559951">PsSetCreateProcessNotifyRoutine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559954">PsSetCreateThreadNotifyRoutine</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PsSetLoadImageNotifyRoutine routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
