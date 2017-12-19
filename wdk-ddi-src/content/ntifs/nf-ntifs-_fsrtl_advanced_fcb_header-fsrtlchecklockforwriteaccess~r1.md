---
UID: NF.ntifs._FSRTL_ADVANCED_FCB_HEADER.FsRtlCheckLockForWriteAccess~r1
title: FsRtlCheckLockForWriteAccess function
author: windows-driver-content
description: The FsRtlCheckLockForWriteAccess routine determines whether the process associated with a given IRP has write access to a locked region of a file.
old-location: ifsk\fsrtlchecklockforwriteaccess.htm
old-project: ifsk
ms.assetid: 549da751-6a28-4d54-995f-dabb9e29ab09
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FsRtlCheckLockForWriteAccess
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlCheckLockForWriteAccess
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

# FsRtlCheckLockForWriteAccess function



## -description
The <b>FsRtlCheckLockForWriteAccess</b> routine determines whether the process associated with a given IRP has write access to a locked region of a file.



## -syntax

````
BOOLEAN FsRtlCheckLockForWriteAccess(
  _In_ PFILE_LOCK FileLock,
  _In_ PIRP       Irp
);
````


## -parameters

### -param FileLock [in]

Pointer to the FILE_LOCK structure for the file. This structure must have been initialized by a previous call to <a href="ifsk.fsrtlallocatefilelock">FsRtlAllocateFileLock</a> or <a href="ifsk.fsrtlinitializefilelock">FsRtlInitializeFileLock</a>.


### -param Irp [in]

Pointer to the IRP. Must be an IRP for a write operation.


## -returns
<b>FsRtlCheckLockForWriteAccess</b> returns <b>TRUE</b> if the process has write access, <b>FALSE</b> otherwise.


## -remarks
On Microsoft Windows XP and later, <b>FsRtlCheckLockForWriteAccess</b> checks the process to which the thread that requested the write operation is currently attached. 

On Microsoft Windows 2000 and earlier, <b>FsRtlCheckLockForWriteAccess</b> checks the process that created the thread. 

<b>FsRtlCheckLockForWriteAccess</b> checks to see if there are any conflicting locks in the byte range that is to be written.

<b>FsRtlCheckLockForWriteAccess</b> does not complete the IRP specified by <i>Irp</i>. 

Minifilters must call <a href="ifsk.fltchecklockforwriteaccess">FltCheckLockForWriteAccess</a> instead of <b>FsRtlCheckLockForWriteAccess</b>. 


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
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
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
<a href="ifsk.fltchecklockforwriteaccess">FltCheckLockForWriteAccess</a>
</dt>
<dt>
<a href="ifsk.fsrtlallocatefilelock">FsRtlAllocateFileLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlchecklockforreadaccess">FsRtlCheckLockForReadAccess</a>
</dt>
<dt>
<a href="ifsk.fsrtlfastchecklockforwrite">FsRtlFastCheckLockForWrite</a>
</dt>
<dt>
<a href="ifsk.fsrtlinitializefilelock">FsRtlInitializeFileLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlprocessfilelock">FsRtlProcessFileLock</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlCheckLockForWriteAccess routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

