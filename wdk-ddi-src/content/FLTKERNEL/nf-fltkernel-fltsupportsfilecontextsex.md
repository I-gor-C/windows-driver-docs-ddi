---
UID: NF.fltkernel.FltSupportsFileContextsEx
title: FltSupportsFileContextsEx
author: windows-driver-content
description: The FltSupportsFileContextsEx routine determines whether the file system or the filter manager support file contexts for a given file.
old-location: ifsk\fltsupportsfilecontextsex.htm
ms.assetid: 42401474-ea2d-441f-ad70-bd95544933ac
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Windows Vista and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltSupportsFileContextsEx
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
ms.keywords: FltSupportsFileContextsEx
req.iface: 
---

# FltSupportsFileContextsEx function



## -description
<p>The <b>FltSupportsFileContextsEx</b> routine determines whether the file system or the filter manager support file contexts for a given file. </p>


## -syntax

````
BOOLEAN FltSupportsFileContextsEx(
  _In_     PFILE_OBJECT  FileObject,
  _In_opt_ PFLT_INSTANCE Instance
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>File object pointer for the file. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>Instance</i> [in, optional]

<dd>
<p>Opaque instance pointer for the caller. This parameter is optional and can be <b>NULL</b>. For more information about this parameter, see the following Remarks section. </p>
</dd>
</dl>

## -returns
<p><b>FltSupportsFileContextsEx</b> returns <b>TRUE</b> if the file system or filter manager supports file contexts for the file; <b>FALSE</b> otherwise. </p>

## -remarks
<p>Minifilter drivers call the <b>FltSupportsFileContextsEx</b> routine to determine whether the underlying file system or the filter manager supports file contexts for the file that is represented by a given file object. </p>

<p>For file systems (such as FAT) that support only a single data stream per file, file contexts are equivalent to stream contexts. Such file systems usually support stream contexts but do not support file contexts. Instead, the filter manager provides file context support, using the file system's existing support for stream contexts. For minifilter instances attached to these file systems, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544574">FltSupportsFileContexts</a> returns <b>FALSE</b>, while <b>FltSupportsFileContextsEx</b> returns <b>TRUE</b> (when a valid non-<b>NULL</b> value is passed for the <i>Instance</i> parameter). </p>

<p>If a non-<b>NULL</b> value is supplied for the <i>Instance</i> parameter, <b>FltSupportsFileContextsEx</b> returns <b>TRUE</b> if the file system or the filter manager supports file contexts for the file; <b>FALSE</b> otherwise. </p>

<p>If the <i>Instance</i> parameter is <b>NULL</b>, <b>FltSupportsFileContextsEx</b> returns <b>TRUE</b> only if the file system supports file contexts for the file. Otherwise, it returns <b>FALSE</b>, even if the filter manager supports file contexts for the file. </p>

<p>Note that a file system might support file contexts for some types of files but not for others. For example, NTFS and FAT do not support file contexts for paging files. </p>

<p>To allocate a new context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>. </p>

<p>To delete a file context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541980">FltDeleteFileContext</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff541960">FltDeleteContext</a>. </p>

<p>To get the file context for a file object, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543025">FltGetFileContext</a>. </p>

<p>To set a file context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544511">FltSetFileContext</a>. </p>

<p>To decrement the reference count on a context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a>. </p>

<p>Minifilter drivers call the <b>FltSupportsFileContextsEx</b> routine to determine whether the underlying file system or the filter manager supports file contexts for the file that is represented by a given file object. </p>

<p>For file systems (such as FAT) that support only a single data stream per file, file contexts are equivalent to stream contexts. Such file systems usually support stream contexts but do not support file contexts. Instead, the filter manager provides file context support, using the file system's existing support for stream contexts. For minifilter instances attached to these file systems, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544574">FltSupportsFileContexts</a> returns <b>FALSE</b>, while <b>FltSupportsFileContextsEx</b> returns <b>TRUE</b> (when a valid non-<b>NULL</b> value is passed for the <i>Instance</i> parameter). </p>

<p>If a non-<b>NULL</b> value is supplied for the <i>Instance</i> parameter, <b>FltSupportsFileContextsEx</b> returns <b>TRUE</b> if the file system or the filter manager supports file contexts for the file; <b>FALSE</b> otherwise. </p>

<p>If the <i>Instance</i> parameter is <b>NULL</b>, <b>FltSupportsFileContextsEx</b> returns <b>TRUE</b> only if the file system supports file contexts for the file. Otherwise, it returns <b>FALSE</b>, even if the filter manager supports file contexts for the file. </p>

<p>Note that a file system might support file contexts for some types of files but not for others. For example, NTFS and FAT do not support file contexts for paging files. </p>

<p>To allocate a new context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>. </p>

<p>To delete a file context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541980">FltDeleteFileContext</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff541960">FltDeleteContext</a>. </p>

<p>To get the file context for a file object, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543025">FltGetFileContext</a>. </p>

<p>To set a file context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544511">FltSetFileContext</a>. </p>

<p>To decrement the reference count on a context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a>. </p>

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
<p>This routine is available on Windows Vista and later. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541960">FltDeleteContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541980">FltDeleteFileContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543025">FltGetFileContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544511">FltSetFileContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544574">FltSupportsFileContexts</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltSupportsFileContextsEx routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
