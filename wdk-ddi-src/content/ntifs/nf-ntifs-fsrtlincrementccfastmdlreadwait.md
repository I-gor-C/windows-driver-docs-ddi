---
UID: NF.ntifs.FsRtlIncrementCcFastMdlReadWait
title: FsRtlIncrementCcFastMdlReadWait
author: windows-driver-content
description: The FsRtlIncrementCcFastMdlReadWait routine increments the cache manager's CcFastMdlReadWait performance counter member in a processor control block (PRCB) object.
old-location: ifsk\fsrtlincrementccfastmdlreadwait.htm
old-project: ifsk
ms.assetid: a3a811dc-1dbf-4656-b7ec-bad818f6d1f1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FsRtlIncrementCcFastMdlReadWait
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlIncrementCcFastMdlReadWait
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
req.irql: <= APC_LEVEL
req.iface: 
---

# FsRtlIncrementCcFastMdlReadWait function



## -description
<p>The <b>FsRtlIncrementCcFastMdlReadWait </b>routine increments the cache manager's <b>CcFastMdlReadWait</b> performance counter member in a processor control block (<a href="wdkgloss.p#wdkgloss.prcb#wdkgloss.prcb"><i>PRCB</i></a>) object.</p>


## -syntax

````
VOID FsRtlIncrementCcFastMdlReadWait(
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
<p><b>FsRtlIncrementCcFastMdlReadWait </b>increments the cache manager's <b>CcFastMdlReadWait</b> performance counter in the per-processor control block for the processor on which <b>FsRtlIncrementCcFastMdlReadWait</b> is called. This counter records the number of fast I/O <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> read operations (FsRtlMdlRead) serviced by a file system driver.  </p>

<p>File system drivers should call this function to update the <b>CcFastMdlReadWait</b> performance counter if the driver chooses to override the default fast I/O MDL read handler.</p>

<p>The counter is only used to record fast I/O MDL read operations for a nonzero length.  <b>FsRtlIncrementCcFastMdlReadWait</b> should not be called for a zero-length fast I/O MDL read.</p>

<p>File system drivers should not increment the <b>CcFastMdlReadWait</b> performance counter if their fast I/O MDL read handler returns <b>FALSE</b> due to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548405">IoGetTopLevelIrp</a> returning a non-<b>NULL</b> value.  The counter should only be incremented if the file system driver actually attempts to satisfy a nonzero-length fast I/O MDL read.</p>

<p><b>FsRtlIncrementCcFastMdlReadWait </b>increments the cache manager's <b>CcFastMdlReadWait</b> performance counter in the per-processor control block for the processor on which <b>FsRtlIncrementCcFastMdlReadWait</b> is called. This counter records the number of fast I/O <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> read operations (FsRtlMdlRead) serviced by a file system driver.  </p>

<p>File system drivers should call this function to update the <b>CcFastMdlReadWait</b> performance counter if the driver chooses to override the default fast I/O MDL read handler.</p>

<p>The counter is only used to record fast I/O MDL read operations for a nonzero length.  <b>FsRtlIncrementCcFastMdlReadWait</b> should not be called for a zero-length fast I/O MDL read.</p>

<p>File system drivers should not increment the <b>CcFastMdlReadWait</b> performance counter if their fast I/O MDL read handler returns <b>FALSE</b> due to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548405">IoGetTopLevelIrp</a> returning a non-<b>NULL</b> value.  The counter should only be incremented if the file system driver actually attempts to satisfy a nonzero-length fast I/O MDL read.</p>

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
<p>Available in Windows Vista and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include FltKernel.h or Ntifs.h)</dt>
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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548405">IoGetTopLevelIrp</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlIncrementCcFastMdlReadWait routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
