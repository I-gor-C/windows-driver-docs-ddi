---
UID: NF.ntifs._FSRTL_ADVANCED_FCB_HEADER.FsRtlAllocateFileLock~r1
title: FsRtlAllocateFileLock function
author: windows-driver-content
description: The FsRtlAllocateFileLock routine allocates and initializes a new FILE_LOCK structure.
old-location: ifsk\fsrtlallocatefilelock.htm
old-project: ifsk
ms.assetid: 148c177d-162a-4578-a40c-2e5fe6176d51
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlAllocateFileLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows 2000 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlAllocateFileLock
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

# FsRtlAllocateFileLock function



## -description
The <b>FsRtlAllocateFileLock</b> routine allocates and initializes a new FILE_LOCK structure. 



## -syntax

````
PFILE_LOCK FsRtlAllocateFileLock(
  _In_opt_ PCOMPLETE_LOCK_IRP_ROUTINE CompleteLockIrpRoutine,
  _In_opt_ PUNLOCK_ROUTINE            UnlockRoutine
);
````


## -parameters

### -param CompleteLockIrpRoutine [in, optional]

A pointer to a <a href="ifsk.pcomplete_lock_irp_routine">PCOMPLETE_LOCK_IRP_ROUTINE</a>-typed callback routine to be called when an <a href="ifsk.irp_mj_lock_control">IRP_MJ_LOCK_CONTROL</a> request is completed. This parameter is optional and can be <b>NULL</b>. 


### -param UnlockRoutine [in, optional]

A pointer to a <a href="ifsk.punlock_routine">PUNLOCK_ROUTINE</a>-typed callback routine to be called when the byte range is unlocked. This parameter is optional and can be <b>NULL</b>. 


## -returns
<b>FsRtlAllocateFileLock</b> returns a pointer to the newly allocated FILE_LOCK structure. 


## -remarks
<b>FsRtlAllocateFileLock</b> allocates a new FILE_LOCK structure from paged pool and initializes it.

Minifilters should call <a href="ifsk.fltallocatefilelock">FltAllocateFileLock</a> instead of <b>FsRtlAllocateFileLock</b>. 


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
This routine is available on Microsoft Windows 2000 and later. 

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
<a href="ifsk.fltallocatefilelock">FltAllocateFileLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlaretherecurrentfilelocks">FsRtlAreThereCurrentFileLocks</a>
</dt>
<dt>
<a href="ifsk.fsrtlchecklockforreadaccess">FsRtlCheckLockForReadAccess</a>
</dt>
<dt>
<a href="ifsk.fsrtlchecklockforwriteaccess">FsRtlCheckLockForWriteAccess</a>
</dt>
<dt>
<a href="ifsk.fsrtlfastchecklockforread">FsRtlFastCheckLockForRead</a>
</dt>
<dt>
<a href="ifsk.fsrtlfastchecklockforwrite">FsRtlFastCheckLockForWrite</a>
</dt>
<dt>
<a href="ifsk.fsrtlfastlock">FsRtlFastLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlfastunlockall">FsRtlFastUnlockAll</a>
</dt>
<dt>
<a href="ifsk.fsrtlfastunlockallbykey">FsRtlFastUnlockAllByKey</a>
</dt>
<dt>
<a href="ifsk.fsrtlfastunlocksingle">FsRtlFastUnlockSingle</a>
</dt>
<dt>
<a href="ifsk.fsrtlgetnextfilelock">FsRtlGetNextFileLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlinitializefilelock">FsRtlInitializeFileLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlprocessfilelock">FsRtlProcessFileLock</a>
</dt>
<dt>
<a href="ifsk.fsrtluninitializefilelock">FsRtlUninitializeFileLock</a>
</dt>
<dt>
<a href="ifsk.irp_mj_lock_control">IRP_MJ_LOCK_CONTROL</a>
</dt>
<dt>
<a href="ifsk.pcomplete_lock_irp_routine">PCOMPLETE_LOCK_IRP_ROUTINE</a>
</dt>
<dt>
<a href="ifsk.punlock_routine">PUNLOCK_ROUTINE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlAllocateFileLock routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

