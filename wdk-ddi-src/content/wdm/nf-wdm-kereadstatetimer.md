---
UID: NF.wdm.KeReadStateTimer
title: KeReadStateTimer
author: windows-driver-content
description: The KeReadStateTimer routine reads the current state of a timer object.
old-location: kernel\kereadstatetimer.htm
old-project: kernel
ms.assetid: 0f7fc534-4a81-42e0-a3e6-8b91baa28b55
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: KeReadStateTimer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeReadStateTimer
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlKeDispatchLte, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# KeReadStateTimer function



## -description
<p>The <b>KeReadStateTimer</b> routine reads the current state of a timer object.</p>


## -syntax

````
BOOLEAN KeReadStateTimer(
  _In_ PKTIMER Timer
);
````


## -parameters
<dl>

### -param <i>Timer</i> [in]

<dd>
<p>A pointer to an initialized timer object, for which the caller provides the storage.</p>
</dd>
</dl>

## -returns
<p><b>KeReadStateTimer</b> returns <b>TRUE</b> if the current state of the timer object is signaled; otherwise, it returns <b>FALSE</b>.</p>

## -remarks
<p>This routine provides an efficient way to poll the signal state of a timer. <b>KeReadStateTimer</b> reads the state of the timer without synchronizing its access to the timer. Do not assume that accesses of a timer state by <b>KeReadStateTimer</b> are mutually exclusive of accesses by routines, such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff553286">KeSetTimer</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553350">KeWaitForSingleObject</a>, that do synchronize their access to the timer state.</p>

<p>For more information about timer objects, see <a href="https://msdn.microsoft.com/b58487de-6e9e-45f4-acb8-9233c8718ee2">Timer Objects and DPCs</a>.</p>

<p>This routine provides an efficient way to poll the signal state of a timer. <b>KeReadStateTimer</b> reads the state of the timer without synchronizing its access to the timer. Do not assume that accesses of a timer state by <b>KeReadStateTimer</b> are mutually exclusive of accesses by routines, such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff553286">KeSetTimer</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553350">KeWaitForSingleObject</a>, that do synchronize their access to the timer state.</p>

<p>For more information about timer objects, see <a href="https://msdn.microsoft.com/b58487de-6e9e-45f4-acb8-9233c8718ee2">Timer Objects and DPCs</a>.</p>

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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547812">IrqlKeDispatchLte</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551970">KeCancelTimer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552168">KeInitializeTimer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553286">KeSetTimer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553350">KeWaitForSingleObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554250">KTIMER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeReadStateTimer routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
