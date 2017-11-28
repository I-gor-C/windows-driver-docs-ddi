---
UID: NF.ntifs.FsRtlIncrementCcFastReadResourceMiss
title: FsRtlIncrementCcFastReadResourceMiss
author: windows-driver-content
description: The FsRtlIncrementCcFastReadResourceMiss routine increments the CcFastReadNotPossible performance counter in a per processor control block of cache manager system counters.
old-location: ifsk\fsrtlincrementccfastreadresourcemiss.htm
old-project: ifsk
ms.assetid: 38264afe-e324-455d-b81a-7dafae8abc1c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FsRtlIncrementCcFastReadResourceMiss
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlIncrementCcFastReadResourceMiss
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
req.irql: Any level
req.iface: 
---

# FsRtlIncrementCcFastReadResourceMiss function



## -description
<p>The <b>FsRtlIncrementCcFastReadResourceMiss</b> routine increments the CcFastReadNotPossible performance counter in a per processor control block of cache manager system counters.</p>


## -syntax

````
VOID FsRtlIncrementCcFastReadResourceMiss(
   VOID 
);
````


## -parameters
<dl>

### -param <i></i> 

<dd>
<p>None</p>
</dd>
</dl>

## -returns
<p>This routine does not return a value.</p>

## -remarks
<p><b>FsRtlIncrementCcFastReadResourceMiss </b>increments the CcFastReadReadResourceMiss performance counter in the per processor control block of cache manager system counters. This counter indicates that a fast I/O read operation (<a href="https://msdn.microsoft.com/library/windows/hardware/ff545791">FsRtlCopyRead</a>) was called, but fast I/O was not possible because the file resource could not be acquired for shared access. </p>

<p>File system drivers should call this function to update the performance counter if the driver chooses to override the default fast I/O read handler.</p>

<p><b>FsRtlIncrementCcFastReadResourceMiss </b>increments the CcFastReadReadResourceMiss performance counter in the per processor control block of cache manager system counters. This counter indicates that a fast I/O read operation (<a href="https://msdn.microsoft.com/library/windows/hardware/ff545791">FsRtlCopyRead</a>) was called, but fast I/O was not possible because the file resource could not be acquired for shared access. </p>

<p>File system drivers should call this function to update the performance counter if the driver chooses to override the default fast I/O read handler.</p>

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
<p>This routine is available on Microsoft Windows XP and later. </p>
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
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545791">FsRtlCopyRead</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546078">FsRtlIncrementCcFastReadNotPossible</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546085">FsRtlIncrementCcFastReadNoWait</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546096">FsRtlIncrementCcFastReadWait</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlIncrementCcFastReadResourceMiss routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
