---
UID: NF.fltkernel.FltSetVolumeContext
title: FltSetVolumeContext
author: windows-driver-content
description: FltSetVolumeContext sets a context for a volume.
old-location: ifsk\fltsetvolumecontext.htm
ms.assetid: e1e8605c-b3d1-40db-bb33-fc1f7ed51617
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available and supported in Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP2, Windows Server 2003 SP1, and later operating systems. Not available nor supported in Windows 2000 SP4 and earlier operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltSetVolumeContext
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
ms.keywords: FltSetVolumeContext
req.iface: 
---

# FltSetVolumeContext function



## -description
<p><b>FltSetVolumeContext</b> sets a context for a volume. </p>


## -syntax

````
NTSTATUS FltSetVolumeContext(
  _In_      PFLT_VOLUME               Volume,
  _In_      FLT_SET_CONTEXT_OPERATION Operation,
  _In_      PFLT_CONTEXT              NewContext,
  _Out_opt_ PFLT_CONTEXT              *OldContext
);
````


## -parameters
<dl>

### -param <i>Volume</i> [in]

<dd>
<p>Opaque volume pointer for the volume. </p>
</dd>

### -param <i>Operation</i> [in]

<dd>
<p>Flag specifying details of the operation to be performed. This parameter must be one of the following: </p>
<p></p>
<dl>

### -param <a id="FLT_SET_CONTEXT_REPLACE_IF_EXISTS"></a><a id="flt_set_context_replace_if_exists"></a>FLT_SET_CONTEXT_REPLACE_IF_EXISTS

<dd>
<p>If a context is already set, replace it with <i>NewContext</i>. Otherwise, insert <i>NewContext</i> into the list of contexts for the volume. </p>
</dd>

### -param <a id="FLT_SET_CONTEXT_KEEP_IF_EXISTS"></a><a id="flt_set_context_keep_if_exists"></a>FLT_SET_CONTEXT_KEEP_IF_EXISTS

<dd>
<p>If a context is already set, return STATUS_FLT_CONTEXT_ALREADY_DEFINED. Otherwise, insert <i>NewContext</i> into the list of contexts for the volume. </p>
</dd>
</dl>
</dd>

### -param <i>NewContext</i> [in]

<dd>
<p>Pointer to the new context to be set for the volume. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>OldContext</i> [out, optional]

<dd>
<p>Pointer to a caller-allocated variable that receives the address of the existing volume context for <i>Instance</i>. This parameter is optional and can be <b>NULL</b>. (For more information about this parameter, see the following Remarks section.) </p>
</dd>
</dl>

## -returns
<p><b>FltSetVolumeContext</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following: </p><dl>
<dt><b>STATUS_FLT_CONTEXT_ALREADY_DEFINED</b></dt>
</dl><p>IF FLT_SET_CONTEXT_KEEP_IF_EXISTS was specified for <i>Operation</i>, this error code indicates that a context is already attached to the volume.  </p><dl>
<dt><b>STATUS_FLT_CONTEXT_ALREADY_LINKED</b></dt>
</dl><p>The context pointed to by the <i>NewContext</i> parameter is already linked to an object.  In other words, this error code indicates that <i>NewContext</i> is already in use due to a successful prior call of an <b>FltSet</b><i>Xxx</i><b>Context</b> routine.</p><dl>
<dt><b>STATUS_FLT_DELETING_OBJECT</b></dt>
</dl><p>The specified <i>Volume</i> is being torn down. This is an error code. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>One of the following: </p>

<p>The <i>NewContext</i> parameter does not point to a valid volume context. </p>

<p>An invalid value was specified for <i>Operation</i>. </p>

<p>STATUS_INVALID_PARAMETER is an error code. </p>

<p> </p>

## -remarks
<p>A minifilter driver calls <b>FltSetVolumeContext</b> to attach a context to a volume, or to remove or replace an existing volume context. A minifilter driver can attach only one context to a volume. </p>

<p>A successful call to <b>FltSetVolumeContext</b> increments the reference count on <i>NewContext</i>. If <b>FltSetVolumeContext</b> fails, the reference count remains unchanged. In either case, the filter calling <b>FltSetVolumeContext</b> must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a> to decrement the <i>NewContext</i> object. If <b>FltSetVolumeContext</b> fails and if the <i>OldContext</i> parameter is not <b>NULL</b> and does not point to NULL_CONTEXT then <i>OldContext</i> is a referenced pointer to the context currently associated with the transaction. The filter calling <b>FltSetVolumeContext</b> must call <b>FltReleaseContext</b> for <i>OldContext</i> as well.</p>

<p>Note that the <i>OldContext</i> pointer returned by <b>FltSetVolumeContext</b> must also be released by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a> when it is no longer needed. For more information, see <a href="ifsk.setting_contexts">Setting Contexts</a> and <a href="ifsk.releasing_contexts">Releasing Contexts</a>. </p>

<p>To allocate a new context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>. </p>

<p>To get a volume context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543189">FltGetVolumeContext</a>. </p>

<p>To delete a volume context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542030">FltDeleteVolumeContext</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff541960">FltDeleteContext</a>. </p>

<p>For more information about context reference counting, see <a href="ifsk.referencing_contexts">Referencing Contexts</a>.</p>

<p>A minifilter driver calls <b>FltSetVolumeContext</b> to attach a context to a volume, or to remove or replace an existing volume context. A minifilter driver can attach only one context to a volume. </p>

<p>A successful call to <b>FltSetVolumeContext</b> increments the reference count on <i>NewContext</i>. If <b>FltSetVolumeContext</b> fails, the reference count remains unchanged. In either case, the filter calling <b>FltSetVolumeContext</b> must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a> to decrement the <i>NewContext</i> object. If <b>FltSetVolumeContext</b> fails and if the <i>OldContext</i> parameter is not <b>NULL</b> and does not point to NULL_CONTEXT then <i>OldContext</i> is a referenced pointer to the context currently associated with the transaction. The filter calling <b>FltSetVolumeContext</b> must call <b>FltReleaseContext</b> for <i>OldContext</i> as well.</p>

<p>Note that the <i>OldContext</i> pointer returned by <b>FltSetVolumeContext</b> must also be released by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a> when it is no longer needed. For more information, see <a href="ifsk.setting_contexts">Setting Contexts</a> and <a href="ifsk.releasing_contexts">Releasing Contexts</a>. </p>

<p>To allocate a new context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>. </p>

<p>To get a volume context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543189">FltGetVolumeContext</a>. </p>

<p>To delete a volume context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542030">FltDeleteVolumeContext</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff541960">FltDeleteContext</a>. </p>

<p>For more information about context reference counting, see <a href="ifsk.referencing_contexts">Referencing Contexts</a>.</p>

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
<p>Available and supported in Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP2, Windows Server 2003 SP1, and later operating systems. Not available nor supported in Windows 2000 SP4 and earlier operating systems.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541960">FltDeleteContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542030">FltDeleteVolumeContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543189">FltGetVolumeContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltSetVolumeContext function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
