---
UID: NF.ntifs.ZwUnlockFile
title: ZwUnlockFile
author: windows-driver-content
description: The ZwUnlockFile routine unlocks a byte-range lock in a file.
old-location: kernel\zwunlockfile.htm
ms.assetid: dca3023b-99d5-471a-a5a2-8453c367ce9b
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
req.alt-api: ZwUnlockFile,NtUnlockFile
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
ms.keywords: ZwUnlockFile
req.iface: 
---

# ZwUnlockFile function



## -description
<p>The <b>ZwUnlockFile</b> routine unlocks a byte-range lock in a file.</p>


## -syntax

````
NTSTATUS ZwUnlockFile(
  _In_  HANDLE           FileHandle,
  _Out_ PIO_STATUS_BLOCK IoStatusBlock,
  _In_  PLARGE_INTEGER   ByteOffset,
  _In_  PLARGE_INTEGER   Length,
  _In_  ULONG            Key
);
````


## -parameters
<dl>

### -param <i>FileHandle</i> [in]

<dd>
<p>A handle for the file object that represents the file whose byte range is to be unlocked.</p>
</dd>

### -param <i>IoStatusBlock</i> [out]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a> structure that contains the final status.</p>
</dd>

### -param <i>ByteOffset</i> [in]

<dd>
<p>A pointer to a variable that specifies the starting byte offset for the byte range to be unlocked.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>A pointer to a variable that specifies the length, in bytes, of the byte range to unlock.</p>
</dd>

### -param <i>Key</i> [in]

<dd>
<p>The caller-assigned value used to describe groups of related locks. This value should be set to zero.</p>
</dd>
</dl>

## -returns
<p>The <b>ZwUnlockFile</b> routine returns STATUS_SUCCESS on success or an appropriate NTSTATUS value. Possible NTSTATUS values include:</p><dl>
<dt><b>STATUS_RANGE_NOT_LOCKED</b></dt>
</dl><p>The byte range specified is not locked.</p>

<p> </p>

## -remarks
<p>The <b>ZwUnlockFile</b> routine takes a range of bytes as specified by the <i>ByteOffset</i> and <i>Length</i> arguments. This range must be identical to a range of bytes in the file that was previously locked with a single call to the <b>ZwUnlockFile</b> routine. It is not possible to unlock two previously locked adjacent ranges with a single call to <b>ZwUnlockFile</b>. It is also not possible to unlock part of a range that was previously locked with a single call to the <b>ZwUnlockFile</b> routine.</p>

<p>Callers of <b>ZwUnlockFile</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with special kernel APCs enabled</a>.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

<p>The <b>ZwUnlockFile</b> routine takes a range of bytes as specified by the <i>ByteOffset</i> and <i>Length</i> arguments. This range must be identical to a range of bytes in the file that was previously locked with a single call to the <b>ZwUnlockFile</b> routine. It is not possible to unlock two previously locked adjacent ranges with a single call to <b>ZwUnlockFile</b>. It is also not possible to unlock part of a range that was previously locked with a single call to the <b>ZwUnlockFile</b> routine.</p>

<p>Callers of <b>ZwUnlockFile</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with special kernel APCs enabled</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566474">ZwLockFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwUnlockFile routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
