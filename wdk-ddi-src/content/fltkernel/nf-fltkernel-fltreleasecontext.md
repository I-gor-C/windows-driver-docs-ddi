---
UID: NF.fltkernel.FltReleaseContext
title: FltReleaseContext function
author: windows-driver-content
description: FltReleaseContext decrements the reference count on a context.
old-location: ifsk\fltreleasecontext.htm
old-project: ifsk
ms.assetid: b0585443-b8e9-41bc-81af-5707fda2465d
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
---

# FltReleaseContext function



## -description
<b>FltReleaseContext</b> decrements the reference count on a context. 


## -syntax

````
VOID FltReleaseContext(
  _In_ PFLT_CONTEXT Context
);
````


## -parameters

### -param Context [in]

Pointer to the context. Must be a valid pointer to a context object for a volume, instance, stream, or stream handle. This parameter is required and cannot be <b>NULL</b>. 

## -returns
None 

## -remarks
A minifilter driver calls <b>FltReleaseContext</b> to release a context. <b>FltReleaseContext</b> decrements the reference count on the given context. When the reference count reaches zero, the context is freed immediately if the caller is running at IRQL &lt;= APC_LEVEL. If the caller is running at IRQL DISPATCH_LEVEL, a work item is scheduled to free the context. 

Every successful call to <a href="ifsk.fltallocatecontext">FltAllocateContext</a>, <b>FltGet</b><i>Xxx</i><b>Context</b>, or <a href="ifsk.fltreferencecontext">FltReferenceContext</a> must eventually be matched by a call to <b>FltReleaseContext</b>. 

Note that the <i>OldContext</i> pointer returned by <b>FltSet</b><i>Xxx</i><b>Context</b> and the <i>Context</i> parameter that is used to call <a href="ifsk.fltdeletecontext">FltDeleteContext</a> must also be released by calling <b>FltReleaseContext</b> when they are no longer needed. 

To allocate a new context, call <a href="ifsk.fltallocatecontext">FltAllocateContext</a>. 

To increment the reference count on a context, call <a href="ifsk.fltreferencecontext">FltReferenceContext</a>. 

For more information about context reference counting, see <a href="ifsk.referencing_contexts">Referencing Contexts</a>. 

Callers of <b>FltReleaseContext</b> must be running at IRQL &lt;= DISPATCH_LEVEL if the context was allocated from nonpaged pool. If the context was allocated from paged pool, callers must be running at IRQL &lt;= APC_LEVEL. 

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
See Remarks section.
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
<a href="ifsk.fltgetcontexts">FltGetContexts</a>
</dt>
<dt>
<a href="ifsk.fltgetfilecontext">FltGetFileContext</a>
</dt>
<dt>
<a href="ifsk.fltgetinstancecontext">FltGetInstanceContext</a>
</dt>
<dt>
<a href="ifsk.fltgetstreamcontext">FltGetStreamContext</a>
</dt>
<dt>
<a href="ifsk.fltgetstreamhandlecontext">FltGetStreamHandleContext</a>
</dt>
<dt>
<a href="ifsk.fltgettransactioncontext">FltGetTransactionContext</a>
</dt>
<dt>
<a href="ifsk.fltgetvolumecontext">FltGetVolumeContext</a>
</dt>
<dt>
<a href="ifsk.fltreferencecontext">FltReferenceContext</a>
</dt>
<dt>
<a href="ifsk.fltreleasecontexts">FltReleaseContexts</a>
</dt>
<dt>
<a href="ifsk.fltsetfilecontext">FltSetFileContext</a>
</dt>
<dt>
<a href="ifsk.fltsetinstancecontext">FltSetInstanceContext</a>
</dt>
<dt>
<a href="ifsk.fltsetstreamcontext">FltSetStreamContext</a>
</dt>
<dt>
<a href="ifsk.fltsetstreamhandlecontext">FltSetStreamHandleContext</a>
</dt>
<dt>
<a href="ifsk.fltsettransactioncontext">FltSetTransactionContext</a>
</dt>
<dt>
<a href="ifsk.fltsetvolumecontext">FltSetVolumeContext</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltReleaseContext function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
