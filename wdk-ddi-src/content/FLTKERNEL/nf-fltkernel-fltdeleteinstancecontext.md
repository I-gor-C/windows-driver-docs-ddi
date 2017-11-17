---
UID: NF.fltkernel.FltDeleteInstanceContext
title: FltDeleteInstanceContext
author: windows-driver-content
description: FltDeleteInstanceContext removes a context from a given instance and marks the context for deletion.
old-location: ifsk\fltdeleteinstancecontext.htm
ms.assetid: 910b62d7-2ef3-4eb2-97c3-9b920fdb0558
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltDeleteInstanceContext
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
ms.keywords: FltDeleteInstanceContext
req.iface: 
---

# FltDeleteInstanceContext function



## -description
<p><b>FltDeleteInstanceContext</b> removes a context from a given instance and marks the context for deletion. </p>


## -syntax

````
NTSTATUS FltDeleteInstanceContext(
  _In_  PFLT_INSTANCE Instance,
  _Out_ PFLT_CONTEXT  *OldContext
);
````


## -parameters
<dl>

### -param <i>Instance</i> [in]

<dd>
<p>Opaque instance pointer for the instance. </p>
</dd>

### -param <i>OldContext</i> [out]

<dd>
<p>Pointer to a caller-allocated variable that receives the address of the deleted context. This parameter is optional and can be <b>NULL</b>. If <i>OldContext</i> is not <b>NULL</b> and does not point to NULL_CONTEXT, the caller is responsible for calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a> to release this context when it is no longer needed. </p>
</dd>
</dl>

## -returns
<p><b>FltDeleteInstanceContext</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following: </p><dl>
<dt><b>STATUS_FLT_DELETING_OBJECT</b></dt>
</dl><p>The specified <i>Instance</i> is being torn down. This is an error code. </p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>No matching context was found. This is an error code. </p>

<p> </p>

## -remarks
<p>Because contexts are reference-counted, it is not usually necessary for a minifilter driver to call a routine such as <b>FltDeleteInstanceContext</b> to explicitly delete a context. </p>

<p>A minifilter driver calls <b>FltDeleteInstanceContext</b> to remove a context from an instance and mark the context for deletion. The context is usually freed immediately unless there is an outstanding reference on it (for example, because the context is still being used by another thread). </p>

<p>To allocate a new context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>. </p>

<p>To get an instance context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543058">FltGetInstanceContext</a>. </p>

<p>To set an instance context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544521">FltSetInstanceContext</a>. </p>

<p>Because contexts are reference-counted, it is not usually necessary for a minifilter driver to call a routine such as <b>FltDeleteInstanceContext</b> to explicitly delete a context. </p>

<p>A minifilter driver calls <b>FltDeleteInstanceContext</b> to remove a context from an instance and mark the context for deletion. The context is usually freed immediately unless there is an outstanding reference on it (for example, because the context is still being used by another thread). </p>

<p>To allocate a new context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>. </p>

<p>To get an instance context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543058">FltGetInstanceContext</a>. </p>

<p>To set an instance context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544521">FltSetInstanceContext</a>. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541960">FltDeleteContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543058">FltGetInstanceContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544521">FltSetInstanceContext</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltDeleteInstanceContext function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
