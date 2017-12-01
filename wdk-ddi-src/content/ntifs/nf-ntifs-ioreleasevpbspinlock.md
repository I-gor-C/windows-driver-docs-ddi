---
UID: NF.ntifs.IoReleaseVpbSpinLock
title: IoReleaseVpbSpinLock
author: windows-driver-content
description: The IoReleaseVpbSpinLock routine releases the Volume Parameter Block (VPB) spin lock.
old-location: ifsk\ioreleasevpbspinlock.htm
old-project: ifsk
ms.assetid: c0b93f32-4c5c-472c-8c13-3e441f86475f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IoReleaseVpbSpinLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoReleaseVpbSpinLock
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
req.irql: DISPATCH_LEVEL
req.iface: 
---

# IoReleaseVpbSpinLock function



## -description
<p>The <b>IoReleaseVpbSpinLock</b> routine releases the Volume Parameter Block (VPB) spin lock. </p>


## -syntax

````
VOID IoReleaseVpbSpinLock(
  _In_ KIRQL Irql
);
````


## -parameters
<dl>

### -param <i>Irql</i> [in]

<dd>
<p>Saved IRQL value returned by <a href="..\ntifs\nf-ntifs-ioacquirevpbspinlock.md">IoAcquireVpbSpinLock</a> when the VPB spin lock was acquired. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>This routine is the reciprocal to <a href="..\ntifs\nf-ntifs-ioacquirevpbspinlock.md">IoAcquireVpbSpinLock</a>. Every successful call to <b>IoAcquireVpbSpinLock</b> must be matched by a subsequent call to <b>IoReleaseVpbSpinLock</b>. </p>

<p>Before using <a href="..\ntifs\nf-ntifs-ioacquirevpbspinlock.md">IoAcquireVpbSpinLock</a> and <b>IoReleaseVpbSpinLock</b>, driver writers are strongly encouraged to study the way these routines are used in the FASTFAT sample. </p>

<p>The holder of the VPB spin lock executes at IRQL DISPATCH_LEVEL after calling <a href="..\ntifs\nf-ntifs-ioacquirevpbspinlock.md">IoAcquireVpbSpinLock</a>. <b>IoReleaseVpbSpinLock</b> restores the caller's original IRQL. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
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
<p>DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\nf-ntifs-ioacquirevpbspinlock.md">IoAcquireVpbSpinLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IoReleaseVpbSpinLock routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
