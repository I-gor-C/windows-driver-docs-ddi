---
UID: NF.ntifs.FsRtlFastLock
title: FsRtlFastLock
author: windows-driver-content
description: The FsRtlFastLock macro is used by file systems and filter drivers to request a byte-range lock for a file stream.
old-location: ifsk\fsrtlfastlock.htm
old-project: ifsk
ms.assetid: c3e209b5-9925-4911-8c42-0f15c1c710be
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FsRtlFastLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlFastLock
req.alt-loc: ntifs.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
---

# FsRtlFastLock function



## -description
<p>The <b>FsRtlFastLock</b> macro is used by file systems and filter drivers to request a byte-range lock for a file stream. </p>


## -syntax

````
BOOLEAN FsRtlFastLock(
  _In_  PFILE_LOCK       FileLock,
  _In_  PFILE_OBJECT     FileObject,
  _In_  PLARGE_INTEGER   FileOffset,
  _In_  PLARGE_INTEGER   Length,
  _In_  PEPROCESS        ProcessId,
  _In_  ULONG            Key,
  _In_  BOOLEAN          FailImmediately,
  _In_  BOOLEAN          ExclusiveLock,
  _Out_ PIO_STATUS_BLOCK Iosb,
  _In_  PVOID            Context,
  _In_  BOOLEAN          AlreadySynchronized
);
````


## -parameters
<dl>

### -param <i>FileLock</i> [in]

<dd>
<p>Pointer to the FILE_LOCK structure for the file. This structure must have been initialized by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545640">FsRtlAllocateFileLock</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff546122">FsRtlInitializeFileLock</a>.</p>
</dd>

### -param <i>FileObject</i> [in]

<dd>
<p>Pointer to the file object for the open file. The file object must have been created with GENERIC_READ or GENERIC_WRITE access to the file (or both). </p>
</dd>

### -param <i>FileOffset</i> [in]

<dd>
<p>Pointer to a variable that specifies the starting byte offset within the file of the range to be locked.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Pointer to a variable that specifies the length in bytes of the range to be locked.</p>
</dd>

### -param <i>ProcessId</i> [in]

<dd>
<p>Pointer to the process ID for the process requesting the byte-range lock.</p>
</dd>

### -param <i>Key</i> [in]

<dd>
<p>The key to be assigned to the byte-range lock.</p>
</dd>

### -param <i>FailImmediately</i> [in]

<dd>
<p>Boolean value specifying whether the lock request should fail if the lock cannot be granted immediately. If the caller can be put into a wait state until the request is granted, set <i>FailImmediately</i> to <b>FALSE</b>. If it cannot, set <i>FailImmediately</i> to <b>TRUE</b>. </p>
</dd>

### -param <i>ExclusiveLock</i> [in]

<dd>
<p>Set to <b>TRUE</b> if an exclusive lock is requested, <b>FALSE</b> if a shared lock is requested.</p>
</dd>

### -param <i>Iosb</i> [out]

<dd>
<p>Pointer to a caller-allocated IO_STATUS_BLOCK structure that receives status information about the lock request. </p>
</dd>

### -param <i>Context</i> [in]

<dd>
<p>Optional pointer to a context to use when releasing the byte-range lock. </p>
</dd>

### -param <i>AlreadySynchronized</i> [in]

<dd>
<p>This parameter is obsolete, but is retained for compatibility with legacy drivers.</p>
</dd>
</dl>

## -returns
<p>If <i>FailImmediately</i> is <b>FALSE</b>, <b>FsRtlFastLock</b> returns <b>TRUE</b> if the lock operation succeeds, <b>FALSE</b> otherwise.</p>

<p>If <i>FailImmediately</i> is <b>TRUE</b>, <b>FsRtlFastLock</b> always returns <b>TRUE</b>.</p>

## -remarks
<p>The <b>FsRtlFastLock</b> macro causes the caller to acquire a byte-range lock on a region of the specified file.</p>

<p>A return value of <b>TRUE</b> indicates that the IO_STATUS_BLOCK structure pointed to by <i>Iosb</i> received status information about the lock operation. To examine the contents of this structure, use the NT_STATUS macro.</p>

<p>The <b>FsRtlFastLock</b> macro causes the caller to acquire a byte-range lock on a region of the specified file.</p>

<p>A return value of <b>TRUE</b> indicates that the IO_STATUS_BLOCK structure pointed to by <i>Iosb</i> received status information about the lock operation. To examine the contents of this structure, use the NT_STATUS macro.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545640">FsRtlAllocateFileLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546122">FsRtlInitializeFileLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlFastLock function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
