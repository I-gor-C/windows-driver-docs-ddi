---
UID: NF.ntifs.ZwLockFile
title: ZwLockFile
author: windows-driver-content
description: The ZwLockFile routine requests a byte-range lock for the specified file.
old-location: kernel\zwlockfile.htm
ms.assetid: d5d4d13c-93d9-4531-85ff-d3fa0e52ecc1
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntifs.h
req.include-header: Ntifs.h, FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwLockFile,NtLockFile
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL (see Remarks section)
ms.keywords: ZwLockFile
req.iface: 
---

# ZwLockFile function



## -description
<p>The <b>ZwLockFile</b> routine requests a byte-range lock for the specified file.</p>


## -syntax

````
NTSTATUS ZwLockFile(
  _In_     HANDLE           FileHandle,
  _In_opt_ HANDLE           Event,
  _In_opt_ PIO_APC_ROUTINE  ApcRoutine,
  _In_opt_ PVOID            ApcContext,
  _Out_    PIO_STATUS_BLOCK IoStatusBlock,
  _In_     PLARGE_INTEGER   ByteOffset,
  _In_     PLARGE_INTEGER   Length,
  _In_     ULONG            Key,
  _In_     BOOLEAN          FailImmediately,
  _In_     BOOLEAN          ExclusiveLock
);
````


## -parameters
<dl>

### -param <i>FileHandle</i> [in]

<dd>
<p>A handle for the file on which a byte-range lock is requested.</p>
</dd>

### -param <i>Event</i> [in, optional]

<dd>
<p>A handle to a caller-created event. If not <b>NULL</b>, the caller is placed into a wait state until the operation succeeds, at which time the event is set into the Signaled state.</p>
</dd>

### -param <i>ApcRoutine</i> [in, optional]

<dd>
<p>A pointer to a caller-supplied APC routine that is executed after the operation completes. Can be <b>NULL</b>.</p>
</dd>

### -param <i>ApcContext</i> [in, optional]

<dd>
<p>A pointer to a caller-specified context for the APC routine. This value is passed to the APC routine when it is executed. Can be <b>NULL</b>.</p>
</dd>

### -param <i>IoStatusBlock</i> [out]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a> structure that contains the final status.</p>
</dd>

### -param <i>ByteOffset</i> [in]

<dd>
<p>A pointer to a variable that specifies the starting byte offset of the range to lock.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>A pointer to a variable that specifies the length in bytes of the range to lock.</p>
</dd>

### -param <i>Key</i> [in]

<dd>
<p>A caller-assigned value used to describe groups of related locks. This value should be set to zero.</p>
</dd>

### -param <i>FailImmediately</i> [in]

<dd>
<p>If <b>TRUE</b>, immediately return if the file cannot be locked. If <b>FALSE</b>, wait for the lock request to be granted.</p>
</dd>

### -param <i>ExclusiveLock</i> [in]

<dd>
<p>If <b>TRUE</b>, byte-range lock is exclusive; otherwise, shared lock.</p>
</dd>
</dl>

## -returns
<p>The <b>ZwLockFile</b> routine returns STATUS_SUCCESS or an appropriate error NTSTATUS value. Possible NTSTATUS values include the following:</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Insufficient resources exist to grant the byte-range lock for the specified file.</p><dl>
<dt><b>STATUS_LOCK_NOT_GRANTED</b></dt>
</dl><p>The byte-range lock was not granted for the specified file.</p>

<p> </p>

## -remarks
<p>Callers of <b>ZwLockFile</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with special kernel APCs enabled</a>.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

<p>Callers of <b>ZwLockFile</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with special kernel APCs enabled</a>.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

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
<p>Available starting with Windows 7.</p>
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
<p>PASSIVE_LEVEL (see Remarks section)</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567118">ZwUnlockFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwLockFile routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
