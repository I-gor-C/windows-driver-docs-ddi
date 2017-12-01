---
UID: NF.fltkernel.FltDeleteContext
title: FltDeleteContext
author: windows-driver-content
description: FltDeleteContext marks a specified context for deletion.
old-location: ifsk\fltdeletecontext.htm
old-project: ifsk
ms.assetid: 1cdb0747-7616-414b-8287-1ef73637ed05
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltDeleteContext
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
req.alt-api: FltDeleteContext
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

# FltDeleteContext function



## -description
<p><b>FltDeleteContext</b> marks a specified context for deletion. </p>


## -syntax

````
VOID FltDeleteContext(
  _In_ PFLT_CONTEXT Context
);
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>A pointer to the context to delete. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p>None. </p>

## -remarks
<p>Because contexts are reference-counted, it is not usually necessary for a minifilter driver to call a routine, such as <b>FltDeleteContext</b>, to explicitly delete a context. </p>

<p><b>FltDeleteContext</b> marks a context for deletion. The context is usually freed as soon as the current reference on it is released, unless there is an outstanding reference on it (for example, because the context is still being used by another thread). </p>

<p>You should consider the following items when you use <b>FltDeleteContext</b>:</p>

<p>When a minifilter driver calls <b>FltDeleteContext</b>, the minifilter driver must already have a reference to the context. However, when the minifilter driver calls <a href="..\fltkernel\nf-fltkernel-fltdeletestreamhandlecontext.md">FltDeleteStreamHandleContext</a>, <a href="..\fltkernel\nf-fltkernel-fltdeletestreamcontext.md">FltDeleteStreamContext</a>, <a href="..\fltkernel\nf-fltkernel-fltdeleteinstancecontext.md">FltDeleteInstanceContext</a>, and so on, the minifilter driver does not require a reference to the context. After the minifilter driver calls <b>FltDeleteContext</b>, that reference to the context is still valid. The minifilter driver must call the <a href="..\fltkernel\nf-fltkernel-fltreleasecontext.md">FltReleaseContext</a> routine to release the reference to the context. </p>

<p><b>FltDeleteContext</b> removes the context from the internal filter manager structures. Then, further calls to functions that retrieve contexts, such as  <a href="..\fltkernel\nf-fltkernel-fltgetcontexts.md">FltGetContexts</a> and <a href="..\fltkernel\nf-fltkernel-fltgetinstancecontext.md">FltGetInstanceContext</a>, cannot locate that context. However, the context memory is not released until the reference count for the context goes to 0. </p>

<p>Contexts can also be deleted by calling the appropriate delete-context routine from the following table. </p>

<p>FLT_FILE_CONTEXT</p>

<p>
<a href="..\fltkernel\nf-fltkernel-fltdeletefilecontext.md">FltDeleteFileContext</a> (Windows Vista and later only.)</p>

<p>FLT_INSTANCE_CONTEXT</p>

<p>
<a href="..\fltkernel\nf-fltkernel-fltdeleteinstancecontext.md">FltDeleteInstanceContext</a>
</p>

<p>FLT_SECTION_CONTEXT</p>

<p>
<a href="..\fltkernel\nf-fltkernel-fltclosesectionfordatascan.md">FltCloseSectionForDataScan</a> (Windows 8 and later only.)</p>

<p>FLT_STREAM_CONTEXT</p>

<p>
<a href="..\fltkernel\nf-fltkernel-fltdeletestreamcontext.md">FltDeleteStreamContext</a>
</p>

<p>FLT_STREAMHANDLE_CONTEXT</p>

<p>
<a href="..\fltkernel\nf-fltkernel-fltdeletestreamhandlecontext.md">FltDeleteStreamHandleContext</a>
</p>

<p>FLT_TRANSACTION_CONTEXT</p>

<p>
<a href="..\fltkernel\nf-fltkernel-fltdeletetransactioncontext.md">FltDeleteTransactionContext</a> (Windows Vista and later only.)</p>

<p>FLT_VOLUME_CONTEXT</p>

<p>
<a href="..\fltkernel\nf-fltkernel-fltdeletevolumecontext.md">FltDeleteVolumeContext</a>
</p>

<p>To allocate a new context, call <a href="..\fltkernel\nf-fltkernel-fltallocatecontext.md">FltAllocateContext</a>. </p>

<p>To increment the reference count on a context, call <a href="..\fltkernel\nf-fltkernel-fltreferencecontext.md">FltReferenceContext</a>. </p>

<p>To decrement the reference count on a context, call <a href="..\fltkernel\nf-fltkernel-fltreleasecontext.md">FltReleaseContext</a>. </p>

<p>A section context, FLT_SECTION_CONTEXT type, must not be deleted using <b>FltDeleteContext</b>. Instead, use  <a href="..\fltkernel\nf-fltkernel-fltreleasecontext.md">FltReleaseContext</a> to deallocate a section context.</p>

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
<a href="..\fltkernel\nf-fltkernel-fltclosesectionfordatascan.md">FltCloseSectionForDataScan</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltdeletefilecontext.md">FltDeleteFileContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltdeleteinstancecontext.md">FltDeleteInstanceContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltdeletestreamcontext.md">FltDeleteStreamContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltdeletestreamhandlecontext.md">FltDeleteStreamHandleContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltdeletetransactioncontext.md">FltDeleteTransactionContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltdeletevolumecontext.md">FltDeleteVolumeContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltreferencecontext.md">FltReferenceContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltreleasecontext.md">FltReleaseContext</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltDeleteContext function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
