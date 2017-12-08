---
UID: NF.ntifs._FSRTL_ADVANCED_FCB_HEADER.FsRtlInitializeFileLock~r2
title: FsRtlInitializeFileLock function
author: windows-driver-content
description: The FsRtlInitializeFileLock routine initializes a FILE_LOCK structure.
old-location: ifsk\fsrtlinitializefilelock.htm
old-project: ifsk
ms.assetid: 0a476cd8-b0e6-4faa-bb97-3647a88ecded
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlInitializeFileLock
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
req.alt-api: FsRtlInitializeFileLock
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

# FsRtlInitializeFileLock function



## -description
The <b>FsRtlInitializeFileLock</b> routine initializes a FILE_LOCK structure.


## -syntax

````
VOID FsRtlInitializeFileLock(
  _In_     PFILE_LOCK                 FileLock,
  _In_opt_ PCOMPLETE_LOCK_IRP_ROUTINE CompleteLockIrpRoutine,
  _In_opt_ PUNLOCK_ROUTINE            UnlockRoutine
);
````


## -parameters

### -param FileLock [in]

Pointer to an uninitialized FILE_LOCK structure. 

### -param CompleteLockIrpRoutine [in, optional]

Pointer to a <a href="ifsk.pcomplete_lock_irp_routine">PCOMPLETE_LOCK_IRP_ROUTINE</a>-typed callback routine to be called when an <a href="ifsk.irp_mj_lock_control">IRP_MJ_LOCK_CONTROL</a> request is completed. This parameter is optional and can be <b>NULL</b>. 

### -param UnlockRoutine [in, optional]

Pointer to a <a href="ifsk.punlock_routine">PUNLOCK_ROUTINE</a>-typed callback routine to be called when the byte range is unlocked. This parameter is optional and can be <b>NULL</b>. 

## -returns
None

## -remarks
<b>FsRtlInitializeFileLock</b> initializes an uninitialized FILE_LOCK structure. 

It is a programming error to call <b>FsRtlInitializeFileLock</b> for a FILE_LOCK structure that has already been initialized by <b>FsRtlInitializeFileLock</b> or <a href="ifsk.fsrtlallocatefilelock">FsRtlAllocateFileLock</a>, unless the structure has been uninitialized by a subsequent call to <a href="ifsk.fsrtluninitializefilelock">FsRtlUninitializeFileLock</a>.

Once initialized, the FILE_LOCK structure can be used to lock a byte range in a file by calling <a href="ifsk.fsrtlprocessfilelock">FsRtlProcessFileLock</a> or <a href="ifsk.fsrtlfastlock">FsRtlFastLock</a>. <b>FsRtlProcessFileLock</b> processes lock IRPs. <b>FsRtlFastLock</b> performs non-IRP locking.

When the FILE_LOCK structure is no longer needed, it can be uninitialized by calling <a href="ifsk.fsrtluninitializefilelock">FsRtlUninitializeFileLock</a>. The uninitialized FILE_LOCK structure can then be initialized for reuse by calling <b>FsRtlInitializeFileLock</b>.

Minifilters must call <a href="ifsk.fltinitializefilelock">FltInitializeFileLock</a> instead of <b>FsRtlInitializeFileLock</b>. 

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
<a href="ifsk.fltinitializefilelock">FltInitializeFileLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlallocatefilelock">FsRtlAllocateFileLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlaretherecurrentfilelocks">FsRtlAreThereCurrentFileLocks</a>
</dt>
<dt>
<a href="ifsk.fsrtlfastlock">FsRtlFastLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlprocessfilelock">FsRtlProcessFileLock</a>
</dt>
<dt>
<a href="ifsk.fsrtluninitializefilelock">FsRtlUninitializeFileLock</a>
</dt>
<dt>
<a href="kernel.iocompleterequest">IoCompleteRequest</a>
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
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlInitializeFileLock routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
