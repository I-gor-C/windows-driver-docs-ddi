---
UID: NF.fltkernel.FltCheckLockForReadAccess
title: FltCheckLockForReadAccess
author: windows-driver-content
description: The FltCheckLockForReadAccess routine determines whether the caller has read access to a locked byte range of a file.
old-location: ifsk\fltchecklockforreadaccess.htm
old-project: ifsk
ms.assetid: 18920aaa-ae43-48ec-a06d-69ccaf75ebd8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltCheckLockForReadAccess
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltCheckLockForReadAccess
req.alt-loc: FltMgr.lib,FltMgr.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
---

# FltCheckLockForReadAccess function



## -description
<p>The <b>FltCheckLockForReadAccess</b> routine determines whether the caller has read access to a locked byte range of a file.</p>


## -syntax

````
BOOLEAN FltCheckLockForReadAccess(
  _In_ PFILE_LOCK         FileLock,
  _In_ PFLT_CALLBACK_DATA CallbackData
);
````


## -parameters
<dl>

### -param <i>FileLock</i> [in]

<dd>
<p>Pointer to the FILE_LOCK structure for the file. This structure must have been initialized by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff543273">FltInitializeFileLock</a>.</p>
</dd>

### -param <i>CallbackData</i> [in]

<dd>
<p>Pointer to the callback data (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>) structure for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a> operation. </p>
</dd>
</dl>

## -returns
<p><b>FltCheckLockForReadAccess</b> returns <b>TRUE</b> if the process has read access, <b>FALSE</b> otherwise.</p>

## -remarks
<p>This routine is available on Microsoft Windows XP SP2, Microsoft Windows Server 2003 SP1, and later. </p>

<p><b>FltCheckLockForReadAccess</b> checks whether the caller has read access to the entire byte range indicated in the callback data structure. </p>

<p><b>FltCheckLockForReadAccess</b> does not complete the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a> operation. </p>

<p>To allocate and initialize a new file lock structure, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a>. </p>

<p>To free an initialized FILE_LOCK structure, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542969">FltFreeFileLock</a>. </p>

<p>This routine is available on Microsoft Windows XP SP2, Microsoft Windows Server 2003 SP1, and later. </p>

<p><b>FltCheckLockForReadAccess</b> checks whether the caller has read access to the entire byte range indicated in the callback data structure. </p>

<p><b>FltCheckLockForReadAccess</b> does not complete the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a> operation. </p>

<p>To allocate and initialize a new file lock structure, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a>. </p>

<p>To free an initialized FILE_LOCK structure, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542969">FltFreeFileLock</a>. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541837">FltCheckLockForWriteAccess</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542969">FltFreeFileLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543273">FltInitializeFileLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543427">FltProcessFileLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544595">FltUninitializeFileLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545758">FsRtlCheckLockForReadAccess</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltCheckLockForReadAccess routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
