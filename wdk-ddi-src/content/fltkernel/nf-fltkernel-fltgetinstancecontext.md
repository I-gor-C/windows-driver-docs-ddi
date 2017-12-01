---
UID: NF.fltkernel.FltGetInstanceContext
title: FltGetInstanceContext
author: windows-driver-content
description: The FltGetInstanceContext routine retrieves a context that was set for an instance by a given minifilter driver.
old-location: ifsk\fltgetinstancecontext.htm
old-project: ifsk
ms.assetid: 74bbffcd-27a9-4a9e-b625-64f9860f2c66
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltGetInstanceContext
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
req.alt-api: FltGetInstanceContext
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

# FltGetInstanceContext function



## -description
<p>The <b>FltGetInstanceContext</b> routine retrieves a context that was set for an instance by a given minifilter driver. </p>


## -syntax

````
NTSTATUS FltGetInstanceContext(
  _In_  PFLT_INSTANCE Instance,
  _Out_ PFLT_CONTEXT  *Context
);
````


## -parameters
<dl>

### -param <i>Instance</i> [in]

<dd>
<p>Opaque instance pointer for the instance. </p>
</dd>

### -param <i>Context</i> [out]

<dd>
<p>Pointer to a caller-allocated variable that receives the address of the instance context. </p>
</dd>
</dl>

## -returns
<p><b>FltGetInstanceContext</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value, such as the following: </p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>No matching context was found. This is an error code. </p>

<p> </p>

## -remarks
<p><b>FltGetInstanceContext</b> retrieves a context that was set for an instance by a given minifilter driver. </p>

<p><b>FltGetInstanceContext</b> increments the reference count on the context that the <i>Context </i>parameter points to. When this context pointer is no longer needed, the caller must decrement its reference count by calling <a href="..\fltkernel\nf-fltkernel-fltreleasecontext.md">FltReleaseContext</a>. Thus every successful call to <b>FltGetInstanceContext</b> must be matched by a subsequent call to <b>FltReleaseContext</b>. </p>

<p>To set a context for an instance, call <a href="..\fltkernel\nf-fltkernel-fltsetinstancecontext.md">FltSetInstanceContext</a>. </p>

<p>To allocate a new context, call <a href="..\fltkernel\nf-fltkernel-fltallocatecontext.md">FltAllocateContext</a>. </p>

<p>To delete an instance context, call <a href="..\fltkernel\nf-fltkernel-fltdeleteinstancecontext.md">FltDeleteInstanceContext</a> or <a href="..\fltkernel\nf-fltkernel-fltdeletecontext.md">FltDeleteContext</a>. </p>

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
<a href="..\fltkernel\nf-fltkernel-fltdeleteinstancecontext.md">FltDeleteInstanceContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltreleasecontext.md">FltReleaseContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltsetinstancecontext.md">FltSetInstanceContext</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetInstanceContext routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
