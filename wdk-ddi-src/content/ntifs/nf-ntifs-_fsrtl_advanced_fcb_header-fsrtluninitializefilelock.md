---
UID: NF.ntifs._FSRTL_ADVANCED_FCB_HEADER.FsRtlUninitializeFileLock
title: FsRtlUninitializeFileLock function
author: windows-driver-content
description: The FsRtlUninitializeFileLock routine uninitializes a FILE_LOCK structure.
old-location: ifsk\fsrtluninitializefilelock.htm
old-project: ifsk
ms.assetid: e92763e2-a15a-41cd-9f69-ec759b254929
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlUninitializeFileLock
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
req.alt-api: FsRtlUninitializeFileLock
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

# FsRtlUninitializeFileLock function



## -description
The <b>FsRtlUninitializeFileLock</b> routine uninitializes a FILE_LOCK structure.


## -syntax

````
VOID FsRtlUninitializeFileLock(
  _In_ PFILE_LOCK FileLock
);
````


## -parameters

### -param FileLock [in]

Pointer to the FILE_LOCK structure for the file. This structure must have been initialized by a previous call to <a href="ifsk.fsrtlallocatefilelock">FsRtlAllocateFileLock</a> or <a href="ifsk.fsrtlinitializefilelock">FsRtlInitializeFileLock</a>.

## -returns
None

## -remarks
<b>FsRtlUninitializeFileLock</b> uninitializes an initialized FILE_LOCK structure and completes any outstanding <a href="ifsk.irp_mj_lock_control">IRP_MJ_LOCK_CONTROL</a> requests. The uninitialized FILE_LOCK structure can be initialized for reuse by a subsequent call to <a href="ifsk.fsrtlinitializefilelock">FsRtlInitializeFileLock</a>.

<b>FsRtlUninitializeFileLock</b> can be used to uninitialize a FILE_LOCK structure that was initialized by a previous call to <a href="ifsk.fsrtlallocatefilelock">FsRtlAllocateFileLock</a> or <a href="ifsk.fsrtlinitializefilelock">FsRtlInitializeFileLock</a>. Do not use <b>FsRtlUninitializeFileLock</b> for such a FILE_LOCK structure unless the structure is to be initialized for reuse. It is a programming error to call <b>FsRtlFreeFileLock</b> for an uninitialized FILE_LOCK structure.

Minifilters must call <a href="ifsk.fltuninitializefilelock">FltUninitializeFileLock</a> instead of <b>FsRtlUninitializeFileLock</b>. 

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
<a href="ifsk.fltuninitializefilelock">FltUninitializeFileLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlallocatefilelock">FsRtlAllocateFileLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlinitializefilelock">FsRtlInitializeFileLock</a>
</dt>
<dt>
<a href="ifsk.irp_mj_lock_control">IRP_MJ_LOCK_CONTROL</a>
</dt>
<dt>
<a href="ifsk.pcomplete_lock_irp_routine">PCOMPLETE_LOCK_IRP_ROUTINE</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlUninitializeFileLock routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
