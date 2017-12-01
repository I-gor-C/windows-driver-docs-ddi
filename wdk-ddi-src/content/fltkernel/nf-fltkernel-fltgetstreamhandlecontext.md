---
UID: NF.fltkernel.FltGetStreamHandleContext
title: FltGetStreamHandleContext
author: windows-driver-content
description: The FltGetStreamHandleContext routine retrieves a context that was set for a stream handle by a given minifilter driver instance.
old-location: ifsk\fltgetstreamhandlecontext.htm
old-project: ifsk
ms.assetid: c6e7c0d8-8005-4a40-a13b-ee58feeabbf0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltGetStreamHandleContext
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
req.alt-api: FltGetStreamHandleContext
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

# FltGetStreamHandleContext function



## -description
<p>The <b>FltGetStreamHandleContext</b> routine retrieves a context that was set for a stream handle by a given minifilter driver instance. </p>


## -syntax

````
NTSTATUS FltGetStreamHandleContext(
  _In_  PFLT_INSTANCE Instance,
  _In_  PFILE_OBJECT  FileObject,
  _Out_ PFLT_CONTEXT  *Context
);
````


## -parameters
<dl>

### -param <i>Instance</i> [in]

<dd>
<p>Opaque instance pointer for the minifilter driver instance whose context is to be retrieved. </p>
</dd>

### -param <i>FileObject</i> [in]

<dd>
<p>Pointer to a file object for the stream handle. </p>
</dd>

### -param <i>Context</i> [out]

<dd>
<p>Pointer to a caller-allocated variable that receives the address of the context. </p>
</dd>
</dl>

## -returns
<p><b>FltGetStreamHandleContext</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value, such as one of the following: </p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>No matching context was found. This is an error code. </p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The file system does not support per-stream contexts for this file stream. This is an error code. </p>

<p> </p>

## -remarks
<p><b>FltGetStreamHandleContext</b> retrieves a context that was set for a stream handle by a given minifilter driver. </p>

<p><b>FltGetStreamHandleContext</b> increments the reference count on the context that the <i>Context </i>parameter points to. When this context pointer is no longer needed, the caller must decrement its reference count by calling <a href="..\fltkernel\nf-fltkernel-fltreleasecontext.md">FltReleaseContext</a>. Thus every successful call to <b>FltGetStreamHandleContext</b> must be matched by a subsequent call to <b>FltReleaseContext</b>. </p>

<p>To set a context for a stream handle, call <a href="..\fltkernel\nf-fltkernel-fltsetstreamhandlecontext.md">FltSetStreamHandleContext</a>. </p>

<p>To allocate a new context, call <a href="..\fltkernel\nf-fltkernel-fltallocatecontext.md">FltAllocateContext</a>. </p>

<p>To delete a stream handle context, call <a href="..\fltkernel\nf-fltkernel-fltdeletestreamhandlecontext.md">FltDeleteStreamHandleContext</a> or <a href="..\fltkernel\nf-fltkernel-fltdeletecontext.md">FltDeleteContext</a>. </p>

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
<a href="..\fltkernel\nf-fltkernel-fltallocatecontext.md">FltAllocateContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltdeletecontext.md">FltDeleteContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltdeletestreamhandlecontext.md">FltDeleteStreamHandleContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltreleasecontext.md">FltReleaseContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltsetstreamhandlecontext.md">FltSetStreamHandleContext</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetStreamHandleContext routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
