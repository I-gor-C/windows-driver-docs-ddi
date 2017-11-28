---
UID: NF.ntifs.CcScheduleReadAheadEx
title: CcScheduleReadAheadEx
author: windows-driver-content
description: The CcScheduleReadAheadEx routine performs read-ahead (also called &#0034;lazy read&#0034;) on a cached file. The I/O byte count for the operation is charged to the issuing thread.
old-location: ifsk\ccschedulereadaheadex.htm
old-project: ifsk
ms.assetid: 8549DAA9-3BD3-4CED-AC2A-EFADF317EF5A
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: CcScheduleReadAheadEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h, FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CcScheduleReadAheadEx
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

# CcScheduleReadAheadEx function



## -description
<p>The <b>CcScheduleReadAheadEx</b> routine performs read-ahead (also called "lazy read") on a cached file. The I/O byte count for the operation is charged to the issuing thread.</p>


## -syntax

````
VOID CcScheduleReadAheadEx(
  _In_ PFILE_OBJECT   FileObject,
  _In_ PLARGE_INTEGER FileOffset,
  _In_ ULONG          Length,
  _In_ PETHREAD       IoIssuerThread
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>Pointer to a file object for the file on which read-ahead is to be performed.</p>
</dd>

### -param <i>FileOffset</i> [in]

<dd>
<p>Pointer to a variable that specifies the starting byte offset within the cached file where the last read occurred.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Length in bytes of the range that was last read.</p>
</dd>

### -param <i>IoIssuerThread</i> [in]

<dd>
<p>The thread issuing the read ahead request. For a file system with disk I/O accounting enabled, this is the thread the I/O is charged to. If <i>IoIssuerThread</i> is NULL, the I/O is charged to the current thread.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>CcScheduleReadAheadEx</b> should be called only when <i>Length</i> &gt;= 256. Measurements have shown that calling <b>CcScheduleReadAheadEx</b> for smaller reads actually decreases performance.</p>

<p><b>CcScheduleReadAheadEx</b> can only be called after a successful call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff539038">CcCopyRead</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh971560">CcCopyReadEx</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff539067">CcFastCopyRead</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff539159">CcMdlRead</a>.</p>

<p><b>CcScheduleReadAheadEx</b> should be called only when <i>Length</i> &gt;= 256. Measurements have shown that calling <b>CcScheduleReadAheadEx</b> for smaller reads actually decreases performance.</p>

<p><b>CcScheduleReadAheadEx</b> can only be called after a successful call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff539038">CcCopyRead</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh971560">CcCopyReadEx</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff539067">CcFastCopyRead</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff539159">CcMdlRead</a>.</p>

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
<dt>Ntifs.h (include Ntifs.h or FltKernel.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539038">CcCopyRead</a>
</dt>
<dt><b>CcCopyReadEx</b></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539067">CcFastCopyRead</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539159">CcMdlRead</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539191">CcReadAhead</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539203">CcSetAdditionalCacheAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539224">CcSetReadAheadGranularity</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcScheduleReadAheadEx routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
