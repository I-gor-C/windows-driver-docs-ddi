---
UID: NF.fltkernel.FltGetContexts
title: FltGetContexts
author: windows-driver-content
description: The FltGetContexts routine retrieves a minifilter driver's contexts for the objects related to the current operation.
old-location: ifsk\fltgetcontexts.htm
old-project: ifsk
ms.assetid: 886a0898-814b-4a24-bc83-c6e82e71dae2
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltGetContexts
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
req.alt-api: FltGetContexts
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

# FltGetContexts function



## -description
<p>The <b>FltGetContexts</b> routine retrieves a minifilter driver's contexts for the objects related to the current operation. </p>


## -syntax

````
VOID FltGetContexts(
  _In_  PCFLT_RELATED_OBJECTS FltObjects,
  _In_  FLT_CONTEXT_TYPE      DesiredContexts,
  _Out_ PFLT_RELATED_CONTEXTS Contexts
);
````


## -parameters
<dl>

### -param FltObjects [in]

<dd>
<p>Pointer to an <a href="..\fltkernel\ns-fltkernel--flt-related-objects.md">FLT_RELATED_OBJECTS</a> structure containing opaque pointers for the objects related to the current operation. (For more information about this parameter, see the  Remarks section.) </p>
</dd>

### -param DesiredContexts [in]

<dd>
<p>Type of contexts to retrieve. This parameter can have one or more of the following values: </p>
<dl>
<dd>
<p>FLT_ALL_CONTEXTS</p>
</dd>
<dd>
<p>FLT_FILE_CONTEXT (Windows Vista and later only.)</p>
</dd>
<dd>
<p>FLT_INSTANCE_CONTEXT</p>
</dd>
<dd>
<p>FLT_STREAM_CONTEXT</p>
</dd>
<dd>
<p>FLT_STREAMHANDLE_CONTEXT</p>
</dd>
<dd>
<p>FLT_TRANSACTION_CONTEXT (Windows Vista and later only.) </p>
</dd>
<dd>
<p>FLT_VOLUME_CONTEXT</p>
</dd>
</dl>
</dd>

### -param Contexts [out]

<dd>
<p>Pointer to a caller-allocated <a href="..\fltkernel\ns-fltkernel--flt-related-contexts.md">FLT_RELATED_CONTEXTS</a> structure that receives the requested contexts. Contexts that are not requested, or requested but not found, are set to zero. </p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>A minifilter driver calls <b>FltGetContexts</b> to retrieve pointers to the minifilter driver's contexts for the objects in an <a href="..\fltkernel\ns-fltkernel--flt-related-objects.md">FLT_RELATED_OBJECTS</a> structure. </p>

<p>The following minifilter driver callback routine types receive a pointer to an <a href="..\fltkernel\ns-fltkernel--flt-related-objects.md">FLT_RELATED_OBJECTS</a> structure as the <i>FltObjects</i> input parameter: </p>

<p>
<a href="..\fltkernel\nc-fltkernel-pflt-pre-operation-callback.md">PFLT_PRE_OPERATION_CALLBACK</a>
</p>

<p>
<a href="..\fltkernel\nc-fltkernel-pflt-post-operation-callback.md">PFLT_POST_OPERATION_CALLBACK</a>
</p>

<p>
<a href="..\fltkernel\nc-fltkernel-pflt-instance-setup-callback.md">PFLT_INSTANCE_SETUP_CALLBACK</a>
</p>

<p>
<a href="..\fltkernel\nc-fltkernel-pflt-instance-query-teardown-callback.md">PFLT_INSTANCE_QUERY_TEARDOWN_CALLBACK</a>
</p>

<p>
<a href="..\fltkernel\nc-fltkernel-pflt-instance-teardown-callback.md">PFLT_INSTANCE_TEARDOWN_CALLBACK</a>
</p>

<p><b>FltGetContexts</b> increments the reference count on each of the contexts returned in the <a href="..\fltkernel\ns-fltkernel--flt-related-contexts.md">FLT_RELATED_CONTEXTS</a> structure that the <i>Contexts </i>parameter points to. Thus for every successful call to <b>FltGetContexts</b>, the caller must either: </p>

<p>Call <a href="..\fltkernel\nf-fltkernel-fltreleasecontexts.md">FltReleaseContexts</a> for the entire structure that the <i>Contexts </i>parameter points to. </p>

<p>Call <a href="..\fltkernel\nf-fltkernel-fltreleasecontext.md">FltReleaseContext</a> for each of the contexts returned in the structure and set each context field returned in the structure to zero. </p>

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
<a href="..\fltkernel\ns-fltkernel--flt-related-contexts.md">FLT_RELATED_CONTEXTS</a>
</dt>
<dt>
<a href="..\fltkernel\ns-fltkernel--flt-related-objects.md">FLT_RELATED_OBJECTS</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltreleasecontext.md">FltReleaseContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltreleasecontexts.md">FltReleaseContexts</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-instance-query-teardown-callback.md">PFLT_INSTANCE_QUERY_TEARDOWN_CALLBACK</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-instance-setup-callback.md">PFLT_INSTANCE_SETUP_CALLBACK</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-instance-teardown-callback.md">PFLT_INSTANCE_TEARDOWN_CALLBACK</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-post-operation-callback.md">PFLT_POST_OPERATION_CALLBACK</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-pre-operation-callback.md">PFLT_PRE_OPERATION_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetContexts routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
