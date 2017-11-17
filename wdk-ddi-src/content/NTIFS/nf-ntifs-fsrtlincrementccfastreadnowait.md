---
UID: NF.ntifs.FsRtlIncrementCcFastReadNoWait
title: FsRtlIncrementCcFastReadNoWait
author: windows-driver-content
description: The FsRtlIncrementCcFastReadNoWait routine increments the CcFastReadNoWait performance counter in a per processor control block of cache manager system counters.
old-location: ifsk\fsrtlincrementccfastreadnowait.htm
ms.assetid: 14a1b22a-5d1b-4da6-9610-396fa128ce01
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlIncrementCcFastReadNoWait
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
ms.keywords: FsRtlIncrementCcFastReadNoWait
req.iface: 
---

# FsRtlIncrementCcFastReadNoWait function



## -description
<p>The <b>FsRtlIncrementCcFastReadNoWait</b> routine increments the CcFastReadNoWait performance counter in a per processor control block of cache manager system counters.</p>


## -syntax

````
VOID FsRtlIncrementCcFastReadNoWait(
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
<p><b>FsRtlIncrementCcFastReadNoWait</b> increments the CcFastReadNoWait performance counter in the per processor control block of cache manager system counters. This counter indicates that a fast I/O read operation, <a href="https://msdn.microsoft.com/library/windows/hardware/ff545791">FsRtlCopyRead</a>, was called with the <i>Wait</i> parameter set to <b>FALSE</b> indicating that the caller cannot be put into a wait state until all the data has been copied.</p>

<p>File system drivers should call this function to update the performance counter if the driver chooses to override the default fast I/O read handler.</p>

<p><b>FsRtlIncrementCcFastReadNoWait</b> increments the CcFastReadNoWait performance counter in the per processor control block of cache manager system counters. This counter indicates that a fast I/O read operation, <a href="https://msdn.microsoft.com/library/windows/hardware/ff545791">FsRtlCopyRead</a>, was called with the <i>Wait</i> parameter set to <b>FALSE</b> indicating that the caller cannot be put into a wait state until all the data has been copied.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546091">FsRtlIncrementCcFastReadResourceMiss</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546096">FsRtlIncrementCcFastReadWait</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlIncrementCcFastReadNoWait routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
