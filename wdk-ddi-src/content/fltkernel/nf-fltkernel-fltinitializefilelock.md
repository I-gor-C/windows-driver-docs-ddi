---
UID: NF.fltkernel.FltInitializeFileLock
title: FltInitializeFileLock
author: windows-driver-content
description: The FltInitializeFileLock routine initializes an opaque FILE_LOCK structure that the caller has allocated from paged pool.
old-location: ifsk\fltinitializefilelock.htm
old-project: ifsk
ms.assetid: 84bfec05-9d77-433e-bec2-ad188269fc61
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltInitializeFileLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with  Windows XP with SP2 or Windows Server 2003 with SP1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltInitializeFileLock
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: <= APC_LEVEL
req.iface: 
---

# FltInitializeFileLock function



## -description
<p>The <b>FltInitializeFileLock</b> routine initializes an opaque <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure that the caller has allocated from paged pool.</p>


## -syntax

````
VOID FltInitializeFileLock(
  _Out_ PFILE_LOCK FileLock
);
````


## -parameters
<dl>

### -param <i>FileLock</i> [out]

<dd>
<p>Pointer to an uninitialized <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure is opaque: that is, its members are reserved for system use. </p>

<p>Once initialized, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure can be used to lock a byte range in a file by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543427">FltProcessFileLock</a>.</p>

<p>It is a programming error to call <b>FltInitializeFileLock</b> for a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure that has already been initialized by <b>FltInitializeFileLock</b> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a>, unless the structure has been uninitialized by a subsequent call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff544595">FltUninitializeFileLock</a>.</p>

<p>When the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure is no longer needed, it can be uninitialized by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544595">FltUninitializeFileLock</a>. The uninitialized <b>FILE_LOCK</b> structure can then be initialized for reuse by calling <b>FltInitializeFileLock</b>.</p>

<p>To allocate and initialize a new opaque <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a>. </p>

<p>To free an initialized <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542969">FltFreeFileLock</a>. </p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure is opaque: that is, its members are reserved for system use. </p>

<p>Once initialized, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure can be used to lock a byte range in a file by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543427">FltProcessFileLock</a>.</p>

<p>It is a programming error to call <b>FltInitializeFileLock</b> for a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure that has already been initialized by <b>FltInitializeFileLock</b> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a>, unless the structure has been uninitialized by a subsequent call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff544595">FltUninitializeFileLock</a>.</p>

<p>When the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure is no longer needed, it can be uninitialized by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544595">FltUninitializeFileLock</a>. The uninitialized <b>FILE_LOCK</b> structure can then be initialized for reuse by calling <b>FltInitializeFileLock</b>.</p>

<p>To allocate and initialize a new opaque <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a>. </p>

<p>To free an initialized <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542969">FltFreeFileLock</a>. </p>

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
<p>Available starting with  Windows XP with SP2 or Windows Server 2003 with SP1.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541834">FltCheckLockForReadAccess</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541837">FltCheckLockForWriteAccess</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542969">FltFreeFileLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543427">FltProcessFileLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544595">FltUninitializeFileLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546122">FsRtlInitializeFileLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltInitializeFileLock routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
