---
UID: NF.wdm.KeReadStateSemaphore
title: KeReadStateSemaphore
author: windows-driver-content
description: The KeReadStateSemaphore routine returns the current state, signaled or not-signaled, of the specified semaphore object.
old-location: kernel\kereadstatesemaphore.htm
ms.assetid: e88c89fb-c308-4c6d-a67d-c8f98d539a43
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
req.alt-api: KeReadStateSemaphore
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: Any level
ms.keywords: KeReadStateSemaphore
req.iface: 
req.product: Windows 10 or later.
---

# KeReadStateSemaphore function



## -description
<p>The <b>KeReadStateSemaphore</b> routine returns the current state, signaled or not-signaled, of the specified semaphore object.</p>


## -syntax

````
LONG KeReadStateSemaphore(
  _In_ PRKSEMAPHORE Semaphore
);
````


## -parameters
<dl>

### -param <i>Semaphore</i> [in]

<dd>
<p>Pointer to an initialized semaphore object for which the caller provides the storage.</p>
</dd>
</dl>

## -returns
<p>If the return value is zero, the semaphore object is set to a not-signaled state.</p>

## -remarks
<p>This routine provides an efficient way to poll the signal state of a semaphore. <b>KeReadStateSemaphore</b> reads the state of the semaphore without synchronizing its access to the semaphore. Do not assume that accesses of a semaphore state by <b>KeReadStateSemaphore</b> are mutually exclusive of accesses by routines, such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff553143">KeReleaseSemaphore</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553350">KeWaitForSingleObject</a>, that do synchronize their access to the semaphore state.</p>

<p>For more information about semaphore objects, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563719">Semaphore Objects</a>. </p>

<p>This routine provides an efficient way to poll the signal state of a semaphore. <b>KeReadStateSemaphore</b> reads the state of the semaphore without synchronizing its access to the semaphore. Do not assume that accesses of a semaphore state by <b>KeReadStateSemaphore</b> are mutually exclusive of accesses by routines, such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff553143">KeReleaseSemaphore</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553350">KeWaitForSingleObject</a>, that do synchronize their access to the semaphore state.</p>

<p>For more information about semaphore objects, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563719">Semaphore Objects</a>. </p>

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
<p>Any level</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552150">KeInitializeSemaphore</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553143">KeReleaseSemaphore</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553350">KeWaitForSingleObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeReadStateSemaphore routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
