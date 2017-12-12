---
UID: NF.ntifs._FSRTL_ADVANCED_FCB_HEADER.FsRtlFastUnlockSingle~r7
title: FsRtlFastUnlockSingle function
author: windows-driver-content
description: The FsRtlFastUnlockSingle routine releases a byte-range lock that was acquired by the specified process, with the specified key value, file offset, and length, for a file.
old-location: ifsk\fsrtlfastunlocksingle.htm
old-project: ifsk
ms.assetid: 8fd7aeea-f8b2-4f53-b4b6-65240ff0c7b6
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlFastUnlockSingle
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows 2000 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlFastUnlockSingle
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
---

# FsRtlFastUnlockSingle function



## -description
The <b>FsRtlFastUnlockSingle</b> routine releases a byte-range lock that was acquired by the specified process, with the specified key value, file offset, and length, for a file. 



## -syntax

````
NTSTATUS FsRtlFastUnlockSingle(
  _In_     PFILE_LOCK              FileLock,
  _In_     PFILE_OBJECT            FileObject,
  _In_     LARGE_INTEGER UNALIGNED *FileOffset,
  _In_     PLARGE_INTEGER          Length,
  _In_     PEPROCESS               ProcessId,
  _In_     ULONG                   Key,
  _In_opt_ PVOID                   Context,
  _In_     BOOLEAN                 AlreadySynchronized
);
````


## -parameters

### -param FileLock [in]

A pointer to the FILE_LOCK structure for the file. This structure must have been initialized by a previous call to <a href="ifsk.fsrtlallocatefilelock">FsRtlAllocateFileLock</a> or <a href="ifsk.fsrtlinitializefilelock">FsRtlInitializeFileLock</a>.


### -param FileObject [in]

A pointer to the file object for the file.


### -param FileOffset [in]

A pointer to a variable that specifies the starting byte offset within the file of the range to be unlocked.


### -param Length [in]

A pointer to a variable that specifies the length, in bytes, of the range to be unlocked.


### -param ProcessId [in]

A pointer to the process ID for the process.


### -param Key [in]

The key for the byte-range lock.


### -param Context [in, optional]

An optional context pointer to be used when completing IRPs. 


### -param AlreadySynchronized [in]

This parameter is obsolete, but is retained for compatibility with legacy drivers.


## -returns
The <b>FsRtlFastUnlockSingle</b> routine returns STATUS_SUCCESS or an error status code such as STATUS_RANGE_NOT_LOCKED. 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Microsoft Windows 2000 and later.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include FltKernel.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= APC_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fsrtlallocatefilelock">FsRtlAllocateFileLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlinitializefilelock">FsRtlInitializeFileLock</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlFastUnlockSingle routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

