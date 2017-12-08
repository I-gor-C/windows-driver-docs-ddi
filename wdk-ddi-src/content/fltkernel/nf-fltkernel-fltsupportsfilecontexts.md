---
UID: NF.fltkernel.FltSupportsFileContexts
title: FltSupportsFileContexts function
author: windows-driver-content
description: The FltSupportsFileContexts routine determines whether the file system supports file contexts for a given file.
old-location: ifsk\fltsupportsfilecontexts.htm
old-project: ifsk
ms.assetid: 968c2c6d-3544-45e7-b852-740fa4930349
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltSupportsFileContexts
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Windows Vista and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltSupportsFileContexts
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
---

# FltSupportsFileContexts function



## -description
The <b>FltSupportsFileContexts</b> routine determines whether the file system supports file contexts for a given file. 


## -syntax

````
BOOLEAN FltSupportsFileContexts(
  _In_ PFILE_OBJECT FileObject
);
````


## -parameters

### -param FileObject [in]

File object pointer for the file. This parameter is required and cannot be <b>NULL</b>. 

## -returns
<b>FltSupportsFileContexts</b> returns <b>TRUE</b> if the file system supports file contexts for the file object; <b>FALSE</b> otherwise. 

## -remarks
Minifilter drivers call <b>FltSupportsFileContexts</b> to determine whether the underlying file system inherently supports file contexts for the file that is represented by a given file object. 

Note that a file system might support file contexts for some types of files but not for others. For example, NTFS and FAT do not support file contexts for paging files. 

To allocate a new context, call <a href="ifsk.fltallocatecontext">FltAllocateContext</a>. 

To delete a file context, call <a href="ifsk.fltdeletefilecontext">FltDeleteFileContext</a> or <a href="ifsk.fltdeletecontext">FltDeleteContext</a>. 

To get the file context for a file object, call <a href="ifsk.fltgetfilecontext">FltGetFileContext</a>. 

To set a file context, call <a href="ifsk.fltsetfilecontext">FltSetFileContext</a>. 

To decrement the reference count on a context, call <a href="ifsk.fltreleasecontext">FltReleaseContext</a>. 

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
This routine is available on Windows Vista and later. 
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
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
<a href="ifsk.fltallocatecontext">FltAllocateContext</a>
</dt>
<dt>
<a href="ifsk.fltdeletecontext">FltDeleteContext</a>
</dt>
<dt>
<a href="ifsk.fltdeletefilecontext">FltDeleteFileContext</a>
</dt>
<dt>
<a href="ifsk.fltgetfilecontext">FltGetFileContext</a>
</dt>
<dt>
<a href="ifsk.fltreleasecontext">FltReleaseContext</a>
</dt>
<dt>
<a href="ifsk.fltsetfilecontext">FltSetFileContext</a>
</dt>
<dt>
<a href="ifsk.fltsupportsfilecontextsex">FltSupportsFileContextsEx</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltSupportsFileContexts routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
