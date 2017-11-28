---
UID: NF.fltkernel.FltReleaseContext
title: FltReleaseContext
author: windows-driver-content
description: FltReleaseContext decrements the reference count on a context.
old-location: ifsk\fltreleasecontext.htm
old-project: ifsk
ms.assetid: b0585443-b8e9-41bc-81af-5707fda2465d
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltReleaseContext
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
req.alt-api: FltReleaseContext
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
req.irql: See Remarks section.
req.iface: 
---

# FltReleaseContext function



## -description
<p><b>FltReleaseContext</b> decrements the reference count on a context. </p>


## -syntax

````
VOID FltReleaseContext(
  _In_ PFLT_CONTEXT Context
);
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>Pointer to the context. Must be a valid pointer to a context object for a volume, instance, stream, or stream handle. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>A minifilter driver calls <b>FltReleaseContext</b> to release a context. <b>FltReleaseContext</b> decrements the reference count on the given context. When the reference count reaches zero, the context is freed immediately if the caller is running at IRQL &lt;= APC_LEVEL. If the caller is running at IRQL DISPATCH_LEVEL, a work item is scheduled to free the context. </p>

<p>Every successful call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>, <b>FltGet</b><i>Xxx</i><b>Context</b>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff544291">FltReferenceContext</a> must eventually be matched by a call to <b>FltReleaseContext</b>. </p>

<p>Note that the <i>OldContext</i> pointer returned by <b>FltSet</b><i>Xxx</i><b>Context</b> and the <i>Context</i> parameter that is used to call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541960">FltDeleteContext</a> must also be released by calling <b>FltReleaseContext</b> when they are no longer needed. </p>

<p>To allocate a new context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>. </p>

<p>To increment the reference count on a context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544291">FltReferenceContext</a>. </p>

<p>For more information about context reference counting, see <a href="ifsk.referencing_contexts">Referencing Contexts</a>. </p>

<p>Callers of <b>FltReleaseContext</b> must be running at IRQL &lt;= DISPATCH_LEVEL if the context was allocated from nonpaged pool. If the context was allocated from paged pool, callers must be running at IRQL &lt;= APC_LEVEL. </p>

<p>A minifilter driver calls <b>FltReleaseContext</b> to release a context. <b>FltReleaseContext</b> decrements the reference count on the given context. When the reference count reaches zero, the context is freed immediately if the caller is running at IRQL &lt;= APC_LEVEL. If the caller is running at IRQL DISPATCH_LEVEL, a work item is scheduled to free the context. </p>

<p>Every successful call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>, <b>FltGet</b><i>Xxx</i><b>Context</b>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff544291">FltReferenceContext</a> must eventually be matched by a call to <b>FltReleaseContext</b>. </p>

<p>Note that the <i>OldContext</i> pointer returned by <b>FltSet</b><i>Xxx</i><b>Context</b> and the <i>Context</i> parameter that is used to call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541960">FltDeleteContext</a> must also be released by calling <b>FltReleaseContext</b> when they are no longer needed. </p>

<p>To allocate a new context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>. </p>

<p>To increment the reference count on a context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544291">FltReferenceContext</a>. </p>

<p>For more information about context reference counting, see <a href="ifsk.referencing_contexts">Referencing Contexts</a>. </p>

<p>Callers of <b>FltReleaseContext</b> must be running at IRQL &lt;= DISPATCH_LEVEL if the context was allocated from nonpaged pool. If the context was allocated from paged pool, callers must be running at IRQL &lt;= APC_LEVEL. </p>

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
<p>See Remarks section.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542997">FltGetContexts</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543025">FltGetFileContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543058">FltGetInstanceContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543144">FltGetStreamContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543155">FltGetStreamHandleContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543175">FltGetTransactionContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543189">FltGetVolumeContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544291">FltReferenceContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544317">FltReleaseContexts</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544511">FltSetFileContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544521">FltSetInstanceContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544543">FltSetStreamContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544552">FltSetStreamHandleContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544554">FltSetTransactionContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544557">FltSetVolumeContext</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltReleaseContext function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
