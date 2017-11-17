---
UID: NF.fltkernel.FltSetFileContext
title: FltSetFileContext
author: windows-driver-content
description: The FltSetFileContext routine sets a context for a file.
old-location: ifsk\fltsetfilecontext.htm
ms.assetid: d56cb216-a757-4ab8-ac7f-04dc22997835
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available and supported starting with Windows Vista. For more information, see the Remarks section.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltSetFileContext
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fltmgr.lib
req.dll: Fltmgr.sys
req.irql: <= APC_LEVEL
ms.keywords: FltSetFileContext
req.iface: 
---

# FltSetFileContext function



## -description
<p>The <b>FltSetFileContext</b> routine sets a context for a file. </p>


## -syntax

````
NTSTATUS FltSetFileContext(
  _In_  PFLT_INSTANCE             Instance,
  _In_  PFILE_OBJECT              FileObject,
  _In_  FLT_SET_CONTEXT_OPERATION Operation,
  _In_  PFLT_CONTEXT              NewContext,
  _Out_ PFLT_CONTEXT              *OldContext
);
````


## -parameters
<dl>

### -param <i>Instance</i> [in]

<dd>
<p>An opaque pointer to a minifilter driver instance for the caller. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>FileObject</i> [in]

<dd>
<p>A file object pointer for the file. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>Operation</i> [in]

<dd>
<p>A flag that specifies the type of operation for <b>FltSetFileContext </b>to perform. This parameter must be one of the following flags:  </p>
<p></p>
<dl>

### -param <a id="FLT_SET_CONTEXT_REPLACE_IF_EXISTS"></a><a id="flt_set_context_replace_if_exists"></a>FLT_SET_CONTEXT_REPLACE_IF_EXISTS

<dd>
<p>If a context is already set for the instance that the <i>Instance </i>parameter points to, <b>FltSetFileContext</b> will replace that context with the context specified in <i>NewContext</i>. Otherwise, the routine will insert the context specified in <i>NewContext</i> into the list of contexts for the file. </p>
</dd>

### -param <a id="FLT_SET_CONTEXT_KEEP_IF_EXISTS"></a><a id="flt_set_context_keep_if_exists"></a>FLT_SET_CONTEXT_KEEP_IF_EXISTS

<dd>
<p>If a context is already set for the instance that the <i>Instance</i> parameter points to, <b>FltSetFileContext</b> will return STATUS_FLT_CONTEXT_ALREADY_DEFINED. Otherwise, the routine will insert the context specified in <i>NewContext</i> into the list of contexts for the file. </p>
</dd>
</dl>
</dd>

### -param <i>NewContext</i> [in]

<dd>
<p>A pointer to the new context to be set for the file. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>OldContext</i> [out]

<dd>
<p>A pointer to a caller-allocated variable that receives the address of the existing file context for the instance pointed to by the <i>Instance </i>parameter. This parameter is optional and can be <b>NULL</b>. For more information about this parameter, see the following Remarks section. </p>
</dd>
</dl>

## -returns
<p>The <b>FltSetFileContext</b> routine returns STATUS_SUCCESS or an appropriate NTSTATUS value, such as one of the following: </p><dl>
<dt><b>STATUS_FLT_CONTEXT_ALREADY_DEFINED</b></dt>
</dl><p>If FLT_SET_CONTEXT_KEEP_IF_EXISTS was specified for the <i>Operation</i> parameter, this error code indicates that a context is already attached to the file. </p><dl>
<dt><b>STATUS_FLT_CONTEXT_ALREADY_LINKED</b></dt>
</dl><p>The context pointed to by the <i>NewContext</i> parameter is already linked to an object.  In other words, this error code indicates that <i>NewContext</i> is already in use due to a successful prior call of a <b>FltSet</b><i>Xxx</i><b>Context</b> routine. </p><dl>
<dt><b>STATUS_FLT_DELETING_OBJECT</b></dt>
</dl><p>The instance specified in the <i>Instance</i> parameter is being torn down. This is an error code. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>This error code indicates one of the following problems:</p>

<p>The <i>NewContext</i> parameter does not point to a valid file context. </p>

<p>An invalid value was specified for the <i>Operation</i> parameter. </p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>File contexts are not supported for this file. This is an error code. </p>

<p> </p>

## -remarks
<p>The <b>FltSetFileContext</b> routine is available on Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP2, Windows Server 2003 SP1, and later operating systems. This routine is available and supported starting with Windows Vista (file contexts are only supported starting with Windows Vista). If <b>FltSetFileContext</b> is called on an operating system where this routine is available but file contexts are not supported, it returns STATUS_NOT_SUPPORTED.  This routine is not available on Windows 2000 SP4 and earlier operating systems.</p>

