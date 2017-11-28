---
UID: NF.ntifs.PsUpdateDiskCounters
title: PsUpdateDiskCounters
author: windows-driver-content
description: The PsUpdateDiskCounters routine updates the disk I/O counters of a given process.
old-location: ifsk\psupdatediskcounters.htm
old-project: ifsk
ms.assetid: 0BDC6629-9C0E-4437-888D-1EF730714CA4
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: PsUpdateDiskCounters
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsUpdateDiskCounters
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# PsUpdateDiskCounters function



## -description
<p>The <b>PsUpdateDiskCounters</b> routine updates the disk I/O counters of a given process.</p>


## -syntax

````
VOID PsUpdateDiskCounters(
   PEPROCESS Process,
   ULONG64   BytesRead,
   ULONG64   BytesWritten,
   ULONG     ReadOperationCount,
   ULONG     WriteOperationCount,
   ULONG     FlushOperationCount
);
````


## -parameters
<dl>

### -param <i>Process</i> 

<dd>
<p>A pointer to the process to update counters for.</p>
</dd>

### -param <i>BytesRead</i> 

<dd>
<p>The number of bytes to update in the Read counter.</p>
</dd>

### -param <i>BytesWritten</i> 

<dd>
<p>The number of bytes to update in the Write counter.</p>
</dd>

### -param <i>ReadOperationCount</i> 

<dd>
<p>The number of read operations to update in the Read Operation counter.</p>
</dd>

### -param <i>WriteOperationCount</i> 

<dd>
<p>The number of write operations to update in the Write Operation counter.</p>
</dd>

### -param <i>FlushOperationCount</i> 

<dd>
<p>The number of flush operations to update in the Flush Operation counter.</p>
</dd>
</dl>

## -returns
<p>This routine does not return a value.</p>

## -remarks
<p>File system drivers use <b>PsUpdateDiskCounters</b> to update counts for disk I/O accounting. A client process can be "charged" the disk I/O counts by the file system.</p>

<p>File system drivers use <b>PsUpdateDiskCounters</b> to update counts for disk I/O accounting. A client process can be "charged" the disk I/O counts by the file system.</p>

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
<p>Available starting with Windows 8.</p>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971608">PsIsDiskCountersEnabled</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PsUpdateDiskCounters routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
