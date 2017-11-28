---
UID: NF.ntifs.CcCopyReadEx
title: CcCopyReadEx
author: windows-driver-content
description: The CcCopyReadEx routine copies data from a cached file to a user buffer. The I/O byte count for the operation is charged to the issuing thread.
old-location: ifsk\cccopyreadex.htm
old-project: ifsk
ms.assetid: 4108EB7A-F8FB-4FA5-8426-BB434E89AF06
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: CcCopyReadEx
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
req.alt-api: CcCopyReadEx
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

# CcCopyReadEx function



## -description
<p>The <b>CcCopyReadEx</b> routine copies data from a cached file to a user buffer. The I/O byte count for the operation is charged to the issuing thread.</p>


## -syntax

````
BOOLEAN CcCopyReadEx(
  _In_  PFILE_OBJECT     FileObject,
  _In_  PLARGE_INTEGER   FileOffset,
  _In_  ULONG            Length,
  _In_  BOOLEAN          Wait,
  _Out_ PVOID            Buffer,
  _Out_ PIO_STATUS_BLOCK IoStatus,
  _In_  PETHREAD         IoIssuerThread
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>A pointer to a file object for the cached file from which the data is to be read.</p>
</dd>

### -param <i>FileOffset</i> [in]

<dd>
<p>A pointer to a variable that specifies the starting byte offset within the cached file.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The length in bytes of the data to be read.</p>
</dd>

### -param <i>Wait</i> [in]

<dd>
<p>Set to <b>TRUE</b> if the caller can be put into a wait state until all the data has been copied, <b>FALSE</b> otherwise.</p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>A pointer to a buffer into which the data is to be copied. </p>
</dd>

### -param <i>IoStatus</i> [out]

<dd>
<p>A pointer to a caller-allocated structure that receives the final completion status and information about the operation. If not all of the data is copied successfully, <i>IoStatus.Information</i> contains the actual number of bytes that were copied.</p>
</dd>

### -param <i>IoIssuerThread</i> [in]

<dd>
<p>The thread issuing the read request. For a file system with disk I/O accounting enabled, this is the thread the I/O is charged to. If <i>IoIssuerThread</i> is NULL, the I/O is charged to the current thread.</p>
</dd>
</dl>

## -returns
<p>The <b>CcCopyReadEx</b> routine returns <b>TRUE</b> if the data was copied successfully, <b>FALSE</b> otherwise.</p>

## -remarks
<p>If <i>Wait</i> is <b>TRUE</b>, <b>CcCopyReadEx</b> is guaranteed to complete the copy request and return <b>TRUE</b>. If the required pages of the cached file are already resident in memory, the data will be copied immediately and no blocking will occur. If any needed pages are not resident, the caller will be put in a wait state until all required pages have been made resident and the data can be copied.</p>

<p>If <i>Wait</i> is <b>FALSE</b>, <b>CcCopyReadEx</b> will refuse to block, and will return <b>FALSE</b>, if the required pages of the cached file are not already resident in memory. </p>

<p><i>FileOffset</i> plus <i>Length</i> must be less than or equal to the size of the cached file, or an assertion failure will occur.</p>

<p>If any failure occurs, <b>CcCopyReadEx</b> raises a status exception for that particular failure. For example, if a pool allocation failure occurs, <b>CcCopyReadEx</b> raises an exception with the <b>STATUS_INSUFFICIENT_RESOURCES</b> status; if an I/O error occurs, <b>CcCopyReadEx</b> raises the status exception of the I/O error. Therefore, to gain control if a failure occurs, the driver should wrap the call to <b>CcCopyReadEx</b> in a <b>try-except</b> or <b>try-finally</b> statement.</p>

<p>To cache a file, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff539135">CcInitializeCacheMap</a>.</p>

<p>If <i>Wait</i> is <b>TRUE</b>, <b>CcCopyReadEx</b> is guaranteed to complete the copy request and return <b>TRUE</b>. If the required pages of the cached file are already resident in memory, the data will be copied immediately and no blocking will occur. If any needed pages are not resident, the caller will be put in a wait state until all required pages have been made resident and the data can be copied.</p>

<p>If <i>Wait</i> is <b>FALSE</b>, <b>CcCopyReadEx</b> will refuse to block, and will return <b>FALSE</b>, if the required pages of the cached file are not already resident in memory. </p>

<p><i>FileOffset</i> plus <i>Length</i> must be less than or equal to the size of the cached file, or an assertion failure will occur.</p>

<p>If any failure occurs, <b>CcCopyReadEx</b> raises a status exception for that particular failure. For example, if a pool allocation failure occurs, <b>CcCopyReadEx</b> raises an exception with the <b>STATUS_INSUFFICIENT_RESOURCES</b> status; if an I/O error occurs, <b>CcCopyReadEx</b> raises the status exception of the I/O error. Therefore, to gain control if a failure occurs, the driver should wrap the call to <b>CcCopyReadEx</b> in a <b>try-except</b> or <b>try-finally</b> statement.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539067">CcFastCopyRead</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcCopyReadEx routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