<p>A minifilter driver calls <b>FltSetFileContext</b> to set or replace its own file context on a file. A minifilter driver can attach one context per minifilter driver instance to the file. </p>

<p>A successful call to <b>FltSetFileContext</b> increments the reference count on <i>NewContext</i>. If <b>FltSetFileContext</b> fails, the reference count remains unchanged. In either case, the filter calling <b>FltSetFileContext</b> must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a> to decrement the <i>NewContext</i> object. If <b>FltSetFileContext</b> fails and if the <i>OldContext</i> parameter is not <b>NULL</b> and does not point to NULL_CONTEXT then <i>OldContext</i> is a referenced pointer to the context currently associated with the transaction. The filter calling <b>FltSetFileContext</b> must call <b>FltReleaseContext</b> for <i>OldContext</i> as well.</p>

<p>Note that the <i>OldContext</i> pointer returned by <b>FltSetFileContext</b> must also be released by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a> when it is no longer needed. For more information, see <a href="ifsk.setting_contexts">Setting Contexts</a> and <a href="ifsk.releasing_contexts">Releasing Contexts</a>.</p>

<p>Be aware that <b>FltSetFileContext</b> cannot be called on an unopened <i>FileObject</i>. Hence <b>FltSetFileContext</b> cannot be called from a pre-create callback for a stream because the stream has not been opened at that point. A minifilter driver can, however, allocate and set up the stream file context in the pre-create callback, pass it to the post-create callback using the completion context parameter and set the stream file context on the file corresponding to that stream in the post-create callback.</p>

<p>To get a file context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543025">FltGetFileContext</a>. </p>

<p>To allocate a new context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>. </p>

<p>To delete a file context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541980">FltDeleteFileContext</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff541960">FltDeleteContext</a>. </p>

<p>To determine whether file contexts are supported for a given file, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544574">FltSupportsFileContexts</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff544576">FltSupportsFileContextsEx</a>. </p>

<p>For more information about context reference counting, see <a href="ifsk.referencing_contexts">Referencing Contexts</a>. </p>

<p>The <b>FltSetFileContext</b> routine is available on Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP2, Windows Server 2003 SP1, and later operating systems. This routine is available and supported starting with Windows Vista (file contexts are only supported starting with Windows Vista). If <b>FltSetFileContext</b> is called on an operating system where this routine is available but file contexts are not supported, it returns STATUS_NOT_SUPPORTED.  This routine is not available on Windows 2000 SP4 and earlier operating systems.</p>

<p>A minifilter driver calls <b>FltSetFileContext</b> to set or replace its own file context on a file. A minifilter driver can attach one context per minifilter driver instance to the file. </p>

<p>A successful call to <b>FltSetFileContext</b> increments the reference count on <i>NewContext</i>. If <b>FltSetFileContext</b> fails, the reference count remains unchanged. In either case, the filter calling <b>FltSetFileContext</b> must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a> to decrement the <i>NewContext</i> object. If <b>FltSetFileContext</b> fails and if the <i>OldContext</i> parameter is not <b>NULL</b> and does not point to NULL_CONTEXT then <i>OldContext</i> is a referenced pointer to the context currently associated with the transaction. The filter calling <b>FltSetFileContext</b> must call <b>FltReleaseContext</b> for <i>OldContext</i> as well.</p>

<p>Note that the <i>OldContext</i> pointer returned by <b>FltSetFileContext</b> must also be released by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a> when it is no longer needed. For more information, see <a href="ifsk.setting_contexts">Setting Contexts</a> and <a href="ifsk.releasing_contexts">Releasing Contexts</a>.</p>

<p>Be aware that <b>FltSetFileContext</b> cannot be called on an unopened <i>FileObject</i>. Hence <b>FltSetFileContext</b> cannot be called from a pre-create callback for a stream because the stream has not been opened at that point. A minifilter driver can, however, allocate and set up the stream file context in the pre-create callback, pass it to the post-create callback using the completion context parameter and set the stream file context on the file corresponding to that stream in the post-create callback.</p>

<p>To get a file context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543025">FltGetFileContext</a>. </p>

<p>To allocate a new context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>. </p>

<p>To delete a file context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541980">FltDeleteFileContext</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff541960">FltDeleteContext</a>. </p>

<p>To determine whether file contexts are supported for a given file, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544574">FltSupportsFileContexts</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff544576">FltSupportsFileContextsEx</a>. </p>

<p>For more information about context reference counting, see <a href="ifsk.referencing_contexts">Referencing Contexts</a>. </p>

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
<p>Available and supported starting with Windows Vista. For more information, see the Remarks section.</p>
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
<dt>Fltmgr.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544629">FLT_CONTEXT_REGISTRATION</a>
</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544574">FltSupportsFileContexts</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544576">FltSupportsFileContextsEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltSetFileContext routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
