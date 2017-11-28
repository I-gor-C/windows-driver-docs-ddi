---
UID: NF.wdm.ExInterlockedAddLargeStatistic
title: ExInterlockedAddLargeStatistic
author: windows-driver-content
description: The ExInterlockedAddLargeStatistic routine performs an interlocked addition of a ULONG increment value to a LARGE_INTEGER variable.
old-location: kernel\exinterlockedaddlargestatistic.htm
old-project: kernel
ms.assetid: f044a344-4768-499b-85b4-714062111b2c
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ExInterlockedAddLargeStatistic
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
req.alt-api: ExInterlockedAddLargeStatistic
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
req.irql: Any level (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# ExInterlockedAddLargeStatistic function



## -description
<p>The <b>ExInterlockedAddLargeStatistic</b> routine performs an interlocked addition of a ULONG increment value to a LARGE_INTEGER variable.</p>


## -syntax

````
VOID ExInterlockedAddLargeStatistic(
  _In_ PLARGE_INTEGER Addend,
  _In_ ULONG          Increment
);
````


## -parameters
<dl>

### -param <i>Addend</i> [in]

<dd>
<p>A pointer to the LARGE_INTEGER variable that is incremented by the value of <i>Increment</i>.</p>
</dd>

### -param <i>Increment</i> [in]

<dd>
<p>Specifies a ULONG value that is added to the variable that <i>Addend</i> points to. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Support routines that do interlocked operations must not cause a page fault. Neither their code nor any of the data they access can cause a page fault without bringing down the system. </p>

<p><b>ExInterlockedAddLargeStatistic</b> masks interrupts, and can be safely used to synchronize an ISR with other driver code.</p>

<p><b>ExInterlockedAddLargeStatistic</b> runs at any IRQL. The storage for the <i>Addend</i> parameter must be resident at all IRQLs.</p>

<p>Support routines that do interlocked operations must not cause a page fault. Neither their code nor any of the data they access can cause a page fault without bringing down the system. </p>

<p><b>ExInterlockedAddLargeStatistic</b> masks interrupts, and can be safely used to synchronize an ISR with other driver code.</p>

<p><b>ExInterlockedAddLargeStatistic</b> runs at any IRQL. The storage for the <i>Addend</i> parameter must be resident at all IRQLs.</p>

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
<p>Any level (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545335">ExInterlockedAddLargeInteger</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545343">ExInterlockedAddUlong</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExInterlockedAddLargeStatistic routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
