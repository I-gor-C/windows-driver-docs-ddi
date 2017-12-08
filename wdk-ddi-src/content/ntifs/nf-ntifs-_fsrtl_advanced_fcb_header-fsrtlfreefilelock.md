---
UID: NF.ntifs._FSRTL_ADVANCED_FCB_HEADER.FsRtlFreeFileLock
title: FsRtlFreeFileLock function
author: windows-driver-content
description: The FsRtlFreeFileLock routine uninitializes and frees a file lock structure.
old-location: ifsk\fsrtlfreefilelock.htm
old-project: ifsk
ms.assetid: 191a7964-4359-4b7f-8760-74f537b0737f
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlFreeFileLock
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
req.alt-api: FsRtlFreeFileLock
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

# FsRtlFreeFileLock function



## -description
The <b>FsRtlFreeFileLock</b> routine uninitializes and frees a file lock structure. 


## -syntax

````
VOID FsRtlFreeFileLock(
  _In_ PFILE_LOCK FileLock
);
````


## -parameters

### -param FileLock [in]

Pointer to the FILE_LOCK structure. This structure must have been allocated by a previous call to <b>FsRtlAllocateFileLock</b>.

## -returns
None

## -remarks
<b>FsRtlFreeFileLock</b> should be used only for file locks that were allocated and initialized by <b>FsRtlAllocateFileLock</b>.

It is a programming error to call <b>FsRtlFreeFileLock</b> for a FILE_LOCK structure that has already been uninitialized by a call to <a href="ifsk.fsrtluninitializefilelock">FsRtlUninitializeFileLock</a>.

Minifilters must call <a href="ifsk.fltfreefilelock">FltFreeFileLock</a> instead of <b>FsRtlFreeFileLock</b>. 

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
<a href="ifsk.fltfreefilelock">FltFreeFileLock</a>
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
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlFreeFileLock routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
