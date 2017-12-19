---
UID: NF.ntifs._FSRTL_ADVANCED_FCB_HEADER.FsRtlCheckLockForReadAccess~r1
title: FsRtlCheckLockForReadAccess function
author: windows-driver-content
description: The FsRtlCheckLockForReadAccess routine determines whether the process associated with a given IRP has read access to a locked region of a file.
old-location: ifsk\fsrtlchecklockforreadaccess.htm
old-project: ifsk
ms.assetid: 3734b286-b5cb-4906-9947-3ad23ef54267
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FsRtlCheckLockForReadAccess
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
req.alt-api: FsRtlCheckLockForReadAccess
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

# FsRtlCheckLockForReadAccess function



## -description
The <b>FsRtlCheckLockForReadAccess</b> routine determines whether the process associated with a given IRP has read access to a locked region of a file.



## -syntax

````
BOOLEAN FsRtlCheckLockForReadAccess(
  _In_ PFILE_LOCK FileLock,
  _In_ PIRP       Irp
);
````


## -parameters

### -param FileLock [in]

Pointer to the FILE_LOCK structure for the file. This structure must have been initialized by a previous call to <a href="ifsk.fsrtlallocatefilelock">FsRtlAllocateFileLock</a> or <a href="ifsk.fsrtlinitializefilelock">FsRtlInitializeFileLock</a>.


### -param Irp [in]

Pointer to the IRP. Must be an IRP for a read operation.


## -returns
<b>FsRtlCheckLockForReadAccess</b> returns <b>TRUE</b> if the process has read access, <b>FALSE</b> otherwise.


## -remarks
On Microsoft Windows XP and later, <b>FsRtlCheckLockForReadAccess</b> checks the process to which the thread that requested the read operation is currently attached. 

On Microsoft Windows 2000 and earlier, <b>FsRtlCheckLockForReadAccess</b> checks the process that created the thread. 

<b>FsRtlCheckLockForReadAccess</b> checks to see if there are any conflicting locks in the byte range that is to be read.

<b>FsRtlCheckLockForReadAccess</b> does not complete the IRP specified by <i>Irp</i>. 

Minifilters must call <a href="ifsk.fltchecklockforreadaccess">FltCheckLockForReadAccess</a> instead of <b>FsRtlCheckLockForReadAccess</b>. 


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
<a href="ifsk.fltchecklockforreadaccess">FltCheckLockForReadAccess</a>
</dt>
<dt>
<a href="ifsk.fsrtlallocatefilelock">FsRtlAllocateFileLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlchecklockforwriteaccess">FsRtlCheckLockForWriteAccess</a>
</dt>
<dt>
<a href="ifsk.fsrtlfastchecklockforread">FsRtlFastCheckLockForRead</a>
</dt>
<dt>
<a href="ifsk.fsrtlinitializefilelock">FsRtlInitializeFileLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlprocessfilelock">FsRtlProcessFileLock</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlCheckLockForReadAccess routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

