---
UID: NF.fltkernel.FltDeleteVolumeContext
title: FltDeleteVolumeContext
author: windows-driver-content
description: FltDeleteVolumeContext removes a context that a given minifilter driver has set for a given volume and marks the context for deletion.
old-location: ifsk\fltdeletevolumecontext.htm
old-project: ifsk
ms.assetid: dfb376af-9910-4708-9248-1104dfc4bdec
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltDeleteVolumeContext
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
req.alt-api: FltDeleteVolumeContext
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

# FltDeleteVolumeContext function



## -description
<p><b>FltDeleteVolumeContext</b> removes a context that a given minifilter driver has set for a given volume and marks the context for deletion. </p>


## -syntax

````
NTSTATUS FltDeleteVolumeContext(
  _In_      PFLT_FILTER  Filter,
  _In_      PFLT_VOLUME  Volume,
  _Out_opt_ PFLT_CONTEXT *OldContext
);
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p>Opaque filter pointer for the caller. </p>
</dd>

### -param <i>Volume</i> [in]

<dd>
<p>Opaque volume pointer for the volume. </p>
</dd>

### -param <i>OldContext</i> [out, optional]

<dd>
<p>Pointer to a caller-allocated variable that receives the address of the deleted context. This parameter is optional and can be <b>NULL</b>. If <i>OldContext</i> is not <b>NULL</b> and does not point to NULL_CONTEXT, the caller is responsible for calling <a href="..\fltkernel\nf-fltkernel-fltreleasecontext.md">FltReleaseContext</a> to release this context when it is no longer needed. </p>
</dd>
</dl>

## -returns
<p><b>FltDeleteVolumeContext</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following: </p><dl>
<dt><b>STATUS_FLT_DELETING_OBJECT</b></dt>
</dl><p>The specified <i>Volume</i> is being torn down. This is an error code. </p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>No matching context was found. This is an error code. </p>

<p> </p>

## -remarks
<p>Because contexts are reference-counted, it is not usually necessary for a minifilter driver to call a routine such as <b>FltDeleteVolumeContext</b> to explicitly delete a context. </p>

<p>A minifilter driver calls <b>FltDeleteVolumeContext</b> to remove a context from a volume and mark the context for deletion. The context is usually freed immediately unless there is an outstanding reference on it (for example, because the context is still in use by another thread). </p>

<p>To allocate a new context, call <a href="..\fltkernel\nf-fltkernel-fltallocatecontext.md">FltAllocateContext</a>. </p>

<p>To get a volume context, call <a href="..\fltkernel\nf-fltkernel-fltgetvolumecontext.md">FltGetVolumeContext</a>. </p>

<p>To set a volume context, call <a href="..\fltkernel\nf-fltkernel-fltsetvolumecontext.md">FltSetVolumeContext</a>. </p>

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
<a href="..\fltkernel\nf-fltkernel-fltallocatecontext.md">FltAllocateContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltdeletecontext.md">FltDeleteContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetvolumecontext.md">FltGetVolumeContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltreleasecontext.md">FltReleaseContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltsetvolumecontext.md">FltSetVolumeContext</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltDeleteVolumeContext function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
