---
UID: NF.ntifs.CcFastCopyRead
title: CcFastCopyRead
author: windows-driver-content
description: The CcFastCopyRead routine performs a fast copy read from a cached file to a buffer in memory.
old-location: ifsk\ccfastcopyread.htm
ms.assetid: 725ede16-5fc6-4465-bcdc-da7702779d68
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CcFastCopyRead
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
req.irql: < DISPATCH_LEVEL
ms.keywords: CcFastCopyRead
req.iface: 
---

# CcFastCopyRead function



## -description
<p>The <b>CcFastCopyRead</b> routine performs a fast copy read from a cached file to a buffer in memory.</p>


## -syntax

````
VOID CcFastCopyRead(
  _In_  PFILE_OBJECT     FileObject,
  _In_  ULONG            FileOffset,
  _In_  ULONG            Length,
  _In_  ULONG            PageCount,
  _Out_ PVOID            Buffer,
  _Out_ PIO_STATUS_BLOCK IoStatus
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>Pointer to a file object for the cached file from which the data is to be read.</p>
</dd>

### -param <i>FileOffset</i> [in]

<dd>
<p>Starting byte offset within the cached file.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Length in bytes of the data to be read.</p>
</dd>

### -param <i>PageCount</i> [in]

<dd>
<p>Number of pages spanned by the read.</p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>Pointer to a buffer into which the data is to be copied. </p>
</dd>

### -param <i>IoStatus</i> [out]

<dd>
<p>Pointer to a structure that receives the final completion status and information about the operation. If not all of the data is copied successfully, <i>IoStatus.Information</i> contains the actual number of bytes that were copied.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>CcFastCopyRead</b> is a faster version of <a href="https://msdn.microsoft.com/library/windows/hardware/ff539038">CcCopyRead</a>. It differs from <b>CcCopyRead</b> in the following respects:</p>

<p><i>FileOffset</i> is a ULONG, not a PLARGE_INTEGER.</p>

<p>There is no <i>Wait</i> parameter. The caller must be able to enter a wait state until all the data has been copied.</p>

<p><b>CcFastCopyRead</b> does not return a BOOLEAN to indicate whether the read operation was successful.</p>

<p><i>FileOffset</i> plus <i>Length</i> must be less than or equal to the size of the cached file, or an assertion failure will occur.</p>

<p>If any failure occurs, <b>CcFastCopyRead</b> raises a status exception for that particular failure. For example, if a pool allocation failure occurs, <b>CcFastCopyRead</b> raises a STATUS_INSUFFICIENT_RESOURCES exception; if an I/O error occurs, <b>CcFastCopyRead</b> raises the status exception of the I/O error. Therefore, to gain control if a failure occurs, the driver should wrap the call to <b>CcFastCopyRead</b> in a <b>try-except</b> or <b>try-finally</b> statement.</p>

<p>To cache a file, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff539135">CcInitializeCacheMap</a>.</p>

<p><b>CcFastCopyRead</b> is a faster version of <a href="https://msdn.microsoft.com/library/windows/hardware/ff539038">CcCopyRead</a>. It differs from <b>CcCopyRead</b> in the following respects:</p>

<p><i>FileOffset</i> is a ULONG, not a PLARGE_INTEGER.</p>

<p>There is no <i>Wait</i> parameter. The caller must be able to enter a wait state until all the data has been copied.</p>

<p><b>CcFastCopyRead</b> does not return a BOOLEAN to indicate whether the read operation was successful.</p>

<p><i>FileOffset</i> plus <i>Length</i> must be less than or equal to the size of the cached file, or an assertion failure will occur.</p>

<p>If any failure occurs, <b>CcFastCopyRead</b> raises a status exception for that particular failure. For example, if a pool allocation failure occurs, <b>CcFastCopyRead</b> raises a STATUS_INSUFFICIENT_RESOURCES exception; if an I/O error occurs, <b>CcFastCopyRead</b> raises the status exception of the I/O error. Therefore, to gain control if a failure occurs, the driver should wrap the call to <b>CcFastCopyRead</b> in a <b>try-except</b> or <b>try-finally</b> statement.</p>

<p>To cache a file, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff539135">CcInitializeCacheMap</a>.</p>

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
<p>&lt; DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539038">CcCopyRead</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539135">CcInitializeCacheMap</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539191">CcReadAhead</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539200">CcScheduleReadAhead</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcFastCopyRead routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
