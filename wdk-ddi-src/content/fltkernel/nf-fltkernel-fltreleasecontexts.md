---
UID: NF.fltkernel.FltReleaseContexts
title: FltReleaseContexts
author: windows-driver-content
description: FltReleaseContexts releases each context in a given FLT_RELATED_CONTEXTS structure.
old-location: ifsk\fltreleasecontexts.htm
old-project: ifsk
ms.assetid: 9b6a28ad-f86c-475b-adee-8d2d8b2d6d61
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltReleaseContexts
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
req.alt-api: FltReleaseContexts
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

# FltReleaseContexts function



## -description
<p><b>FltReleaseContexts</b> releases each context in a given <a href="..\fltkernel\ns-fltkernel--flt-related-contexts.md">FLT_RELATED_CONTEXTS</a> structure. </p>


## -syntax

````
VOID FltReleaseContexts(
  _In_ PFLT_RELATED_CONTEXTS Contexts
);
````


## -parameters
<dl>

### -param Contexts [in]

<dd>
<p>Pointer to the <a href="..\fltkernel\ns-fltkernel--flt-related-contexts.md">FLT_RELATED_CONTEXTS</a> structure. </p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p><b>FltReleaseContexts</b> decrements the reference count on all contexts in the <a href="..\fltkernel\ns-fltkernel--flt-related-contexts.md">FLT_RELATED_CONTEXTS</a> structure and sets all members of the structure to NULL_CONTEXT. </p>

<p>To get the <a href="..\fltkernel\ns-fltkernel--flt-related-contexts.md">FLT_RELATED_CONTEXTS</a> structure for a given minifilter driver for a given I/O request, call <a href="..\fltkernel\nf-fltkernel-fltgetcontexts.md">FltGetContexts</a>. </p>

<p>For more information about context reference counting, see <a href="ifsk.referencing_contexts">Referencing Contexts</a>. </p>

<p>Callers of <b>FltReleaseContexts</b> must be running at IRQL &lt;= DISPATCH_LEVEL if all contexts were allocated from nonpaged pool. If any contexts were allocated from paged pool, callers must be running at IRQL &lt;= APC_LEVEL. </p>

<p>When each context's reference count reaches zero, the context is freed immediately if the caller is running at IRQL &lt;= APC_LEVEL. If the caller is running at IRQL DISPATCH_LEVEL, a work item is scheduled to free the context. </p>

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
<a href="..\fltkernel\ns-fltkernel--flt-context-registration.md">FLT_CONTEXT_REGISTRATION</a>
</dt>
<dt>
<a href="..\fltkernel\ns-fltkernel--flt-related-contexts.md">FLT_RELATED_CONTEXTS</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltallocatecontext.md">FltAllocateContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetcontexts.md">FltGetContexts</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltreleasecontext.md">FltReleaseContext</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltReleaseContexts function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
