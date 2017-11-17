---
UID: NF.fltkernel.FltGetContextsEx
title: FltGetContextsEx
author: windows-driver-content
description: The FltGetContextsEx routine retrieves a minifilter driver's contexts for the objects related to the current operation.
old-location: ifsk\fltgetcontextsex.htm
ms.assetid: 99903B10-5FA8-430F-9E1F-90A45E07B7D0
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltGetContextsEx
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
ms.keywords: FltGetContextsEx
req.iface: 
---

# FltGetContextsEx function



## -description
<p>The <b>FltGetContextsEx</b> routine retrieves a minifilter driver's contexts for the objects related to the current operation. </p>


## -syntax

````
VOID FltGetContextsEx(
  _In_  PCFLT_RELATED_OBJECTS    FltObjects,
  _In_  FLT_CONTEXT_TYPE         DesiredContexts,
  _In_  SIZE_T                   ContextsSize,
  _Out_ PFLT_RELATED_CONTEXTS_EX Contexts
);
````


## -parameters
<dl>

### -param <i>FltObjects</i> [in]

<dd>
<p>Pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff544816">FLT_RELATED_OBJECTS</a> structure containing opaque pointers for the objects related to the current operation. (For more information about this parameter, see the  Remarks section.) </p>
</dd>

### -param <i>DesiredContexts</i> [in]

<dd>
<p>Type of contexts to retrieve. This parameter can have one or more of the following values: </p>
<dl>
<dd>
<p>FLT_ALL_CONTEXTS</p>
</dd>
<dd>
<p>FLT_FILE_CONTEXT (Windows Vista and later only.)</p>
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
<p>FLT_TRANSACTION_CONTEXT (Windows Vista and later only.) </p>
</dd>
<dd>
<p>FLT_VOLUME_CONTEXT</p>
</dd>
<dd>
<p>FLT_SECTION_CONTEXT (Windows 8 and later only.)</p>
</dd>
</dl>
</dd>

### -param <i>ContextsSize</i> [in]

<dd>
<p>The size, in bytes, of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh967703">FLT_RELATED_CONTEXTS_EX</a> structure pointed to by <i>Contexts</i>. Set to <b>sizeof</b>(FLT_RELATED_CONTEXTS_EX).</p>
</dd>

### -param <i>Contexts</i> [out]

<dd>
<p>Pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/hh967703">FLT_RELATED_CONTEXTS_EX</a> structure that receives the requested contexts. Contexts that are not requested, or requested but not found, are set to zero. </p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>A minifilter driver calls <b>FltGetContextsEx</b> to retrieve pointers to the minifilter driver's contexts for the objects in an <a href="https://msdn.microsoft.com/library/windows/hardware/ff544816">FLT_RELATED_OBJECTS</a> structure. </p>

<p>The following minifilter driver callback routine types receive a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff544816">FLT_RELATED_OBJECTS</a> structure as the <i>FltObjects</i> input parameter: </p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109">PFLT_PRE_OPERATION_CALLBACK</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551107">PFLT_POST_OPERATION_CALLBACK</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551096">PFLT_INSTANCE_SETUP_CALLBACK</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551095">PFLT_INSTANCE_QUERY_TEARDOWN_CALLBACK</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551098">PFLT_INSTANCE_TEARDOWN_CALLBACK</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109">PFLT_PRE_OPERATION_CALLBACK</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551107">PFLT_POST_OPERATION_CALLBACK</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551096">PFLT_INSTANCE_SETUP_CALLBACK</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551095">PFLT_INSTANCE_QUERY_TEARDOWN_CALLBACK</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551098">PFLT_INSTANCE_TEARDOWN_CALLBACK</a>
</p>

<p><b>FltGetContextsEx</b> increments the reference count on each of the contexts returned in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh967703">FLT_RELATED_CONTEXTS_EX</a> structure that the <i>Contexts </i>parameter points to. Thus for every successful call to <b>FltGetContextsEx</b>, the caller must either: </p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/hh967701">FltReleaseContextsEx</a> for the entire structure that the <i>Contexts</i> parameter points to.</p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a> for each of the contexts returned in the structure and set each context field returned in the structure to zero. </p>

<p>A minifilter driver calls <b>FltGetContextsEx</b> to retrieve pointers to the minifilter driver's contexts for the objects in an <a href="https://msdn.microsoft.com/library/windows/hardware/ff544816">FLT_RELATED_OBJECTS</a> structure. </p>

<p>The following minifilter driver callback routine types receive a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff544816">FLT_RELATED_OBJECTS</a> structure as the <i>FltObjects</i> input parameter: </p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109">PFLT_PRE_OPERATION_CALLBACK</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551107">PFLT_POST_OPERATION_CALLBACK</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551096">PFLT_INSTANCE_SETUP_CALLBACK</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551095">PFLT_INSTANCE_QUERY_TEARDOWN_CALLBACK</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551098">PFLT_INSTANCE_TEARDOWN_CALLBACK</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109">PFLT_PRE_OPERATION_CALLBACK</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551107">PFLT_POST_OPERATION_CALLBACK</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551096">PFLT_INSTANCE_SETUP_CALLBACK</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551095">PFLT_INSTANCE_QUERY_TEARDOWN_CALLBACK</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551098">PFLT_INSTANCE_TEARDOWN_CALLBACK</a>
</p>

<p><b>FltGetContextsEx</b> increments the reference count on each of the contexts returned in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh967703">FLT_RELATED_CONTEXTS_EX</a> structure that the <i>Contexts </i>parameter points to. Thus for every successful call to <b>FltGetContextsEx</b>, the caller must either: </p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/hh967701">FltReleaseContextsEx</a> for the entire structure that the <i>Contexts</i> parameter points to.</p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a> for each of the contexts returned in the structure and set each context field returned in the structure to zero. </p>

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
<p>Available starting with Windows 8.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh967703">FLT_RELATED_CONTEXTS_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544816">FLT_RELATED_OBJECTS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544305">FltRegisterFilter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh967701">FltReleaseContextsEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551095">PFLT_INSTANCE_QUERY_TEARDOWN_CALLBACK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551096">PFLT_INSTANCE_SETUP_CALLBACK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551098">PFLT_INSTANCE_TEARDOWN_CALLBACK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551107">PFLT_POST_OPERATION_CALLBACK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109">PFLT_PRE_OPERATION_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetContextsEx routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
