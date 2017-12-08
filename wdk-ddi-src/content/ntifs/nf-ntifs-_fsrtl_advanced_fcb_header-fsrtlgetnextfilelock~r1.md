---
UID: NF.ntifs._FSRTL_ADVANCED_FCB_HEADER.FsRtlGetNextFileLock~r1
title: FsRtlGetNextFileLock function
author: windows-driver-content
description: The FsRtlGetNextFileLock routine is used to enumerate the byte-range locks that currently exist for a specified file.
old-location: ifsk\fsrtlgetnextfilelock.htm
old-project: ifsk
ms.assetid: 175fa4a7-a8e0-4fb1-8103-e513ea8c0778
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlGetNextFileLock
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
req.alt-api: FsRtlGetNextFileLock
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

# FsRtlGetNextFileLock function



## -description
The <b>FsRtlGetNextFileLock</b> routine is used to enumerate the byte-range locks that currently exist for a specified file.


## -syntax

````
PFILE_LOCK_INFO FsRtlGetNextFileLock(
  _In_ PFILE_LOCK FileLock,
  _In_ BOOLEAN    Restart
);
````


## -parameters

### -param FileLock [in]

Pointer to the FILE_LOCK structure for the file. This structure must have been initialized by a previous call to <b>FsRtlAllocateFileLock</b> or <a href="ifsk.fsrtlinitializefilelock">FsRtlInitializeFileLock</a>.

### -param Restart [in]

Set to <b>TRUE</b> if the enumeration is to start at the beginning of the list of byte range locks. Set to <b>FALSE</b> if resuming the enumeration from a previous call.
To enumerate all byte-range locks for a given file, use <b>FsRtlGetNextFileLock</b> as follows:
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>for (p = FsRtlGetNextFileLock( FileLock, TRUE );
     p != NULL;
     p = FsRtlGetNextFileLock( FileLock, FALSE )) {
        // Process the lock information pointed to by p
}</pre>
</td>
</tr>
</table></span></div>

## -returns
<b>FsRtlGetNextFileLock</b> returns a pointer to the FILE_LOCK_INFO structure for the next byte-range lock, if one exists. If there are no more byte-range locks for this file, <b>FsRtlGetNextFileLock</b> returns <b>NULL</b>.

## -remarks
The byte range locks are not enumerated in any particular order.

Note that because the current enumeration state is stored in the FILE_LOCK structure, callers must be careful to synchronize calls to <b>FsRtlGetNextFileLock</b>, and to avoid modifying any of the structures that it returns. If multiple threads attempt to use <b>FsRtlGetNextFileLock</b> at the same time, the results will be unpredictable, and the enumeration will not be reliably complete.

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
<a href="ifsk.fsrtlinitializefilelock">FsRtlInitializeFileLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlprocessfilelock">FsRtlProcessFileLock</a>
</dt>
<dt>
<a href="ifsk.fsrtluninitializefilelock">FsRtlUninitializeFileLock</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlGetNextFileLock routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
